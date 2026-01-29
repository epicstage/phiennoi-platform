import { NextRequest, NextResponse } from "next/server";
import { createClient } from "@supabase/supabase-js";

function getSupabaseClient() {
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const supabaseServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

  if (!supabaseUrl || !supabaseServiceKey) {
    return null;
  }

  return createClient(supabaseUrl, supabaseServiceKey);
}

export async function POST(request: NextRequest) {
  try {
    const supabase = getSupabaseClient();

    if (!supabase) {
      return NextResponse.json(
        { error: "서비스가 준비 중입니다. 잠시 후 다시 시도해주세요." },
        { status: 503 }
      );
    }
    const formData = await request.formData();

    const name = formData.get("name") as string;
    const email = formData.get("email") as string;
    const phone = formData.get("phone") as string;
    const location = formData.get("location") as string;
    const domains = formData.getAll("domains") as string[];
    const file = formData.get("resume") as File | null;

    // 유효성 검사
    if (!name || !email || !phone) {
      return NextResponse.json(
        { error: "이름, 이메일, 연락처는 필수 항목입니다." },
        { status: 400 }
      );
    }

    let resumeUrl: string | null = null;

    // 파일 업로드
    if (file) {
      const fileExt = file.name.split(".").pop();
      const fileName = `${Date.now()}-${Math.random().toString(36).substring(2)}.${fileExt}`;
      const filePath = `resumes/${fileName}`;

      const { error: uploadError } = await supabase.storage
        .from("uploads")
        .upload(filePath, file, {
          contentType: file.type,
          upsert: false,
        });

      if (uploadError) {
        console.error("File upload error:", uploadError);
        return NextResponse.json(
          { error: "파일 업로드에 실패했습니다." },
          { status: 500 }
        );
      }

      const { data: urlData } = supabase.storage
        .from("uploads")
        .getPublicUrl(filePath);

      resumeUrl = urlData.publicUrl;
    }

    // DB에 통역사 정보 저장
    const { data, error } = await supabase
      .from("interpreters")
      .insert({
        name,
        email,
        phone,
        location,
        domains,
        resume_url: resumeUrl,
        status: "pending",
      })
      .select()
      .single();

    if (error) {
      console.error("DB insert error:", error);
      return NextResponse.json(
        { error: "등록에 실패했습니다. 다시 시도해주세요." },
        { status: 500 }
      );
    }

    return NextResponse.json({
      success: true,
      message: "이력서가 성공적으로 등록되었습니다.",
      id: data.id,
    });
  } catch (error) {
    console.error("Upload API error:", error);
    return NextResponse.json(
      { error: "서버 오류가 발생했습니다." },
      { status: 500 }
    );
  }
}
