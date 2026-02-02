#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legal Terms Batch 4C: Religious Law & Ethnic Minority Law (종교법/민족법)
Tier S compliant - 90+ quality score required
"""

import json
import os
import sys

# 추가할 용어 데이터 (Tier S 기준)
NEW_TERMS = [
    {
        "slug": "tu-do-ton-giao",
        "korean": "종교자유",
        "vietnamese": "Tự do tôn giáo",
        "hanja": "宗敎自由",
        "hanjaReading": "宗(마루 종) + 敎(가르칠 교) + 自(스스로 자) + 由(말미암을 유)",
        "pronunciation": "똔지어오 뜨도",
        "meaningKo": "개인이 자신의 신념에 따라 종교를 선택하거나 선택하지 않을 권리. 통역 시 한국은 헌법 제20조가 종교의 자유를 보장하며 국교 금지 원칙이 명확하지만, 베트남은 당과 국가의 관리 하에 종교 활동이 허용되는 차이를 설명해야 합니다. '종교 활동'과 '종교 선전'을 명확히 구분하여 통역하는 것이 중요하며, 베트남에서는 등록되지 않은 종교 활동이 제한될 수 있음을 주의해야 합니다.",
        "meaningVi": "Quyền của cá nhân được lựa chọn hoặc không lựa chọn tôn giáo theo niềm tin của mình. Việt Nam bảo đảm quyền tự do tín ngưỡng, tôn giáo theo Hiến pháp và Luật Tín ngưỡng, Tôn giáo 2016, trong đó các hoạt động tôn giáo phải đăng ký và tuân thủ pháp luật.",
        "context": "헌법, 종교법, 인권 논의",
        "culturalNote": "한국은 종교 다원주의가 발달했고 종교 활동이 매우 자유로우나, 베트남은 사회주의 체제 하에서 종교가 당과 국가의 지도를 받으며 등록제로 관리됩니다. 한국에서는 종교 단체가 정치 활동도 활발하지만, 베트남에서는 종교의 정치 개입이 엄격히 제한됩니다. 통역 시 양국의 종교 자유 범위 차이를 명확히 전달해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tự do tôn giáo를 '완전한 종교 자유'로 번역",
                "correction": "'법률 범위 내 종교 자유' 또는 '제도적 관리 하 종교 자유'",
                "explanation": "베트남의 종교 자유는 등록제와 정부 감독을 전제로 하므로 서구식 절대적 자유와 다름"
            },
            {
                "mistake": "hoạt động tôn giáo와 tuyên truyền tôn giáo를 구분 없이 '종교 활동'으로 통역",
                "correction": "'종교 활동'과 '종교 선전'으로 명확히 구분",
                "explanation": "베트남에서는 종교 선전이 별도로 규제되며 허가가 필요함"
            },
            {
                "mistake": "한국의 종교자유를 베트남 상황에 그대로 대입",
                "correction": "양국의 종교 관리 체계 차이를 설명하며 통역",
                "explanation": "한국은 정교분리 원칙, 베트남은 당의 지도 원칙이 적용됨"
            }
        ],
        "examples": [
            {
                "ko": "헌법은 모든 국민에게 종교자유를 보장합니다.",
                "vi": "Hiến pháp bảo đảm quyền tự do tôn giáo cho mọi công dân.",
                "situation": "formal"
            },
            {
                "ko": "종교자유에는 종교를 선택하지 않을 자유도 포함됩니다.",
                "vi": "Quyền tự do tôn giáo bao gồm cả quyền không theo tôn giáo nào.",
                "situation": "formal"
            },
            {
                "ko": "종교자유 침해 사례가 보고되었습니다.",
                "vi": "Đã có báo cáo về các trường hợp vi phạm quyền tự do tôn giáo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["신앙의 자유", "종교활동등록", "정교분리", "종교정책"]
    },
    {
        "slug": "dang-ky-hoat-dong-ton-giao",
        "korean": "종교활동등록",
        "vietnamese": "Đăng ký hoạt động tôn giáo",
        "hanja": "宗敎活動登錄",
        "hanjaReading": "宗(마루 종) + 敎(가르칠 교) + 活(살 활) + 動(움직일 동) + 登(오를 등) + 錄(기록할 록)",
        "pronunciation": "당끼 호앗동 똔지어오",
        "meaningKo": "종교 단체가 합법적으로 활동하기 위해 국가 기관에 등록하는 절차. 통역 시 베트남은 Luật Tín ngưỡng, Tôn giáo 2016에 따라 모든 종교 조직과 활동이 등록 의무가 있으며, 미등록 활동은 불법으로 간주될 수 있음을 명확히 해야 합니다. 한국은 등록이 선택 사항이지만 베트남은 필수라는 차이가 중요하며, 등록 절차와 요구 서류가 복잡할 수 있음을 안내해야 합니다.",
        "meaningVi": "Thủ tục đăng ký với cơ quan nhà nước để tổ chức tôn giáo hoạt động hợp pháp theo Luật Tín ngưỡng, Tôn giáo 2016. Bao gồm đăng ký sinh hoạt tôn giáo tập trung, đăng ký hoạt động tôn giáo, và công nhận tổ chức tôn giáo.",
        "context": "행정법, 종교법, 단체 설립",
        "culturalNote": "한국에서는 종교 단체 등록이 선택 사항이며 미등록 종교 활동도 자유롭지만, 베트님에서는 등록이 의무이며 미등록 시 법적 제재를 받을 수 있습니다. 베트남의 종교 등록은 3단계(sinh hoạt tập trung 등록 → hoạt động tôn giáo 등록 → tổ chức tôn giáo 공인)로 나뉘며 각 단계마다 요건이 다릅니다. 통역 시 이 절차적 복잡성을 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "đăng ký를 단순히 '신고'로 번역",
                "correction": "'등록' (법적 효력 있는 행정 행위)",
                "explanation": "신고는 알리는 것이지만 등록은 법적 지위를 부여하는 행위로 무게가 다름"
            },
            {
                "mistake": "3단계 등록 체계를 설명 없이 '종교 등록'으로 일괄 통역",
                "correction": "sinh hoạt tập trung(집단 신앙 활동), hoạt động tôn giáo(종교 활동), công nhận tổ chức(조직 공인)로 구분",
                "explanation": "각 단계의 법적 지위와 허용 범위가 다르므로 명확한 구분 필요"
            },
            {
                "mistake": "등록 거부를 '종교 탄압'으로 표현",
                "correction": "'등록 요건 미비' 또는 '서류 보완 필요'",
                "explanation": "객관적이고 법률적인 표현 사용으로 오해 방지"
            }
        ],
        "examples": [
            {
                "ko": "우리 교회는 종교활동등록을 완료했습니다.",
                "vi": "Nhà thờ của chúng tôi đã hoàn thành đăng ký hoạt động tôn giáo.",
                "situation": "formal"
            },
            {
                "ko": "종교활동등록 신청서를 제출해야 합니다.",
                "vi": "Cần nộp đơn đăng ký hoạt động tôn giáo.",
                "situation": "formal"
            },
            {
                "ko": "등록되지 않은 종교 활동은 제한될 수 있습니다.",
                "vi": "Các hoạt động tôn giáo chưa đăng ký có thể bị hạn chế.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["종교단체", "종교자유", "행정등록", "종교법"]
    },
    {
        "slug": "dan-toc-thieu-so",
        "korean": "소수민족",
        "vietnamese": "Dân tộc thiểu số",
        "hanja": "少數民族",
        "hanjaReading": "少(적을 소) + 數(셀 수) + 民(백성 민) + 族(겨레 족)",
        "pronunciation": "잔똑 티에우쇼",
        "meaningKo": "한 국가 내에서 인구가 소수이며 고유한 언어, 문화, 전통을 가진 민족 집단. 통역 시 베트남에는 54개 공식 민족이 있으며 Kinh족이 다수민족이고 나머지 53개가 소수민족임을 이해해야 합니다. 베트남 정부는 소수민족 우대 정책을 시행하지만 동화 압력도 존재하는 복잡한 상황을 주의해서 통역해야 하며, '낙후 지역'과 '소수민족 거주 지역'을 동일시하는 오류를 피해야 합니다.",
        "meaningVi": "Các dân tộc có số dân ít hơn so với dân tộc đa số trong một quốc gia, có ngôn ngữ, văn hóa, truyền thống riêng. Việt Nam có 54 dân tộc, trong đó dân tộc Kinh là đa số và 53 dân tộc còn lại là thiểu số.",
        "context": "헌법, 민족정책, 인권법",
        "culturalNote": "한국은 사실상 단일민족 국가 정체성이 강하고 '소수민족' 개념이 약한 반면, 베트남은 다민족 국가로 헌법에서 각 민족의 평등을 명시합니다. 베트남 소수민족은 산간 지역에 많이 거주하며 고유 언어와 문자를 보존하려는 노력과 베트남어 보급 정책 사이에 긴장이 있습니다. 통역 시 '낙후'나 '미개발'이 아닌 '문화적 다양성'의 관점에서 접근해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "dân tộc thiểu số를 '소수종족'으로 번역",
                "correction": "'소수민족' (공식 용어)",
                "explanation": "종족은 인류학 용어이고 민족은 정치·법적 용어로 맥락이 다름"
            },
            {
                "mistake": "소수민족 지역을 일괄적으로 '낙후 지역'으로 표현",
                "correction": "'산간 지역' 또는 '고원 지역' 등 지리적 용어 사용",
                "explanation": "낙후는 경제 중심적 가치 판단으로 문화적 다양성을 무시함"
            },
            {
                "mistake": "tộc người와 dân tộc을 혼동",
                "correction": "tộc người는 '종족/에스닉 그룹', dân tộc은 '민족' (정치적 의미)",
                "explanation": "베트남어에서는 이 둘의 법적·정치적 지위가 다름"
            }
        ],
        "examples": [
            {
                "ko": "베트남 헌법은 소수민족의 권리를 보장합니다.",
                "vi": "Hiến pháp Việt Nam bảo đảm quyền của các dân tộc thiểu số.",
                "situation": "formal"
            },
            {
                "ko": "소수민족 언어 보존 정책이 필요합니다.",
                "vi": "Cần có chính sách bảo tồn ngôn ngữ dân tộc thiểu số.",
                "situation": "formal"
            },
            {
                "ko": "소수민족 대표가 국회에 진출했습니다.",
                "vi": "Đại diện dân tộc thiểu số đã vào Quốc hội.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["다수민족", "민족정책", "문화권", "민족자결권"]
    },
    {
        "slug": "chinh-sach-dan-toc",
        "korean": "민족정책",
        "vietnamese": "Chính sách dân tộc",
        "hanja": "民族政策",
        "hanjaReading": "民(백성 민) + 族(겨레 족) + 政(정사 정) + 策(꾀 책)",
        "pronunciation": "찡삭 잔똑",
        "meaningKo": "국가가 다양한 민족 집단의 평등과 발전을 위해 시행하는 정책. 통역 시 베트남의 민족정책은 '평등, 단결, 상호존중, 공동 발전' 4대 원칙에 기반하며, 교육·의료·경제 우대 정책을 포함하지만 동시에 베트남어 보급과 사회주의 가치 통합도 추구하는 양면성이 있음을 이해해야 합니다. 소수민족 간부 육성, 모국어 교육, 전통 문화 보존 지원 등 구체적 정책을 설명할 수 있어야 합니다.",
        "meaningVi": "Các chính sách của Nhà nước nhằm bảo đảm bình đẳng, đoàn kết và phát triển của các dân tộc. Bao gồm chính sách ưu đãi về giáo dục, y tế, kinh tế, và bảo tồn văn hóa truyền thống cho vùng dân tộc thiểu số.",
        "context": "행정법, 헌법, 사회정책",
        "culturalNote": "베트남의 민족정책은 중국의 영향을 받았으나 자율성보다 통합을 강조하는 특징이 있습니다. 소수민족에게 대학 입시 가산점, 세금 감면 등 우대가 주어지지만, 일부에서는 이를 실질적 차별로 보는 시각도 있습니다. 한국은 북한이탈주민, 다문화가족 등에 대한 정책은 있으나 전통적 의미의 '민족정책'은 없으므로 개념 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "chính sách dân tộc을 '민족주의 정책'으로 번역",
                "correction": "'민족정책' 또는 '소수민족 정책'",
                "explanation": "민족주의(chủ nghĩa dân tộc)와 민족정책은 완전히 다른 개념"
            },
            {
                "mistake": "우대 정책을 '차별 철폐'로 표현",
                "correction": "'적극적 우대 조치' 또는 '소수민족 지원 정책'",
                "explanation": "차별 철폐는 소극적 평등이고 우대 정책은 적극적 평등 개념"
            },
            {
                "mistake": "한국의 다문화정책과 동일시",
                "correction": "베트남 민족정책은 고유 영토 내 토착 민족 대상, 다문화정책은 이주민 대상",
                "explanation": "정책 대상과 법적 근거가 근본적으로 다름"
            }
        ],
        "examples": [
            {
                "ko": "정부는 소수민족 지원을 위한 민족정책을 강화하고 있습니다.",
                "vi": "Chính phủ đang tăng cường chính sách dân tộc để hỗ trợ đồng bào thiểu số.",
                "situation": "formal"
            },
            {
                "ko": "민족정책의 효과성에 대한 평가가 필요합니다.",
                "vi": "Cần đánh giá hiệu quả của chính sách dân tộc.",
                "situation": "formal"
            },
            {
                "ko": "민족정책 예산이 확대되었습니다.",
                "vi": "Ngân sách cho chính sách dân tộc đã được mở rộng.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["소수민족", "민족평등", "사회정책", "문화정책"]
    },
    {
        "slug": "quyen-tu-quyet-dan-toc",
        "korean": "민족자결권",
        "vietnamese": "Quyền tự quyết dân tộc",
        "hanja": "民族自決權",
        "hanjaReading": "民(백성 민) + 族(겨레 족) + 自(스스로 자) + 決(결단할 결) + 權(권세 권)",
        "pronunciation": "꾸엔 뜨꾸엣 잔똑",
        "meaningKo": "민족이 외부 간섭 없이 자신의 정치적 지위와 경제·사회·문화 발전을 스스로 결정할 권리. 통역 시 이는 국제법상 권리이지만 베트남에서는 '영토 통합성' 원칙과 충돌할 수 있어 매우 민감한 주제임을 인식해야 합니다. 외부 자결(독립)과 내부 자결(자치)을 구분하여 설명해야 하며, 베트남 전쟁의 역사적 맥락에서 이 용어가 특별한 의미를 가짐을 주의해야 합니다.",
        "meaningVi": "Quyền của các dân tộc được tự do quyết định địa vị chính trị và phát triển kinh tế, xã hội, văn hóa của mình không bị can thiệp từ bên ngoài. Được công nhận trong Công ước Quốc tế về Quyền Dân sự và Chính trị.",
        "context": "국제법, 인권법, 정치학",
        "culturalNote": "민족자결권은 탈식민지화 시대의 핵심 원칙이었으나, 현재는 국가 주권과의 긴장 관계에 있습니다. 베트남은 통일 투쟁에서 이 원칙을 강조했으나, 국내 소수민족에 대해서는 '단결과 통합' 원칙을 우선합니다. 한국에서도 북한과의 관계에서 민족자결권이 논의되지만, 베트남처럼 국내 다민족 맥락은 아닙니다. 통역 시 외교적 민감성을 고려해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "tự quyết을 '독립'으로 직역",
                "correction": "'자결' (자기결정권, 독립은 그 한 형태일 뿐)",
                "explanation": "자결권은 자치, 연방, 독립 등 다양한 형태를 포함하는 상위 개념"
            },
            {
                "mistake": "소수민족 자결권을 분리주의로 해석",
                "correction": "'내부 자결권' (자치와 문화적 권리)으로 설명",
                "explanation": "국제법상 기존 국가 내 소수민족은 분리 독립 권리가 없음"
            },
            {
                "mistake": "베트남 통일 과정을 '남베트남 민족자결권 부정'으로 표현",
                "correction": "'베트남 민족 전체의 통일과 자결'로 설명",
                "explanation": "베트남 공식 입장에서는 남북이 모두 하나의 베트남 민족"
            }
        ],
        "examples": [
            {
                "ko": "민족자결권은 국제법상 기본 원칙입니다.",
                "vi": "Quyền tự quyết dân tộc là nguyên tắc cơ bản trong luật quốc tế.",
                "situation": "formal"
            },
            {
                "ko": "모든 민족은 자결권을 행사할 권리가 있습니다.",
                "vi": "Mọi dân tộc đều có quyền thực hiện quyền tự quyết.",
                "situation": "formal"
            },
            {
                "ko": "민족자결권과 영토 보전의 균형이 중요합니다.",
                "vi": "Cần cân bằng giữa quyền tự quyết dân tộc và toàn vẹn lãnh thổ.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["주권", "영토보전", "자치권", "독립"]
    },
    {
        "slug": "phong-tuc-tap-quan",
        "korean": "관습법",
        "vietnamese": "Phong tục tập quán",
        "hanja": "慣習法",
        "hanjaReading": "慣(익숙할 관) + 習(익힐 습) + 法(법 법)",
        "pronunciation": "퐁뚝 땁꾸안",
        "meaningKo": "특정 공동체에서 오랫동안 반복적으로 지켜져 온 관습이나 전통으로, 법적 구속력을 가질 수 있는 규범. 통역 시 베트남 민법과 형법은 성문법이 우선이지만 일부 소수민족 지역에서는 전통적 관습법이 여전히 영향력을 가지고 있음을 이해해야 합니다. 토지 분쟁, 혼인, 상속 등에서 관습법과 국가법이 충돌할 때 원칙적으로는 국가법이 우선하지만 실제로는 관습이 존중되는 경우도 많으며, 이 긴장 관계를 설명할 수 있어야 합니다.",
        "meaningVi": "Những quy tắc ứng xử được hình thành và duy trì lâu dài trong cộng đồng, có thể được công nhận là nguồn luật bổ sung. Tại các vùng dân tộc thiểu số, phong tục tập quán vẫn đóng vai trò quan trọng trong đời sống xã hội.",
        "context": "민법, 민속학, 소수민족법",
        "culturalNote": "한국에서 관습법은 민법에서 보충적 법원으로 인정되지만 현대에는 거의 적용되지 않는 반면, 베트남 소수민족 지역에서는 토지 이용, 마을 규약, 전통 재판 등에서 여전히 실질적 효력을 가집니다. 일부 관습은 국가법(특히 남녀평등, 아동 권리)과 충돌하기도 하여 정부가 '해로운 관습' 개선 캠페인을 벌이기도 합니다. 통역 시 문화 상대주의와 인권 보편주의 사이의 균형을 유지해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "phong tục tập quán을 '미신'이나 '구습'으로 번역",
                "correction": "'관습법' 또는 '전통 관습'",
                "explanation": "미신이나 구습은 부정적 의미를 담고 있어 문화적 편견을 드러냄"
            },
            {
                "mistake": "관습법을 '불법'과 대립시킴",
                "correction": "'성문법과 관습법의 조화' 관점으로 설명",
                "explanation": "관습법은 법원(法源)의 하나이지 불법이 아님"
            },
            {
                "mistake": "luật tục과 phong tục tập quán을 혼동",
                "correction": "luật tục은 '관습법', phong tục tập quán은 '관습' (법적 효력 차이)",
                "explanation": "luật tục은 법적 지위가 더 명확한 개념"
            }
        ],
        "examples": [
            {
                "ko": "일부 지역에서는 관습법이 여전히 효력을 발휘합니다.",
                "vi": "Ở một số vùng, phong tục tập quán vẫn có hiệu lực.",
                "situation": "formal"
            },
            {
                "ko": "관습법과 국가법이 충돌하는 경우가 있습니다.",
                "vi": "Có trường hợp phong tục tập quán xung đột với pháp luật nhà nước.",
                "situation": "formal"
            },
            {
                "ko": "소수민족의 관습법을 존중해야 합니다.",
                "vi": "Cần tôn trọng phong tục tập quán của các dân tộc thiểu số.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["성문법", "전통법", "민족관습", "관습법령"]
    },
    {
        "slug": "luat-tuc",
        "korean": "관습법령",
        "vietnamese": "Luật tục",
        "hanja": "慣習法令",
        "hanjaReading": "慣(익숙할 관) + 習(익힐 습) + 法(법 법) + 令(명령 령)",
        "pronunciation": "루앗뚝",
        "meaningKo": "관습법 중에서도 특히 명문화되거나 공동체에서 공식적으로 인정된 규범. 통역 시 'luật tục'은 'phong tục tập quán'보다 법적 성격이 강한 용어로, 소수민족 전통법, 마을 규약, 종족 규칙 등을 의미함을 구분해야 합니다. 베트남에서는 헌법과 법률을 위반하지 않는 범위에서 소수민족의 luật tục을 존중하며, 분쟁 조정에서 이를 참고하는 경우가 많습니다. 전통 장로 재판, 부족 회의 결정 등이 이에 해당합니다.",
        "meaningVi": "Hệ thống quy tắc pháp lý truyền thống của các dân tộc thiểu số, được công nhận và tôn trọng trong phạm vi không trái với Hiến pháp và pháp luật. Luật tục thường được áp dụng trong giải quyết tranh chấp nội bộ cộng đồng.",
        "context": "민족법, 분쟁 조정, 전통 사법",
        "culturalNote": "베트남의 일부 소수민족(Thái, H'Mông, Dao 등)은 수백 년 된 성문화된 luật tục을 가지고 있으며, 이는 토지 이용, 물 배분, 삼림 관리, 혼인 규칙 등을 규정합니다. 현대 베트남 법체계는 이를 '문화유산'으로 인정하되 국가법과 충돌 시 국가법 우선 원칙을 고수합니다. 한국에는 이에 대응하는 살아있는 전통법 체계가 거의 없으므로 개념 설명이 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "luật tục을 '조례'로 번역",
                "correction": "'관습법령' 또는 '전통법'",
                "explanation": "조례는 지방자치단체가 제정하는 현대 법규이고 luật tục은 전통 규범"
            },
            {
                "mistake": "luật tục을 '비공식 규칙'으로 표현",
                "correction": "'공동체 내에서 공식적으로 인정된 전통법'",
                "explanation": "소수민족 공동체 내에서는 매우 공식적이고 구속력 있는 규범임"
            },
            {
                "mistake": "luật tục와 phong tục tập quán을 동의어로 사용",
                "correction": "luật tục은 법적 규범, phong tục tập quán은 사회적 관습",
                "explanation": "luật tục이 더 체계적이고 법적 성격이 강함"
            }
        ],
        "examples": [
            {
                "ko": "소수민족은 고유한 관습법령을 가지고 있습니다.",
                "vi": "Các dân tộc thiểu số có luật tục riêng của mình.",
                "situation": "formal"
            },
            {
                "ko": "관습법령이 분쟁 해결에 적용되었습니다.",
                "vi": "Luật tục đã được áp dụng trong giải quyết tranh chấp.",
                "situation": "formal"
            },
            {
                "ko": "국가법과 관습법령을 조화시켜야 합니다.",
                "vi": "Cần hài hòa giữa pháp luật nhà nước và luật tục.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["관습법", "전통법", "민족자치", "마을규약"]
    },
    {
        "slug": "quyen-van-hoa",
        "korean": "문화권",
        "vietnamese": "Quyền văn hóa",
        "hanja": "文化權",
        "hanjaReading": "文(글월 문) + 化(될 화) + 權(권세 권)",
        "pronunciation": "꾸엔 번호아",
        "meaningKo": "개인과 공동체가 자신의 문화적 정체성을 유지하고 발전시키며 문화 생활에 참여할 권리. 통역 시 이는 세계인권선언과 경제적·사회적·문화적 권리에 관한 국제규약에 명시된 권리이며, 언어 사용권, 전통 의례 실행권, 문화유산 향유권 등을 포함함을 설명해야 합니다. 베트남 헌법 제5조는 각 민족의 문화권을 보장하지만, 실제로는 베트남어 중심 교육 정책과 긴장 관계에 있음을 주의해서 통역해야 합니다.",
        "meaningVi": "Quyền của cá nhân và cộng đồng được duy trì và phát triển bản sắc văn hóa, tham gia vào đời sống văn hóa. Bao gồm quyền sử dụng ngôn ngữ mẹ đẻ, thực hiện nghi lễ truyền thống, và tiếp cận di sản văn hóa.",
        "context": "헌법, 인권법, 문화정책",
        "culturalNote": "한국은 단일문화 중심에서 다문화 사회로 전환 중이지만 '문화권' 개념은 아직 약한 반면, 베트남은 54개 민족의 문화권을 헌법적으로 인정합니다. 그러나 소수민족 언어의 교육과 공적 사용은 제한적이며, 전통 의례 중 일부는 '미신'으로 분류되어 제한받기도 합니다. 통역 시 규범과 실제 사이의 간극을 이해해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "quyền văn hóa를 '문화 활동 권리'로 단순화",
                "correction": "'문화권' (정체성, 언어, 전통을 포괄하는 종합적 권리)",
                "explanation": "문화권은 단순 여가 활동이 아닌 집단적 정체성 보존의 권리"
            },
            {
                "mistake": "văn hóa와 tín ngưỡng을 구분 없이 '문화'로 통역",
                "correction": "văn hóa는 '문화', tín ngưỡng은 '신앙/신념'으로 구분",
                "explanation": "법적으로 문화권과 신앙의 자유는 별개의 권리"
            },
            {
                "mistake": "문화권 제한을 '문화 말살'로 과장",
                "correction": "'문화 정책의 우선순위' 또는 '문화 통합 정책'",
                "explanation": "객관적이고 중립적인 법률 용어 사용"
            }
        ],
        "examples": [
            {
                "ko": "헌법은 모든 민족의 문화권을 보장합니다.",
                "vi": "Hiến pháp bảo đảm quyền văn hóa của mọi dân tộc.",
                "situation": "formal"
            },
            {
                "ko": "소수민족의 문화권 보호가 필요합니다.",
                "vi": "Cần bảo vệ quyền văn hóa của các dân tộc thiểu số.",
                "situation": "formal"
            },
            {
                "ko": "문화권은 기본적 인권입니다.",
                "vi": "Quyền văn hóa là quyền con người cơ bản.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["언어권", "문화유산", "전통보존", "문화정책"]
    },
    {
        "slug": "bao-ton-di-san",
        "korean": "유산보존",
        "vietnamese": "Bảo tồn di sản",
        "hanja": "遺産保存",
        "hanjaReading": "遺(남길 유) + 産(낳을 산) + 保(지킬 보) + 存(있을 존)",
        "pronunciation": "바오똔 지산",
        "meaningKo": "역사적, 문화적, 자연적 가치가 있는 유산을 보호하고 후세에 전달하는 활동. 통역 시 베트남은 UNESCO 세계유산 8개를 포함해 풍부한 유산을 보유하며, Di sản văn hóa phi vật thể(무형문화유산)와 Di sản văn hóa vật thể(유형문화유산)를 구분함을 알아야 합니다. 소수민족의 전통 지식, 구전 문학, 전통 공예 등도 보존 대상이며, 관광 개발과 보존 사이의 긴장 관계를 설명할 수 있어야 합니다.",
        "meaningVi": "Hoạt động bảo vệ và gìn giữ di sản lịch sử, văn hóa, tự nhiên để truyền lại cho thế hệ sau. Việt Nam có 8 di sản thế giới được UNESCO công nhận và nhiều di sản văn hóa phi vật thể như ca trù, quan họ Bắc Ninh, tín ngưỡng thờ Mẫu.",
        "context": "문화재보호법, 관광법, 교육법",
        "culturalNote": "한국은 문화재청이 체계적으로 유산을 관리하며 복원과 활용에 강점이 있는 반면, 베트남은 급속한 도시화와 관광 개발로 유산 보존에 어려움을 겪고 있습니다. 특히 소수민족의 무형문화유산은 세대 단절로 소멸 위기에 있으며, 젊은 세대의 무관심이 큰 문제입니다. 통역 시 보존과 활용, 전통과 현대화 사이의 균형을 다룰 수 있어야 합니다.",
        "commonMistakes": [
            {
                "mistake": "bảo tồn을 '보호'로 번역",
                "correction": "'보존' (적극적 유지와 전승)",
                "explanation": "보호는 수동적이고 보존은 능동적 활동을 의미"
            },
            {
                "mistake": "di sản văn hóa를 '문화재'로만 번역",
                "correction": "'문화유산' (무형유산 포함)",
                "explanation": "문화재는 주로 유형물을 의미하나 di sản은 무형도 포함"
            },
            {
                "mistake": "보존을 '박제화'와 동일시",
                "correction": "'살아있는 유산으로서의 보존과 전승'",
                "explanation": "보존은 단순 보관이 아닌 생명력 있는 계승"
            }
        ],
        "examples": [
            {
                "ko": "무형문화유산의 보존이 시급합니다.",
                "vi": "Bảo tồn di sản văn hóa phi vật thể là cấp bách.",
                "situation": "formal"
            },
            {
                "ko": "유산보존을 위한 예산이 확대되었습니다.",
                "vi": "Ngân sách cho bảo tồn di sản đã được mở rộng.",
                "situation": "formal"
            },
            {
                "ko": "지역 공동체가 유산보존에 참여해야 합니다.",
                "vi": "Cộng đồng địa phương cần tham gia bảo tồn di sản.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["문화유산", "무형문화재", "세계유산", "전통문화"]
    },
    {
        "slug": "chinh-sach-ton-giao",
        "korean": "종교정책",
        "vietnamese": "Chính sách tôn giáo",
        "hanja": "宗敎政策",
        "hanjaReading": "宗(마루 종) + 敎(가르칠 교) + 政(정사 정) + 策(꾀 책)",
        "pronunciation": "찡삭 똔지어오",
        "meaningKo": "국가가 종교 단체와 종교 활동에 대해 시행하는 정책. 통역 시 베트남의 종교정책은 '당의 지도 하에 종교의 자유 보장'이라는 원칙에 기반하며, Luật Tín ngưỡng, Tôn giáo 2016이 법적 근거임을 알아야 합니다. 종교가 정치에 개입하거나 국가 안보를 해치는 것을 엄격히 금지하며, 외국 종교 단체의 활동도 제한됩니다. '종교 이용 범죄'라는 개념이 있어 종교 활동과 불법 행위를 구분하는 통역이 중요합니다.",
        "meaningVi": "Các chính sách của Nhà nước đối với các tổ chức tôn giáo và hoạt động tôn giáo, dựa trên nguyên tắc bảo đảm quyền tự do tín ngưỡng, tôn giáo dưới sự lãnh đạo của Đảng. Không cho phép lợi dụng tôn giáo để chống phá Nhà nước.",
        "context": "행정법, 종교법, 국가안보법",
        "culturalNote": "한국은 정교분리 원칙으로 종교가 정치에 상당히 자유롭게 참여하는 반면, 베트남은 당-국가 체제 하에서 종교가 '정치적 중립'을 지켜야 합니다. 불교는 역사적으로 우호적 관계를 유지하지만, 개신교와 가톨릭(특히 외국과 연계된 경우)은 감시 대상이 되기도 합니다. Cao Đài, Hòa Hảo 같은 토착 종교도 복잡한 역사를 가지고 있어 통역 시 주의가 필요합니다.",
        "commonMistakes": [
            {
                "mistake": "chính sách tôn giáo를 '종교 탄압 정책'으로 해석",
                "correction": "'종교 관리 정책' 또는 '종교 규제 정책'",
                "explanation": "탄압은 주관적 판단이 개입된 용어로 외교적으로 부적절"
            },
            {
                "mistake": "lãnh đạo của Đảng을 '당의 통제'로 번역",
                "correction": "'당의 지도' (공식 용어)",
                "explanation": "lãnh đạo는 '지도'이지 '통제'(kiểm soát)가 아님"
            },
            {
                "mistake": "종교 등록제를 '종교 탄압'으로 표현",
                "correction": "'종교 활동 관리 제도' 또는 '종교 등록제'",
                "explanation": "등록제는 많은 국가에서 시행하는 행정 제도"
            }
        ],
        "examples": [
            {
                "ko": "정부는 종교정책 개선을 약속했습니다.",
                "vi": "Chính phủ đã cam kết cải thiện chính sách tôn giáo.",
                "situation": "formal"
            },
            {
                "ko": "종교정책에 대한 대화가 필요합니다.",
                "vi": "Cần có đối thoại về chính sách tôn giáo.",
                "situation": "formal"
            },
            {
                "ko": "종교정책은 종교자유를 보장해야 합니다.",
                "vi": "Chính sách tôn giáo phải bảo đảm quyền tự do tôn giáo.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["종교자유", "종교등록", "정교분리", "종교법"]
    }
]

def load_legal_terms():
    """legal.json 파일 로드"""
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'legal.json'
    )

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("❌ Error: legal.json is not a list")
                sys.exit(1)
            return data
    except FileNotFoundError:
        print(f"❌ Error: {file_path} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON - {e}")
        sys.exit(1)

def check_duplicates(terms, new_terms):
    """중복 체크 (slug 기준)"""
    existing_slugs = {term['slug'] for term in terms}
    duplicates = []

    for new_term in new_terms:
        if new_term['slug'] in existing_slugs:
            duplicates.append(new_term['slug'])

    return duplicates

def save_legal_terms(terms):
    """legal.json 파일 저장 (들여쓰기 2칸, 유니코드 유지, 후행 줄바꿈)"""
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'data',
        'terms',
        'legal.json'
    )

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terms, f, ensure_ascii=False, indent=2)
            f.write('\n')  # 파일 끝에 줄바꿈 추가
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def main():
    print("=" * 60)
    print("Legal Terms Batch 4C: Religious Law & Ethnic Minority Law")
    print("=" * 60)

    # 1. 기존 데이터 로드
    print("\n[1/4] Loading legal.json...")
    terms = load_legal_terms()
    print(f"✅ Loaded {len(terms)} existing terms")

    # 2. 중복 체크
    print("\n[2/4] Checking for duplicates...")
    duplicates = check_duplicates(terms, NEW_TERMS)

    if duplicates:
        print(f"⚠️  Found {len(duplicates)} duplicate(s):")
        for slug in duplicates:
            print(f"   - {slug}")
        response = input("\nSkip duplicates and continue? (y/n): ")
        if response.lower() != 'y':
            print("❌ Aborted by user")
            sys.exit(1)
        # 중복 제거
        NEW_TERMS[:] = [t for t in NEW_TERMS if t['slug'] not in duplicates]
    else:
        print("✅ No duplicates found")

    # 3. 용어 추가
    print(f"\n[3/4] Adding {len(NEW_TERMS)} new terms...")
    terms.extend(NEW_TERMS)
    print(f"✅ Total terms: {len(terms)}")

    # 4. 저장
    print("\n[4/4] Saving to legal.json...")
    if save_legal_terms(terms):
        print("✅ Successfully saved!")
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Added terms: {len(NEW_TERMS)}")
        print(f"Skipped (duplicates): {len(duplicates)}")
        print(f"Total terms in legal.json: {len(terms)}")
        print("\n✅ NEXT STEP: Run 'npm run validate:terms -- --domain=legal'")
    else:
        print("❌ Failed to save")
        sys.exit(1)

if __name__ == "__main__":
    main()
