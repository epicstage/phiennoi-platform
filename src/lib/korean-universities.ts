// 한국 대학교 리스트 (통역사 이력서에서 자주 등장하는 대학 위주)
// 자동완성 검색용 데이터

export interface KoreanUniversity {
  id: string;
  nameKo: string;      // 한국어 이름
  nameEn: string;      // 영어 이름
  city: string;
  type: 'national' | 'public' | 'private';
}

export const koreanUniversities: KoreanUniversity[] = [
  // ===== 서울 주요 대학 =====
  { id: 'snu', nameKo: '서울대학교', nameEn: 'Seoul National University', city: '서울', type: 'national' },
  { id: 'yonsei', nameKo: '연세대학교', nameEn: 'Yonsei University', city: '서울', type: 'private' },
  { id: 'korea', nameKo: '고려대학교', nameEn: 'Korea University', city: '서울', type: 'private' },
  { id: 'skku', nameKo: '성균관대학교', nameEn: 'Sungkyunkwan University', city: '서울', type: 'private' },
  { id: 'hanyang', nameKo: '한양대학교', nameEn: 'Hanyang University', city: '서울', type: 'private' },
  { id: 'sogang', nameKo: '서강대학교', nameEn: 'Sogang University', city: '서울', type: 'private' },
  { id: 'cau', nameKo: '중앙대학교', nameEn: 'Chung-Ang University', city: '서울', type: 'private' },
  { id: 'khu', nameKo: '경희대학교', nameEn: 'Kyung Hee University', city: '서울', type: 'private' },
  { id: 'hufs', nameKo: '한국외국어대학교', nameEn: 'Hankuk University of Foreign Studies', city: '서울', type: 'private' },
  { id: 'dongguk', nameKo: '동국대학교', nameEn: 'Dongguk University', city: '서울', type: 'private' },
  { id: 'konkuk', nameKo: '건국대학교', nameEn: 'Konkuk University', city: '서울', type: 'private' },
  { id: 'sejong', nameKo: '세종대학교', nameEn: 'Sejong University', city: '서울', type: 'private' },
  { id: 'hongik', nameKo: '홍익대학교', nameEn: 'Hongik University', city: '서울', type: 'private' },
  { id: 'kookmin', nameKo: '국민대학교', nameEn: 'Kookmin University', city: '서울', type: 'private' },
  { id: 'smu', nameKo: '숭실대학교', nameEn: 'Soongsil University', city: '서울', type: 'private' },
  { id: 'kwu', nameKo: '광운대학교', nameEn: 'Kwangwoon University', city: '서울', type: 'private' },
  { id: 'uos', nameKo: '서울시립대학교', nameEn: 'University of Seoul', city: '서울', type: 'public' },
  { id: 'snue', nameKo: '서울교육대학교', nameEn: 'Seoul National University of Education', city: '서울', type: 'national' },
  { id: 'sangmyung', nameKo: '상명대학교', nameEn: 'Sangmyung University', city: '서울', type: 'private' },
  { id: 'duksung', nameKo: '덕성여자대학교', nameEn: 'Duksung Women\'s University', city: '서울', type: 'private' },
  { id: 'sungshin', nameKo: '성신여자대학교', nameEn: 'Sungshin Women\'s University', city: '서울', type: 'private' },
  { id: 'ewha', nameKo: '이화여자대학교', nameEn: 'Ewha Womans University', city: '서울', type: 'private' },
  { id: 'sookmyung', nameKo: '숙명여자대학교', nameEn: 'Sookmyung Women\'s University', city: '서울', type: 'private' },

  // ===== 경기/인천 =====
  { id: 'ajou', nameKo: '아주대학교', nameEn: 'Ajou University', city: '수원', type: 'private' },
  { id: 'suwon', nameKo: '수원대학교', nameEn: 'Suwon University', city: '수원', type: 'private' },
  { id: 'gachon', nameKo: '가천대학교', nameEn: 'Gachon University', city: '성남', type: 'private' },
  { id: 'inu', nameKo: '인천대학교', nameEn: 'Incheon National University', city: '인천', type: 'national' },
  { id: 'inha', nameKo: '인하대학교', nameEn: 'Inha University', city: '인천', type: 'private' },
  { id: 'kpu', nameKo: '한국산업기술대학교', nameEn: 'Korea Polytechnic University', city: '시흥', type: 'public' },
  { id: 'kyonggi', nameKo: '경기대학교', nameEn: 'Kyonggi University', city: '수원', type: 'private' },
  { id: 'hansung', nameKo: '한성대학교', nameEn: 'Hansung University', city: '서울', type: 'private' },
  { id: 'hknu', nameKo: '한경대학교', nameEn: 'Hankyong National University', city: '안성', type: 'national' },
  { id: 'dankook', nameKo: '단국대학교', nameEn: 'Dankook University', city: '용인', type: 'private' },
  { id: 'myongji', nameKo: '명지대학교', nameEn: 'Myongji University', city: '용인', type: 'private' },

  // ===== 대전/충청 =====
  { id: 'kaist', nameKo: '한국과학기술원', nameEn: 'KAIST', city: '대전', type: 'national' },
  { id: 'cnu', nameKo: '충남대학교', nameEn: 'Chungnam National University', city: '대전', type: 'national' },
  { id: 'hanbat', nameKo: '한밭대학교', nameEn: 'Hanbat National University', city: '대전', type: 'national' },
  { id: 'woosong', nameKo: '우송대학교', nameEn: 'Woosong University', city: '대전', type: 'private' },
  { id: 'daejeon', nameKo: '대전대학교', nameEn: 'Daejeon University', city: '대전', type: 'private' },
  { id: 'cbnu', nameKo: '충북대학교', nameEn: 'Chungbuk National University', city: '청주', type: 'national' },
  { id: 'kku', nameKo: '건국대학교 글로컬캠퍼스', nameEn: 'Konkuk University Glocal Campus', city: '충주', type: 'private' },

  // ===== 부산/경남 =====
  { id: 'pnu', nameKo: '부산대학교', nameEn: 'Pusan National University', city: '부산', type: 'national' },
  { id: 'pknu', nameKo: '부경대학교', nameEn: 'Pukyong National University', city: '부산', type: 'national' },
  { id: 'dong-a', nameKo: '동아대학교', nameEn: 'Dong-A University', city: '부산', type: 'private' },
  { id: 'pusan-ufs', nameKo: '부산외국어대학교', nameEn: 'Busan University of Foreign Studies', city: '부산', type: 'private' },
  { id: 'inje', nameKo: '인제대학교', nameEn: 'Inje University', city: '김해', type: 'private' },
  { id: 'gyeongsang', nameKo: '경상대학교', nameEn: 'Gyeongsang National University', city: '진주', type: 'national' },
  { id: 'changwon', nameKo: '창원대학교', nameEn: 'Changwon National University', city: '창원', type: 'national' },

  // ===== 대구/경북 =====
  { id: 'knu', nameKo: '경북대학교', nameEn: 'Kyungpook National University', city: '대구', type: 'national' },
  { id: 'yeungnam', nameKo: '영남대학교', nameEn: 'Yeungnam University', city: '경산', type: 'private' },
  { id: 'daegu', nameKo: '대구대학교', nameEn: 'Daegu University', city: '경산', type: 'private' },
  { id: 'keimyung', nameKo: '계명대학교', nameEn: 'Keimyung University', city: '대구', type: 'private' },
  { id: 'dgist', nameKo: '대구경북과학기술원', nameEn: 'DGIST', city: '대구', type: 'national' },

  // ===== 광주/전라 =====
  { id: 'jnu', nameKo: '전남대학교', nameEn: 'Chonnam National University', city: '광주', type: 'national' },
  { id: 'jbnu', nameKo: '전북대학교', nameEn: 'Jeonbuk National University', city: '전주', type: 'national' },
  { id: 'chosun', nameKo: '조선대학교', nameEn: 'Chosun University', city: '광주', type: 'private' },
  { id: 'gist', nameKo: '광주과학기술원', nameEn: 'GIST', city: '광주', type: 'national' },
  { id: 'honam', nameKo: '호남대학교', nameEn: 'Honam University', city: '광주', type: 'private' },
  { id: 'wonkwang', nameKo: '원광대학교', nameEn: 'Wonkwang University', city: '익산', type: 'private' },

  // ===== 강원 =====
  { id: 'kangwon', nameKo: '강원대학교', nameEn: 'Kangwon National University', city: '춘천', type: 'national' },
  { id: 'hallym', nameKo: '한림대학교', nameEn: 'Hallym University', city: '춘천', type: 'private' },

  // ===== 제주 =====
  { id: 'jeju', nameKo: '제주대학교', nameEn: 'Jeju National University', city: '제주', type: 'national' },

  // ===== 울산 =====
  { id: 'ulsan', nameKo: '울산대학교', nameEn: 'University of Ulsan', city: '울산', type: 'private' },
  { id: 'unist', nameKo: '울산과학기술원', nameEn: 'UNIST', city: '울산', type: 'national' },
];

// 검색 함수
export function searchKoreanUniversities(query: string): KoreanUniversity[] {
  if (!query || query.trim().length === 0) {
    return [];
  }

  const normalizedQuery = query.toLowerCase().trim();

  return koreanUniversities.filter(uni => {
    const searchFields = [
      uni.nameKo.toLowerCase(),
      uni.nameEn.toLowerCase(),
      uni.city.toLowerCase(),
    ];

    return searchFields.some(field => field.includes(normalizedQuery));
  }).slice(0, 20);
}

// 모든 대학 목록
export function getAllKoreanUniversities(): KoreanUniversity[] {
  return koreanUniversities;
}
