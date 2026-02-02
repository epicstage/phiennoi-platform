// 베트남 대학교 전체 리스트 (Vietnam Ministry of Education & Training 기준)
// 자동완성 검색용 데이터

export interface VietnamUniversity {
  id: string;
  nameVi: string;      // 베트남어 이름
  nameEn: string;      // 영어 이름
  nameKo?: string;     // 한국어 이름 (선택)
  abbreviation?: string;
  city: string;
  type: 'national' | 'regional' | 'public' | 'private' | 'foreign';
}

export const vietnamUniversities: VietnamUniversity[] = [
  // ===== 국립대학교 (National Universities) =====
  // Vietnam National University, Hanoi (VNU-HN)
  {
    id: 'vnu-hn',
    nameVi: 'Đại học Quốc gia Hà Nội',
    nameEn: 'Vietnam National University, Hanoi',
    nameKo: '베트남 국립대학교 하노이',
    abbreviation: 'VNU-HN',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-uet',
    nameVi: 'Trường Đại học Công nghệ',
    nameEn: 'University of Engineering and Technology',
    nameKo: '공과대학교 (하노이국립대)',
    abbreviation: 'UET',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-ussh',
    nameVi: 'Trường Đại học Khoa học Xã hội và Nhân văn',
    nameEn: 'University of Social Sciences and Humanities',
    nameKo: '사회과학인문대학교',
    abbreviation: 'USSH',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-hus',
    nameVi: 'Trường Đại học Khoa học Tự nhiên',
    nameEn: 'University of Science',
    nameKo: '자연과학대학교',
    abbreviation: 'HUS',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-ulis',
    nameVi: 'Trường Đại học Ngoại ngữ',
    nameEn: 'University of Languages and International Studies',
    nameKo: '외국어대학교',
    abbreviation: 'ULIS',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-ueb',
    nameVi: 'Trường Đại học Kinh tế',
    nameEn: 'University of Economics and Business',
    nameKo: '경제경영대학교',
    abbreviation: 'UEB',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-vju',
    nameVi: 'Trường Đại học Việt Nhật',
    nameEn: 'Vietnam Japan University',
    nameKo: '베트남일본대학교',
    abbreviation: 'VJU',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-uel',
    nameVi: 'Trường Đại học Luật',
    nameEn: 'University of Law',
    nameKo: '법학대학교',
    abbreviation: 'UEL',
    city: 'Hanoi',
    type: 'national'
  },
  {
    id: 'vnu-hn-ued',
    nameVi: 'Trường Đại học Giáo dục',
    nameEn: 'University of Education',
    nameKo: '교육대학교',
    abbreviation: 'UED',
    city: 'Hanoi',
    type: 'national'
  },

  // Vietnam National University, Ho Chi Minh City (VNU-HCM)
  {
    id: 'vnu-hcm',
    nameVi: 'Đại học Quốc gia Thành phố Hồ Chí Minh',
    nameEn: 'Vietnam National University, Ho Chi Minh City',
    nameKo: '베트남 국립대학교 호치민',
    abbreviation: 'VNU-HCM',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-hcmut',
    nameVi: 'Trường Đại học Bách khoa',
    nameEn: 'Ho Chi Minh City University of Technology',
    nameKo: '호치민공과대학교',
    abbreviation: 'HCMUT',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-hcmus',
    nameVi: 'Trường Đại học Khoa học Tự nhiên',
    nameEn: 'University of Science',
    nameKo: '자연과학대학교 (호치민)',
    abbreviation: 'HCMUS',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-ussh',
    nameVi: 'Trường Đại học Khoa học Xã hội và Nhân văn',
    nameEn: 'University of Social Sciences and Humanities',
    nameKo: '사회과학인문대학교 (호치민)',
    abbreviation: 'USSH-HCM',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-uit',
    nameVi: 'Trường Đại học Công nghệ Thông tin',
    nameEn: 'University of Information Technology',
    nameKo: '정보기술대학교',
    abbreviation: 'UIT',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-uel',
    nameVi: 'Trường Đại học Kinh tế - Luật',
    nameEn: 'University of Economics and Law',
    nameKo: '경제법률대학교',
    abbreviation: 'UEL-HCM',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnu-hcm-iu',
    nameVi: 'Trường Đại học Quốc tế',
    nameEn: 'International University',
    nameKo: '국제대학교',
    abbreviation: 'IU',
    city: 'Ho Chi Minh City',
    type: 'national'
  },

  // ===== 지역거점대학교 (Regional Universities) =====
  // University of Da Nang
  {
    id: 'ud',
    nameVi: 'Đại học Đà Nẵng',
    nameEn: 'University of Da Nang',
    nameKo: '다낭대학교',
    abbreviation: 'UD',
    city: 'Da Nang',
    type: 'regional'
  },
  {
    id: 'ud-dut',
    nameVi: 'Trường Đại học Bách khoa Đà Nẵng',
    nameEn: 'Da Nang University of Science and Technology',
    nameKo: '다낭공과대학교',
    abbreviation: 'DUT',
    city: 'Da Nang',
    type: 'regional'
  },
  {
    id: 'ud-ued',
    nameVi: 'Trường Đại học Sư phạm Đà Nẵng',
    nameEn: 'University of Education - Da Nang',
    nameKo: '다낭사범대학교',
    abbreviation: 'UED-DN',
    city: 'Da Nang',
    type: 'regional'
  },
  {
    id: 'ud-due',
    nameVi: 'Trường Đại học Kinh tế Đà Nẵng',
    nameEn: 'Da Nang University of Economics',
    nameKo: '다낭경제대학교',
    abbreviation: 'DUE',
    city: 'Da Nang',
    type: 'regional'
  },
  {
    id: 'ud-ufl',
    nameVi: 'Trường Đại học Ngoại ngữ Đà Nẵng',
    nameEn: 'University of Foreign Languages - Da Nang',
    nameKo: '다낭외국어대학교',
    abbreviation: 'UFL-DN',
    city: 'Da Nang',
    type: 'regional'
  },

  // Hue University
  {
    id: 'hue',
    nameVi: 'Đại học Huế',
    nameEn: 'Hue University',
    nameKo: '후에대학교',
    abbreviation: 'HU',
    city: 'Hue',
    type: 'regional'
  },
  {
    id: 'hue-hueuni-med',
    nameVi: 'Trường Đại học Y Dược Huế',
    nameEn: 'Hue University of Medicine and Pharmacy',
    nameKo: '후에의약대학교',
    abbreviation: 'HUMP',
    city: 'Hue',
    type: 'regional'
  },
  {
    id: 'hue-hueuni-agr',
    nameVi: 'Trường Đại học Nông Lâm Huế',
    nameEn: 'Hue University of Agriculture and Forestry',
    nameKo: '후에농림대학교',
    abbreviation: 'HUAF',
    city: 'Hue',
    type: 'regional'
  },
  {
    id: 'hue-hueuni-edu',
    nameVi: 'Trường Đại học Sư phạm Huế',
    nameEn: 'Hue University of Education',
    nameKo: '후에사범대학교',
    abbreviation: 'HUED',
    city: 'Hue',
    type: 'regional'
  },
  {
    id: 'hue-hueuni-sci',
    nameVi: 'Trường Đại học Khoa học Huế',
    nameEn: 'Hue University of Sciences',
    nameKo: '후에과학대학교',
    abbreviation: 'HUS-Hue',
    city: 'Hue',
    type: 'regional'
  },

  // Thai Nguyen University
  {
    id: 'tnu',
    nameVi: 'Đại học Thái Nguyên',
    nameEn: 'Thai Nguyen University',
    nameKo: '타이응우옌대학교',
    abbreviation: 'TNU',
    city: 'Thai Nguyen',
    type: 'regional'
  },
  {
    id: 'tnu-tuet',
    nameVi: 'Trường Đại học Kỹ thuật Công nghiệp',
    nameEn: 'Thai Nguyen University of Technology',
    nameKo: '타이응우옌공과대학교',
    abbreviation: 'TNUT',
    city: 'Thai Nguyen',
    type: 'regional'
  },
  {
    id: 'tnu-tuaf',
    nameVi: 'Trường Đại học Nông Lâm',
    nameEn: 'Thai Nguyen University of Agriculture and Forestry',
    nameKo: '타이응우옌농림대학교',
    abbreviation: 'TUAF',
    city: 'Thai Nguyen',
    type: 'regional'
  },

  // ===== 주요 공립대학교 (Major Public Universities) =====
  // Hanoi
  {
    id: 'hust',
    nameVi: 'Trường Đại học Bách khoa Hà Nội',
    nameEn: 'Hanoi University of Science and Technology',
    nameKo: '하노이과학기술대학교',
    abbreviation: 'HUST',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'neu',
    nameVi: 'Trường Đại học Kinh tế Quốc dân',
    nameEn: 'National Economics University',
    nameKo: '국민경제대학교',
    abbreviation: 'NEU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'ftu',
    nameVi: 'Trường Đại học Ngoại thương',
    nameEn: 'Foreign Trade University',
    nameKo: '외국무역대학교',
    abbreviation: 'FTU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hnue',
    nameVi: 'Trường Đại học Sư phạm Hà Nội',
    nameEn: 'Hanoi National University of Education',
    nameKo: '하노이사범대학교',
    abbreviation: 'HNUE',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hanu',
    nameVi: 'Trường Đại học Hà Nội',
    nameEn: 'Hanoi University',
    nameKo: '하노이대학교',
    abbreviation: 'HANU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hua',
    nameVi: 'Học viện Nông nghiệp Việt Nam',
    nameEn: 'Vietnam National University of Agriculture',
    nameKo: '베트남국립농업대학교',
    abbreviation: 'VNUA',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hmu',
    nameVi: 'Trường Đại học Y Hà Nội',
    nameEn: 'Hanoi Medical University',
    nameKo: '하노이의과대학교',
    abbreviation: 'HMU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'ntu',
    nameVi: 'Trường Đại học Giao thông Vận tải',
    nameEn: 'University of Transport and Communications',
    nameKo: '교통통신대학교',
    abbreviation: 'UTC',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hau',
    nameVi: 'Trường Đại học Kiến trúc Hà Nội',
    nameEn: 'Hanoi Architectural University',
    nameKo: '하노이건축대학교',
    abbreviation: 'HAU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'ptit',
    nameVi: 'Học viện Công nghệ Bưu chính Viễn thông',
    nameEn: 'Posts and Telecommunications Institute of Technology',
    nameKo: '우전통신기술학원',
    abbreviation: 'PTIT',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hvtc',
    nameVi: 'Học viện Tài chính',
    nameEn: 'Academy of Finance',
    nameKo: '재정학원',
    abbreviation: 'AOF',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hvnh',
    nameVi: 'Học viện Ngân hàng',
    nameEn: 'Banking Academy',
    nameKo: '은행학원',
    abbreviation: 'BA',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'dav',
    nameVi: 'Học viện Ngoại giao',
    nameEn: 'Diplomatic Academy of Vietnam',
    nameKo: '외교학원',
    abbreviation: 'DAV',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'vnu-law',
    nameVi: 'Trường Đại học Luật Hà Nội',
    nameEn: 'Hanoi Law University',
    nameKo: '하노이법과대학교',
    abbreviation: 'HLU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'vaa',
    nameVi: 'Học viện Hàng không Việt Nam',
    nameEn: 'Vietnam Aviation Academy',
    nameKo: '베트남항공학원',
    abbreviation: 'VAA',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hubt',
    nameVi: 'Trường Đại học Kinh doanh và Công nghệ Hà Nội',
    nameEn: 'Hanoi University of Business and Technology',
    nameKo: '하노이경영기술대학교',
    abbreviation: 'HUBT',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'huce',
    nameVi: 'Trường Đại học Xây dựng Hà Nội',
    nameEn: 'Hanoi University of Civil Engineering',
    nameKo: '하노이건설대학교',
    abbreviation: 'HUCE',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'nuce',
    nameVi: 'Trường Đại học Xây dựng',
    nameEn: 'National University of Civil Engineering',
    nameKo: '국립건설대학교',
    abbreviation: 'NUCE',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'ueh-hn',
    nameVi: 'Trường Đại học Thương mại',
    nameEn: 'Thuongmai University',
    nameKo: '상업대학교',
    abbreviation: 'TMU',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'vnuad',
    nameVi: 'Học viện Âm nhạc Quốc gia Việt Nam',
    nameEn: 'Vietnam National Academy of Music',
    nameKo: '베트남국립음악학원',
    abbreviation: 'VNAM',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'vufa',
    nameVi: 'Trường Đại học Mỹ thuật Việt Nam',
    nameEn: 'Vietnam University of Fine Arts',
    nameKo: '베트남미술대학교',
    abbreviation: 'VUFA',
    city: 'Hanoi',
    type: 'public'
  },

  // Ho Chi Minh City
  {
    id: 'ueh',
    nameVi: 'Trường Đại học Kinh tế TP. Hồ Chí Minh',
    nameEn: 'University of Economics Ho Chi Minh City',
    nameKo: '호치민경제대학교',
    abbreviation: 'UEH',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'hcmute',
    nameVi: 'Trường Đại học Sư phạm Kỹ thuật TP.HCM',
    nameEn: 'Ho Chi Minh City University of Technology and Education',
    nameKo: '호치민기술교육대학교',
    abbreviation: 'HCMUTE',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'hcmup',
    nameVi: 'Trường Đại học Sư phạm TP.HCM',
    nameEn: 'Ho Chi Minh City University of Education',
    nameKo: '호치민사범대학교',
    abbreviation: 'HCMUE',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'nlu',
    nameVi: 'Trường Đại học Nông Lâm TP.HCM',
    nameEn: 'Nong Lam University',
    nameKo: '농림대학교',
    abbreviation: 'NLU',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'ump',
    nameVi: 'Trường Đại học Y Dược TP.HCM',
    nameEn: 'University of Medicine and Pharmacy at HCMC',
    nameKo: '호치민의약대학교',
    abbreviation: 'UMP',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'hcmuaf',
    nameVi: 'Trường Đại học Công nghiệp TP.HCM',
    nameEn: 'Industrial University of Ho Chi Minh City',
    nameKo: '호치민산업대학교',
    abbreviation: 'IUH',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'uah',
    nameVi: 'Trường Đại học Kiến trúc TP.HCM',
    nameEn: 'University of Architecture Ho Chi Minh City',
    nameKo: '호치민건축대학교',
    abbreviation: 'UAH',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'ufm',
    nameVi: 'Trường Đại học Tài chính - Marketing',
    nameEn: 'University of Finance - Marketing',
    nameKo: '재정마케팅대학교',
    abbreviation: 'UFM',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'ulaw',
    nameVi: 'Trường Đại học Luật TP.HCM',
    nameEn: 'Ho Chi Minh City University of Law',
    nameKo: '호치민법과대학교',
    abbreviation: 'HCMULAW',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'ou',
    nameVi: 'Trường Đại học Mở TP.HCM',
    nameEn: 'Ho Chi Minh City Open University',
    nameKo: '호치민방송통신대학교',
    abbreviation: 'OU',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'hcmuns',
    nameVi: 'Trường Đại học Khoa học Tự nhiên TP.HCM',
    nameEn: 'University of Science - HCMC',
    nameKo: '호치민자연과학대학교',
    abbreviation: 'HCMUNS',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'huflit',
    nameVi: 'Trường Đại học Ngoại ngữ - Tin học TP.HCM',
    nameEn: 'HCMC University of Foreign Languages - Information Technology',
    nameKo: '호치민외국어정보기술대학교',
    abbreviation: 'HUFLIT',
    city: 'Ho Chi Minh City',
    type: 'public'
  },

  // Can Tho
  {
    id: 'ctu',
    nameVi: 'Trường Đại học Cần Thơ',
    nameEn: 'Can Tho University',
    nameKo: '껀터대학교',
    abbreviation: 'CTU',
    city: 'Can Tho',
    type: 'public'
  },
  {
    id: 'ctump',
    nameVi: 'Trường Đại học Y Dược Cần Thơ',
    nameEn: 'Can Tho University of Medicine and Pharmacy',
    nameKo: '껀터의약대학교',
    abbreviation: 'CTUMP',
    city: 'Can Tho',
    type: 'public'
  },

  // Other major cities
  {
    id: 'hpu',
    nameVi: 'Trường Đại học Hải Phòng',
    nameEn: 'Hai Phong University',
    nameKo: '하이퐁대학교',
    abbreviation: 'HPU',
    city: 'Hai Phong',
    type: 'public'
  },
  {
    id: 'vimaru',
    nameVi: 'Trường Đại học Hàng hải Việt Nam',
    nameEn: 'Vietnam Maritime University',
    nameKo: '베트남해양대학교',
    abbreviation: 'VMU',
    city: 'Hai Phong',
    type: 'public'
  },
  {
    id: 'ntu-nt',
    nameVi: 'Trường Đại học Nha Trang',
    nameEn: 'Nha Trang University',
    nameKo: '나짱대학교',
    abbreviation: 'NTU',
    city: 'Nha Trang',
    type: 'public'
  },
  {
    id: 'qnu',
    nameVi: 'Trường Đại học Quy Nhơn',
    nameEn: 'Quy Nhon University',
    nameKo: '꾸이년대학교',
    abbreviation: 'QNU',
    city: 'Quy Nhon',
    type: 'public'
  },
  {
    id: 'dlu',
    nameVi: 'Trường Đại học Đà Lạt',
    nameEn: 'Da Lat University',
    nameKo: '달랏대학교',
    abbreviation: 'DLU',
    city: 'Da Lat',
    type: 'public'
  },
  {
    id: 'vinhuni',
    nameVi: 'Trường Đại học Vinh',
    nameEn: 'Vinh University',
    nameKo: '빈대학교',
    abbreviation: 'VU',
    city: 'Vinh',
    type: 'public'
  },
  {
    id: 'tdu',
    nameVi: 'Trường Đại học Tây Đô',
    nameEn: 'Tay Do University',
    nameKo: '떠이도대학교',
    abbreviation: 'TDU',
    city: 'Can Tho',
    type: 'public'
  },
  {
    id: 'bdu',
    nameVi: 'Trường Đại học Bình Dương',
    nameEn: 'Binh Duong University',
    nameKo: '빈즈엉대학교',
    abbreviation: 'BDU',
    city: 'Binh Duong',
    type: 'public'
  },
  {
    id: 'tdtu',
    nameVi: 'Trường Đại học Tôn Đức Thắng',
    nameEn: 'Ton Duc Thang University',
    nameKo: '톤득탕대학교',
    abbreviation: 'TDTU',
    city: 'Ho Chi Minh City',
    type: 'public'
  },

  // ===== 주요 사립대학교 (Major Private Universities) =====
  {
    id: 'fpt',
    nameVi: 'Trường Đại học FPT',
    nameEn: 'FPT University',
    nameKo: 'FPT대학교',
    abbreviation: 'FPTU',
    city: 'Hanoi',
    type: 'private'
  },
  {
    id: 'rmit',
    nameVi: 'Đại học RMIT Việt Nam',
    nameEn: 'RMIT University Vietnam',
    nameKo: 'RMIT 베트남',
    abbreviation: 'RMIT',
    city: 'Ho Chi Minh City',
    type: 'foreign'
  },
  {
    id: 'vgu',
    nameVi: 'Trường Đại học Việt Đức',
    nameEn: 'Vietnamese-German University',
    nameKo: '베트남독일대학교',
    abbreviation: 'VGU',
    city: 'Binh Duong',
    type: 'foreign'
  },
  {
    id: 'siu',
    nameVi: 'Trường Đại học Quốc tế Sài Gòn',
    nameEn: 'Saigon International University',
    nameKo: '사이공국제대학교',
    abbreviation: 'SIU',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'hiu',
    nameVi: 'Trường Đại học Quốc tế Hồng Bàng',
    nameEn: 'Hong Bang International University',
    nameKo: '홍방국제대학교',
    abbreviation: 'HIU',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'hutech',
    nameVi: 'Trường Đại học Công nghệ TP.HCM',
    nameEn: 'Ho Chi Minh City University of Technology',
    nameKo: '호치민기술대학교',
    abbreviation: 'HUTECH',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'vlu',
    nameVi: 'Trường Đại học Văn Lang',
    nameEn: 'Van Lang University',
    nameKo: '반랑대학교',
    abbreviation: 'VLU',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'hcmiu',
    nameVi: 'Trường Đại học Công nghệ Sài Gòn',
    nameEn: 'Saigon Technology University',
    nameKo: '사이공기술대학교',
    abbreviation: 'STU',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'duy-tan',
    nameVi: 'Trường Đại học Duy Tân',
    nameEn: 'Duy Tan University',
    nameKo: '주이떤대학교',
    abbreviation: 'DTU',
    city: 'Da Nang',
    type: 'private'
  },
  {
    id: 'tdmu',
    nameVi: 'Trường Đại học Thủ Dầu Một',
    nameEn: 'Thu Dau Mot University',
    nameKo: '투저우못대학교',
    abbreviation: 'TDMU',
    city: 'Binh Duong',
    type: 'private'
  },
  {
    id: 'eiu',
    nameVi: 'Trường Đại học Quốc tế Miền Đông',
    nameEn: 'Eastern International University',
    nameKo: '동부국제대학교',
    abbreviation: 'EIU',
    city: 'Binh Duong',
    type: 'private'
  },
  {
    id: 'buh',
    nameVi: 'Trường Đại học Ngân hàng TP.HCM',
    nameEn: 'Banking University of Ho Chi Minh City',
    nameKo: '호치민은행대학교',
    abbreviation: 'BUH',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'hcmc-ou',
    nameVi: 'Trường Đại học Mở TP.HCM',
    nameEn: 'Ho Chi Minh City Open University',
    nameKo: '호치민개방대학교',
    abbreviation: 'HCMCOU',
    city: 'Ho Chi Minh City',
    type: 'private'
  },
  {
    id: 'agu',
    nameVi: 'Trường Đại học An Giang',
    nameEn: 'An Giang University',
    nameKo: '안장대학교',
    abbreviation: 'AGU',
    city: 'An Giang',
    type: 'public'
  },
  {
    id: 'vnuf',
    nameVi: 'Trường Đại học Lâm nghiệp',
    nameEn: 'Vietnam National University of Forestry',
    nameKo: '베트남국립임업대학교',
    abbreviation: 'VNUF',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hvct',
    nameVi: 'Học viện Chính trị Quốc gia Hồ Chí Minh',
    nameEn: 'Ho Chi Minh National Academy of Politics',
    nameKo: '호치민정치학원',
    abbreviation: 'HCMA',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'hvu',
    nameVi: 'Trường Đại học Hùng Vương',
    nameEn: 'Hung Vuong University',
    nameKo: '흥브엉대학교',
    abbreviation: 'HVU',
    city: 'Phu Tho',
    type: 'public'
  },
  {
    id: 'tnut',
    nameVi: 'Trường Đại học Kỹ thuật Công nghiệp Thái Nguyên',
    nameEn: 'Thai Nguyen University of Technology',
    nameKo: '타이응우옌기술대학교',
    abbreviation: 'TNUT',
    city: 'Thai Nguyen',
    type: 'public'
  },
  {
    id: 'bku',
    nameVi: 'Trường Đại học Bách khoa - ĐHQG TP.HCM',
    nameEn: 'Bach Khoa University - VNU HCMC',
    nameKo: '백과대학교 (국립호치민대)',
    abbreviation: 'BKU',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'vnuhcm-us',
    nameVi: 'Trường Đại học Khoa học Tự nhiên - ĐHQG TP.HCM',
    nameEn: 'University of Science - VNU HCMC',
    nameKo: '자연과학대학교 (국립호치민대)',
    abbreviation: 'HCMUS',
    city: 'Ho Chi Minh City',
    type: 'national'
  },
  {
    id: 'thanglong',
    nameVi: 'Trường Đại học Thăng Long',
    nameEn: 'Thang Long University',
    nameKo: '탕롱대학교',
    abbreviation: 'TLU',
    city: 'Hanoi',
    type: 'private'
  },
  {
    id: 'phenikaa',
    nameVi: 'Trường Đại học Phenikaa',
    nameEn: 'Phenikaa University',
    nameKo: '페니카대학교',
    abbreviation: 'PU',
    city: 'Hanoi',
    type: 'private'
  },
  {
    id: 'vinuni',
    nameVi: 'Trường Đại học VinUni',
    nameEn: 'VinUniversity',
    nameKo: '빈대학교',
    abbreviation: 'VinUni',
    city: 'Hanoi',
    type: 'private'
  },
  {
    id: 'fulbright',
    nameVi: 'Trường Đại học Fulbright Việt Nam',
    nameEn: 'Fulbright University Vietnam',
    nameKo: '풀브라이트베트남대학교',
    abbreviation: 'FUV',
    city: 'Ho Chi Minh City',
    type: 'foreign'
  },
  {
    id: 'sgu',
    nameVi: 'Trường Đại học Sài Gòn',
    nameEn: 'Saigon University',
    nameKo: '사이공대학교',
    abbreviation: 'SGU',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'utc2',
    nameVi: 'Trường Đại học Giao thông Vận tải TP.HCM',
    nameEn: 'Ho Chi Minh City University of Transport',
    nameKo: '호치민교통대학교',
    abbreviation: 'UT-HCMC',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'tvu',
    nameVi: 'Trường Đại học Trà Vinh',
    nameEn: 'Tra Vinh University',
    nameKo: '짜빈대학교',
    abbreviation: 'TVU',
    city: 'Tra Vinh',
    type: 'public'
  },
  {
    id: 'dtu-dnang',
    nameVi: 'Trường Đại học Đông Á',
    nameEn: 'Dong A University',
    nameKo: '동아대학교',
    abbreviation: 'DAU',
    city: 'Da Nang',
    type: 'private'
  },
  {
    id: 'bru',
    nameVi: 'Trường Đại học Bà Rịa - Vũng Tàu',
    nameEn: 'Ba Ria - Vung Tau University',
    nameKo: '바리아붕따우대학교',
    abbreviation: 'BVU',
    city: 'Vung Tau',
    type: 'public'
  },
  {
    id: 'pvmtu',
    nameVi: 'Trường Đại học Dầu khí Việt Nam',
    nameEn: 'Petrovietnam University',
    nameKo: '베트남석유대학교',
    abbreviation: 'PVU',
    city: 'Ba Ria',
    type: 'public'
  },
  {
    id: 'lhu',
    nameVi: 'Trường Đại học Lạc Hồng',
    nameEn: 'Lac Hong University',
    nameKo: '락홍대학교',
    abbreviation: 'LHU',
    city: 'Dong Nai',
    type: 'private'
  },
  {
    id: 'udn',
    nameVi: 'Trường Đại học Đồng Nai',
    nameEn: 'Dong Nai University',
    nameKo: '동나이대학교',
    abbreviation: 'DNU',
    city: 'Dong Nai',
    type: 'public'
  },
  {
    id: 'ktu',
    nameVi: 'Trường Đại học Khánh Hòa',
    nameEn: 'Khanh Hoa University',
    nameKo: '카인호아대학교',
    abbreviation: 'KHU',
    city: 'Nha Trang',
    type: 'public'
  },
  {
    id: 'hcmunre',
    nameVi: 'Trường Đại học Tài nguyên và Môi trường TP.HCM',
    nameEn: 'Ho Chi Minh City University of Natural Resources and Environment',
    nameKo: '호치민자원환경대학교',
    abbreviation: 'HCMUNRE',
    city: 'Ho Chi Minh City',
    type: 'public'
  },
  {
    id: 'hunre',
    nameVi: 'Trường Đại học Tài nguyên và Môi trường Hà Nội',
    nameEn: 'Hanoi University of Natural Resources and Environment',
    nameKo: '하노이자원환경대학교',
    abbreviation: 'HUNRE',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'mta',
    nameVi: 'Học viện Kỹ thuật Quân sự',
    nameEn: 'Military Technical Academy',
    nameKo: '군사기술학원',
    abbreviation: 'MTA',
    city: 'Hanoi',
    type: 'public'
  },
  {
    id: 'ppa',
    nameVi: 'Học viện Cảnh sát Nhân dân',
    nameEn: "People's Police Academy",
    nameKo: '인민경찰학원',
    abbreviation: 'PPA',
    city: 'Hanoi',
    type: 'public'
  },
];

// 검색 함수: 이름(베트남어, 영어, 한국어), 약어, 도시로 검색
export function searchUniversities(query: string): VietnamUniversity[] {
  if (!query || query.trim().length === 0) {
    return [];
  }

  const normalizedQuery = query.toLowerCase().trim();

  // 정확한 약어 매치 먼저
  const exactAbbrevMatch = vietnamUniversities.filter(
    uni => uni.abbreviation?.toLowerCase() === normalizedQuery
  );
  if (exactAbbrevMatch.length > 0) {
    return exactAbbrevMatch;
  }

  // 부분 매치
  return vietnamUniversities.filter(uni => {
    const searchFields = [
      uni.nameVi.toLowerCase(),
      uni.nameEn.toLowerCase(),
      uni.nameKo?.toLowerCase() || '',
      uni.abbreviation?.toLowerCase() || '',
      uni.city.toLowerCase(),
    ];

    return searchFields.some(field => field.includes(normalizedQuery));
  }).slice(0, 20); // 최대 20개 결과
}

// 도시별 대학 필터
export function getUniversitiesByCity(city: string): VietnamUniversity[] {
  return vietnamUniversities.filter(
    uni => uni.city.toLowerCase() === city.toLowerCase()
  );
}

// 유형별 대학 필터
export function getUniversitiesByType(type: VietnamUniversity['type']): VietnamUniversity[] {
  return vietnamUniversities.filter(uni => uni.type === type);
}

// ID로 대학 찾기
export function getUniversityById(id: string): VietnamUniversity | undefined {
  return vietnamUniversities.find(uni => uni.id === id);
}

// 모든 도시 목록
export function getAllCities(): string[] {
  const cities = new Set(vietnamUniversities.map(uni => uni.city));
  return Array.from(cities).sort();
}

// 통계
export function getUniversityStats() {
  return {
    total: vietnamUniversities.length,
    byType: {
      national: vietnamUniversities.filter(u => u.type === 'national').length,
      regional: vietnamUniversities.filter(u => u.type === 'regional').length,
      public: vietnamUniversities.filter(u => u.type === 'public').length,
      private: vietnamUniversities.filter(u => u.type === 'private').length,
      foreign: vietnamUniversities.filter(u => u.type === 'foreign').length,
    },
    cities: getAllCities().length,
  };
}
