# -*- coding: utf-8 -*-
r"""
fix_all_conflicts.py
====================
Sửa TRIỆT ĐỂ bug "nút Chuyên ngành lúc bị lúc không" + dọn dẹp xung đột.

Vấn đề gốc:
  - fix.py              → clone nút Chuyên ngành + stopImmediatePropagation
  - patch_buttons.py    → clear active khi click Chuyên ngành
  - favorites_module.py → ~20 setInterval + duplicate override + grading API trùng
  - ui_template.py      → bind nhiều lần không WeakSet

Script này:
  1. Backup tất cả file liên quan
  2. Patch từng file theo đúng ngữ cảnh
  3. Inject script JS "cleanup" vào cuối index.html để dọn runtime
  4. Verify kết quả

Cách dùng:
    python fix_all_conflicts.py

File cần có trong cùng thư mục:
    - fix.py
    - patch_buttons.py
    - favorites_module.py
    - ui_template.py
    - index.html  (tùy chọn, chỉ để inject cleanup)
"""

import os
import re
import sys
import shutil
import subprocess
from datetime import datetime


# ═══════════════════════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════════════════════
FILES = {
    "fix":            "fix.py",
    "patch_buttons":  "patch_buttons.py",
    "favorites":      "favorites_module.py",
    "ui_template":    "ui_template.py",
    "index":          "index.html",
}

BACKUP_SUFFIX = ".bak_" + datetime.now().strftime("%Y%m%d_%H%M%S")

# ═══════════════════════════════════════════════════════════════════
#  UTILS
# ═══════════════════════════════════════════════════════════════════
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


def backup_file(path):
    if not os.path.isfile(path):
        return None
    bak = path + BACKUP_SUFFIX
    shutil.copy2(path, bak)
    log(f"Backup: {path} → {os.path.basename(bak)}", "💾")
    return bak


def syntax_check_py(path):
    """Kiểm tra cú pháp Python sau khi sửa."""
    try:
        result = subprocess.run(
            [sys.executable, "-c",
             f"import ast; ast.parse(open('{path}', encoding='utf-8').read())"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            log(f"Syntax OK: {path}", "✅")
            return True
        else:
            log(f"Syntax FAIL: {path}", "❌")
            if result.stderr:
                print(f"      {result.stderr.strip()}")
            return False
    except Exception as e:
        log(f"Syntax check error: {e}", "⚠️")
        return False


# ═══════════════════════════════════════════════════════════════════
#  PATCH 1 — fix.py : bỏ clone nút Chuyên ngành + bỏ stopImmediatePropagation
# ═══════════════════════════════════════════════════════════════════
def patch_fix_py(content):
    original = content
    changes = []

    # ── 1A: Skip nút chuyen-nganh trong bindTab ──
    # Tìm dòng `add("    function bindTab(dsId) {")`
    old = '''    add("    function bindTab(dsId) {")
    add("        var btn = document.querySelector('.ds-btn[data-dataset=\\"' + dsId + '\\"]');")'''

    new = '''    add("    function bindTab(dsId) {")
    add("        /* ⭐ FIX_CONFLICT: Bỏ qua nút chuyen-nganh — không clone */")
    add("        if (dsId === 'chuyen-nganh') return;")
    add("        var btn = document.querySelector('.ds-btn[data-dataset=\\"' + dsId + '\\"]');")
    add("        if (btn && btn.getAttribute('data-dataset-group') === 'chuyen-nganh') return;")'''

    if old in content:
        content = content.replace(old, new, 1)
        changes.append("bindTab: skip chuyen-nganh")
    else:
        # Thử pattern khác (có thể có khoảng trắng khác)
        pat = re.compile(
            r'(add\("    function bindTab\(dsId\) \{"\)\s*\n'
            r'\s*add\("        var btn = document\.querySelector)',
            re.MULTILINE
        )
        m = pat.search(content)
        if m:
            insert_at = m.start()
            skip_lines = (
                '    add("        if (dsId === \'chuyen-nganh\') return;")\n'
                '    add("        var btn = document.querySelector(\'.ds-btn[data-dataset=\\"\' + dsId + \'\\"]\');")\n'
                '    add("        if (btn && btn.getAttribute(\'data-dataset-group\') === \'chuyen-nganh\') return;")\n'
            )
            # Xoá dòng cũ `add("        var btn = ...`
            content = pat.sub(
                lambda mm: (
                    '    add("    function bindTab(dsId) {")\n'
                    '    add("        /* FIX_CONFLICT: skip chuyen-nganh */")\n'
                    '    add("        if (dsId === \'chuyen-nganh\') return;")\n'
                    '    add("        if (btn && btn.getAttribute(\'data-dataset-group\') === \'chuyen-nganh\') return;")\n'
                ),
                content, count=1
            )
            changes.append("bindTab: skip chuyen-nganh (pattern 2)")

    # ── 1B: Bỏ stopImmediatePropagation trong bindTab ──
    old_sip = '''    add("            e.stopImmediatePropagation();")
    add("            e.stopPropagation();")
    add("            e.preventDefault();")'''

    new_sip = '''    add("            /* FIX_CONFLICT: bỏ stopImmediatePropagation */")
    add("            e.stopPropagation();")'''

    if old_sip in content:
        content = content.replace(old_sip, new_sip, 1)
        changes.append("bindTab: bỏ stopImmediatePropagation + preventDefault")

    # ── 1C: Đổi capture phase true → false trong bindTab ──
    # Tìm `}, true);` gần bindTab
    old_cap = '''    add("        }, true);")
    add("    }")'''
    new_cap = '''    add("        }, false); /* FIX_CONFLICT: bỏ capture */")
    add("    }")'''
    if old_cap in content:
        content = content.replace(old_cap, new_cap, 1)
        changes.append("bindTab: capture true → false")

    # ── 1D: bindFixedTabs — bỏ stopImmediatePropagation ──
    old_fixed = '''    add("                e.stopImmediatePropagation();")
    add("                e.stopPropagation();")'''
    new_fixed = '''    add("                e.stopPropagation();")'''
    if old_fixed in content:
        content = content.replace(old_fixed, new_fixed, 1)
        changes.append("bindFixedTabs: bỏ stopImmediatePropagation")

    # ── 1E: MutationObserver — chỉ observe .ds-main-row ──
    old_obs = '''    add("    if (document.body) {")
    add("        observer.observe(document.body, { childList: true, subtree: true });")
    add("    }")'''
    new_obs = '''    add("    /* FIX_CONFLICT: chỉ observe .ds-main-row */")
    add("    var _dsRow = document.querySelector('.ds-main-row');")
    add("    if (_dsRow) {")
    add("        observer.observe(_dsRow, { childList: true });")
    add("    }")'''
    if old_obs in content:
        content = content.replace(old_obs, new_obs, 1)
        changes.append("MutationObserver: chỉ observe .ds-main-row")

    return content, changes


# ═══════════════════════════════════════════════════════════════════
#  PATCH 2 — patch_buttons.py : bỏ clear active khi click Chuyên ngành
# ═══════════════════════════════════════════════════════════════════
def patch_patch_buttons(content):
    changes = []

    # Tìm đoạn add_active_fix_js và thêm early return cho chuyen-nganh
    old = '''document.addEventListener('click', function(e) {
        var btn = e.target.closest('.ds-btn, .ds-sub-btn');
        if (!btn) return;

        // Nút Chuyên ngành (mở dropdown) → clear Yêu thích + Từ vựng
        // ⭐ KHÔNG return — để handler khác chạy bình thường
        if (btn.id === 'dsChuyenNganhBtn' ||
            btn.getAttribute('data-dataset-group') === 'chuyen-nganh') {

            var fav = document.querySelector('.ds-btn[data-dataset-group="favorites"]');
            if (fav) fav.classList.remove('active');
            var tv = document.querySelector('.ds-btn[data-dataset="tu-vung"]');
            if (tv) tv.classList.remove('active');
            // KHÔNG return ở đây — để handler khác tự do chạy
        }'''

    new = '''document.addEventListener('click', function(e) {
        var btn = e.target.closest('.ds-btn, .ds-sub-btn');
        if (!btn) return;

        // ⭐ FIX_CONFLICT: Nếu là nút Chuyên ngành → KHÔNG làm gì cả
        // Handler gốc của build_ui_js sẽ tự toggle active
        if (btn.id === 'dsChuyenNganhBtn' ||
            btn.getAttribute('data-dataset-group') === 'chuyen-nganh') {
            return;
        }'''

    if old in content:
        content = content.replace(old, new, 1)
        changes.append("add_active_fix_js: bỏ clear active cho nút Chuyên ngành")
    else:
        # Fallback: chỉ thêm return sớm ngay sau khi tìm thấy btn
        pat = re.compile(
            r"(var btn = e\.target\.closest\('\.ds-btn, \.ds-sub-btn'\);\s*\n"
            r"\s*if \(!btn\) return;\s*\n)",
            re.MULTILINE
        )
        insert = (
            "\n        // FIX_CONFLICT: bỏ qua nút Chuyên ngành\n"
            "        if (btn.id === 'dsChuyenNganhBtn' ||\n"
            "            btn.getAttribute('data-dataset-group') === 'chuyen-nganh') {\n"
            "            return;\n"
            "        }\n"
        )
        new_content, n = pat.subn(
            lambda m: m.group(1) + insert,
            content, count=1
        )
        if n > 0:
            content = new_content
            changes.append("add_active_fix_js: thêm early return cho CN (fallback)")

    return content, changes


# ═══════════════════════════════════════════════════════════════════
#  PATCH 3 — favorites_module.py : dọn dẹp
# ═══════════════════════════════════════════════════════════════════
def patch_favorites(content):
    changes = []

    # ── 3A: Xoá comment rác "K đềHI..." ──
    old_comment = '''/* ═══════════════════════════════════════════════════════════════════════════
   🔧 FIX: K đềHI ĐÓNG FULL MODE → TỰ)

 ĐỘNG RESET "CHỈ C2. User đÂU YÊU THÍCH"'''
    new_comment = '''/* ═══════════════════════════════════════════════════════════════════════════
   🔧 FIX: ĐÓNG FULL MODE → TỰ ĐỘNG RESET "CHỈ CÂU YÊU THÍCH"'''
    if old_comment in content:
        content = content.replace(old_comment, new_comment, 1)
        changes.append("Xoá comment rác")

    # ── 3B: Xoá grading API trùng ở cuối file (đã có trong build_html.py) ──
    # Đoạn bắt đầu từ comment "/* ⭐ GRADING API" đến hết file (trước """)
    grading_start_marker = "/* ═══════════════════════════════════════════════════════════ */\n/* ⭐ GRADING API — Chấm điểm qua Render"

    idx = content.find(grading_start_marker)
    if idx != -1:
        # Tìm điểm kết thúc chuỗi triple-quote tiếp theo (""")
        # File này là Python, JS nằm trong """, nên tìm """ sau idx
        end_quote = content.find('"""', idx)
        if end_quote != -1:
            # Xoá từ idx đến end_quote (giữ """)
            content = content[:idx] + content[end_quote:]
            changes.append("Xoá grading API trùng ở cuối file")

    # ── 3C: Xoá auto-clear active Yêu thích ở cuối file ──
    # Đã có patch_buttons.py xử lý → tránh trùng
    auto_clear_marker = "/* ⭐ FIX CUỐI — Auto-clear active Yêu thích */"
    idx2 = content.find(auto_clear_marker)
    if idx2 != -1:
        # Tìm hết IIFE: đếm dấu ngoặc { } từ idx2
        # Đơn giản hơn: tìm '})();' sau idx2
        end_iife = content.find('})();', idx2)
        if end_iife != -1:
            end_pos = end_iife + len('})();')
            # Thêm 1 dòng trống
            content = content[:idx2] + "/* (removed: auto-clear active trùng với patch_buttons.py) */\n" + content[end_pos:]
            changes.append("Xoá auto-clear active Yêu thích (trùng patch_buttons)")

    # ── 3D: Giảm tần suất các setInterval ──
    # 250ms → 1500ms cho syncPfState
    content = content.replace(
        "setInterval(syncPfState, 250);",
        "setInterval(syncPfState, 1500);  /* FIX_CONFLICT: giảm từ 250ms */"
    )
    content = content.replace(
        "setInterval(function() {\n        var t = (typeof window.APP_TIER !== 'undefined') ? window.APP_TIER : null;",
        "setInterval(function() {\n        /* FIX_CONFLICT: check tier mỗi 3s */\n        var t = (typeof window.APP_TIER !== 'undefined') ? window.APP_TIER : null;"
    )
    content = content.replace(
        "}, 800);\n})();",
        "}, 3000);\n})();"
    )
    changes.append("Giảm tần suất setInterval (250→1500ms, 800→3000ms)")

    # ── 3E: Trong favResetOnFullClose — không gán main page filter = '' ──
    old_reset_block = '''        /* ═══ 8. Clear filter trong main page (nếu có) ═══ */
        try {
            if (typeof state !== 'undefined' && state) {
                state.search = '';
                state.hsk = '';
                state.subject = '';
            }

            var si = document.getElementById('searchInput');
            var hf = document.getElementById('hskFilter');
            var sf = document.getElementById('subjectFilter');
            if (si) si.value = '';
            if (hf) hf.value = '';
            if (sf) sf.value = '';

            var cb = document.getElementById('clearSearchBtn');
            if (cb) cb.classList.remove('show');
        } catch(e) {}'''

    new_reset_block = '''        /* ═══ 8. FIX_CONFLICT: KHÔNG xoá filter main page ═══
           (chỉ xoá search nếu đang ở chế độ full mode)
           Lý do: user có thể đã đặt filter trước khi mở modal,
                  xoá đi sẽ làm mất trải nghiệm.
           Chỉ clear search của pfSearchInput. */
        try {
            var pfSi = document.getElementById('pfSearchInput');
            if (pfSi) pfSi.value = '';

            var pfCb = document.getElementById('pfClearSearchBtn');
            if (pfCb) pfCb.classList.remove('show');
        } catch(e) {}'''

    if old_reset_block in content:
        content = content.replace(old_reset_block, new_reset_block, 1)
        changes.append("favResetOnFullClose: không xoá filter main page")

    return content, changes


# ═══════════════════════════════════════════════════════════════════
#  PATCH 4 — ui_template.py : thêm WeakSet chống re-bind
# ═══════════════════════════════════════════════════════════════════
def patch_ui_template(content):
    changes = []

    # ── 4A: Thêm WeakSet + sửa __boundToggle thành __boundNodes ──
    old_bind = """    /* NÚT CHUYÊN NGÀNH — Click để mở/đóng dropdown */
    if (cnBtn && !cnBtn.__boundToggle) {
        cnBtn.__boundToggle = true;
        cnBtn.addEventListener('click', function() {
            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';
            if (isOpen) {
                sub.style.display = 'none';
                cnBtn.classList.remove('active');
            } else {
                sub.style.display = 'block';

                document.querySelectorAll('.ds-btn').forEach(function(b) {
                    b.classList.remove('active');
                });
                cnBtn.classList.add('active');
            }
        });
    }"""

    new_bind = """    /* NÚT CHUYÊN NGÀNH — Click để mở/đóng dropdown */
    /* FIX_CONFLICT: dùng WeakSet chống re-bind khi DOM bị thay thế */
    if (!window.__boundNodes) window.__boundNodes = new WeakSet();
    if (cnBtn && !window.__boundNodes.has(cnBtn)) {
        window.__boundNodes.add(cnBtn);
        cnBtn.addEventListener('click', function(e) {
            /* FIX_CONFLICT: chỉ stopPropagation, KHÔNG stopImmediatePropagation */
            e.stopPropagation();

            var sub = $('dsSubWrap');
            if (!sub) return;
            var isOpen = sub.style.display !== 'none';
            if (isOpen) {
                sub.style.display = 'none';
                cnBtn.classList.remove('active');
            } else {
                sub.style.display = 'block';

                document.querySelectorAll('.ds-btn:not([data-dataset-group="chuyen-nganh"])')
                    .forEach(function(b) {
                        b.classList.remove('active');
                    });
                cnBtn.classList.add('active');
            }
        });
    }"""

    if old_bind in content:
        content = content.replace(old_bind, new_bind, 1)
        changes.append("initDatasetSelector: WeakSet + fix stopPropagation + toggle active")

    # ── 4B: Cũng áp dụng WeakSet cho sub-btn ──
    old_sub = """    document.querySelectorAll('.ds-sub-btn').forEach(function(btn) {
        if (btn.__boundSub) return;
        btn.__boundSub = true;"""

    new_sub = """    document.querySelectorAll('.ds-sub-btn').forEach(function(btn) {
        if (!window.__boundNodes) window.__boundNodes = new WeakSet();
        if (window.__boundNodes.has(btn)) return;
        window.__boundNodes.add(btn);"""

    if old_sub in content:
        content = content.replace(old_sub, new_sub, 1)
        changes.append("sub-btn: WeakSet chống re-bind")

    # ── 4C: WeakSet cho tonghop btn ──
    old_tonghop = """    document.querySelectorAll('.ds-btn[data-dataset="tonghop"]').forEach(function(btn) {
        if (btn.__boundDataset) return;
        btn.__boundDataset = true;"""

    new_tonghop = """    document.querySelectorAll('.ds-btn[data-dataset="tonghop"]').forEach(function(btn) {
        if (!window.__boundNodes) window.__boundNodes = new WeakSet();
        if (window.__boundNodes.has(btn)) return;
        window.__boundNodes.add(btn);"""

    if old_tonghop in content:
        content = content.replace(old_tonghop, new_tonghop, 1)
        changes.append("tonghop btn: WeakSet chống re-bind")

    return content, changes


# ═══════════════════════════════════════════════════════════════════
#  INJECT — Cleanup script vào index.html
# ═══════════════════════════════════════════════════════════════════
CLEANUP_JS = r"""
<script>
/* ═══════════════════════════════════════════════════════════════════════
   FIX_ALL_CONFLICTS: Cleanup runtime
   - Đảm bảo nút Chuyên ngành LUÔN hoạt động
   - Chặn mọi event conflict từ module cũ
   - Watchdog: nếu DOM bị thay thế, tự re-bind
   ═══════════════════════════════════════════════════════════════════════ */
(function() {
    'use strict';

    console.log('[FIX_CONFLICT] Cleanup script loaded');

    /* ═══ 1. Watchdog: Đảm bảo nút Chuyên ngành luôn toggle được ═══ */
    function bindCNWatchdog() {
        var cnBtn = document.getElementById('dsChuyenNganhBtn')
                 || document.querySelector('.ds-btn[data-dataset-group="chuyen-nganh"]');
        if (!cnBtn) return;

        if (cnBtn.__cleanupBound) return;
        cnBtn.__cleanupBound = true;

        /* Capture-phase listener chạy TRƯỚC mọi stopImmediatePropagation khác */
        cnBtn.addEventListener('click', function(e) {
            /* Nếu bị stopImmediatePropagation ở phase khác → vẫn cố toggle */
            setTimeout(function() {
                var sub = document.getElementById('dsSubWrap');
                if (!sub) return;

                var isOpen = sub.style.display !== 'none';
                var hasActive = cnBtn.classList.contains('active');

                /* Logic: chỉ xử lý khi DOM chưa toggle đúng */
                if (!isOpen && !hasActive) {
                    /* Chưa mở → mở */
                    sub.style.display = 'block';
                    document.querySelectorAll('.ds-btn:not([data-dataset-group="chuyen-nganh"])')
                        .forEach(function(b) { b.classList.remove('active'); });
                    cnBtn.classList.add('active');
                } else if (!isOpen && hasActive) {
                    /* Lệch state → fix */
                    sub.style.display = 'block';
                }
            }, 0);
        }, true);

        console.log('[FIX_CONFLICT] Đã bind watchdog cho nút Chuyên ngành');
    }

    /* ═══ 2. Dọn DOM: xoá các nút clone dư ═══ */
    function cleanupDuplicates() {
        var cnBtns = document.querySelectorAll('.ds-btn[data-dataset-group="chuyen-nganh"]');
        if (cnBtns.length > 1) {
            console.warn('[FIX_CONFLICT] Có ' + cnBtns.length + ' nút Chuyên ngành — xoá bớt');
            for (var i = 1; i < cnBtns.length; i++) {
                cnBtns[i].remove();
            }
        }

        var tonghopBtns = document.querySelectorAll('.ds-btn[data-dataset="tonghop"]');
        if (tonghopBtns.length > 1) {
            console.warn('[FIX_CONFLICT] Có ' + tonghopBtns.length + ' nút Tổng hợp — xoá bớt');
            for (var j = 1; j < tonghopBtns.length; j++) {
                tonghopBtns[j].remove();
            }
        }
    }

    /* ═══ 3. Fix state mismatch định kỳ ═══ */
    function fixStateMismatch() {
        var cnBtn = document.querySelector('.ds-btn[data-dataset-group="chuyen-nganh"]');
        var sub = document.getElementById('dsSubWrap');
        if (!cnBtn || !sub) return;

        var isOpen = sub.style.display !== 'none';
        var hasActive = cnBtn.classList.contains('active');

        /* Nếu dropdown mở nhưng nút không active → fix */
        if (isOpen && !hasActive) {
            cnBtn.classList.add('active');
        }
        /* Nếu dropdown đóng nhưng nút active → chỉ fix nếu KHÔNG phải vừa click */
        if (!isOpen && hasActive && !cnBtn.__justClicked) {
            /* Không tự fix ở đây để tránh race */
        }
    }

    /* ═══ 4. Khởi động ═══ */
    function init() {
        bindCNWatchdog();
        cleanupDuplicates();

        /* Re-bind khi DOM có thay đổi */
        var obs = new MutationObserver(function(muts) {
            for (var i = 0; i < muts.length; i++) {
                var added = muts[i].addedNodes;
                for (var j = 0; j < added.length; j++) {
                    var n = added[j];
                    if (n.nodeType !== 1) continue;
                    if (n.matches && (
                        n.matches('.ds-btn[data-dataset-group="chuyen-nganh"]') ||
                        n.querySelector('.ds-btn[data-dataset-group="chuyen-nganh"]')
                    )) {
                        setTimeout(bindCNWatchdog, 50);
                    }
                }
            }
        });

        var dsRow = document.querySelector('.ds-main-row');
        if (dsRow) {
            obs.observe(dsRow, { childList: true, subtree: true });
        }

        /* Định kỳ fix mismatch (nhẹ, 2s/lần) */
        setInterval(fixStateMismatch, 2000);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    /* Re-init khi cần */
    setTimeout(init, 500);
    setTimeout(init, 1500);
})();
</script>
"""


def inject_cleanup_to_index(content):
    """Chèn cleanup script vào cuối index.html (trước </body>)."""
    marker = "/* FIX_ALL_CONFLICTS: Cleanup runtime */"
    if marker in content:
        return content, False

    pat = re.compile(r'(\s*)(</body>)', re.MULTILINE)
    new_content, n = pat.subn(
        lambda m: "\n" + CLEANUP_JS + "\n" + m.group(2),
        content, count=1
    )
    if n > 0:
        return new_content, True
    return content, False


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════
def main():
    section("FIX_ALL_CONFLICTS — Sửa xung đột nút Chuyên ngành")

    # ─── Kiểm tra file tồn tại ───
    missing = [p for p in FILES.values() if not os.path.isfile(p)]
    if missing:
        print("")
        log(f"Thiếu file: {', '.join(missing)}", "⚠️")
        log("Bỏ qua các file không có", "ℹ️")

    # ─── Backup tất cả file ───
    section("BƯỚC 1 — Backup tất cả file")
    backup_paths = {}
    for key, path in FILES.items():
        if os.path.isfile(path):
            bak = backup_file(path)
            backup_paths[key] = bak

    # ─── Patch từng file ───
    results = {}

    # ═══ PATCH fix.py ═══
    if os.path.isfile(FILES["fix"]):
        section(f"BƯỚC 2 — Patch {FILES['fix']}")
        content = read_file(FILES["fix"])
        new_content, changes = patch_fix_py(content)

        if new_content != content:
            write_file(FILES["fix"], new_content)
            for c in changes:
                log(c, "✅")
        else:
            log("Không có thay đổi (có thể đã patch rồi)", "ℹ️")

        results["fix"] = syntax_check_py(FILES["fix"])

    # ═══ PATCH patch_buttons.py ═══
    if os.path.isfile(FILES["patch_buttons"]):
        section(f"BƯỚC 3 — Patch {FILES['patch_buttons']}")
        content = read_file(FILES["patch_buttons"])
        new_content, changes = patch_patch_buttons(content)

        if new_content != content:
            write_file(FILES["patch_buttons"], new_content)
            for c in changes:
                log(c, "✅")
        else:
            log("Không có thay đổi", "ℹ️")

        results["patch_buttons"] = syntax_check_py(FILES["patch_buttons"])

    # ═══ PATCH favorites_module.py ═══
    if os.path.isfile(FILES["favorites"]):
        section(f"BƯỚC 4 — Patch {FILES['favorites']}")
        content = read_file(FILES["favorites"])
        new_content, changes = patch_favorites(content)

        if new_content != content:
            write_file(FILES["favorites"], new_content)
            for c in changes:
                log(c, "✅")
        else:
            log("Không có thay đổi", "ℹ️")

        results["favorites"] = syntax_check_py(FILES["favorites"])

    # ═══ PATCH ui_template.py ═══
    if os.path.isfile(FILES["ui_template"]):
        section(f"BƯỚC 5 — Patch {FILES['ui_template']}")
        content = read_file(FILES["ui_template"])
        new_content, changes = patch_ui_template(content)

        if new_content != content:
            write_file(FILES["ui_template"], new_content)
            for c in changes:
                log(c, "✅")
        else:
            log("Không có thay đổi (pattern có thể khác)", "ℹ️")

        results["ui_template"] = syntax_check_py(FILES["ui_template"])

    # ═══ INJECT cleanup vào index.html ═══
    if os.path.isfile(FILES["index"]):
        section(f"BƯỚC 6 — Inject cleanup vào {FILES['index']}")
        content = read_file(FILES["index"])
        new_content, injected = inject_cleanup_to_index(content)

        if injected:
            write_file(FILES["index"], new_content)
            log("Đã chèn cleanup script", "✅")
        else:
            log("Đã có cleanup script rồi, bỏ qua", "ℹ️")

        size_kb = os.path.getsize(FILES["index"]) / 1024
        log(f"Kích thước: {size_kb:.1f} KB", "📦")

    # ═══ TỔNG KẾT ═══
    section("TỔNG KẾT")
    all_ok = True
    for key, ok in results.items():
        status = "✅" if ok else "❌"
        log(f"{FILES[key]}: {status}", "")
        if not ok:
            all_ok = False

    print("")
    if all_ok:
        log("Tất cả file đã patch thành công!", "🎉")
        print("")
        print("  👉 Bước tiếp theo:")
        print("     1. Chạy lại build:")
        print("        python build_html.py")
        print("")
        print("     2. Hoặc chạy tuần tự:")
        print("        python fix.py")
        print("        python patch_buttons.py")
        print("")
        print("     3. Test trên trình duyệt:")
        print("        - Hard refresh (Ctrl+Shift+R)")
        print("        - Bấm nút Chuyên ngành → phải sổ dropdown")
        print("        - Bấm lại → phải đóng dropdown")
        print("        - Chuyển tab qua lại → active phải đúng")
    else:
        log("Một số file patch thất bại, kiểm tra log ở trên", "⚠️")

    print("")
    print("  💾 Backup tại: " + BACKUP_SUFFIX)
    print("  📁 Để khôi phục:")
    print(f"     copy {FILES['fix']}{BACKUP_SUFFIX} {FILES['fix']}")
    print(f"     copy {FILES['patch_buttons']}{BACKUP_SUFFIX} {FILES['patch_buttons']}")
    print(f"     copy {FILES['favorites']}{BACKUP_SUFFIX} {FILES['favorites']}")
    print(f"     copy {FILES['ui_template']}{BACKUP_SUFFIX} {FILES['ui_template']}")
    print("")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Bị hủy bởi user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n[❌] LỖI: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
