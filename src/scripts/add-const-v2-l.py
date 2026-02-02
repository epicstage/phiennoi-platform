#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
건설(Construction) 용어 추가 스크립트 - 조경/외구공사 (Landscaping & Site Work)
테마: 수목식재, 잔디, 포장블록, 인터로킹, 보도블록, 배수구, 맨홀, 경계석, 옥외조명, 주차장바닥
Tier S 품질 기준 (90점 이상)
"""

import json
import os

# 추가할 용어 데이터 (배열 형식)
data = [
    {
        "slug": "cay-xanh-canh-quan",
        "korean": "조경수목",
        "vietnamese": "Cây xanh cảnh quan",
        "hanja": "造景樹木",
        "hanjaReading": "造(지을 조) + 景(경치 경) + 樹(나무 수) + 木(나무 목)",
        "pronunciation": "조경수목",
        "meaningKo": "조경을 위해 심는 나무를 의미합니다. 베트남 현장에서는 'cây xanh' (나무)와 'cảnh quan' (조경)을 함께 사용하여 강조합니다. 통역 시 주의: 베트남에서는 열대 수종이 많아 한국의 사계절 수종과 생육 조건이 다릅니다. 수목 규격 표기 방식(수고, 흉고직경)도 양국이 다를 수 있으므로 도면 검토 시 단위 확인이 필수입니다. 'cây bóng mát' (그늘수), 'cây hoa' (꽃나무) 등 용도별 구분을 명확히 하세요.",
        "meaningVi": "Cây xanh được trồng để tạo cảnh quan, bao gồm cây bóng mát, cây hoa, cây cảnh. Khi thông dịch cần phân biệt rõ loại cây (cây lớn, cây bụi, cây hoa), quy cách (chiều cao, đường kính), và điều kiện chăm sóc theo khí hậu Việt Nam.",
        "context": "조경 도면 검토, 수목 식재 시방서, 현장 식재 작업 지시 시",
        "culturalNote": "한국은 사계절이 뚜렷해 낙엽수·상록수 구분이 중요하지만, 베트남은 열대·아열대 기후로 상록수 위주입니다. 한국 조경에서 흔한 소나무, 단풍나무 등은 베트남에서 생육이 어렵고, 대신 bằng lăng, phượng vĩ, sao đen 같은 열대 수종이 많이 쓰입니다. 수목 규격도 한국은 '수고(H) × 흉고직경(R)', 베트남은 'chiều cao × đường kính gốc' 표기가 일반적이므로 도면 통역 시 단위 환산과 표기법 차이를 설명해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cây xanh를 '녹색 나무'로 직역",
                "correction": "조경수목 또는 가로수로 문맥에 맞게 번역",
                "explanation": "cây xanh는 녹색이 아니라 '살아있는 나무' 전반을 뜻하는 조경 용어"
            },
            {
                "mistake": "수고(樹高)를 chiều dài(길이)로 번역",
                "correction": "chiều cao cây (나무 높이)로 번역",
                "explanation": "chiều dài는 수평 길이, 수목은 chiều cao(높이) 사용"
            },
            {
                "mistake": "흉고직경을 đường kính thân(줄기 직경)으로만 표현",
                "correction": "đường kính ngang ngực (흉고 높이 직경) 또는 DBH로 명시",
                "explanation": "수목 규격은 지면 1.2m 높이에서 측정하는 표준이 있음"
            }
        ],
        "examples": [
            {
                "ko": "이 조경수목은 수고 4m, 흉고직경 15cm입니다.",
                "vi": "Cây xanh cảnh quan này có chiều cao 4m, đường kính gốc (DBH) 15cm.",
                "situation": "formal"
            },
            {
                "ko": "조경수 식재 후 3년간 하자보수 의무가 있습니다.",
                "vi": "Sau khi trồng cây cảnh quan, có nghĩa vụ bảo hành trong 3 năm.",
                "situation": "onsite"
            },
            {
                "ko": "이 수종은 베트남 기후에 적합한지 확인 부탁드립니다.",
                "vi": "Vui lòng xác nhận loại cây này có phù hợp với khí hậu Việt Nam không.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["식재공사", "수목보호", "지반조성", "하자보수"],
        "level": "intermediate",
        "tags": ["조경", "수목", "식재", "외구공사"]
    },
    {
        "slug": "co-nhan-tao",
        "korean": "인조잔디",
        "vietnamese": "Cỏ nhân tạo",
        "hanja": "人造芝",
        "hanjaReading": "人(사람 인) + 造(지을 조) + 芝(잔디 지)",
        "pronunciation": "인조잔디",
        "meaningKo": "천연 잔디가 아닌 합성수지로 만든 인공 잔디를 의미합니다. 베트남 현장에서는 'cỏ nhân tạo' 또는 'cỏ giả' (fake grass)라고 부릅니다. 통역 시 주의: 베트남에서는 축구장, 골프장, 옥상정원 등에 인조잔디를 많이 사용하며, 열대 기후 특성상 배수와 열 축적 문제가 중요합니다. 잔디 파일 길이(pile height), 밀도(density), 배수구멍(drainage hole) 등 시방 항목을 정확히 전달하세요. 천연 잔디(cỏ tự nhiên)와 혼동되지 않도록 'nhân tạo' 강조가 필수입니다.",
        "meaningVi": "Cỏ làm từ chất liệu tổng hợp (nhựa PE, PP) thay vì cỏ tự nhiên. Dùng cho sân bóng, sân golf, sân thượng. Khi thông dịch cần nói rõ chiều cao sợi cỏ (pile height), độ thoát nước, và khả năng chịu nhiệt dưới khí hậu nhiệt đới Việt Nam.",
        "context": "축구장 시공, 옥상정원 조성, 골프장 퍼팅그린 공사 시",
        "culturalNote": "한국에서는 인조잔디를 주로 학교 운동장, 실내 체육관에 많이 쓰지만, 베트남은 열대 기후로 천연 잔디 유지가 어려워 축구장, 공원, 옥상정원 등 다양한 곳에 인조잔디를 선호합니다. 베트남 인조잔디 시장은 중국산 저가 제품이 많아 품질 편차가 크므로, 시방서에서 '파일 높이 30~50mm', 'UV 저항성', '배수 구멍 간격' 등을 명확히 요구해야 합니다. 또한 베트남은 햇빛이 강해 표면 온도가 60도 이상 올라갈 수 있어 열 축적 문제를 설명할 때 'nhiệt độ bề mặt cao' (표면 고온) 표현을 써야 합니다.",
        "commonMistakes": [
            {
                "mistake": "cỏ nhân tạo를 '인공 풀'로 번역",
                "correction": "인조잔디로 번역",
                "explanation": "건설 용어로는 '인조잔디'가 표준"
            },
            {
                "mistake": "pile height를 '높이'로만 번역",
                "correction": "파일 높이 또는 잔디 길이로 설명",
                "explanation": "인조잔디 규격 용어는 파일(pile) 개념 전달 필요"
            },
            {
                "mistake": "배수구멍을 lỗ thoát nước(일반 배수구)로 번역",
                "correction": "lỗ thoát nước trên tấm cỏ (잔디 매트 위 배수구멍)로 명시",
                "explanation": "인조잔디 자체에 뚫린 구멍임을 명확히 해야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 인조잔디는 파일 높이 40mm, UV 저항성 8년 보증입니다.",
                "vi": "Cỏ nhân tạo này có chiều cao sợi cỏ 40mm, bảo hành chống UV 8 năm.",
                "situation": "formal"
            },
            {
                "ko": "인조잔디 시공 전에 배수층을 먼저 깔아야 합니다.",
                "vi": "Trước khi thi công cỏ nhân tạo, phải lót lớp thoát nước trước.",
                "situation": "onsite"
            },
            {
                "ko": "베트남 햇빛에 표면 온도가 높아질 수 있어 쿨링 타입을 권장합니다.",
                "vi": "Dưới ánh nắng Việt Nam, nhiệt độ bề mặt có thể rất cao, nên dùng loại cỏ có tính năng làm mát.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["천연잔디", "파일높이", "배수층", "UV저항성"],
        "level": "intermediate",
        "tags": ["조경", "인조잔디", "운동장", "외구공사"]
    },
    {
        "slug": "gach-lat-via-he",
        "korean": "보도블록",
        "vietnamese": "Gạch lát vỉa hè",
        "hanja": "步道block",
        "hanjaReading": "步(걸을 보) + 道(길 도) + block(외래어)",
        "pronunciation": "보도블록",
        "meaningKo": "보행자 도로(인도)에 깔리는 콘크리트 또는 점토 블록을 의미합니다. 베트남에서는 'gạch lát vỉa hè' (보도 포장 블록) 또는 'gạch bê tông' (콘크리트 블록)이라고 합니다. 통역 시 주의: 베트남 도로는 오토바이 주차와 노점 적재로 보도블록 파손이 잦아, 한국보다 하중 조건이 까다롭습니다. 블록 두께(dày), 압축강도(cường độ nén), 미끄럼 방지(chống trượt) 성능을 반드시 확인하세요. 시각장애인용 점자블록(gạch chỉ đường cho người khiếm thị)도 구분해서 전달해야 합니다.",
        "meaningVi": "Gạch bê tông hoặc đất nung dùng để lát vỉa hè (lối đi bộ). Cần chú ý độ dày, cường độ chịu lực, khả năng chống trượt, và khả năng chịu tải của xe máy đỗ trên vỉa hè ở Việt Nam. Có loại gạch chỉ đường cho người khiếm thị (gạch nổi).",
        "context": "인도 포장 공사, 보도 정비 공사, 도로 외구 시공 시",
        "culturalNote": "한국의 보도블록은 보행자 전용으로 설계되지만, 베트남은 오토바이 주차, 노점상 무게, 심지어 소형 차량이 올라가는 경우가 많아 하중 조건이 훨씬 가혹합니다. 따라서 베트남 현장에서는 한국보다 두꺼운 블록(60~80mm)을 요구하거나, 하부 기초(lớp móng)를 보강하는 경우가 많습니다. 또한 베트남은 우기 집중 호우로 배수가 중요해, 블록 틈새(khe hở giữa các viên gạch)를 통한 투수성(tính thấm nước)을 고려한 시공이 필요합니다. 시각장애인용 점자블록은 베트남에서 최근 의무화되는 추세이나, 시공 품질은 아직 한국만큼 정착되지 않았습니다.",
        "commonMistakes": [
            {
                "mistake": "보도블록을 gạch đường(도로 블록)으로 번역",
                "correction": "gạch lát vỉa hè (보도 포장 블록)로 번역",
                "explanation": "đường은 차도, vỉa hè가 인도(보행자 도로)"
            },
            {
                "mistake": "점자블록을 gạch nổi(돌출 블록)로만 표현",
                "correction": "gạch chỉ đường cho người khiếm thị (시각장애인 유도 블록)로 명시",
                "explanation": "용도와 대상을 명확히 해야 설계 의도 전달됨"
            },
            {
                "mistake": "미끄럼 방지를 không trơn(미끄럽지 않음)으로만 표현",
                "correction": "chống trượt (미끄럼 방지) 또는 có bề mặt nhám (거친 표면)으로 설명",
                "explanation": "시방서에서는 기술 용어 chống trượt 사용"
            }
        ],
        "examples": [
            {
                "ko": "이 보도블록은 두께 60mm, 압축강도 30MPa입니다.",
                "vi": "Gạch lát vỉa hè này dày 60mm, cường độ nén 30MPa.",
                "situation": "formal"
            },
            {
                "ko": "점자블록은 횡단보도 앞에 설치해야 합니다.",
                "vi": "Gạch chỉ đường cho người khiếm thị phải lắp trước vạch sang đường.",
                "situation": "onsite"
            },
            {
                "ko": "우기 배수를 위해 블록 틈새를 5mm로 유지하세요.",
                "vi": "Để thoát nước mùa mưa, giữ khe hở giữa các viên gạch là 5mm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["인도포장", "점자블록", "투수블록", "보도정비"],
        "level": "intermediate",
        "tags": ["조경", "보도블록", "외구공사", "포장"]
    },
    {
        "slug": "gach-interlocking",
        "korean": "인터로킹블록",
        "vietnamese": "Gạch interlocking",
        "hanja": None,
        "hanjaReading": None,
        "pronunciation": "인터로킹블록",
        "meaningKo": "블록끼리 맞물리는 구조로 시공하는 포장재를 의미합니다. 베트남에서는 'gạch interlocking' 또는 'gạch tự chèn' (자체 끼움 블록)이라고 합니다. 통역 시 주의: 인터로킹은 모래층 위에 블록을 깔고 다짐(đầm chặt)으로 고정하는 무시멘트 공법이 특징입니다. 베트남 현장에서는 주차장, 보행로, 공원 산책로에 많이 쓰이며, 일반 보도블록(gạch lát vỉa hè)과 달리 쉽게 탈착·재시공이 가능하다는 점을 강조하세요. 블록 형태(S자형, I자형, 지그재그 등)에 따라 결속력이 달라지므로 도면 설명 시 형상을 정확히 전달해야 합니다.",
        "meaningVi": "Gạch bê tông có hình dạng răng cưa, khớp với nhau khi lát, không cần xi măng dính. Thi công trên lớp cát, sau đó đầm chặt. Ưu điểm là dễ tháo lắp, sửa chữa. Dùng cho bãi đỗ xe, lối đi bộ, công viên. Có nhiều hình dạng: chữ S, chữ I, ziczắc.",
        "context": "주차장 포장, 공원 산책로, 광장 바닥재 시공 시",
        "culturalNote": "한국에서는 인터로킹블록을 주차장, 보행로에 많이 쓰며, 시공이 빠르고 유지보수가 쉬운 장점이 있습니다. 베트남도 최근 고급 주거단지, 공원, 산업단지 주차장에서 인터로킹을 선호하는 추세입니다. 베트남 현장에서는 'gạch con sâu' (S자형 블록, 애벌레 모양), 'gạch chữ I' (I자형) 등 블록 형태를 속칭으로 부르는 경우가 많아, 도면 지시 시 형상 그림을 함께 보여주는 것이 좋습니다. 또한 베트남은 하부 모래층(lớp cát lót) 다짐이 불충분하면 블록이 침하되거나 들뜨는 문제가 많아, 다짐 장비(máy đầm rung) 사용과 다짐 횟수를 시방서에 명확히 기재해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "interlocking을 khóa(자물쇠)로 번역",
                "correction": "gạch interlocking 또는 gạch tự chèn으로 표현",
                "explanation": "베트남 건설 현장에서는 'interlocking' 외래어 그대로 사용"
            },
            {
                "mistake": "무시멘트 공법을 không dùng xi măng(시멘트 안 씀)로만 표현",
                "correction": "thi công không cần xi măng dính, chỉ dùng cát lót (시멘트 접착 없이 모래층 시공)으로 설명",
                "explanation": "공법 특징을 구체적으로 전달해야 이해 쉬움"
            },
            {
                "mistake": "다짐을 nén(누르다)로 번역",
                "correction": "đầm chặt (다짐) 또는 sử dụng máy đầm rung (진동다짐기 사용)으로 표현",
                "explanation": "nén은 일반적 압력, đầm chặt이 토목 용어"
            }
        ],
        "examples": [
            {
                "ko": "인터로킹블록은 모래층 위에 깔고 진동다짐기로 3회 다져주세요.",
                "vi": "Gạch interlocking lát trên lớp cát, sau đó dùng máy đầm rung đầm 3 lần.",
                "situation": "onsite"
            },
            {
                "ko": "이 블록은 S자형 인터로킹으로 결속력이 우수합니다.",
                "vi": "Gạch này là loại interlocking hình chữ S, có độ khớp chặt cao.",
                "situation": "formal"
            },
            {
                "ko": "나중에 보수가 필요하면 블록만 뜯어내고 재시공할 수 있습니다.",
                "vi": "Nếu cần sửa chữa sau này, chỉ cần tháo gạch ra và lát lại.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보도블록", "주차장포장", "다짐작업", "모래층"],
        "level": "intermediate",
        "tags": ["조경", "인터로킹", "포장", "외구공사"]
    },
    {
        "slug": "cong-thoat-nuoc",
        "korean": "배수구",
        "vietnamese": "Cống thoát nước",
        "hanja": "排水口",
        "hanjaReading": "排(물뿌릴 배) + 水(물 수) + 口(입 구)",
        "pronunciation": "배수구",
        "meaningKo": "빗물이나 오수를 모아 배출하는 구조물을 의미합니다. 베트남에서는 'cống thoát nước' (배수관) 또는 'hố ga' (집수정)라고 구분해서 부릅니다. 통역 시 주의: 베트남은 우기 집중호우가 많아 배수 시설이 매우 중요하며, 한국보다 배수 용량(lưu lượng)을 크게 설계하는 경우가 많습니다. 'cống' (관로), 'hố ga' (맨홀·집수정), 'rãnh thoát nước' (배수로) 등을 명확히 구분하세요. 우수(nước mưa)와 오수(nước thải) 분리 여부도 확인이 필요합니다.",
        "meaningVi": "Công trình thu gom và thoát nước mưa hoặc nước thải. Bao gồm cống (đường ống), hố ga (giếng thu), rãnh thoát nước (홈통). Khi thông dịch phải phân biệt rõ nước mưa (nước mưa) và nước thải (nước bẩn), cũng như lưu lượng thoát nước theo quy chuẩn Việt Nam.",
        "context": "외구 배수 공사, 도로 배수 설계, 우수 배수 시스템 시공 시",
        "culturalNote": "한국은 우수와 오수를 분리 배수하는 시스템이 일반적이지만, 베트남은 구도심 지역에서 합류식(hệ thống thoát nước chung) 배수가 많아 홍수 시 오수가 역류하는 문제가 있습니다. 신규 개발 지역에서는 분류식(hệ thống thoát nước riêng)을 의무화하는 추세입니다. 베트남은 1시간에 100mm 이상 내리는 집중호우가 흔해, 한국 기준보다 배수관 직경을 크게 잡거나 배수로(rãnh) 폭을 넓게 설계해야 합니다. 또한 베트남 도로는 쓰레기 투기로 배수구 막힘(tắc cống)이 잦아, 유지보수 접근성과 청소 용이성을 설계에 반영해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "배수구를 lỗ thoát nước(배수 구멍)로만 번역",
                "correction": "cống thoát nước (배수관) 또는 hố ga (집수정)로 구분",
                "explanation": "lỗ는 작은 구멍, 토목 구조물은 cống/hố ga 사용"
            },
            {
                "mistake": "우수를 nước sông(강물)로 번역",
                "correction": "nước mưa (빗물)로 번역",
                "explanation": "nước sông은 하천수, 우수는 nước mưa"
            },
            {
                "mistake": "합류식을 hợp lưu(합류)로만 번역",
                "correction": "hệ thống thoát nước chung (합류식 배수 시스템)으로 설명",
                "explanation": "시스템 전체를 설명해야 설계 의도 전달됨"
            }
        ],
        "examples": [
            {
                "ko": "이 도로는 우수와 오수 분리 배수 시스템입니다.",
                "vi": "Con đường này dùng hệ thống thoát nước riêng (nước mưa và nước thải tách biệt).",
                "situation": "formal"
            },
            {
                "ko": "배수구 덮개(뚜껑)가 파손되어 교체가 필요합니다.",
                "vi": "Nắp hố ga bị hỏng, cần thay mới.",
                "situation": "onsite"
            },
            {
                "ko": "집중호우 시 배수 용량 부족으로 침수될 우려가 있습니다.",
                "vi": "Khi mưa lớn, lưu lượng thoát nước không đủ, có nguy cơ bị ngập.",
                "situation": "formal"
            }
        ],
        "relatedTerms": ["집수정", "배수관", "우수관", "오수관"],
        "level": "intermediate",
        "tags": ["조경", "배수", "외구공사", "토목"]
    },
    {
        "slug": "ho-ga",
        "korean": "맨홀",
        "vietnamese": "Hố ga",
        "hanja": "manhole",
        "hanjaReading": None,
        "pronunciation": "맨홀",
        "meaningKo": "지하 배수관, 전력선, 통신선 등을 점검하거나 접근하기 위한 지상 출입구를 의미합니다. 베트남에서는 'hố ga' (집수정·맨홀) 또는 'giếng thăm' (점검구)라고 합니다. 통역 시 주의: 베트남에서 'hố ga'는 배수용 집수정과 통신·전력 맨홀을 모두 지칭하므로, 용도를 명확히(hố ga thoát nước, hố ga điện, hố ga viễn thông) 구분해야 합니다. 맨홀 뚜껑(nắp hố ga)은 하중 등급(class A, B, C)과 도난 방지(chống trộm) 기능 여부를 확인하세요. 베트남은 맨홀 뚜껑 절도가 잦아 잠금장치 여부가 중요합니다.",
        "meaningVi": "Giếng kiểm tra, lối vào hệ thống thoát nước hoặc hầm kỹ thuật (điện, viễn thông) dưới lòng đất. Nắp hố ga có phân loại tải trọng (class A, B, C) và tính năng chống trộm. Cần phân biệt hố ga thoát nước (배수), hố ga điện (전력), hố ga viễn thông (통신).",
        "context": "지하 배수 시공, 전력·통신 인입 공사, 도로 유지보수 시",
        "culturalNote": "한국에서는 맨홀을 '맨홀' 또는 '점검구'라고 부르며, 용도별(통신, 전력, 하수)로 뚜껑 색상·표시가 다릅니다. 베트남은 'hố ga'로 통칭하며, 뚜껑에 용도 표시가 없거나 부실한 경우가 많아 현장에서 혼동이 잦습니다. 베트남은 맨홀 뚜껑 절도가 빈번해(재활용 금속 판매 목적) 주철(gang) 대신 콘크리트 또는 복합재(composite) 뚜껑을 쓰거나 잠금장치(khóa chống trộm)를 설치하는 경우가 많습니다. 또한 베트남 도로는 맨홀 주변 침하(sụt lún xung quanh hố ga)가 흔해, 시공 시 주변 되메우기(đắp lại xung quanh) 다짐을 철저히 해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "맨홀을 lỗ(구멍)로 번역",
                "correction": "hố ga (맨홀·집수정) 또는 giếng thăm (점검구)으로 번역",
                "explanation": "lỗ는 작은 구멍, 지하 구조물은 hố ga 사용"
            },
            {
                "mistake": "뚜껑을 nắp đậy(일반 덮개)로만 표현",
                "correction": "nắp hố ga (맨홀 뚜껑)로 명시",
                "explanation": "맨홀 전용 뚜껑은 nắp hố ga로 구분"
            },
            {
                "mistake": "하중 등급을 trọng lượng(무게)로 번역",
                "correction": "cấp tải trọng (하중 등급) 또는 class A/B/C로 표기",
                "explanation": "하중 등급은 표준화된 class 개념"
            }
        ],
        "examples": [
            {
                "ko": "이 맨홀은 통신용으로 전력 맨홀과 분리되어 있습니다.",
                "vi": "Hố ga này dùng cho viễn thông, tách biệt với hố ga điện.",
                "situation": "formal"
            },
            {
                "ko": "맨홀 뚜껑은 차량 하중을 견딜 수 있는 Class C로 해야 합니다.",
                "vi": "Nắp hố ga phải là loại Class C, chịu được tải trọng xe cộ.",
                "situation": "onsite"
            },
            {
                "ko": "절도 방지를 위해 잠금장치가 있는 뚜껑을 쓰세요.",
                "vi": "Để chống trộm, hãy dùng nắp có khóa chống trộm.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["배수구", "점검구", "집수정", "하수관"],
        "level": "intermediate",
        "tags": ["조경", "맨홀", "배수", "외구공사"]
    },
    {
        "slug": "duong-vien-da",
        "korean": "경계석",
        "vietnamese": "Đường viền đá",
        "hanja": "境界石",
        "hanjaReading": "境(지경 경) + 界(지경 계) + 石(돌 석)",
        "pronunciation": "경계석",
        "meaningKo": "도로와 인도, 차도와 중앙분리대, 화단과 보행로 등의 경계를 표시하는 돌 또는 콘크리트 구조물을 의미합니다. 베트남에서는 'đường viền đá' (석재 경계선) 또는 'dải phân cách' (분리대)라고 합니다. 통역 시 주의: 베트남 도로는 오토바이와 보행자 동선이 혼재되어 경계석 높이(chiều cao)와 경사(độ dốc)가 중요합니다. 높은 경계석(15~20cm)은 차량 진입 방지, 낮은 경계석(5~10cm)은 장애인 접근성 확보용입니다. 시각장애인 유도블록(gạch chỉ đường)과 연계된 경계석 경사로(dốc vỉa hè) 시공 지시 시 각도와 폭을 명확히 하세요.",
        "meaningVi": "Dải đá hoặc bê tông đánh dấu ranh giới giữa đường xe và vỉa hè, giữa làn đường và dải phân cách, hoặc giữa vườn hoa và lối đi. Có độ cao khác nhau: cao (15~20cm) để ngăn xe, thấp (5~10cm) để dễ tiếp cận cho người khuyết tật. Cần kết hợp với dốc vỉa hè (rampe) và gạch chỉ đường.",
        "context": "도로 외구 공사, 인도 정비, 화단 조성, 주차장 경계 시공 시",
        "culturalNote": "한국은 경계석을 주로 화강석(đá granite) 또는 콘크리트로 만들며, 표준 규격(높이 15cm, 폭 20cm)이 정해져 있습니다. 베트남도 비슷한 규격을 쓰지만, 시공 품질이 지역마다 편차가 커서 경계석이 흔들리거나(lung lay) 침하되는(sụt lún) 경우가 많습니다. 베트남은 장애인 접근성(tiếp cận cho người khuyết tật) 법규가 최근 강화되어, 횡단보도 앞 경계석 경사로(dốc vỉa hè) 설치가 의무화되었지만, 시공 각도(8% 이하)와 폭(최소 1.2m) 기준을 지키지 않는 현장이 많아 도면 지시 시 명확한 수치를 제시해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "경계석을 đá ranh giới(경계 돌)로 번역",
                "correction": "đường viền đá (경계석) 또는 dải phân cách (분리대)로 번역",
                "explanation": "건설 현장에서는 đường viền đá가 표준 용어"
            },
            {
                "mistake": "경사로를 đường dốc(경사길)로만 번역",
                "correction": "dốc vỉa hè (보도 경사로) 또는 rampe (경사로 외래어)로 명시",
                "explanation": "장애인 접근성 시설은 dốc vỉa hè로 구분"
            },
            {
                "mistake": "높이를 cao(높음)로만 표현",
                "correction": "chiều cao đường viền (경계석 높이) + 구체적 수치(15cm)로 표기",
                "explanation": "시공 시 정확한 높이 전달이 중요"
            }
        ],
        "examples": [
            {
                "ko": "이 경계석은 높이 15cm, 폭 20cm 화강석으로 시공하세요.",
                "vi": "Đường viền đá này cao 15cm, rộng 20cm, dùng đá granite.",
                "situation": "formal"
            },
            {
                "ko": "횡단보도 앞에는 경계석 경사로를 8% 이하로 만들어야 합니다.",
                "vi": "Trước vạch sang đường phải làm dốc vỉa hè dưới 8%.",
                "situation": "onsite"
            },
            {
                "ko": "경계석이 흔들리지 않도록 기초 콘크리트를 타설하세요.",
                "vi": "Đổ bê tông móng để đường viền đá không bị lung lay.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["보도블록", "중앙분리대", "경사로", "화단"],
        "level": "intermediate",
        "tags": ["조경", "경계석", "외구공사", "도로"]
    },
    {
        "slug": "den-ngoai-troi",
        "korean": "옥외조명",
        "vietnamese": "Đèn ngoài trời",
        "hanja": "屋外照明",
        "hanjaReading": "屋(집 옥) + 外(바깥 외) + 照(비출 조) + 明(밝을 명)",
        "pronunciation": "옥외조명",
        "meaningKo": "건물 외부, 도로, 공원, 주차장 등 실외 공간에 설치하는 조명 기구를 의미합니다. 베트남에서는 'đèn ngoài trời' (실외 조명) 또는 'đèn chiếu sáng công cộng' (공공 조명)이라고 합니다. 통역 시 주의: 베트남은 열대 기후로 습도가 높고 해충이 많아, 조명의 방수등급(IP 등급)과 방충(chống côn trùng) 성능이 중요합니다. 도로조명(đèn đường), 보안등(đèn an ninh), 경관조명(đèn trang trí cảnh quan)을 구분하고, LED 교체 시 색온도(nhiệt độ màu)와 조도(độ chiếu sáng lux) 기준을 명확히 하세요. 베트남은 가로등 절도(trộm đèn)와 부품 탈거가 잦아 고정 방식도 중요합니다.",
        "meaningVi": "Hệ thống đèn chiếu sáng lắp đặt ngoài trời: đường phố, công viên, bãi đỗ xe, sân vườn. Cần chú ý cấp độ chống nước (IP rating), nhiệt độ màu (K), độ chiếu sáng (lux), và khả năng chống trộm. Phân loại: đèn đường (가로등), đèn an ninh (보안등), đèn trang trí cảnh quan (경관조명).",
        "context": "도로 조명 공사, 공원 야간 경관 조성, 주차장 보안등 설치 시",
        "culturalNote": "한국은 옥외조명으로 LED를 많이 쓰며, 색온도 5000K(주광색)가 표준입니다. 베트남도 LED가 보급되고 있지만 기존 나트륨등(đèn natri, 황색)이나 수은등(đèn thủy ngân)이 많이 남아있어 교체 프로젝트가 많습니다. 베트남은 습도가 높아 조명 내부 결로(đọng nước trong đèn)가 잦으므로 IP65 이상 방수등급을 권장하며, 밤에 날벌레(côn trùng)가 많아 적외선 유인이 적은 LED가 유리합니다. 또한 베트남은 가로등 전선 절도와 LED 모듈 탈거 사건이 많아, 나사 대신 특수 고정구(ốc chống trộm)나 용접(hàn)으로 고정하는 경우가 흔합니다. 조명 간격(khoảng cách giữa các cột đèn)도 한국은 30~40m, 베트남은 20~30m로 더 촘촘한 편입니다.",
        "commonMistakes": [
            {
                "mistake": "옥외조명을 đèn ngoài(바깥 등)로만 번역",
                "correction": "đèn ngoài trời (실외 조명) 또는 đèn chiếu sáng công cộng (공공 조명)으로 번역",
                "explanation": "ngoài는 일상어, ngoài trời가 기술 용어"
            },
            {
                "mistake": "IP등급을 cấp IP(레벨 IP)로만 표현",
                "correction": "cấp độ chống nước IP (방수등급 IP) + 숫자(IP65)로 명시",
                "explanation": "IP 등급은 방수·방진 개념 설명 필요"
            },
            {
                "mistake": "조도를 độ sáng(밝기)로만 번역",
                "correction": "độ chiếu sáng (조도) + 단위 lux로 표기",
                "explanation": "조도는 정량적 단위(lux)와 함께 써야 함"
            }
        ],
        "examples": [
            {
                "ko": "이 가로등은 IP65 방수등급, 5000K 색온도 LED입니다.",
                "vi": "Đèn đường này có cấp độ chống nước IP65, LED nhiệt độ màu 5000K.",
                "situation": "formal"
            },
            {
                "ko": "주차장 조명은 보안등 기능으로 밤에 자동 점등되어야 합니다.",
                "vi": "Đèn bãi đỗ xe phải có chức năng đèn an ninh, tự động bật vào ban đêm.",
                "situation": "onsite"
            },
            {
                "ko": "조명 간격은 25m로 하고, 고정은 특수 나사로 하세요.",
                "vi": "Khoảng cách giữa các cột đèn là 25m, dùng ốc chống trộm để cố định.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["가로등", "보안등", "경관조명", "LED조명"],
        "level": "intermediate",
        "tags": ["조경", "옥외조명", "외구공사", "전기"]
    },
    {
        "slug": "mat-bai-xe",
        "korean": "주차장바닥",
        "vietnamese": "Mặt bãi xe",
        "hanja": "駐車場바닥",
        "hanjaReading": "駐(머물 주) + 車(수레 차) + 場(마당 장) + 바닥(순우리말)",
        "pronunciation": "주차장바닥",
        "meaningKo": "주차장의 포장 표면(바닥재)을 의미하며, 콘크리트, 아스팔트, 인터로킹블록 등 다양한 재료로 시공합니다. 베트남에서는 'mặt bãi xe' (주차장 표면) 또는 'nền bãi đỗ xe' (주차장 기초)라고 합니다. 통역 시 주의: 베트남은 햇빛이 강해 아스팔트가 여름에 연화(mềm ra)되어 타이어 자국(vết lốp xe)이 쉽게 생기므로, 고온 안정성이 높은 SMA(đá-nhựa cải tiến) 아스팔트나 콘크리트 포장을 권장합니다. 주차장 표시선(vạch kẻ bãi xe), 경사도(độ dốc), 배수(thoát nước)도 함께 설명해야 하며, 차량 하중(3톤, 5톤, 10톤)에 따른 두께 설계 차이를 명확히 하세요.",
        "meaningVi": "Mặt lát (bề mặt) của bãi đỗ xe, thi công bằng bê tông, nhựa đường, hoặc gạch interlocking. Phải chịu tải trọng xe, chống nóng, thoát nước tốt. Cần chú ý độ dốc thoát nước, vạch kẻ chỗ đỗ, và độ dày theo loại xe (xe con, xe tải).",
        "context": "주차장 신축 공사, 주차장 포장 보수, 외구 주차 공간 조성 시",
        "culturalNote": "한국은 주차장 바닥을 주로 아스팔트 콘크리트(아스콘)로 시공하며, 지하주차장은 에폭시 도장(sơn epoxy)을 많이 씁니다. 베트남은 옥외 주차장을 아스팔트, 콘크리트, 인터로킹블록으로 다양하게 시공하는데, 열대 기후 특성상 아스팔트는 여름(40도 이상)에 표면이 물러져(mềm) 타이어 자국이 남는 문제가 있습니다. 따라서 고급 주차장은 콘크리트 포장이나 SMA 아스팔트(석분과 개질 아스팔트 혼합)를 선호합니다. 베트남 주차장은 오토바이 전용 구역(khu để xe máy)과 자동차 구역(khu để ô tô)을 명확히 구분하며, 주차선 색상(màu sơn vạch kẻ)은 흰색(차선), 노란색(금지선)이 일반적입니다. 배수 경사는 최소 1~2% 확보가 필요하며, 집중호우 대비 배수구(cống thoát nước) 위치를 충분히 배치해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "주차장바닥을 sàn bãi xe(주차장 바닥판)로 번역",
                "correction": "mặt bãi xe (주차장 표면) 또는 nền bãi đỗ xe (주차장 기초)로 번역",
                "explanation": "sàn은 실내 바닥, 옥외 포장은 mặt/nền 사용"
            },
            {
                "mistake": "아스팔트를 nhựa(플라스틱)로만 번역",
                "correction": "nhựa đường (아스팔트 도로) 또는 bê tông nhựa (아스콘)로 명시",
                "explanation": "nhựa는 일반 플라스틱, 도로 재료는 nhựa đường"
            },
            {
                "mistake": "경사를 dốc(경사)로만 표현",
                "correction": "độ dốc thoát nước (배수 경사) + 퍼센트(1~2%)로 명시",
                "explanation": "배수 목적과 정량 수치 전달이 중요"
            }
        ],
        "examples": [
            {
                "ko": "이 주차장은 콘크리트 포장 두께 20cm로 5톤 차량 하중을 견딜 수 있습니다.",
                "vi": "Bãi xe này lát bê tông dày 20cm, chịu được tải trọng xe 5 tấn.",
                "situation": "formal"
            },
            {
                "ko": "배수를 위해 바닥 경사를 2%로 주고 배수구를 설치하세요.",
                "vi": "Để thoát nước, làm độ dốc mặt bãi 2% và lắp cống thoát nước.",
                "situation": "onsite"
            },
            {
                "ko": "주차선은 흰색 페인트로 폭 10cm, 길이 5m로 그려주세요.",
                "vi": "Vạch kẻ chỗ đỗ xe dùng sơn trắng, rộng 10cm, dài 5m.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["아스팔트", "콘크리트포장", "인터로킹블록", "주차선"],
        "level": "intermediate",
        "tags": ["조경", "주차장", "외구공사", "포장"]
    },
    {
        "slug": "trong-cay",
        "korean": "식재공사",
        "vietnamese": "Trồng cây",
        "hanja": "植栽工事",
        "hanjaReading": "植(심을 식) + 栽(심을 재) + 工(장인 공) + 事(일 사)",
        "pronunciation": "식재공사",
        "meaningKo": "나무, 관목, 초화류 등을 심는 조경 공사를 의미합니다. 베트남에서는 'trồng cây' (나무 심기) 또는 'thi công cảnh quan cây xanh' (조경수 시공)이라고 합니다. 통역 시 주의: 베트남은 열대 기후로 우기·건기가 뚜렷해, 식재 시기(thời điểm trồng)가 매우 중요합니다. 우기 초(5~6월)에 심어야 활착률(tỷ lệ sống)이 높고, 건기(12~4월)에는 관수(tưới nước) 빈도를 늘려야 합니다. 수목 크기(quy cách cây), 식재 간격(khoảng cách trồng), 뿌리분(bầu đất) 처리, 지주목(cọc chống) 설치 방법을 명확히 전달하세요. 하자보수 기간(bảo hành)은 보통 3년이며, 고사(chết) 시 재식재 의무가 있습니다.",
        "meaningVi": "Công việc trồng cây xanh, cây bụi, hoa cỏ trong dự án cảnh quan. Cần chú ý thời điểm trồng (mùa mưa tốt nhất), quy cách cây (chiều cao, đường kính gốc), khoảng cách trồng, xử lý bầu đất, cọc chống đỡ, tưới nước, và bảo hành (thường 3 năm). Nếu cây chết phải trồng lại.",
        "context": "조경 공사, 공원 조성, 가로수 식재, 아파트 단지 녹지 조성 시",
        "culturalNote": "한국은 봄(3~5월)이 식재 적기이지만, 베트남은 열대 기후로 우기 시작(5~6월)이 최적 식재 시기입니다. 건기(12~4월)에 심으면 활착률이 떨어지고 관수 비용이 증가합니다. 베트남 조경 시장은 중국·태국산 수입 묘목이 많아 병충해 검역(kiểm dịch sâu bệnh)과 토양 적응성(thích nghi đất) 확인이 필수입니다. 한국은 지주목을 2~3개 세우는 반면, 베트남은 태풍(bão) 대비로 3~4개 또는 삼각 지지대(giá đỡ tam giác)를 쓰는 경우가 많습니다. 베트남 현장에서는 식재 후 뿌리분에 충분한 물을 주지 않거나(không tưới đủ nước) 지주목을 너무 조여 수목을 상하게 하는(thắt chặt làm cây bị thương) 시공 오류가 잦으므로, 시방서에 '뿌리분 관수 20L 이상', '지주목 완충재 사용' 등 구체적 지시를 명기해야 합니다.",
        "commonMistakes": [
            {
                "mistake": "식재를 trồng(심다)로만 번역",
                "correction": "thi công trồng cây (식재 공사) 또는 công tác cảnh quan (조경 작업)으로 표현",
                "explanation": "trồng은 동사, 공사는 thi công 추가 필요"
            },
            {
                "mistake": "활착률을 tỷ lệ sống(생존율)로만 번역",
                "correction": "tỷ lệ sống sau khi trồng (식재 후 생존율) 또는 활착률로 설명",
                "explanation": "맥락 없이 '생존율'만 쓰면 의미 모호"
            },
            {
                "mistake": "지주목을 cây gỗ(나무)로 번역",
                "correction": "cọc chống (지주목) 또는 cột chống đỡ cây (나무 지지대)로 명시",
                "explanation": "cây gỗ는 일반 목재, 지주목은 cọc chống"
            }
        ],
        "examples": [
            {
                "ko": "이 수목은 우기 시작 전에 식재하고 지주목을 3개 설치하세요.",
                "vi": "Trồng cây này trước mùa mưa và lắp 3 cọc chống đỡ.",
                "situation": "onsite"
            },
            {
                "ko": "식재 후 3년간 하자보수가 있으며, 고사 시 동일 규격으로 재식재합니다.",
                "vi": "Sau khi trồng có bảo hành 3 năm, nếu cây chết phải trồng lại cây cùng quy cách.",
                "situation": "formal"
            },
            {
                "ko": "뿌리분에 물을 20L 이상 충분히 주고 뿌리 주변을 다져주세요.",
                "vi": "Tưới ít nhất 20L nước vào bầu đất và đầm chặt xung quanh gốc cây.",
                "situation": "onsite"
            }
        ],
        "relatedTerms": ["조경수목", "지주목", "관수", "하자보수"],
        "level": "intermediate",
        "tags": ["조경", "식재", "외구공사", "수목"]
    }
]

def main():
    """메인 실행 함수"""

    # 파일 경로
    json_file = "/Users/mac/Documents/claude_code/projects/vn.epicstage.co.kr/src/data/terms/construction.json"

    # 기존 JSON 파일 읽기
    with open(json_file, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    print(f"기존 용어 수: {len(existing_data)}")

    # 중복 체크 (slug 기준)
    existing_slugs = {term['slug'] for term in existing_data}
    new_terms = [term for term in data if term['slug'] not in existing_slugs]

    if not new_terms:
        print("⚠️ 모든 용어가 이미 존재합니다. 추가할 용어가 없습니다.")
        return

    print(f"추가할 신규 용어 수: {len(new_terms)}")

    # 기존 데이터에 신규 용어 추가
    existing_data.extend(new_terms)

    # JSON 파일 저장 (pretty print)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(new_terms)}개 용어 추가 완료!")
    print(f"총 용어 수: {len(existing_data)}")
    print("\n추가된 용어:")
    for term in new_terms:
        print(f"  - {term['korean']} ({term['slug']})")

if __name__ == "__main__":
    main()
