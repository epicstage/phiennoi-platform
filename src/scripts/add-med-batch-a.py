#!/usr/bin/env python3
import json, os
path = os.path.join(os.path.dirname(__file__), '../data/terms/medical.json')
with open(path, 'r', encoding='utf-8') as f: data = json.load(f)
existing = {t['slug'] for t in data}

def t(s,k,v,mk,mv,cx,cn,cm,ex,rt):
    return {"slug":s,"korean":k,"vietnamese":v,"hanja":None,"hanjaReading":None,"pronunciation":s,"meaningKo":mk,"meaningVi":mv,"context":cx,"culturalNote":cn,"commonMistakes":cm,"examples":ex,"relatedTerms":rt}

new = [
t("benh-crohn","크론병","bệnh Crohn","소화관 어디서든 발생할 수 있는 만성 염증성 장질환입니다. 복통, 설사, 체중 감소가 나타납니다. 약물과 식이로 관리합니다. 통역 시 만성 질환임, 재발 가능성, 장기 관리를 설명해야 합니다.",
"Bệnh viêm ruột mãn tính có thể xảy ra ở bất kỳ đâu trong đường tiêu hóa","소화기내과","한국에서 크론병 환자가 증가하고 있습니다. 젊은 층에 많으며 평생 관리가 필요합니다.",
[{"mistake":"완치 가능하다고 설명","correction":"관해 유지가 목표, 완치 개념과 다름","explanation":"현실적 기대를 갖게 합니다"},
{"mistake":"식이 제한 일률적 안내","correction":"개인차 있어 자신에게 맞는 식이 찾기","explanation":"맞춤형 관리가 중요합니다"},
{"mistake":"수술하면 끝이라고 설명","correction":"수술 후에도 재발 가능, 약물 치료 지속","explanation":"지속적 관리의 중요성을 강조합니다"}],
[{"ko":"크론병으로 약물 치료가 필요합니다.","vi":"Bệnh Crohn cần điều trị bằng thuốc.","situation":"formal"},
{"ko":"증상이 없어도 약을 드셔야 해요.","vi":"Dù không có triệu chứng vẫn phải uống thuốc.","situation":"formal"},
{"ko":"스트레스 받으면 더 심해질 수 있어요.","vi":"Stress có thể làm nặng thêm.","situation":"informal"}],
["염증성장질환","생물학적제제","장폐색"]),

t("viem-loet-dai-trang","궤양성대장염","viêm loét đại tràng","대장에 궤양이 생기는 만성 염증성 장질환입니다. 혈변, 설사, 복통이 특징입니다. 크론병과 구분됩니다. 통역 시 대장암 위험 증가, 정기 검진 필요성을 설명해야 합니다.",
"Bệnh viêm ruột mãn tính với loét ở đại tràng","소화기내과","한국에서 궤양성대장염도 증가 추세입니다. 10년 이상 이환 시 대장암 위험이 높아집니다.",
[{"mistake":"크론병과 동일시","correction":"궤양성대장염은 대장에만, 크론병은 전 소화관","explanation":"정확한 진단을 이해시킵니다"},
{"mistake":"대장암 위험 미설명","correction":"10년 이상 이환 시 정기 대장내시경 필요","explanation":"암 조기 발견을 위해 중요합니다"},
{"mistake":"약 중단 가능성 과대평가","correction":"대부분 장기 약물 치료 필요","explanation":"치료 지속의 중요성을 강조합니다"}],
[{"ko":"궤양성대장염으로 진단되었습니다.","vi":"Được chẩn đoán viêm loét đại tràng.","situation":"formal"},
{"ko":"정기적으로 대장내시경을 받으셔야 합니다.","vi":"Cần nội soi đại tràng định kỳ.","situation":"formal"},
{"ko":"피 섞인 설사가 계속되면 바로 오세요.","vi":"Nếu tiêu chảy ra máu liên tục thì đến ngay.","situation":"informal"}],
["염증성장질환","대장암","5-ASA"]),

t("viem-tuy-cap","급성췌장염","viêm tụy cấp","췌장에 급성 염증이 발생하는 질환입니다. 심한 복통, 구토가 특징입니다. 담석, 음주가 주요 원인입니다. 통역 시 금식, 통증 관리, 원인 제거 중요성을 설명해야 합니다.",
"Viêm tụy cấp tính gây đau bụng dữ dội và nôn","소화기내과, 응급의학","한국에서 급성췌장염은 음주와 관련이 많습니다. 중증 시 생명을 위협할 수 있습니다.",
[{"mistake":"가벼운 질환으로 설명","correction":"중증 시 생명 위험, 입원 필요함을 강조","explanation":"질환의 심각성을 인지시킵니다"},
{"mistake":"금식 이유 미설명","correction":"췌장을 쉬게 하기 위해 금식 필요","explanation":"치료 협조를 얻습니다"},
{"mistake":"원인 제거 미강조","correction":"담석 제거, 금주가 재발 방지에 필수","explanation":"재발을 예방합니다"}],
[{"ko":"급성췌장염으로 입원이 필요합니다.","vi":"Viêm tụy cấp cần nhập viện.","situation":"formal"},
{"ko":"며칠간 드시면 안 됩니다.","vi":"Vài ngày không được ăn.","situation":"formal"},
{"ko":"술 때문에 췌장이 망가졌어요.","vi":"Tụy hỏng vì rượu.","situation":"informal"}],
["담석","금주","통증관리"]),

t("xo-gan","간경변","xơ gan","간이 딱딱하게 굳어 기능이 떨어지는 말기 간질환입니다. B/C형 간염, 알코올이 주요 원인입니다. 복수, 황달, 정맥류 출혈이 나타납니다. 통역 시 합병증 관리, 이식 가능성을 설명해야 합니다.",
"Bệnh gan giai đoạn cuối, gan cứng và mất chức năng","소화기내과","한국에서 간경변은 B형간염과 알코올이 주요 원인입니다. 정기 관리로 합병증을 예방합니다.",
[{"mistake":"간경변을 완치 가능하다고 설명","correction":"비가역적 손상, 진행 방지와 합병증 관리 목표","explanation":"현실적 기대를 갖게 합니다"},
{"mistake":"간이식 가능성 미언급","correction":"말기 간경변 시 이식이 유일한 치료","explanation":"치료 옵션을 알립니다"},
{"mistake":"금주 중요성 미강조","correction":"알코올성이든 아니든 절대 금주 필요","explanation":"질환 진행을 막습니다"}],
[{"ko":"간경변으로 정기 관리가 필요합니다.","vi":"Xơ gan cần quản lý định kỳ.","situation":"formal"},
{"ko":"술은 절대로 드시면 안 됩니다.","vi":"Tuyệt đối không được uống rượu.","situation":"formal"},
{"ko":"배에 물 차면 바로 오세요.","vi":"Nếu bụng sưng nước thì đến ngay.","situation":"informal"}],
["복수","정맥류","간이식"]),

t("soi-mat","담석증","sỏi mật","담낭이나 담도에 돌이 생기는 질환입니다. 우상복부 통증, 소화불량이 나타납니다. 증상 있으면 담낭절제술이 필요합니다. 통역 시 증상 유무에 따른 치료 방침을 설명해야 합니다.",
"Sỏi hình thành trong túi mật hoặc đường mật","소화기내과, 외과","한국에서 담석증은 복강경 담낭절제술로 치료합니다. 무증상이면 경과 관찰도 가능합니다.",
[{"mistake":"무증상 담석도 수술 필요하다고 설명","correction":"무증상이면 경과 관찰 가능, 증상 시 수술","explanation":"불필요한 수술을 피합니다"},
{"mistake":"담낭 제거 후 소화 문제 과장","correction":"대부분 적응되어 정상 생활 가능","explanation":"수술 공포를 줄입니다"},
{"mistake":"담도결석과 담낭결석 미구분","correction":"위치에 따라 치료 방법이 다름을 설명","explanation":"정확한 치료 계획을 세웁니다"}],
[{"ko":"담석증으로 수술을 권합니다.","vi":"Sỏi mật nên mổ.","situation":"formal"},
{"ko":"복강경으로 하면 회복이 빠릅니다.","vi":"Mổ nội soi thì hồi phục nhanh.","situation":"formal"},
{"ko":"담석 있어도 증상 없으면 놔둬도 돼요.","vi":"Có sỏi mà không triệu chứng thì để yên cũng được.","situation":"informal"}],
["담낭절제술","담도결석","복강경"]),

t("trao-nguoc-da-day","역류성식도염","trào ngược dạ dày","위산이 식도로 역류하여 염증이 생기는 질환입니다. 속쓰림, 신트림이 특징입니다. 위산억제제로 치료합니다. 통역 시 생활습관 개선, 약물 복용 기간을 설명해야 합니다.",
"Viêm thực quản do trào ngược acid dạ dày","소화기내과","한국에서 역류성식도염은 매우 흔합니다. 생활습관 개선과 함께 약물 치료가 효과적입니다.",
[{"mistake":"약으로만 치료 가능하다고 설명","correction":"식이, 자세, 체중 관리도 중요","explanation":"생활습관 개선을 강조합니다"},
{"mistake":"증상 없으면 약 중단해도 된다고 설명","correction":"의사 상담 후 서서히 줄이기","explanation":"재발을 방지합니다"},
{"mistake":"합병증 미설명","correction":"장기간 방치 시 식도암 위험 증가","explanation":"치료 필요성을 강조합니다"}],
[{"ko":"역류성식도염으로 약을 처방합니다.","vi":"Viêm trào ngược nên kê thuốc.","situation":"formal"},
{"ko":"식후 바로 눕지 마세요.","vi":"Không nằm ngay sau khi ăn.","situation":"formal"},
{"ko":"커피, 술 줄이면 많이 좋아져요.","vi":"Giảm cà phê và rượu thì đỡ nhiều.","situation":"informal"}],
["위산억제제","속쓰림","생활습관"]),

t("viem-tuyen-giap","갑상선염","viêm tuyến giáp","갑상선에 염증이 생기는 질환입니다. 급성, 아급성, 만성(하시모토)으로 구분됩니다. 갑상선 기능 이상을 유발합니다. 통역 시 염증 유형, 기능 검사 필요성을 설명해야 합니다.",
"Viêm tuyến giáp, có nhiều loại với nguyên nhân khác nhau","내분비내과","한국에서 하시모토갑상선염은 갑상선기능저하증의 흔한 원인입니다.",
[{"mistake":"모든 갑상선염이 같다고 설명","correction":"유형에 따라 치료와 예후가 다름","explanation":"정확한 진단이 중요합니다"},
{"mistake":"갑상선암과 혼동","correction":"염증과 암은 다름, 결절 검사는 별도","explanation":"불필요한 공포를 줄입니다"},
{"mistake":"평생 약 복용 필요 단정","correction":"아급성은 회복 가능, 만성은 약 필요할 수 있음","explanation":"유형별 설명이 필요합니다"}],
[{"ko":"갑상선염으로 기능 검사가 필요합니다.","vi":"Viêm tuyến giáp cần xét nghiệm chức năng.","situation":"formal"},
{"ko":"목이 아프고 열이 나는 건 아급성 갑상선염 증상입니다.","vi":"Đau cổ và sốt là triệu chứng viêm tuyến giáp bán cấp.","situation":"formal"},
{"ko":"이 종류는 시간 지나면 괜찮아져요.","vi":"Loại này qua thời gian sẽ khỏi.","situation":"informal"}],
["갑상선기능검사","하시모토","갑상선호르몬"]),

t("benh-basedow","그레이브스병","bệnh Basedow","갑상선 기능이 항진되는 자가면역 질환입니다. 체중 감소, 빈맥, 안구돌출이 특징입니다. 항갑상선제, 방사성요오드, 수술로 치료합니다. 통역 시 치료 옵션, 장기 관리를 설명해야 합니다.",
"Bệnh tự miễn gây cường giáp với sụt cân, tim đập nhanh, lồi mắt","내분비내과","한국에서 그레이브스병은 갑상선기능항진증의 가장 흔한 원인입니다.",
[{"mistake":"약물 치료로 완치된다고만 설명","correction":"재발 가능성 있어 장기 추적 필요","explanation":"현실적 기대를 갖게 합니다"},
{"mistake":"방사성요오드 치료 두려움 과장","correction":"안전하고 효과적인 치료임을 설명","explanation":"치료 옵션을 균형있게 안내합니다"},
{"mistake":"안구 증상 치료 미언급","correction":"안과 진료가 필요할 수 있음 안내","explanation":"합병증 관리를 포함합니다"}],
[{"ko":"그레이브스병으로 갑상선 기능이 높습니다.","vi":"Bệnh Basedow làm chức năng tuyến giáp cao.","situation":"formal"},
{"ko":"약으로 조절하다가 다른 치료가 필요할 수 있어요.","vi":"Dùng thuốc kiểm soát, có thể cần điều trị khác sau.","situation":"formal"},
{"ko":"심장이 빨리 뛰는 건 갑상선 때문이에요.","vi":"Tim đập nhanh là do tuyến giáp.","situation":"informal"}],
["갑상선기능항진증","항갑상선제","안구돌출"]),

t("suy-tuyen-giap","갑상선기능저하증","suy tuyến giáp","갑상선 호르몬이 부족한 상태입니다. 피로, 체중 증가, 추위 못 참음이 특징입니다. 갑상선 호르몬제로 치료합니다. 통역 시 평생 복용 필요성, 정기 검사를 설명해야 합니다.",
"Tình trạng thiếu hormone tuyến giáp gây mệt mỏi, tăng cân, sợ lạnh","내분비내과","한국에서 갑상선기능저하증은 여성에게 많습니다. 약물로 잘 조절됩니다.",
[{"mistake":"증상 호전되면 약 중단해도 된다고 설명","correction":"대부분 평생 복용 필요, 중단 시 증상 재발","explanation":"약물 복용의 중요성을 강조합니다"},
{"mistake":"부작용 과장","correction":"적절한 용량은 부작용 없이 정상 상태 유지","explanation":"약에 대한 불안을 줄입니다"},
{"mistake":"임신 시 주의사항 미설명","correction":"임신 중에도 복용 필요, 용량 조절 필요할 수 있음","explanation":"가임기 여성에게 중요합니다"}],
[{"ko":"갑상선기능저하증으로 호르몬제가 필요합니다.","vi":"Suy tuyến giáp cần uống hormone.","situation":"formal"},
{"ko":"이 약은 평생 드셔야 합니다.","vi":"Thuốc này phải uống suốt đời.","situation":"formal"},
{"ko":"약 먹으면 피곤한 거 없어져요.","vi":"Uống thuốc thì hết mệt.","situation":"informal"}],
["갑상선호르몬","하시모토","피로"]),

t("hoi-chung-cushing","쿠싱증후군","hội chứng Cushing","코르티솔 과다로 발생하는 질환입니다. 비만, 달덩이얼굴, 고혈압이 특징입니다. 원인에 따라 수술, 약물로 치료합니다. 통역 시 원인 규명, 치료 옵션을 설명해야 합니다.",
"Bệnh do thừa cortisol gây béo phì, mặt tròn, cao huyết áp","내분비내과","한국에서 쿠싱증후군은 드물지만 심각한 합병증을 유발합니다.",
[{"mistake":"단순 비만과 혼동","correction":"특징적인 체형 변화(중심 비만, 얇은 팔다리)가 다름","explanation":"정확한 진단을 이해시킵니다"},
{"mistake":"스테로이드 유발 가능성 미설명","correction":"장기 스테로이드 복용이 원인일 수 있음","explanation":"원인 파악에 중요합니다"},
{"mistake":"치료 후 회복 기간 미설명","correction":"원인 제거 후에도 회복에 수개월-수년 소요","explanation":"현실적 기대를 갖게 합니다"}],
[{"ko":"쿠싱증후군 의심으로 추가 검사가 필요합니다.","vi":"Nghi hội chứng Cushing cần xét nghiệm thêm.","situation":"formal"},
{"ko":"혹시 스테로이드 약을 오래 드셨나요?","vi":"Có uống thuốc steroid lâu không?","situation":"formal"},
{"ko":"살이 찌는 게 병 때문일 수 있어요.","vi":"Tăng cân có thể là do bệnh.","situation":"informal"}],
["코르티솔","부신종양","스테로이드"]),

t("suy-tuyen-thuong-than","부신기능저하증","suy tuyến thượng thận","부신에서 호르몬이 부족한 상태입니다. 피로, 저혈압, 피부 착색이 특징입니다. 호르몬 보충이 필요합니다. 통역 시 응급 상황(부신위기), 스테로이드 카드 휴대를 설명해야 합니다.",
"Tình trạng thiếu hormone từ tuyến thượng thận","내분비내과","한국에서 부신기능저하증은 드물지만 응급 상황이 될 수 있어 환자 교육이 중요합니다.",
[{"mistake":"부신위기 가능성 미설명","correction":"스트레스, 감염 시 응급 상황 발생 가능","explanation":"응급 대처를 준비시킵니다"},
{"mistake":"약물 임의 중단 위험 미강조","correction":"갑자기 끊으면 생명 위협적, 절대 금지","explanation":"약물 복용의 중요성을 강조합니다"},
{"mistake":"스테로이드 카드 미안내","correction":"응급 시 의료진에게 보여줄 카드 휴대 권고","explanation":"안전을 보장합니다"}],
[{"ko":"부신기능저하증으로 호르몬 보충이 필요합니다.","vi":"Suy tuyến thượng thận cần bổ sung hormone.","situation":"formal"},
{"ko":"아플 때는 약 용량을 늘려야 합니다.","vi":"Khi ốm phải tăng liều thuốc.","situation":"formal"},
{"ko":"이 약 끊으면 위험해요, 꼭 드세요.","vi":"Ngưng thuốc này nguy hiểm, phải uống.","situation":"informal"}],
["애디슨병","부신위기","스테로이드"]),

t("loang-xuong","골다공증","loãng xương","뼈 밀도가 낮아져 골절 위험이 높은 상태입니다. 폐경 후 여성에게 흔합니다. 칼슘, 비타민D, 약물로 치료합니다. 통역 시 골밀도검사, 약물, 낙상 예방을 설명해야 합니다.",
"Tình trạng mật độ xương thấp, dễ gãy xương","내분비내과, 정형외과","한국에서 골다공증은 65세 이상 여성의 30%에서 발견됩니다. 예방이 중요합니다.",
[{"mistake":"골다공증이 아프다고 설명","correction":"대부분 무증상, 골절로 발견되는 경우 많음","explanation":"검진의 중요성을 강조합니다"},
{"mistake":"칼슘만 먹으면 된다고 설명","correction":"비타민D, 운동, 약물 치료도 필요","explanation":"종합적 관리를 안내합니다"},
{"mistake":"약물 부작용만 강조","correction":"골절 예방 효과가 부작용보다 큼","explanation":"약물 복용을 독려합니다"}],
[{"ko":"골다공증으로 약물 치료가 필요합니다.","vi":"Loãng xương cần điều trị bằng thuốc.","situation":"formal"},
{"ko":"칼슘과 비타민D를 같이 드세요.","vi":"Uống canxi cùng vitamin D.","situation":"formal"},
{"ko":"넘어지면 뼈 쉽게 부러져요, 조심하세요.","vi":"Ngã thì dễ gãy xương, cẩn thận.","situation":"informal"}],
["골밀도검사","칼슘","비스포스포네이트"]),
]

added = [n for n in new if n['slug'] not in existing]
data.extend(added)
print(f"A배치 추가: {len(added)}개, 총: {len(data)}개")
with open(path, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False, indent=2)
