#!/usr/bin/env python3
"""
Fix Medical domain placeholder Vietnamese terms and slugs.
92 terms have placeholder vietnamese like [신경외과 베트남어] and Korean slugs.
This script replaces them with correct Vietnamese medical terminology.
"""

import json
import re
import unicodedata
from pathlib import Path


# Korean → Vietnamese medical term mapping (verified medical terminology)
MEDICAL_VN_MAP = {
    '신경외과': 'Khoa phẫu thuật thần kinh',
    '흉부외과': 'Khoa phẫu thuật lồng ngực',
    '성형외과': 'Khoa phẫu thuật tạo hình',
    '비뇨기과': 'Khoa tiết niệu',
    '정신건강의학과': 'Khoa tâm thần',
    '재활의학과': 'Khoa phục hồi chức năng',
    '가정의학과': 'Khoa y học gia đình',
    '응급의학과': 'Khoa cấp cứu',
    '마취통증의학과': 'Khoa gây mê hồi sức',
    '영상의학과': 'Khoa chẩn đoán hình ảnh',
    '진단검사의학과': 'Khoa xét nghiệm',
    '병리과': 'Khoa giải phẫu bệnh',
    '순환기내과': 'Khoa nội tim mạch',
    '소화기내과': 'Khoa nội tiêu hóa',
    '호흡기내과': 'Khoa nội hô hấp',
    '내분비내과': 'Khoa nội tiết',
    '신장내과': 'Khoa nội thận',
    '혈액종양내과': 'Khoa huyết học ung thư',
    '류마티스내과': 'Khoa nội thấp khớp',
    '감염내과': 'Khoa nhiễm',
    '알레르기내과': 'Khoa dị ứng',
    '신경과': 'Khoa thần kinh',
    '척추센터': 'Trung tâm cột sống',
    '관절센터': 'Trung tâm khớp',
    '암센터': 'Trung tâm ung bướu',
    '심장센터': 'Trung tâm tim mạch',
    '뇌졸중센터': 'Trung tâm đột quỵ',
    '외상센터': 'Trung tâm chấn thương',
    '통증클리닉': 'Phòng khám đau',
    '비만클리닉': 'Phòng khám béo phì',
    '당뇨클리닉': 'Phòng khám tiểu đường',
    '갑상선클리닉': 'Phòng khám tuyến giáp',
    '피부미용': 'Da liễu thẩm mỹ',
    '레이저클리닉': 'Phòng khám laser',
    '탈모클리닉': 'Phòng khám rụng tóc',
    '알레르기클리닉': 'Phòng khám dị ứng',
    '수면클리닉': 'Phòng khám giấc ngủ',
    '건강검진센터': 'Trung tâm kiểm tra sức khỏe',
    '예방접종센터': 'Trung tâm tiêm chủng',
    '모유수유클리닉': 'Phòng khám nuôi con bằng sữa mẹ',
    '산전관리': 'Chăm sóc trước sinh',
    '산후조리': 'Chăm sóc sau sinh',
    '소아심장': 'Tim mạch nhi',
    '소아신경': 'Thần kinh nhi',
    '소아알레르기': 'Dị ứng nhi',
    '소아내분비': 'Nội tiết nhi',
    '발달클리닉': 'Phòng khám phát triển',
    '청소년클리닉': 'Phòng khám vị thành niên',
    '노인의학': 'Lão khoa',
    '완화의료': 'Chăm sóc giảm nhẹ',
    '호스피스': 'Hospice',
    '재택의료': 'Y tế tại nhà',
    '직업환경의학': 'Y học lao động',
    '항공의학': 'Y học hàng không',
    '스포츠의학': 'Y học thể thao',
    '미용의학': 'Y học thẩm mỹ',
    '비만대사외과': 'Khoa phẫu thuật béo phì',
    '이식외과': 'Khoa phẫu thuật ghép tạng',
    '혈관외과': 'Khoa phẫu thuật mạch máu',
    '유방외과': 'Khoa phẫu thuật vú',
    '갑상선외과': 'Khoa phẫu thuật tuyến giáp',
    '대장항문외과': 'Khoa phẫu thuật đại trực tràng',
    '두경부외과': 'Khoa phẫu thuật đầu cổ',
    '구강외과': 'Khoa phẫu thuật miệng',
    '안면윤곽': 'Tạo hình khuôn mặt',
    '눈성형': 'Phẫu thuật mắt thẩm mỹ',
    '코성형': 'Phẫu thuật mũi thẩm mỹ',
    '가슴성형': 'Phẫu thuật ngực thẩm mỹ',
    '지방흡입': 'Hút mỡ',
    '리프팅': 'Căng da mặt',
    '보톡스': 'Botox',
    '필러': 'Filler',
    '백내장': 'Đục thủy tinh thể',
    '녹내장': 'Tăng nhãn áp',
    '망막': 'Võng mạc',
    '각막': 'Giác mạc',
    '사시': 'Lác mắt',
    '굴절이상': 'Tật khúc xạ',
    '라식': 'LASIK',
    '라섹': 'LASEK',
    '렌즈삽입술': 'Phẫu thuật đặt kính nội nhãn',
    '노안교정': 'Chỉnh viễn thị lão',
    '청력검사': 'Kiểm tra thính lực',
    '이명': 'Ù tai',
    '어지럼증': 'Chóng mặt',
    '수면무호흡': 'Ngưng thở khi ngủ',
    '코골이': 'Ngáy',
    '비염': 'Viêm mũi',
    '축농증': 'Viêm xoang',
    '편도선': 'Amidan',
    '성대': 'Dây thanh',
    '음성장애': 'Rối loạn giọng nói',
}


def slugify(text: str) -> str:
    """Convert Vietnamese text to URL-safe slug."""
    vn_map = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'đ': 'd',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
    }
    result = text.lower().strip()
    mapped = []
    for ch in result:
        mapped.append(vn_map.get(ch, ch))
    result = ''.join(mapped)
    result = unicodedata.normalize('NFKD', result)
    result = result.encode('ascii', 'ignore').decode('ascii')
    result = re.sub(r'[^a-z0-9]+', '-', result)
    result = result.strip('-')
    result = re.sub(r'-+', '-', result)
    return result


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    medical_path = project_root / 'src' / 'data' / 'terms' / 'medical.json'

    with open(medical_path, 'r', encoding='utf-8') as f:
        terms = json.load(f)

    fixed = 0
    slug_dupes = {}  # Track slug uniqueness

    for term in terms:
        korean = term.get('korean', '')
        vietnamese = term.get('vietnamese', '')
        slug = term.get('slug', '')

        # Check if this term needs fixing (placeholder vietnamese or bad slug)
        is_placeholder = vietnamese.startswith('[') and vietnamese.endswith('베트남어]')
        is_bad_slug = not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug)

        if korean in MEDICAL_VN_MAP and (is_placeholder or is_bad_slug):
            new_vn = MEDICAL_VN_MAP[korean]
            new_slug = slugify(new_vn)

            # Handle duplicate slugs
            if new_slug in slug_dupes:
                slug_dupes[new_slug] += 1
                new_slug = f"{new_slug}-{slug_dupes[new_slug]}"
            else:
                slug_dupes[new_slug] = 1

            if is_placeholder:
                term['vietnamese'] = new_vn

            term['slug'] = new_slug
            fixed += 1
            print(f"  ✅ {korean}: slug={new_slug}, vn={new_vn}")

    print(f"\nFixed {fixed} terms")

    # Verify all slugs are now valid
    remaining_bad = 0
    for term in terms:
        slug = term.get('slug', '')
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug):
            remaining_bad += 1
            print(f"  ❌ Still bad: {term.get('korean','')} → {slug}")

    print(f"Remaining bad slugs: {remaining_bad}")

    # Check for slug duplicates across entire file
    all_slugs = [t['slug'] for t in terms]
    from collections import Counter
    dupes = {s: c for s, c in Counter(all_slugs).items() if c > 1}
    if dupes:
        print(f"\n⚠️ Duplicate slugs found: {len(dupes)}")
        for s, c in list(dupes.items())[:5]:
            print(f"  {s}: {c} occurrences")

    # Save
    with open(medical_path, 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)

    print(f"\nSaved to {medical_path}")


if __name__ == '__main__':
    main()
