import NextAuth from 'next-auth';
import Google from 'next-auth/providers/google';
import Credentials from 'next-auth/providers/credentials';
import { getOrCreateUser, getUserByEmail } from './d1';
import type { NextAuthConfig } from 'next-auth';

declare module 'next-auth' {
  interface Session {
    user: {
      id: string;
      name?: string | null;
      email?: string | null;
      image?: string | null;
      credits: number;
      profileCompleted: boolean;
      referralCode?: string;
    };
  }
}

const config: NextAuthConfig = {
  providers: [
    Google({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
    // Test login (개발용)
    Credentials({
      id: 'test-login',
      name: 'Test Login',
      credentials: {
        email: { label: 'Email', type: 'email' },
      },
      async authorize(credentials) {
        if (!credentials?.email || typeof credentials.email !== 'string') return null;
        const user = await getOrCreateUser(credentials.email, 'Test User');
        if (!user) return null;
        return {
          id: user.id,
          email: user.email,
          name: user.name,
          image: user.image,
        };
      },
    }),
  ],
  callbacks: {
    async signIn({ user }) {
      if (!user.email) return false;
      const dbUser = await getOrCreateUser(user.email, user.name ?? undefined, user.image ?? undefined);
      return !!dbUser;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.sub as string;
        session.user.credits = (token.credits as number) ?? 5;
        session.user.profileCompleted = (token.profileCompleted as boolean) ?? false;
        session.user.referralCode = token.referralCode as string | undefined;
      }
      return session;
    },
    async jwt({ token, trigger }) {
      // Refresh user data on sign in or when triggered
      if (trigger === 'signIn' || trigger === 'update') {
        if (token.email) {
          const user = await getUserByEmail(token.email);
          if (user) {
            token.id = user.id;
            token.credits = user.credits;
            token.profileCompleted = !!user.profile_completed;
            token.referralCode = user.referral_code ?? undefined;
          }
        }
      }
      return token;
    },
  },
  pages: {
    signIn: '/login',
  },
  trustHost: true,
};

export const { handlers, auth, signIn, signOut } = NextAuth(config);
