from openpyxl import load_workbook
import re
import os
import shutil

SRC_FILE = 'data/tu_vung_hsk.xlsx'
DST_FILE = 'data/tu_vung_hsk_normalized.xlsx'
COLUMN = 'B'
START_ROW = 3

def normalize_text(text: str) -> str:
    """Chuẩn hóa: dấu phân cách -> |, tối đa 2 từ, định dạng 'A | B'"""
    if not text or not isinstance(text, str):
        return text

    text = text.strip()

    # 1. Dấu phân cách -> |
    cleaned = re.sub(r'[\(\)\[\]\{\};,/\-_、，；]+', '|', text)

    # 2. Khoảng trắng quanh | -> |
    cleaned = re.sub(r'\s*\|\s*', '|', cleaned)

    # 3. Gộp nhiều | thành 1
    cleaned = re.sub(r'\|+', '|', cleaned)

    # 4. Bỏ | đầu/cuối
    cleaned = cleaned.strip('|')

    # 5. Nếu không có | mà có khoảng trắng giữa chữ Hán -> coi là phân cách
    if '|' not in cleaned and re.search(r'[\u4e00-\u9fff]\s+[\u4e00-\u9fff]', cleaned):
        cleaned = re.sub(r'\s+', '|', cleaned)

    # 6. Tối đa 2 từ
    parts = [p.strip() for p in cleaned.split('|') if p.strip()]
    parts = parts[:2]

    # 7. Ghép chuẩn "A | B"
    return ' | '.join(parts)


def verify_only_column_b_changed(src, dst, column='B'):
    """So sánh 2 file: đảm bảo chỉ cột B thay đổi"""
    print('\n🔍 Kiểm tra an toàn...')
    wb_src = load_workbook(src)
    wb_dst = load_workbook(dst)

    # Kiểm tra số lượng sheet khớp
    if wb_src.sheetnames != wb_dst.sheetnames:
        print(f'❌ Danh sách sheet khác nhau!')
        return False

    diffs_outside_b = 0
    diffs_inside_b = 0

    for sheet in wb_src.sheetnames:
        ws1, ws2 = wb_src[sheet], wb_dst[sheet]
        for row in ws1.iter_rows():
            for c1 in row:
                c2 = ws2[c1.coordinate]
                if c1.value != c2.value:
                    if c1.column_letter == column:
                        diffs_inside_b += 1
                    else:
                        diffs_outside_b += 1
                        print(f'   ⚠️ Khác ngoài cột B: {sheet}!{c1.coordinate}: "{c1.value}" → "{c2.value}"')

    print(f'\n📊 Kết quả kiểm tra:')
    print(f'   - Số ô cột {column} đã sửa: {diffs_inside_b}')
    print(f'   - Số ô NGOÀI cột {column} bị thay đổi: {diffs_outside_b}')

    if diffs_outside_b == 0:
        print(f'   ✅ Xác nhận: chỉ cột {column} thay đổi, các cột khác nguyên vẹn.')
        return True
    else:
        print(f'   ❌ CẢNH BÁO: có {diffs_outside_b} ô ngoài cột {column} bị thay đổi!')
        return False


def main():
    if not os.path.isfile(SRC_FILE):
        print(f'❌ Không tìm thấy file: {SRC_FILE}')
        return

    # 🔁 Tạo bản sao từ file gốc
    shutil.copyfile(SRC_FILE, DST_FILE)
    print(f'📋 Đã tạo bản sao: {DST_FILE}')

    # Mở bản sao để sửa (file gốc không bị chạm)
    wb = load_workbook(DST_FILE)
    total_edit = 0

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        print(f'  📄 Sheet: {sheet_name}')

        for row in range(START_ROW, ws.max_row + 1):
            cell = ws[f'{COLUMN}{row}']
            old_value = cell.value
            if old_value is None:
                continue
            new_value = normalize_text(str(old_value))
            if new_value != str(old_value).strip():
                cell.value = new_value
                total_edit += 1
                print(f'     ✔ {COLUMN}{row}: "{old_value}" → "{new_value}"')

    wb.save(DST_FILE)
    print(f'\n✅ Đã lưu {DST_FILE}. Tổng số ô sửa: {total_edit}')

    # 🔍 Chạy kiểm tra an toàn
    ok = verify_only_column_b_changed(SRC_FILE, DST_FILE, COLUMN)

    if not ok:
        raise SystemExit('❌ Kiểm tra thất bại: có ô ngoài cột B bị thay đổi!')
    print('\n🎉 Hoàn tất thành công!')


if __name__ == '__main__':
    main()
