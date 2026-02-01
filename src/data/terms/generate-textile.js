const fs = require('fs');
const path = require('path');

const existing = JSON.parse(fs.readFileSync(path.join(__dirname, 'textile.json'), 'utf8'));

const newTerms = [
  {
    slug: "vai-denim",
    korean: "데님",
    vietnamese: "vải denim",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "면사를 능직(twill)으로 짠 두꺼운 직물로, 청바지(jeans)의 대표 소재입니다. 경사에 인디고 염색, 위사에 미염색 실을 사용하여 특유의 색감을 냅니다. 베트남은 세계적인 데님 의류 수출국으로, 한국 바이어의 데님 제품 발주가 활발합니다. 통역 시 데님의 중량(oz)과 가공법을 정확히 전달해야 합니다.",
    meaningVi: "Vải dày dệt chéo (twill) từ sợi bông, là chất liệu đại diện của quần jeans. Sử dụng sợi dọc nhuộm indigo và sợi ngang không nhuộm tạo màu đặc trưng. Việt Nam là nước xuất khẩu quần áo denim hàng đầu thế giới, đơn hàng denim từ buyer Hàn Quốc rất sôi động.",
    pronunciation: "denim",
    commonMistakes: ["denim과 jeans를 혼동 - denim은 원단, jeans는 제품", "데님 중량 단위 oz(온스)를 모름", "워싱(washing) 가공 종류를 구분하지 못함"],
    culturalNote: "베트남의 데님 산업은 호치민 인근에 집중되어 있으며, 친환경 데님 가공(레이저 워싱, 오존 워싱)이 트렌드입니다.",
    context: "원단, 청바지, 캐주얼 의류",
    examples: [
      { ko: "이 데님 원단의 중량과 워싱 가공을 확인해 주세요.", vi: "Xin hãy kiểm tra trọng lượng và gia công washing của vải denim này.", situation: "formal" },
      { ko: "데님 샘플 워싱 결과 어때?", vi: "Kết quả washing mẫu denim thế nào?", situation: "onsite" },
      { ko: "요즘 가벼운 데님이 인기야.", vi: "Dạo này denim nhẹ đang được ưa chuộng.", situation: "informal" }
    ],
    relatedTerms: ["면", "직물", "워싱", "인디고"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  },
  {
    slug: "vai-voan",
    korean: "시폰",
    vietnamese: "vải voan",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "가볍고 투명한 직물로, 폴리에스터나 실크로 만들어집니다. 드레이프성이 뛰어나 여성 드레스, 블라우스, 스카프에 사용됩니다. 베트남에서 시폰 원단은 열대 기후에 적합한 가벼운 의류 생산에 많이 사용되며, 한국 패션 브랜드의 시폰 제품 발주가 꾸준합니다. 통역 시 시폰의 소재 조성과 두께를 정확히 전달해야 합니다.",
    meaningVi: "Vải nhẹ và trong suốt, được làm từ polyester hoặc lụa. Có độ rủ tuyệt vời nên dùng cho đầm, áo kiểu, khăn quàng nữ. Tại Việt Nam vải voan dùng nhiều cho sản xuất quần áo nhẹ phù hợp khí hậu nhiệt đới, đơn hàng sản phẩm voan từ thương hiệu thời trang Hàn Quốc ổn định.",
    pronunciation: "sipon",
    commonMistakes: ["voan과 tulle(튤)을 혼동", "시폰의 소재가 반드시 실크라고 오해", "vải voan의 발음 주의"],
    culturalNote: "베트남 여성 전통 의상 아오자이(áo dài)에도 시폰 소재가 많이 사용되어, 시폰은 베트남에서 매우 친숙한 원단입니다.",
    context: "여성 의류, 원단, 패션",
    examples: [
      { ko: "시폰 원단의 투명도와 드레이프성을 확인합니다.", vi: "Kiểm tra độ trong suốt và độ rủ của vải voan.", situation: "formal" },
      { ko: "시폰 원단 좀 더 두꺼운 건 없어?", vi: "Có vải voan dày hơn không?", situation: "onsite" },
      { ko: "시폰은 가벼워서 여름에 딱이야.", vi: "Vải voan nhẹ nên hợp mùa hè.", situation: "informal" }
    ],
    relatedTerms: ["실크", "폴리에스터", "드레스", "블라우스"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "spandex",
    korean: "스판덱스",
    vietnamese: "spandex",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "폴리우레탄 계열의 합성 탄성 섬유로, 라이크라(Lycra)라고도 합니다. 원래 길이의 5~8배까지 늘어나는 뛰어난 신축성이 특징이며, 다른 섬유와 혼방하여 사용됩니다. 베트남에서 스판덱스 혼방 원단은 스포츠웨어, 속옷, 레깅스 생산에 핵심 소재입니다. 통역 시 스판덱스 혼용률(예: 5%)을 정확히 전달해야 합니다.",
    meaningVi: "Sợi tổng hợp đàn hồi thuộc họ polyurethane, còn gọi là Lycra. Có khả năng co giãn 5-8 lần chiều dài gốc, thường pha trộn với sợi khác. Tại Việt Nam vải pha spandex là nguyên liệu then chốt cho sản xuất đồ thể thao, đồ lót, legging.",
    pronunciation: "seupandekseu",
    commonMistakes: ["spandex와 Lycra가 같은 소재임을 모름", "스판덱스와 elastane이 동의어임을 모름", "혼용률 표기법(예: 95% cotton 5% spandex)을 모름"],
    culturalNote: "베트남에서 한국 기업이 스판덱스 원사 공장을 운영하고 있으며, 효성(Hyosung)이 대표적인 투자 기업입니다.",
    context: "소재, 기능성, 스포츠웨어",
    examples: [
      { ko: "이 원단의 스판덱스 혼용률을 확인해 주세요.", vi: "Xin hãy kiểm tra tỷ lệ pha spandex của vải này.", situation: "formal" },
      { ko: "스판덱스 비율이 좀 더 높아야 할 것 같은데.", vi: "Hình như tỷ lệ spandex phải cao hơn.", situation: "onsite" },
      { ko: "스판덱스 들어가야 신축성이 나오지.", vi: "Phải có spandex thì mới co giãn được.", situation: "informal" }
    ],
    relatedTerms: ["폴리에스터", "나일론", "신축성", "라이크라"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  },
  {
    slug: "vai-lanh",
    korean: "린넨",
    vietnamese: "vải lanh",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "아마(flax) 식물에서 얻는 천연 섬유로, 면보다 강하고 흡습성과 통기성이 뛰어납니다. 린넨 원단은 여름 의류에 적합하며, 구김이 잘 가는 특성이 있습니다. 베트남에서 린넨 혼방 제품의 수요가 증가하고 있으며, 한국 바이어의 린넨 의류 발주가 활발합니다. 통역 시 린넨의 등급과 혼방 비율을 전달해야 합니다.",
    meaningVi: "Sợi tự nhiên từ cây lanh (flax), bền hơn bông và có khả năng hút ẩm, thoáng khí tuyệt vời. Vải lanh phù hợp quần áo mùa hè nhưng dễ nhăn. Nhu cầu sản phẩm pha lanh tại Việt Nam đang tăng, đơn hàng quần áo lanh từ buyer Hàn Quốc rất sôi động.",
    pronunciation: "rinnen",
    commonMistakes: ["vải lanh(린넨)과 vải bố(캔버스)를 혼동", "린넨과 리넨의 표기 차이", "린넨의 구김 특성을 결함으로 오해"],
    culturalNote: "베트남에서 린넨은 고급 소재로 인식되며, 한국 리조트웨어 브랜드의 베트남 생산 린넨 의류가 인기입니다.",
    context: "천연 소재, 여름 의류, 고급",
    examples: [
      { ko: "린넨 원단의 수축률과 촉감을 확인합니다.", vi: "Kiểm tra tỷ lệ co rút và cảm giác sờ của vải lanh.", situation: "formal" },
      { ko: "린넨 구김 방지 가공 됐어?", vi: "Vải lanh đã xử lý chống nhăn chưa?", situation: "onsite" },
      { ko: "린넨은 여름에 시원하지만 구김이 문제야.", vi: "Vải lanh mát vào mùa hè nhưng nhăn là vấn đề.", situation: "informal" }
    ],
    relatedTerms: ["면", "천연섬유", "여름의류", "아마"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "viscose",
    korean: "비스코스",
    vietnamese: "viscose",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "목재 펄프의 셀룰로스를 화학적으로 용해하여 재생한 섬유로, 레이온의 대표적 형태입니다. 면과 유사한 흡습성과 부드러운 촉감을 가지며, 드레이프성이 좋아 여성 의류에 많이 사용됩니다. 베트남에서 비스코스 원단 수요가 꾸준히 증가하고 있으며, 가격이 면보다 저렴하여 대량 생산 의류에 적합합니다.",
    meaningVi: "Sợi tái sinh từ cellulose bột gỗ hòa tan bằng hóa chất, là dạng đại diện của rayon. Có hút ẩm tương tự bông và cảm giác sờ mềm mại, độ rủ tốt nên dùng nhiều cho quần áo nữ. Nhu cầu vải viscose tại Việt Nam tăng đều, giá rẻ hơn bông nên phù hợp sản xuất hàng loạt.",
    pronunciation: "bisukoseu",
    commonMistakes: ["viscose와 polyester를 혼동", "비스코스와 레이온이 같은 계열임을 모름", "비스코스의 세탁 수축 특성을 간과"],
    culturalNote: "베트남 열대 기후에서 비스코스의 통기성과 가벼움이 장점으로, 현지 시장용 의류에도 많이 사용됩니다.",
    context: "소재, 재생섬유, 여성의류",
    examples: [
      { ko: "비스코스 원단의 세탁 수축률을 테스트합니다.", vi: "Kiểm tra tỷ lệ co rút khi giặt của vải viscose.", situation: "formal" },
      { ko: "비스코스 원단 색상이 잘 나왔어?", vi: "Màu vải viscose ra đẹp không?", situation: "onsite" },
      { ko: "비스코스가 면보다 싸고 촉감도 좋아.", vi: "Viscose rẻ hơn bông mà cảm giác sờ cũng tốt.", situation: "informal" }
    ],
    relatedTerms: ["레이온", "면", "텐셀", "모달"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "modal",
    korean: "모달",
    vietnamese: "modal",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "너도밤나무 펄프에서 추출한 고급 재생 섬유로, 비스코스보다 강도와 흡습성이 우수합니다. 면보다 50% 더 높은 흡습력을 가지며, 속옷과 라운지웨어에 많이 사용됩니다. 베트남에서 모달 혼방 속옷 생산이 증가하고 있으며, 한국 속옷 브랜드의 모달 제품 OEM 생산이 활발합니다.",
    meaningVi: "Sợi tái sinh cao cấp từ bột gỗ sồi, có độ bền và hút ẩm tốt hơn viscose. Hút ẩm cao hơn bông 50%, dùng nhiều cho đồ lót và loungewear. Sản xuất đồ lót pha modal tại Việt Nam đang tăng, sản xuất OEM sản phẩm modal cho thương hiệu đồ lót Hàn Quốc rất sôi động.",
    pronunciation: "modal",
    commonMistakes: ["modal과 viscose의 차이를 모름", "모달이 천연인지 합성인지 혼동", "모달과 텐셀의 차이를 구분하지 못함"],
    culturalNote: "한국 속옷 시장에서 모달 소재가 인기이며, 베트남 공장에서 한국 속옷 브랜드의 모달 제품을 대량 생산하고 있습니다.",
    context: "소재, 속옷, 고급 재생섬유",
    examples: [
      { ko: "모달 원단의 필링 테스트 결과를 확인합니다.", vi: "Kiểm tra kết quả test pilling của vải modal.", situation: "formal" },
      { ko: "모달 혼방 비율 어떻게 잡을까?", vi: "Tỷ lệ pha modal tính thế nào?", situation: "onsite" },
      { ko: "모달이 면보다 부드럽고 잘 안 줄어들어.", vi: "Modal mềm hơn bông và ít co rút hơn.", situation: "informal" }
    ],
    relatedTerms: ["비스코스", "텐셀", "레이온", "속옷"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "tencel",
    korean: "텐셀",
    vietnamese: "tencel",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "유칼립투스 나무 펄프에서 친환경 공정으로 생산한 리오셀(Lyocell) 섬유의 브랜드명입니다. 부드러운 촉감, 우수한 흡습성, 생분해성이 특징이며, 친환경 패션의 핵심 소재입니다. 베트남에서 텐셀 원단을 사용한 지속가능 패션 제품 생산이 증가하고 있으며, 한국 바이어의 친환경 소재 요구가 높아지고 있습니다.",
    meaningVi: "Tên thương hiệu của sợi Lyocell sản xuất từ bột gỗ bạch đàn bằng quy trình thân thiện môi trường. Có cảm giác sờ mềm mại, hút ẩm tốt, phân hủy sinh học. Sản xuất sản phẩm thời trang bền vững sử dụng vải tencel tại Việt Nam đang tăng, yêu cầu chất liệu thân thiện môi trường từ buyer Hàn Quốc ngày càng cao.",
    pronunciation: "tensel",
    commonMistakes: ["텐셀과 리오셀이 같은 소재임을 모름", "텐셀이 합성섬유라고 오해", "Tencel이 Lenzing사의 상표명임을 모름"],
    culturalNote: "한국 소비자의 친환경 의식이 높아지면서 텐셀 소재 수요가 급증하고 있으며, 베트남 공장에서의 텐셀 제품 생산도 확대 중입니다.",
    context: "친환경, 소재, 지속가능 패션",
    examples: [
      { ko: "텐셀 원단의 인증서를 확인해 주세요.", vi: "Xin hãy kiểm tra chứng nhận của vải tencel.", situation: "formal" },
      { ko: "텐셀 원단 촉감 확인해 봐.", vi: "Kiểm tra cảm giác sờ vải tencel đi.", situation: "onsite" },
      { ko: "텐셀은 친환경이라 요즘 잘 나가.", vi: "Tencel thân thiện môi trường nên dạo này bán chạy.", situation: "informal" }
    ],
    relatedTerms: ["리오셀", "비스코스", "모달", "친환경"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "vai-gai",
    korean: "대마",
    vietnamese: "vải gai",
    hanja: "大麻",
    hanjaReading: "대(큰 대) + 마(삼 마)",
    termType: "word",
    meaningKo: "대마(hemp) 식물에서 얻는 천연 섬유로, 매우 강하고 내구성이 뛰어납니다. 통기성과 항균성이 좋아 친환경 섬유로 주목받고 있으며, 면보다 적은 물과 농약으로 재배됩니다. 베트남에서는 소수민족 전통 직물에 대마가 사용되며, 최근 친환경 패션 트렌드와 함께 관심이 높아지고 있습니다.",
    meaningVi: "Sợi tự nhiên từ cây gai dầu (hemp), rất bền và có độ bền cao. Thoáng khí và kháng khuẩn tốt nên được chú ý là sợi thân thiện môi trường, cần ít nước và thuốc trừ sâu hơn bông. Tại Việt Nam vải gai được dùng trong dệt truyền thống dân tộc thiểu số, gần đây được quan tâm cùng xu hướng thời trang bền vững.",
    pronunciation: "daema",
    commonMistakes: ["vải gai(대마)와 vải bố(캔버스)를 혼동", "대마 섬유와 마리화나를 연관짓는 오해", "hemp와 linen을 혼동"],
    culturalNote: "베트남 북부 소수민족인 흐몽(Hmong)족은 전통적으로 대마 섬유를 사용하여 직물을 짜며, 이는 관광 상품으로도 가치가 높습니다.",
    context: "천연섬유, 친환경, 전통",
    examples: [
      { ko: "대마 혼방 원단의 촉감과 내구성을 테스트합니다.", vi: "Kiểm tra cảm giác sờ và độ bền của vải pha gai.", situation: "formal" },
      { ko: "대마 원단 가격이 좀 비싸지 않아?", vi: "Giá vải gai hơi đắt không?", situation: "onsite" },
      { ko: "대마는 친환경이라 유럽에서 수요가 많아.", vi: "Vải gai thân thiện môi trường nên nhu cầu ở châu Âu nhiều.", situation: "informal" }
    ],
    relatedTerms: ["린넨", "천연섬유", "친환경", "지속가능"],
    difficulty: "advanced",
    frequency: 2,
    formalLevel: "neutral"
  },
  {
    slug: "det",
    korean: "제직",
    vietnamese: "dệt",
    hanja: "製織",
    hanjaReading: "제(만들 제) + 직(짤 직)",
    termType: "word",
    meaningKo: "실(원사)을 경사와 위사로 교차시켜 원단을 만드는 공정입니다. 평직, 능직, 수자직 등 다양한 조직으로 제직할 수 있으며, 직기(loom)를 사용합니다. 베트남의 제직 공장은 편직에 비해 적은 편이며, 직물 원단의 수입 의존도가 높습니다. 통역 시 조직 구조와 직기 종류를 정확히 전달해야 합니다.",
    meaningVi: "Quy trình đan sợi dọc và sợi ngang để tạo vải. Có thể dệt nhiều kiểu tổ chức như dệt trơn, dệt chéo, dệt sa tanh, sử dụng máy dệt (loom). Nhà máy dệt thoi tại Việt Nam ít hơn so với dệt kim, phụ thuộc nhập khẩu vải dệt thoi cao.",
    pronunciation: "jejik",
    commonMistakes: ["dệt(제직)과 dệt kim(편직)을 혼동", "제직과 방직의 차이를 모름", "dệt thoi와 dệt kim의 기술적 차이"],
    culturalNote: "베트남 정부는 원단 자급률 향상을 위해 제직 산업에 대한 투자를 장려하고 있으며, 한국 기업의 제직 공장 투자도 증가 추세입니다.",
    context: "생산 공정, 원단, 기술",
    examples: [
      { ko: "제직 공정에서 경사 밀도를 조정합니다.", vi: "Điều chỉnh mật độ sợi dọc trong quy trình dệt.", situation: "formal" },
      { ko: "제직 속도 좀 올릴 수 있어?", vi: "Có thể tăng tốc độ dệt không?", situation: "onsite" },
      { ko: "제직 품질이 원단 가격을 좌우해.", vi: "Chất lượng dệt quyết định giá vải.", situation: "informal" }
    ],
    relatedTerms: ["직물", "직기", "원사", "조직"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  },
  {
    slug: "keo-soi",
    korean: "방적",
    vietnamese: "kéo sợi",
    hanja: "紡績",
    hanjaReading: "방(자을 방) + 적(쌓을 적)",
    termType: "word",
    meaningKo: "섬유를 꼬아서 실(yarn)을 만드는 공정입니다. 면방적, 모방적, 합섬방적 등이 있으며, 실의 굵기와 꼬임에 따라 원단 특성이 달라집니다. 베트남의 방적 산업은 한국, 대만 기업의 투자로 성장했으며, 면방적과 합섬방적 모두 규모가 확대되고 있습니다.",
    meaningVi: "Quy trình xoắn sợi để tạo chỉ (yarn). Có kéo sợi bông, kéo sợi len, kéo sợi tổng hợp. Đặc tính vải thay đổi theo độ dày và độ xoắn của sợi. Ngành kéo sợi Việt Nam phát triển nhờ đầu tư từ doanh nghiệp Hàn Quốc, Đài Loan.",
    pronunciation: "bangjeok",
    commonMistakes: ["kéo sợi(방적)와 dệt(제직)을 혼동", "방적과 방직의 차이 - 방적은 실 만들기, 방직은 포괄적 용어", "번수(chi số sợi) 개념을 모름"],
    culturalNote: "베트남 방적 산업은 북부(남딩, 타이빈)에 집중되어 있으며, 한국 기업이 다수의 대규모 방적 공장을 운영하고 있습니다.",
    context: "원사 생산, 공정, 기술",
    examples: [
      { ko: "방적 공정에서 원사 굵기를 조절합니다.", vi: "Điều chỉnh độ dày sợi trong quy trình kéo sợi.", situation: "formal" },
      { ko: "방적 라인 가동률 체크해.", vi: "Kiểm tra tỷ lệ vận hành dây chuyền kéo sợi.", situation: "onsite" },
      { ko: "방적이 잘 되어야 원단 품질이 좋아.", vi: "Kéo sợi tốt thì chất lượng vải mới tốt.", situation: "informal" }
    ],
    relatedTerms: ["원사", "제직", "편직", "번수"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "tay-trang",
    korean: "표백",
    vietnamese: "tẩy trắng",
    hanja: "漂白",
    hanjaReading: "표(뜰 표) + 백(흰 백)",
    termType: "word",
    meaningKo: "원단이나 원사의 천연 색소와 불순물을 제거하여 하얗게 만드는 가공 공정입니다. 염색 전 전처리 단계로 필수적이며, 화학 표백과 천연 표백이 있습니다. 베트남 염색 공장에서 표백 공정의 폐수 처리가 환경 규제의 핵심 이슈입니다.",
    meaningVi: "Quy trình gia công loại bỏ sắc tố tự nhiên và tạp chất của vải hoặc sợi để làm trắng. Là bước tiền xử lý cần thiết trước nhuộm, có tẩy trắng hóa học và tự nhiên. Xử lý nước thải từ quy trình tẩy trắng là vấn đề then chốt về quy định môi trường tại nhà máy nhuộm Việt Nam.",
    pronunciation: "pyobaek",
    commonMistakes: ["tẩy trắng(표백)과 nhuộm trắng(백색 염색)을 혼동", "표백 정도에 따른 원단 강도 변화를 모름", "과표백이 원단 손상을 초래함을 모름"],
    culturalNote: "베트남 환경부는 표백 공정의 화학약품 사용을 규제하고 있으며, 한국 기업은 친환경 표백 기술 도입을 추진하고 있습니다.",
    context: "원단 가공, 전처리, 환경",
    examples: [
      { ko: "표백 처리 후 원단 강도를 확인합니다.", vi: "Kiểm tra độ bền vải sau khi tẩy trắng.", situation: "formal" },
      { ko: "표백이 너무 세서 원단이 약해졌어.", vi: "Tẩy trắng quá mạnh nên vải yếu đi.", situation: "onsite" },
      { ko: "표백 안 하면 염색이 잘 안 돼.", vi: "Không tẩy trắng thì nhuộm không đẹp.", situation: "informal" }
    ],
    relatedTerms: ["염색", "전처리", "가공", "폐수"],
    difficulty: "intermediate",
    frequency: 3,
    formalLevel: "neutral"
  },
  {
    slug: "hoan-tat",
    korean: "후가공",
    vietnamese: "hoàn tất",
    hanja: "後加工",
    hanjaReading: "후(뒤 후) + 가(더할 가) + 공(장인 공)",
    termType: "word",
    meaningKo: "원단의 제직이나 편직 후에 기능성이나 외관을 향상시키는 모든 가공 공정을 말합니다. 발수 가공, 방축 가공, 유연 가공, 기모 가공 등이 포함됩니다. 후가공 기술은 제품의 부가가치를 높이는 핵심 요소이며, 베트남의 후가공 역량 강화가 산업 발전의 과제입니다.",
    meaningVi: "Tất cả quy trình gia công cải thiện chức năng hoặc ngoại quan của vải sau khi dệt hoặc dệt kim. Bao gồm chống thấm nước, chống co, làm mềm, chải lông. Kỹ thuật hoàn tất là yếu tố then chốt nâng cao giá trị gia tăng, tăng cường năng lực hoàn tất là thách thức phát triển ngành của Việt Nam.",
    pronunciation: "hugagong",
    commonMistakes: ["hoàn tất(후가공)과 hoàn thiện(완성)을 혼동", "후가공과 염색을 같은 공정으로 오해", "finishing의 범위가 매우 넓음을 모름"],
    culturalNote: "베트남의 후가공 기술은 한국, 대만에 비해 아직 부족하여, 한국 기업의 기술 이전과 설비 투자가 활발합니다.",
    context: "원단 가공, 기능성, 부가가치",
    examples: [
      { ko: "후가공 공정에서 발수 처리를 진행합니다.", vi: "Tiến hành xử lý chống thấm trong quy trình hoàn tất.", situation: "formal" },
      { ko: "후가공 결과 촉감이 어때?", vi: "Cảm giác sờ sau hoàn tất thế nào?", situation: "onsite" },
      { ko: "후가공을 잘 하면 제품 가치가 확 올라가.", vi: "Hoàn tất tốt thì giá trị sản phẩm tăng hẳn.", situation: "informal" }
    ],
    relatedTerms: ["가공", "발수", "방축", "기능성"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  },
  {
    slug: "lam-bong",
    korean: "머서라이징",
    vietnamese: "làm bóng",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "면직물을 가성소다(NaOH) 용액에 처리하여 광택, 강도, 염색성을 향상시키는 가공법입니다. 머서라이즈드 코튼(mercerized cotton)은 일반 면보다 광택이 있고 색상이 선명합니다. 고급 면제품 생산에 필수적인 공정으로, 폴로셔츠, 드레스셔츠 등에 적용됩니다.",
    meaningVi: "Phương pháp gia công xử lý vải bông trong dung dịch xút (NaOH) để cải thiện độ bóng, độ bền, khả năng nhuộm. Cotton mercerized có độ bóng và màu sắc rõ hơn bông thường. Là quy trình cần thiết cho sản xuất sản phẩm bông cao cấp như áo polo, áo sơ mi.",
    pronunciation: "meoseoraijing",
    commonMistakes: ["làm bóng(머서라이징)과 là(다림질)를 혼동", "머서라이징과 실켓의 차이를 모름", "가공 후 원단 수축 특성 변화를 간과"],
    culturalNote: "한국 바이어가 발주하는 고급 면제품에는 머서라이징 가공이 필수인 경우가 많아, 베트남 공장의 해당 설비 보유가 중요합니다.",
    context: "원단 가공, 고급 면, 기술",
    examples: [
      { ko: "이 면직물에 머서라이징 가공을 적용합니다.", vi: "Áp dụng gia công làm bóng cho vải bông này.", situation: "formal" },
      { ko: "머서라이징 된 건지 확인해 봐.", vi: "Kiểm tra xem đã làm bóng chưa.", situation: "onsite" },
      { ko: "머서라이징 하면 광택이 확 달라져.", vi: "Làm bóng thì độ bóng khác hẳn.", situation: "informal" }
    ],
    relatedTerms: ["면", "광택", "가공", "실켓"],
    difficulty: "advanced",
    frequency: 2,
    formalLevel: "neutral"
  },
  {
    slug: "chong-co",
    korean: "산포라이징",
    vietnamese: "chống co",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "원단의 세탁 수축을 방지하기 위한 기계적 가공법입니다. 원단을 미리 수축시켜 이후 세탁 시 추가 수축을 최소화합니다. 잔수축률(residual shrinkage)을 1% 이내로 관리하는 것이 목표이며, 면직물에 주로 적용됩니다. 바이어의 수축률 규격을 맞추기 위해 필수적인 공정입니다.",
    meaningVi: "Phương pháp gia công cơ học để ngăn co rút khi giặt vải. Cho vải co trước để giảm thiểu co rút thêm khi giặt sau này. Mục tiêu quản lý tỷ lệ co rút còn lại (residual shrinkage) dưới 1%, chủ yếu áp dụng cho vải bông. Là quy trình cần thiết để đạt quy cách co rút của buyer.",
    pronunciation: "sanporaijing",
    commonMistakes: ["chống co(산포라이징)와 방축의 차이를 모름", "산포라이징이 기계적 가공임을 모름", "잔수축률 개념을 이해하지 못함"],
    culturalNote: "한국 바이어의 수축률 기준이 매우 엄격하여, 베트남 공장에서 산포라이징 공정의 정밀 관리가 필수입니다.",
    context: "원단 가공, 품질 관리, 수축",
    examples: [
      { ko: "산포라이징 처리 후 잔수축률을 측정합니다.", vi: "Đo tỷ lệ co rút còn lại sau khi xử lý chống co.", situation: "formal" },
      { ko: "산포라이징 안 하면 수축률 기준 못 맞춰.", vi: "Không xử lý chống co thì không đạt tiêu chuẩn co rút.", situation: "onsite" },
      { ko: "산포라이징이 안 되면 세탁하면 줄어들어.", vi: "Không chống co thì giặt sẽ co rút.", situation: "informal" }
    ],
    relatedTerms: ["수축률", "가공", "면", "품질"],
    difficulty: "advanced",
    frequency: 2,
    formalLevel: "neutral"
  },
  {
    slug: "in-hoa",
    korean: "날염",
    vietnamese: "in hoa",
    hanja: null,
    hanjaReading: null,
    termType: "word",
    meaningKo: "원단 표면에 무늬나 그림을 인쇄하는 공정으로, 스크린 프린팅, 로타리 프린팅, 디지털 프린팅 등이 있습니다. 염색과 달리 부분적으로 색을 입히는 기술이며, 패션 트렌드에 따라 다양한 프린트 기법이 사용됩니다. 베트남의 날염 기술이 발전하면서 한국 바이어의 프린트 제품 발주가 증가하고 있습니다.",
    meaningVi: "Quy trình in hoa văn hoặc hình ảnh lên bề mặt vải, có in lưới (screen), in trục quay (rotary), in kỹ thuật số (digital). Khác với nhuộm là kỹ thuật tạo màu cục bộ. Kỹ thuật in hoa Việt Nam phát triển nên đơn hàng sản phẩm in từ buyer Hàn Quốc đang tăng.",
    pronunciation: "nalyeom",
    commonMistakes: ["in hoa(날염)과 nhuộm(염색)을 혼동", "날염과 프린트가 같은 의미임을 모름", "스크린 날염과 디지털 날염의 차이를 모름"],
    culturalNote: "베트남의 디지털 날염 기술이 빠르게 성장하고 있으며, 소량 다품종 프린트 제품 생산이 가능해지고 있습니다.",
    context: "원단 가공, 디자인, 패션",
    examples: [
      { ko: "디지털 날염으로 소량 다품종 생산이 가능합니다.", vi: "In kỹ thuật số cho phép sản xuất số lượng nhỏ nhiều mẫu.", situation: "formal" },
      { ko: "날염 색상이 샘플이랑 좀 다른데?", vi: "Màu in hoa hơi khác với mẫu nhỉ?", situation: "onsite" },
      { ko: "날염이 요즘 디지털로 많이 바뀌었어.", vi: "In hoa dạo này chuyển sang digital nhiều rồi.", situation: "informal" }
    ],
    relatedTerms: ["염색", "프린팅", "디자인", "스크린"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  },
  {
    slug: "theu",
    korean: "자수",
    vietnamese: "thêu",
    hanja: "刺繡",
    hanjaReading: "자(찌를 자) + 수(수놓을 수)",
    termType: "word",
    meaningKo: "원단에 실로 무늬나 글자를 놓는 장식 기법입니다. 기계 자수와 수(手)자수가 있으며, 로고, 브랜드명, 장식 무늬에 사용됩니다. 베트남은 수자수 기술이 뛰어나 한국 브랜드의 고급 자수 작업을 많이 수행합니다. 자수의 밀도, 색상, 위치가 품질 포인트입니다.",
    meaningVi: "Kỹ thuật trang trí thêu hoa văn hoặc chữ bằng chỉ trên vải. Có thêu máy và thêu tay, dùng cho logo, tên thương hiệu, hoa văn trang trí. Việt Nam có kỹ thuật thêu tay xuất sắc, thực hiện nhiều công việc thêu cao cấp cho thương hiệu Hàn Quốc.",
    pronunciation: "jasu",
    commonMistakes: ["thêu(자수)와 in(프린트)를 혼동", "기계 자수와 수자수의 품질 차이를 모름", "자수 밀도(stitch count) 개념을 모름"],
    culturalNote: "베트남의 수자수 기술은 오랜 전통을 가지고 있으며, 특히 하노이 근교의 자수 마을이 유명합니다.",
    context: "장식, 브랜드, 의류",
    examples: [
      { ko: "로고 자수의 밀도와 색상을 확인합니다.", vi: "Kiểm tra mật độ và màu sắc thêu logo.", situation: "formal" },
      { ko: "자수 위치가 좀 틀어진 것 같아.", vi: "Vị trí thêu hình như hơi lệch.", situation: "onsite" },
      { ko: "자수가 프린트보다 고급스러워 보여.", vi: "Thêu trông sang hơn in.", situation: "informal" }
    ],
    relatedTerms: ["날염", "로고", "장식", "브랜드"],
    difficulty: "intermediate",
    frequency: 4,
    formalLevel: "neutral"
  }
];

// Write first batch
const batch1Path = path.join(__dirname, '_batch1.json');
fs.writeFileSync(batch1Path, JSON.stringify(newTerms, null, 2));
console.log(`Batch 1: ${newTerms.length} terms written`);
console.log(`Total so far: ${existing.length + newTerms.length}`);
