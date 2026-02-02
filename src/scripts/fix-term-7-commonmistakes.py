#!/usr/bin/env python3
"""
Fix term at index 7 (tu-cach-cu-tru) - add third commonMistake
"""

import json
from pathlib import Path

def main():
    json_path = Path(__file__).parent.parent / 'data' / 'terms' / 'legal.json'

    print(f"📂 Loading {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    term = data[7]
    print(f"\n🎯 Fixing: [{7}] {term['slug']} ({term['korean']})")
    print(f"   Current commonMistakes: {len(term['commonMistakes'])}개")

    # Add third commonMistake
    new_mistake = {
        "mistake": "체류자격을 거류증으로 혼동",
        "correction": "체류자격은 법적 지위, 거류증은 증명 카드",
        "explanation": "체류자격(tư cách cư trú)은 외국인이 베트남에 합법적으로 머물 수 있는 법적 신분이고, 거류증(thẻ tạm trú/thường trú)은 이를 증명하는 물리적 카드입니다. 한국의 체류자격과 외국인등록증의 관계와 유사합니다."
    }

    term['commonMistakes'].append(new_mistake)

    print(f"   ✅ Added third commonMistake")
    print(f"   New count: {len(term['commonMistakes'])}개")

    # Save
    print(f"\n💾 Saving to {json_path}")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved\n")
    print("🎉 Term 7 now meets Tier S criteria!")

if __name__ == '__main__':
    main()
