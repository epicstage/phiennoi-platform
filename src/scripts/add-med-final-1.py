#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Medical 500개 달성을 위한 마지막 1개 용어 추가"""

import json

def t(s,k,v,mk,mv,cx,cn,cm,ex,rt):
    return {"slug":s,"korean":k,"vietnamese":v,"hanja":None,"hanjaReading":None,
            "pronunciation":s,"meaningKo":mk,"meaningVi":mv,"context":cx,
            "culturalNote":cn,"commonMistakes":cm,"examples":ex,"relatedTerms":rt}

terms = [
    t("chan-doan-hinh-anh",
      "영상의학검사",
      "chẩn đoán hình ảnh",
      "X선, CT, MRI, 초음파 등 영상 장비를 이용해 몸 내부를 촬영하여 질병을 진단하는 검사입니다. 각 검사의 특성, 장단점, 주의사항이 다르므로 통역 시 환자가 받는 검사의 목적과 방법을 정확히 설명해야 합니다. 조영제 사용 여부, 금식 필요 여부, 검사 소요 시간 등 실질적인 정보 전달이 중요합니다.",
      "Các xét nghiệm sử dụng thiết bị hình ảnh như X-quang, CT, MRI, siêu âm để chụp bên trong cơ thể và chẩn đoán bệnh. Mỗi loại xét nghiệm có đặc điểm, ưu nhược điểm và lưu ý khác nhau.",
      ["영상의학과", "진단검사", "건강검진"],
      "베트남에서는 MRI, CT 등 고가 장비가 대도시 대형병원에 집중되어 있어 접근성이 낮습니다. 한국의 영상검사 접근성과 정확도에 대해 긍정적으로 인식하는 경우가 많습니다. 그러나 과잉 검사에 대한 우려도 있으므로, 검사의 필요성을 명확히 설명해야 합니다. 조영제 알레르기 병력 확인은 필수입니다.",
      [{"mistake":"검사 종류별 차이 설명 없이 통칭","correction":"X선, CT, MRI, 초음파 각각의 특성 설명","explanation":"환자가 자신이 받는 검사를 정확히 이해해야 협조할 수 있습니다"},
       {"mistake":"조영제 관련 설명 누락","correction":"조영제 사용 여부, 알레르기 확인 필수","explanation":"조영제 부작용은 심각할 수 있으므로 사전 확인 중요합니다"},
       {"mistake":"검사 전 주의사항 미전달","correction":"금식, 금속 제거, 폐소공포증 확인 등 안내","explanation":"검사 준비가 제대로 안 되면 재검사가 필요할 수 있습니다"}],
      [{"korean":"CT 검사를 예약했습니다. 조영제를 사용하므로 검사 전 4시간 금식이 필요합니다.","vietnamese":"Đã đặt lịch chụp CT. Vì sử dụng thuốc cản quang nên cần nhịn ăn 4 tiếng trước khi chụp.","situation":"formal"},
       {"korean":"MRI 찍어야 해요. 몸에 금속 있으면 안 돼요. 심장박동기 있으세요?","vietnamese":"Cần chụp MRI. Không được có kim loại trong người. Anh/Chị có máy tạo nhịp tim không?","situation":"onsite"},
       {"korean":"엑스레이 찍을 거예요. 안 아파요. 숨 참으세요 하면 참으세요.","vietnamese":"Sẽ chụp X-quang. Không đau. Khi bảo nín thở thì nín thở nhé.","situation":"informal"}],
      ["CT", "MRI", "초음파", "X선", "조영제"])
]

# Load and update
with open('../data/terms/medical.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_slugs = {term['slug'] for term in data}
new_terms = [t for t in terms if t['slug'] not in existing_slugs]
data.extend(new_terms)

with open('../data/terms/medical.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Added {len(new_terms)} terms. Total: {len(data)}")
print("🎉 500개 마일스톤 달성!" if len(data) >= 500 else f"📊 {500 - len(data)}개 더 필요")
