#!/usr/bin/env python3
"""Gmail mbox 파싱 스크립트 - zip에서 직접 읽기"""

import zipfile
import mailbox
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
import json
import csv
import tempfile
import os
from datetime import datetime
import re

def decode_mime_header(header):
    """MIME 헤더 디코딩"""
    if header is None:
        return ""

    decoded_parts = []
    try:
        parts = decode_header(header)
        for content, charset in parts:
            if isinstance(content, bytes):
                charset = charset or 'utf-8'
                try:
                    decoded_parts.append(content.decode(charset, errors='replace'))
                except:
                    decoded_parts.append(content.decode('utf-8', errors='replace'))
            else:
                decoded_parts.append(content)
    except:
        return str(header)

    return ''.join(decoded_parts)

def get_email_body(msg):
    """이메일 본문 추출"""
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition", ""))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    charset = part.get_content_charset() or 'utf-8'
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode(charset, errors='replace')
                        break
                except:
                    pass
            elif content_type == "text/html" and "attachment" not in content_disposition and not body:
                try:
                    charset = part.get_content_charset() or 'utf-8'
                    payload = part.get_payload(decode=True)
                    if payload:
                        # HTML 태그 제거 (간단한 버전)
                        html_body = payload.decode(charset, errors='replace')
                        body = re.sub(r'<[^>]+>', '', html_body)
                        body = re.sub(r'\s+', ' ', body).strip()
                except:
                    pass
    else:
        try:
            charset = msg.get_content_charset() or 'utf-8'
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode(charset, errors='replace')
        except:
            body = str(msg.get_payload())

    # 본문 길이 제한 (너무 길면 자르기)
    if len(body) > 10000:
        body = body[:10000] + "... [truncated]"

    return body.strip()

def get_attachments(msg):
    """첨부파일 목록 추출"""
    attachments = []

    if msg.is_multipart():
        for part in msg.walk():
            content_disposition = str(part.get("Content-Disposition", ""))
            if "attachment" in content_disposition:
                filename = part.get_filename()
                if filename:
                    filename = decode_mime_header(filename)
                    attachments.append(filename)

    return attachments

def parse_mbox_from_zip(zip_path):
    """ZIP 파일에서 mbox 읽어서 파싱"""
    emails = []

    with zipfile.ZipFile(zip_path, 'r') as z:
        # mbox 파일 찾기
        mbox_files = [n for n in z.namelist() if n.endswith('.mbox')]

        if not mbox_files:
            print("mbox 파일을 찾을 수 없습니다.")
            return emails

        mbox_path = mbox_files[0]
        print(f"파싱 중: {mbox_path}")

        # 임시 파일로 추출
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mbox') as tmp:
            tmp_path = tmp.name
            print(f"임시 파일로 추출 중... (463MB, 잠시 기다려주세요)")
            tmp.write(z.read(mbox_path))

        try:
            # mbox 파싱
            mbox = mailbox.mbox(tmp_path)
            total = len(mbox)
            print(f"총 {total}개 메일 발견")

            for i, msg in enumerate(mbox):
                try:
                    # 날짜 파싱
                    date_str = msg.get('Date', '')
                    try:
                        date_obj = parsedate_to_datetime(date_str)
                        date_formatted = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        date_formatted = date_str

                    email_data = {
                        'id': i + 1,
                        'from': decode_mime_header(msg.get('From', '')),
                        'to': decode_mime_header(msg.get('To', '')),
                        'cc': decode_mime_header(msg.get('Cc', '')),
                        'subject': decode_mime_header(msg.get('Subject', '')),
                        'date': date_formatted,
                        'body': get_email_body(msg),
                        'attachments': get_attachments(msg),
                        'message_id': msg.get('Message-ID', ''),
                        'labels': msg.get('X-Gmail-Labels', '')
                    }

                    emails.append(email_data)

                    if (i + 1) % 50 == 0:
                        print(f"진행: {i + 1}/{total}")

                except Exception as e:
                    print(f"메일 {i+1} 파싱 오류: {e}")
                    continue

            mbox.close()

        finally:
            # 임시 파일 삭제
            os.unlink(tmp_path)

    return emails

def save_to_json(emails, output_path):
    """JSON으로 저장"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(emails, f, ensure_ascii=False, indent=2)
    print(f"JSON 저장 완료: {output_path}")

def save_to_csv(emails, output_path):
    """CSV로 저장"""
    if not emails:
        return

    # 첨부파일은 쉼표로 구분된 문자열로
    for email in emails:
        email['attachments'] = ', '.join(email['attachments'])

    fieldnames = ['id', 'date', 'from', 'to', 'cc', 'subject', 'body', 'attachments', 'labels', 'message_id']

    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(emails)

    print(f"CSV 저장 완료: {output_path}")

def main():
    zip_path = "takeout-20260126T135321Z-3-001.zip"

    print("=" * 50)
    print("Gmail Takeout 파싱 시작")
    print("=" * 50)

    emails = parse_mbox_from_zip(zip_path)

    print(f"\n총 {len(emails)}개 메일 파싱 완료")

    # 저장
    save_to_json(emails, "gmail_data.json")
    save_to_csv(emails, "gmail_data.csv")

    # 요약 출력
    print("\n" + "=" * 50)
    print("데이터 요약")
    print("=" * 50)

    if emails:
        # 발신자 통계
        from collections import Counter
        senders = Counter([e['from'].split('<')[0].strip() for e in emails])
        print("\n상위 발신자:")
        for sender, count in senders.most_common(10):
            print(f"  {sender}: {count}통")

        # 날짜 범위
        dates = [e['date'] for e in emails if e['date']]
        if dates:
            print(f"\n기간: {min(dates)} ~ {max(dates)}")

if __name__ == "__main__":
    main()
