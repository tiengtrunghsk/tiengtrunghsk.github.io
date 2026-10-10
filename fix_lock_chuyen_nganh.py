# -*- coding: utf-8 -*-
r"""
fix_lock_chuyen_nganh.py
========================
Khoá nút Chuyên ngành cho đến khi data load xong.

Sửa 3 chỗ trong scripts/ui_template.py:
  1. CSS: thêm style .locked-loading + spinner
  2. JS: chặn click nút Chuyên ngành khi data chưa load
  3. JS: tự động thêm/xoá class locked-loading

Cách dùng:
    python fix_lock_chuyen_nganh.py
"""

import os
import re
import sys
import shutil
from datetime import datetime

TARGET = "scripts/ui_template.py"
BACKUP_SUFFIX = ".bak_lock_" + datetime.now().strftime("%Y%m%d_%H%M%S")


def log(msg, icon="•"):
    print(f"  {icon} {msg}")


def section(title):
    print("")
    print("=" * 66)
    print(f"  {title}")
    print("=" * 66)


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ═══════════════════════════════════════════════════════════════════
#  PATCH 1 — CSS: thêm style .locked-loading
# ═══════════════════════════════════════════════════════════════════
def patch_css(content):
    """Tìm cuối build_ui_css() và thêm CSS mới trước dấu đóng."""

    # CSS cần chèn
    new_css = r'''

/* ═══════════════════════════════════════════════════════════ */
/* ⭐ KHOÁ NÚT DATASET KHI DATA CHƯA LOAD XONG                  */
/* ═══════════════════════════════════════════════════════════ */
.ds-btn.locked-loading {
    opacity: 0.5;
    cursor: not-allowed !important;
    pointer-events: none !important;
    filter: grayscale(0.4);
    position: relative;
}

.ds-btn.locked-loading::before {
    content: '\f110';
    font-family: 'Font Awesome 6 Free', 'Font Awesome 5 Free';
    font-weight: 900;
    position: absolute;
    top: 50%;
    right: 12px;
    transform: translateY(-50%);
    font-size: 0.9rem;
    color: #94a3b8;
    animation: dsLockSpin 1s linear infinite;
}

@keyframes dsLockSpin {
    to { transform: translateY(-50%) rotate(360deg); }
}

/* Sub-wrap loading state */
.ds-sub-wrap.loading .ds-sub-btn {
    opacity: 0.4;
    pointer-events: none !important;
    filter: grayscale(0.5);
}

.ds-sub-wrap.loading .ds-sub-btn i:first-child {
    color: #94a3b8 !important;
}
'''

    # Tìm dấu kết thúc build_ui_css() — thường là chuỗi return r"""..."""
    # Cách đơn giản: tìm `def build_ui_html():` và chèn CSS ngay trước
    marker = "\ndef build_ui_html()"

    if marker not in content:
        log("Không tìm thấy marker build_ui_html()", "⚠️")
        return content, False

    # Tìm dấu `"""` đóng gần nhất trước marker
    idx = content.find(marker)
    if idx == -1:
        return content, False

    # Tìm dấu `"""` cuối cùng trước idx (đóng CSS)
    before = content[:idx]
    last_triple = before.rfind('"""')

    if last_triple == -1:
        log("Không tìm thấy dấu đóng CSS (\"\"\")", "⚠️")
        return content, False

    # Chèn CSS mới trước dấu """
    content = (
        content[:last_triple]
        + new_css
        + content[last_triple:]
    )
    return content, True


# ═══════════════════════════════════════════════════════════════════
#  PATCH 2 — JS: chặn click nút Chuyên ngành khi data chưa load
# ═══════════════════════════════════════════════════════════════════
def patch_click_lock(content):
    """Tìm handler click của cnBtn và chèn check __dataLoaded."""

    # Pattern 1: Có WeakSet
    old_weakset = """    if (cnBtn && !window.__boundNodes.has(cnBtn)) {
        window.__boundNodes.add(cnBtn);
        cnBtn.addEventListener('click', function(e) {
            /* FIX_CONFLICT: chỉ stopPropagation, KHÔNG stopImmediatePropagation */
            e.stopPropagation();

            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';"""

    new_weakset = """    if (cnBtn && !window.__boundNodes.has(cnBtn)) {
        window.__boundNodes.add(cnBtn);
        cnBtn.addEventListener('click', function(e) {
            /* FIX_CONFLICT: chỉ stopPropagation, KHÔNG stopImmediatePropagation */
            e.stopPropagation();

            /* ⭐ LOCK: Chặn click nếu data chưa load xong */
            if (!window.__dataLoaded) {
                if (typeof showTagToast === 'function') {
                    showTagToast('Đang tải dữ liệu, vui lòng đợi...');
                }
                return;
            }

            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';"""

    # Pattern 2: Không có WeakSet (bản gốc)
    old_orig = """    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';"""

    new_orig = """    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            /* ⭐ LOCK: Chặn click nếu data chưa load xong */
            if (!window.__dataLoaded) {
                if (typeof showTagToast === 'function') {
                    showTagToast('Đang tải dữ liệu, vui lòng đợi...');
                }
                return;
            }

            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';"""

    if old_weakset in content:
        content = content.replace(old_weakset, new_weakset, 1)
        return content, True, "WeakSet"
    elif old_orig in content:
        content = content.replace(old_orig, new_orig, 1)
        return content, True, "Original"
    else:
        log("Không tìm thấy handler click của cnBtn", "⚠️")
        return content, False, None


# ═══════════════════════════════════════════════════════════════════
#  PATCH 3 — JS: auto lock/unlock dựa trên __dataLoaded
# ═══════════════════════════════════════════════════════════════════
def patch_auto_lock(content):
    """Chèn logic auto lock/unlock vào cuối initDatasetSelector()."""

    # Tìm `markCurrentDatasetActive();` ở cuối initDatasetSelector
    # (có thể có 2 chỗ gọi — nhưng chỗ cuối là trong initDatasetSelector)

    marker = "    markCurrentDatasetActive();\n}"

    if marker not in content:
        # Thử pattern khác: có khoảng trắng
        pattern = re.compile(
            r"(    markCurrentDatasetActive\(\);\s*\n\})",
            re.MULTILINE
        )
        m = pattern.search(content)
        if not m:
            log("Không tìm thấy markCurrentDatasetActive() cuối initDatasetSelector", "⚠️")
            return content, False

        auto_lock_code = """    markCurrentDatasetActive();

    /* ⭐ LOCK: Tự động khoá nút dataset khi data chưa load */
    (function initDataLocking() {
        var allDatasetBtns = document.querySelectorAll('.ds-btn[data-dataset], .ds-btn[data-dataset-group]');
        var subWrap = $('dsSubWrap');

        if (window.__dataLoaded) {
            allDatasetBtns.forEach(function(b) { b.classList.remove('locked-loading'); });
            if (subWrap) subWrap.classList.remove('loading');
            return;
        }

        allDatasetBtns.forEach(function(b) {
            b.classList.add('locked-loading');
        });
        if (subWrap) subWrap.classList.add('loading');

        var unlock = function() {
            allDatasetBtns.forEach(function(b) {
                b.classList.remove('locked-loading');
            });
            if (subWrap) subWrap.classList.remove('loading');
            console.log('[DataLock] Đã mở khoá nút dataset');
        };

        if (window.__dataLoadPromise) {
            window.__dataLoadPromise.then(unlock).catch(function() {
                unlock();
            });
        } else {
            window.addEventListener('dataLoaded', unlock, { once: true });
        }
    })();
}"""

        content = content[:m.start()] + auto_lock_code + content[m.end():]
        return content, True

    auto_lock_code = marker.replace("}",
        """
    /* ⭐ LOCK: Tự động khoá nút dataset khi data chưa load */
    (function initDataLocking() {
        var allDatasetBtns = document.querySelectorAll('.ds-btn[data-dataset], .ds-btn[data-dataset-group]');
        var subWrap = $('dsSubWrap');

        if (window.__dataLoaded) {
            allDatasetBtns.forEach(function(b) { b.classList.remove('locked-loading'); });
            if (subWrap) subWrap.classList.remove('loading');
            return;
        }

        allDatasetBtns.forEach(function(b) {
            b.classList.add('locked-loading');
        });
        if (subWrap) subWrap.classList.add('loading');

        var unlock = function() {
            allDatasetBtns.forEach(function(b) {
                b.classList.remove('locked-loading');
            });
            if (subWrap) subWrap.classList.remove('loading');
            console.log('[DataLock] Đã mở khoá nút dataset');
        };

        if (window.__dataLoadPromise) {
            window.__dataLoadPromise.then(unlock).catch(function() {
                unlock();
            });
        } else {
            window.addEventListener('dataLoaded', unlock, { once: true });
        }
    })();
}""")

    content = content.replace(marker, auto_lock_code, 1)
    return content, True


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════
def main():
    section("LOCK NÚT CHUYÊN NGÀNH KHI DATA CHƯA LOAD")

    if not os.path.isfile(TARGET):
        log(f"Không tìm thấy {TARGET}", "❌")
        sys.exit(1)

    # Backup
    bak = TARGET + BACKUP_SUFFIX
    shutil.copy2(TARGET, bak)
    log(f"Backup: {TARGET} → {os.path.basename(bak)}", "💾")

    content = read_file(TARGET)
    original = content
    total = 0

    # ── PATCH 1: CSS ──
    section("BƯỚC 1 — CSS: style .locked-loading")
    content, ok1 = patch_css(content)
    if ok1:
        log("Đã chèn CSS khoá nút", "✅")
        total += 1
    else:
        log("Bỏ qua (có thể đã có)", "ℹ️")

    # ── PATCH 2: Chặn click ──
    section("BƯỚC 2 — JS: chặn click khi data chưa load")
    content, ok2, variant = patch_click_lock(content)
    if ok2:
        log(f"Đã chèn check __dataLoaded (variant: {variant})", "✅")
        total += 1
    else:
        log("Bỏ qua (có thể đã có)", "ℹ️")

    # ── PATCH 3: Auto lock/unlock ──
    section("BƯỚC 3 — JS: auto lock/unlock theo __dataLoaded")
    content, ok3 = patch_auto_lock(content)
    if ok3:
        log("Đã chèn logic auto lock/unlock", "✅")
        total += 1
    else:
        log("Bỏ qua (có thể đã có)", "ℹ️")

    # ── Verify syntax ──
    section("BƯỚC 4 — Verify syntax Python")
    try:
        import ast
        ast.parse(content)
        log("Syntax OK", "✅")
    except SyntaxError as e:
        log(f"Syntax ERROR: {e}", "❌")
        log("Rollback...", "↩️")
        shutil.copy2(bak, TARGET)
        sys.exit(1)

    # ── Save ──
    if content != original:
        write_file(TARGET, content)
        section("HOÀN TẤT")
        log(f"Đã patch {total} chỗ trong {TARGET}", "🎉")
        print("")
        print("  👉 Bước tiếp theo:")
        print("     1. python fix.py")
        print("     2. python patch_buttons.py")
        print("     3. Test trên browser (Ctrl+Shift+R)")
        print("")
        print("  🧪 Test race condition:")
        print("     1. Mở DevTools → Network → Slow 3G")
        print("     2. Hard refresh")
        print("     3. Bấm nút Chuyên ngành NGAY khi page load")
        print("     4. Phải thấy: nút mờ + spinner + toast 'Đang tải...'")
        print("     5. Sau ~3s: nút sáng, bấm được bình thường")
    else:
        log("Không có thay đổi (có thể đã patch rồi)", "ℹ️")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Hủy")
        sys.exit(1)
    except Exception as e:
        print(f"\n[❌] {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
