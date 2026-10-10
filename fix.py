# -*- coding: utf-8 -*-
r"""
fix.py - Auto-scan data/ và thêm MỌI file Excel thành tab riêng.
+ TỰ ĐỘNG thêm tab TỪ VỰNG PREMIUM từ data/tu_vung_hsk.xlsx

Chạy:
    python scripts/convert.py
    python fix.py
"""
import json
import os
import re
import sys
import glob
import unicodedata

import openpyxl


# =================================================================
#  CONFIG
# =================================================================
INDEX_HTML = "index.html"
CONFIG_JSON = "config.json"
DATA_DIR = "data"

SKIP_FILES = {"input.xlsx", "input.xls", "input.csv"}

VOCAB_FILE = os.path.join(DATA_DIR, "tu_vung_hsk.xlsx")
VOCAB_ID = "tu-vung"
VOCAB_LABEL = "11000+ Từ vựng HSK"

TAB_ICONS = [
    "fa-comments", "fa-file-alt", "fa-book", "fa-graduation-cap",
    "fa-star", "fa-fire", "fa-bolt", "fa-rocket",
]
TAB_COLORS = [
    "#0891b2", "#dc2626", "#059669", "#d97706",
    "#7c3aed", "#db2777", "#0284c7", "#65a30d",
]


# ═══════════════════════════════════════════════════════════════════
#  VOCAB WARNING CSS
# ═══════════════════════════════════════════════════════════════════
VOCAB_WARNING_CSS = r"""
.vocab-warning-banner {
    display: flex; align-items: center; gap: .85rem;
    padding: .85rem 1rem; margin-bottom: 1rem;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(251, 191, 36, .15), rgba(245, 158, 11, .08));
    border: 1.5px solid rgba(245, 158, 11, .45);
    animation: vocabWarnIn .4s cubic-bezier(.34, 1.56, .64, 1);
}
@keyframes vocabWarnIn {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0); }
}
.vocab-warning-banner.tier-trial {
    background: linear-gradient(135deg, rgba(99, 102, 241, .12), rgba(139, 92, 246, .08));
    border-color: rgba(99, 102, 241, .45);
}
.vocab-warning-banner.tier-expired {
    background: linear-gradient(135deg, rgba(220, 38, 38, .12), rgba(251, 146, 60, .08));
    border-color: rgba(220, 38, 38, .5);
}
.vocab-warning-banner.tier-active {
    background: linear-gradient(135deg, rgba(8, 145, 178, .12), rgba(6, 182, 212, .08));
    border-color: rgba(8, 145, 178, .45);
}
.vocab-warning-icon {
    width: 40px; height: 40px; border-radius: 50%;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #fff; display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(245, 158, 11, .4);
}
.vocab-warning-banner.tier-trial .vocab-warning-icon {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    box-shadow: 0 4px 12px rgba(99, 102, 241, .4);
}
.vocab-warning-banner.tier-expired .vocab-warning-icon {
    background: linear-gradient(135deg, #dc2626, #b91c1c);
    box-shadow: 0 4px 12px rgba(220, 38, 38, .4);
}
.vocab-warning-banner.tier-active .vocab-warning-icon {
    background: linear-gradient(135deg, #0891b2, #06b6d4);
    box-shadow: 0 4px 12px rgba(8, 145, 178, .4);
}
.vocab-warning-text { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: .15rem; }
.vocab-warning-text strong { font-size: .92rem; font-weight: 800; color: #92400e; }
.vocab-warning-banner.tier-trial .vocab-warning-text strong { color: #4f46e5; }
.vocab-warning-banner.tier-expired .vocab-warning-text strong { color: #991b1b; }
.vocab-warning-banner.tier-active .vocab-warning-text strong { color: #075985; }
.vocab-warning-text span { font-size: .8rem; color: var(--text-2); line-height: 1.4; }
.vocab-warning-btn {
    padding: .55rem .9rem; border-radius: 10px; border: none;
    background: linear-gradient(135deg, #fbbf24, #f59e0b 50%, #ea580c);
    color: #fff; font-weight: 800; font-size: .8rem;
    font-family: inherit; cursor: pointer;
    display: inline-flex; align-items: center; gap: .35rem;
    box-shadow: 0 4px 12px rgba(245, 158, 11, .4);
    transition: all .2s; white-space: nowrap; flex-shrink: 0;
}
.vocab-warning-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(245, 158, 11, .6);
}
[data-theme="dark"] .vocab-warning-banner {
    background: linear-gradient(135deg, rgba(251, 191, 36, .2), rgba(245, 158, 11, .1));
}
[data-theme="dark"] .vocab-warning-text strong { color: #fcd34d; }
[data-theme="dark"] .vocab-warning-banner.tier-trial .vocab-warning-text strong { color: #c4b5fd; }
[data-theme="dark"] .vocab-warning-banner.tier-expired .vocab-warning-text strong { color: #fca5a5; }
[data-theme="dark"] .vocab-warning-banner.tier-active .vocab-warning-text strong { color: #67e8f9; }
@media (max-width: 600px) {
    .vocab-warning-banner { flex-wrap: wrap; gap: .6rem; padding: .7rem .8rem; }
    .vocab-warning-icon { width: 34px; height: 34px; font-size: .95rem; }
    .vocab-warning-text strong { font-size: .85rem; }
    .vocab-warning-text span { font-size: .74rem; }
}
"""


def build_vocab_js_patch():
    return r"""
(function() {
    'use strict';
    var VOCAB_ID = 'tu-vung';

    function getVocabAccess() {
        var cfg = (typeof ONBOARDING_CONFIG !== 'undefined' && ONBOARDING_CONFIG) || {};
        var appTier = (typeof window.APP_TIER !== 'undefined') ? window.APP_TIER : null;

        var u = null;
        try {
            if (typeof window.currentUser !== 'undefined' && window.currentUser) u = window.currentUser;
            else if (typeof currentUser !== 'undefined' && currentUser) u = currentUser;
        } catch(e) {}

        if (u && u.role === 'admin') {
            return { allowed: true, tier: 'admin',
                hskAllowed: [1,2,3,4,5,6,7,8,9], maxQuestions: -1,
                label: 'Admin - Toàn bộ HSK', warning: null };
        }
        if (u && u.isPermanent === true) {
            return { allowed: true, tier: 'premium',
                hskAllowed: [1,2,3,4,5,6,7,8,9], maxQuestions: -1,
                label: 'Premium - Toàn bộ HSK', warning: null };
        }

        var tier = 'demo';
        if (appTier === 'active') tier = 'active';
        else if (appTier === 'trial') tier = 'trial';
        else if (appTier === 'expired') tier = 'expired';
        else if (appTier === 'demo') tier = 'demo';
        else if (u) {
            if (u.isTrial === true || u.tier === 'trial') tier = 'trial';
            else if (u.isExpiredOnly === true || u.tier === 'expired') tier = 'expired';
            else tier = 'active';
        }

        var tierCfg = cfg[tier] || {};
        var hskArr = tierCfg.hsk_allowed || [];
        var maxQ = (typeof tierCfg.max_questions === 'number') ? tierCfg.max_questions : -1;
        var maxT = (typeof tierCfg.topics_per_user === 'number') ? tierCfg.topics_per_user : -1;
        var isUnlimited = (maxQ === -1 && maxT === -1);

        var hskRange = hskArr.length
            ? 'HSK ' + hskArr[0] + '-' + hskArr[hskArr.length - 1]
            : 'cơ bản';

        if (tier === 'expired') {
            return { allowed: false, tier: 'expired', hskAllowed: [], maxQuestions: 0,
                label: 'Tài khoản hết hạn',
                warning: 'Tài khoản đã hết hạn — gia hạn để tiếp tục dùng Từ vựng HSK.' };
        }
        if (tier === 'demo') {
            return { allowed: true, tier: 'demo', hskAllowed: hskArr, maxQuestions: maxQ,
                label: 'Demo - ' + hskRange,
                warning: 'Bạn Demo giới hạn ' + hskRange + ' và tối đa ' +
                         (maxQ > 0 ? maxQ + ' từ' : 'một số từ') +
                         ' — đăng nhập để dùng đầy đủ.' };
        }
        if (tier === 'trial') {
            if (isUnlimited) {
                return { allowed: true, tier: 'trial',
                    hskAllowed: hskArr.length ? hskArr : [1,2,3,4,5,6,7,8,9],
                    maxQuestions: -1,
                    label: 'Trial - ' + hskRange, warning: null };
            }
            return { allowed: true, tier: 'trial', hskAllowed: hskArr, maxQuestions: maxQ,
                label: 'Trial - ' + hskRange,
                warning: 'Bạn Trial giới hạn ' + hskRange + ' và ' +
                         (maxQ > 0 ? maxQ + ' từ' : 'một số từ') +
                         ' — nâng cấp Premium để mở toàn bộ.' };
        }
        if (isUnlimited) {
            return { allowed: true, tier: 'active',
                hskAllowed: hskArr.length ? hskArr : [1,2,3,4,5,6,7,8,9],
                maxQuestions: -1,
                label: 'Active - ' + hskRange, warning: null };
        }
        return { allowed: true, tier: 'active', hskAllowed: hskArr, maxQuestions: maxQ,
            label: 'Active - ' + hskRange,
            warning: 'Bạn Active giới hạn ' + hskRange + ' và ' +
                     (maxQ > 0 ? maxQ + ' từ' : 'một số từ') +
                     ' — nâng cấp Premium để mở toàn bộ.' };
    }

    function applyVocabLimits(list, access) {
        var result = list;
        if (access.hskAllowed && access.hskAllowed.length &&
            access.hskAllowed.length < 9) {
            var allowSet = {};
            access.hskAllowed.forEach(function(h) {
                allowSet['HSK' + h] = true;
                allowSet[String(h)] = true;
            });
            result = result.filter(function(r) {
                var h = (r.hsk || '').toString().toUpperCase().trim();
                if (!h) return true;
                if (h === 'HSK7-9') {
                    return allowSet['HSK7-9'] === true;
                }
                var num = h.replace(/[^0-9]/g, '');
                if (!num) return true;
                return allowSet['HSK' + num] === true || allowSet[num] === true;
            });
        }
        var maxQ = access.maxQuestions;
        if (typeof maxQ === 'number' && maxQ > 0 && result.length > maxQ) {
            result = result.slice(0, maxQ);
        }
        return result;
    }

    function _esc(s) {
        return (typeof escapeHtml === 'function')
            ? escapeHtml(s) : String(s == null ? '' : s);
    }

    function _isVocabMode() {
        return (typeof CURRENT_DATASET !== 'undefined') && CURRENT_DATASET === VOCAB_ID;
    }

    function updateTabLockState() {
        var btn = document.querySelector('.ds-btn[data-dataset="' + VOCAB_ID + '"]');
        if (!btn) return;
        var acc = getVocabAccess();
        var oldLock = btn.querySelector('.vocab-lock-icon');
        if (oldLock) oldLock.remove();
        var badge = btn.querySelector('.ds-vocab-badge');

        if (acc.allowed) {
            btn.classList.remove('vocab-locked');
            btn.classList.add('vocab-unlocked');
            btn.title = acc.label;
            if (badge) {
                badge.textContent = (acc.tier === 'admin' || acc.tier === 'premium')
                    ? 'PREMIUM' : (acc.tier === 'active' ? 'ACTIVE'
                    : (acc.tier === 'trial' ? 'TRIAL' : 'DEMO'));
            }
        } else {
            btn.classList.add('vocab-locked');
            btn.classList.remove('vocab-unlocked');
            btn.title = acc.label;
            var lock = document.createElement('i');
            lock.className = 'fas fa-lock vocab-lock-icon';
            btn.appendChild(lock);
        }
    }

    /* ⭐ BANNER GỘP — hiện ở mọi tab, gộp thông tin lượt Nghe + Viết */
    function injectVocabWarningBanner() {
        var acc = getVocabAccess();
        if (!acc.warning) {
            var oldOut = document.getElementById('vocabWarningBanner');
            if (oldOut) oldOut.remove();
            return;
        }
        var old = document.getElementById('vocabWarningBanner');
        if (old) old.remove();

        var main = document.getElementById('mainContent');
        if (!main) return;

        /* ⭐ Tính thông tin hiển thị tuỳ tab */
        var limitedCount = 0, totalCount = 0;
        var unit = _isVocabMode() ? 'từ' : 'câu';

        try {
            if (_isVocabMode() && window.FIXPY_DATASETS && window.FIXPY_DATASETS[VOCAB_ID]) {
                var full = window.FIXPY_DATASETS[VOCAB_ID].data || [];
                totalCount = full.length;
                limitedCount = applyVocabLimits(full, acc).length;
            } else {
                var info = (typeof getTierInfo === 'function') ? getTierInfo() : {};
                var maxQ = info.maxQuestions || 60;
                var fullCount = (typeof RAW_DATA !== 'undefined' && Array.isArray(RAW_DATA)) ? RAW_DATA.length : 0;
                totalCount = fullCount;
                limitedCount = Math.min(maxQ, fullCount);
            }
        } catch(e) {}

        /* ⭐ Thông tin lượt Nghe + Viết còn lại */
        var remaining = 0;
        try {
            if (typeof getDemoRemaining === 'function') {
                remaining = getDemoRemaining();
            }
        } catch(e) {}
        var showRemaining = (acc.tier === 'demo' || acc.tier === 'expired')
                            && remaining !== Infinity && remaining >= 0;

        var limitInfo = '';
        if (acc.maxQuestions > 0 && limitedCount > 0 && totalCount > limitedCount) {
            limitInfo = ' <span style="opacity:.75">(' +
                        limitedCount + '/' + totalCount + ' ' + unit + ')</span>';
        }

        var icon = acc.tier === 'expired' ? 'fa-exclamation-triangle'
                 : acc.tier === 'trial' ? 'fa-hourglass-half'
                 : acc.tier === 'demo' ? 'fa-user'
                 : 'fa-info-circle';
        var btnLabel = acc.tier === 'expired' ? 'Gia hạn ngay'
                     : acc.tier === 'demo' ? 'Đăng nhập'
                     : 'Nâng cấp Premium';
        var btnFn = acc.tier === 'demo' ? 'vocabUpgradeLogin()'
                  : 'vocabUpgradeRenew()';

        /* ⭐ Warning message có dấu + ngắn gọn */
        var descText = '';
        if (acc.tier === 'demo') {
            descText = 'Đăng nhập bằng Gmail để dùng toàn bộ kho câu, không giới hạn.';
        } else if (acc.tier === 'expired') {
            descText = 'Tài khoản đã hết hạn — gia hạn để tiếp tục dùng toàn bộ tính năng.';
        } else if (acc.tier === 'trial') {
            descText = 'Nâng cấp Premium để mở toàn bộ nội dung, không giới hạn.';
        } else {
            descText = acc.warning || '';
        }

        var remainingHtml = '';
        if (showRemaining) {
            remainingHtml = ' · <span style="color:#16a34a;font-weight:800">Nghe + Viết còn ' +
                            remaining + ' lượt</span>';
        }

        var banner = document.createElement('div');
        banner.id = 'vocabWarningBanner';
        banner.className = 'vocab-warning-banner tier-' + acc.tier;
        banner.innerHTML =
            '<div class="vocab-warning-icon"><i class="fas ' + icon + '"></i></div>' +
            '<div class="vocab-warning-text">' +
                '<strong>' + _esc(acc.label) + limitInfo + remainingHtml + '</strong>' +
                '<span>' + _esc(descText) + '</span>' +
            '</div>' +
            '<button class="vocab-warning-btn" onclick="' + btnFn + '">' +
                '<i class="fas fa-crown"></i> ' + btnLabel +
            '</button>';
        main.insertBefore(banner, main.firstChild);
    }

    function watchVocabMode() {
        var isVocab = (typeof CURRENT_DATASET !== 'undefined') && CURRENT_DATASET === VOCAB_ID;

        if (isVocab) {
            document.body.setAttribute('data-vocab-mode', '1');
        } else {
            document.body.removeAttribute('data-vocab-mode');
        }

        var selects = [
            document.getElementById('subjectFilter'),
            document.getElementById('pfSubjectFilter')
        ];
        selects.forEach(function(sf) {
            if (!sf) return;
            if (isVocab && !sf.disabled) {
                sf.disabled = true;
                sf.value = '';
                sf.style.opacity = '0.5';
                sf.style.cursor = 'not-allowed';
                sf.title = 'Không khả dụng cho Từ vựng';
            } else if (!isVocab && sf.disabled) {
                sf.disabled = false;
                sf.style.opacity = '';
                sf.style.cursor = '';
                sf.title = '';
            }
        });

        var hskSelects = [
            document.getElementById('hskFilter'),
            document.getElementById('pfHskFilter')
        ];
        hskSelects.forEach(function(hf) {
            if (!hf) return;
            var hsk79 = hf.querySelector('option[value="HSK7-9"]');
            var has79 = !!hsk79;
            if (isVocab && !has79) {
                var opt = document.createElement('option');
                opt.value = 'HSK7-9';
                opt.textContent = 'HSK7-9';
                hf.appendChild(opt);
            } else if (!isVocab && has79) {
                if (hf.value === 'HSK7-9') {
                    hf.value = '';
                }
                hsk79.remove();
            }
        });
    }

    window.getVocabAccess = getVocabAccess;
    window.vocabUpdateLockState = updateTabLockState;
    window.vocabInjectWarning = injectVocabWarningBanner;

    function patchLoop() {
        var vocabBtn = document.querySelector('.ds-btn[data-dataset="' + VOCAB_ID + '"]');
        if (!vocabBtn) {
            setTimeout(patchLoop, 300);
            return;
        }

        window.vocabUpdateLockState = updateTabLockState;

        if (!window.__vocabBuildFiltersPatched && typeof window.buildFilters === 'function') {
            window.__vocabBuildFiltersPatched = true;
            var origBuildFilters = window.buildFilters;
            window.buildFilters = function() {
                var result = origBuildFilters.apply(this, arguments);
                if (_isVocabMode()) {
                    var hf = document.getElementById('hskFilter');
                    if (hf && !hf.querySelector('option[value="HSK7-9"]')) {
                        var opt = document.createElement('option');
                        opt.value = 'HSK7-9';
                        opt.textContent = 'HSK7-9';
                        hf.appendChild(opt);
                    }
                }
                return result;
            };
        }

        if (!window.__vocabPfFilterPatched && typeof window.pfBuildFilterOptions === 'function') {
            window.__vocabPfFilterPatched = true;
            var origPfBuild = window.pfBuildFilterOptions;
            window.pfBuildFilterOptions = function() {
                var result = origPfBuild.apply(this, arguments);
                if (_isVocabMode()) {
                    var pfHf = document.getElementById('pfHskFilter');
                    if (pfHf && !pfHf.querySelector('option[value="HSK7-9"]')) {
                        var opt = document.createElement('option');
                        opt.value = 'HSK7-9';
                        opt.textContent = 'HSK7-9';
                        pfHf.appendChild(opt);
                    }
                    var pfSubj = document.getElementById('pfSubjectFilter');
                    if (pfSubj) {
                        pfSubj.disabled = true;
                        pfSubj.value = '';
                        pfSubj.style.opacity = '0.5';
                        pfSubj.style.cursor = 'not-allowed';
                        pfSubj.title = 'Không khả dụng cho Từ vựng';
                    }
                }
                return result;
            };
        }

        if (!vocabBtn.__vocabLimitHooked) {
            vocabBtn.__vocabLimitHooked = true;
            vocabBtn.addEventListener('click', function() {
                setTimeout(function() {
                    var acc = getVocabAccess();
                    if (!acc.allowed) return;
                    if (_isVocabMode() && window.FIXPY_DATASETS &&
                        window.FIXPY_DATASETS[VOCAB_ID]) {
                        var full = window.FIXPY_DATASETS[VOCAB_ID].data || [];
                        var limited = applyVocabLimits(full, acc);
                        if (limited.length !== full.length) {
                            RAW_DATA = limited;
                            if (typeof applyFilter === 'function') applyFilter();
                            if (typeof updateResultCount === 'function') updateResultCount();
                        }
                    }
                    updateTabLockState();
                    injectVocabWarningBanner();
                    watchVocabMode();
                }, 500);
            }, false);
        }

        updateTabLockState();

        /* ⭐ Luôn inject banner ở MỌI TAB (không chỉ vocab) */
        setInterval(function() {
            updateTabLockState();
            injectVocabWarningBanner();
        }, 2000);

        watchVocabMode();
        setInterval(watchVocabMode, 800);
    }
    setTimeout(patchLoop, 800);
})();
"""


# =================================================================
#  IMPORT VOCAB MODULE
# =================================================================
if not os.path.isfile(CONFIG_JSON) and os.path.isfile(os.path.join("..", CONFIG_JSON)):
    os.chdir("..")
    print("[fix.py] Phat hien chay tu scripts/ -> chuyen ve root")

try:
    from vocab_premium import (
        read_vocab_excel,
        build_vocab_css,
        build_vocab_tab_html,
        build_vocab_modal_html,
        build_vocab_js_override,
    )
    HAS_VOCAB_MODULE = True
    print("[fix.py] OK - Da load module vocab_premium")
except ImportError as e:
    HAS_VOCAB_MODULE = False
    print("[fix.py] WARN - Khong load duoc vocab_premium: " + str(e))


# =================================================================
#  CN2AN
# =================================================================
try:
    import cn2an
    HAS_CN2AN = True
except ImportError:
    HAS_CN2AN = False

_CN_DIGITS = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
_CN_UNITS = ['', '十', '百', '千']


def _num_to_chinese_basic(num):
    if num == 0:
        return '零'
    if num < 0:
        return '负' + _num_to_chinese_basic(-num)
    result = ''
    unit_idx = 0
    n = num
    while n > 0:
        digit = n % 10
        if digit != 0:
            if not (unit_idx == 1 and digit == 1 and n < 20 and result == ''):
                result = _CN_DIGITS[digit] + _CN_UNITS[unit_idx] + result
            else:
                result = _CN_UNITS[unit_idx] + result
        else:
            if result and not result.startswith('零'):
                result = '零' + result
        n //= 10
        unit_idx += 1
    if result.startswith('一十'):
        result = result[1:]
    return result


def _num_to_chinese(num):
    if HAS_CN2AN:
        try:
            return cn2an.an2cn(num)
        except Exception:
            pass
    return _num_to_chinese_basic(num)


def _digits_to_chinese(digits_str):
    return ''.join([_CN_DIGITS[int(d)] for d in digits_str])


def convert_arabic_to_chinese(text):
    if not text or not isinstance(text, str):
        return text

    def replace_percent(match):
        num_str = match.group(1)
        if '.' in num_str:
            parts = num_str.split('.')
            int_part = _num_to_chinese(int(parts[0]))
            dec_part = _digits_to_chinese(parts[1])
            return '百分之' + int_part + '点' + dec_part
        return '百分之' + _num_to_chinese(int(num_str))

    text = re.sub(r'(\d+(?:\.\d+)?)%', replace_percent, text)

    def replace_decimal(match):
        num_str = match.group(0)
        parts = num_str.split('.')
        int_part = _num_to_chinese(int(parts[0]))
        dec_part = _digits_to_chinese(parts[1])
        return int_part + '点' + dec_part

    text = re.sub(
        r'(?<![A-Za-z\-\.])\d+\.\d+(?![A-Za-z])',
        replace_decimal, text
    )

    def replace_int(match):
        return _num_to_chinese(int(match.group(0)))

    text = re.sub(
        r'(?<![A-Za-z\-\.])\d+(?![A-Za-z]|\.\d)',
        replace_int, text
    )

    return text


def _clean(s):
    if s is None:
        return ""
    return (str(s).replace('\n', ' ').replace('\r', ' ')
            .replace('\t', ' ').replace('\\', '\\\\'))


# =================================================================
#  HELPERS
# =================================================================
def _slugify(filename):
    base = filename.rsplit(".", 1)[0]
    base = unicodedata.normalize("NFD", base)
    base = "".join(c for c in base if unicodedata.category(c) != "Mn")
    base = base.replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower() or "dataset"


def _display_name(filename):
    name = filename.rsplit(".", 1)[0].replace("_", " ").strip()
    name = unicodedata.normalize("NFC", name)
    if name.islower() or name.isupper():
        name = name.title()
    return name


def _escape_json_for_script(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/")


def _js_str(s):
    if s is None:
        return ""
    return (str(s)
            .replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("'", "\\'")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("</", "<\\/"))


def _find_file_safe(filepath):
    if os.path.isfile(filepath):
        return filepath
    dirname = os.path.dirname(filepath) or "."
    basename = os.path.basename(filepath)
    if not os.path.isdir(dirname):
        return None
    variants = set()
    variants.add(basename)
    variants.add(unicodedata.normalize("NFC", basename))
    variants.add(unicodedata.normalize("NFD", basename))
    try:
        for fname in os.listdir(dirname):
            fname_nfc = unicodedata.normalize("NFC", fname)
            fname_nfd = unicodedata.normalize("NFD", fname)
            for variant in variants:
                if (fname == variant
                        or fname_nfc == unicodedata.normalize("NFC", variant)
                        or fname_nfd == unicodedata.normalize("NFD", variant)):
                    return os.path.join(dirname, fname)
    except Exception:
        pass
    return None


def _read_excel_rows(filepath):
    real_path = _find_file_safe(filepath)
    if not real_path:
        print("      [X] Khong tim thay file: " + os.path.basename(filepath))
        return []

    try:
        wb = openpyxl.load_workbook(real_path, data_only=True)
    except Exception as e:
        print("      [X] Loi load: " + type(e).__name__ + ": " + str(e))
        return []

    try:
        ws = wb.worksheets[0]
    except Exception as e:
        print("      [X] Loi sheet: " + str(e))
        return []

    print("      Sheet: " + ws.title
          + " - " + str(ws.max_row) + " dong, "
          + str(ws.max_column) + " cot")

    COL_STT = 0
    COL_HSK = 1
    COL_TOPIC = 2
    COL_SUBJECT = 3
    COL_VI = 4
    COL_ZH = 5
    COL_PINYIN = 6
    DATA_START = 2

    rows = []
    converted_count = 0
    skipped_empty = 0

    for row in ws.iter_rows(min_row=DATA_START, values_only=True):
        if not row or len(row) <= max(COL_VI, COL_ZH):
            skipped_empty += 1
            continue

        stt_val = row[COL_STT] if COL_STT < len(row) and row[COL_STT] is not None else ""
        hsk = _clean(row[COL_HSK]) if COL_HSK < len(row) else ""
        topic = _clean(row[COL_TOPIC]) if COL_TOPIC < len(row) else ""
        subject = _clean(row[COL_SUBJECT]) if COL_SUBJECT < len(row) else ""
        vi = _clean(row[COL_VI]) if COL_VI < len(row) else ""
        zh = _clean(row[COL_ZH]) if COL_ZH < len(row) else ""
        pinyin = _clean(row[COL_PINYIN]) if COL_PINYIN < len(row) else ""

        if not vi and not zh:
            skipped_empty += 1
            continue

        zh_original = zh
        zh = convert_arabic_to_chinese(zh)
        if zh != zh_original:
            converted_count += 1

        rows.append({
            "stt": str(stt_val),
            "hsk": hsk,
            "topic": topic,
            "subject": subject,
            "vi": vi,
            "zh": zh,
            "pinyin": pinyin,
        })

    print("      [OK] " + str(len(rows)) + " cau (bo qua "
          + str(skipped_empty) + " dong rong)")
    if converted_count > 0:
        print("      [OK] Chuyen so A Rap -> Han: " + str(converted_count) + " cau")

    return rows


# =================================================================
#  SCAN data/
# =================================================================
def scan_data_dir():
    if not os.path.isdir(DATA_DIR):
        print("[fix.py] Khong thay thu muc '" + DATA_DIR + "/' - bo qua.")
        return []

    files = []
    for ext in ("*.xlsx", "*.xls", "*.csv"):
        files.extend(glob.glob(os.path.join(DATA_DIR, ext)))
    files = sorted(set(files))

    if not files:
        print("[fix.py] Khong co file Excel trong '" + DATA_DIR + "/'")
        return []

    print("")
    print("[fix.py] Quet '" + DATA_DIR + "/' - " + str(len(files)) + " file")

    datasets = []
    used_ids = set()

    vocab_basename = os.path.basename(VOCAB_FILE).lower()

    for filepath in files:
        fname = os.path.basename(filepath)

        if fname.startswith("~$"):
            print("   [skip] " + fname + " - file tam")
            continue

        if fname.lower() in SKIP_FILES:
            print("   [skip] " + fname + " - da la tab Tong hop")
            continue

        if fname.lower() == vocab_basename:
            print("   [skip] " + fname + " - se tao tab Tu vung Premium rieng")
            continue

        print("   [file] " + fname)
        rows = _read_excel_rows(filepath)
        if not rows:
            print("   [!] " + fname + " - rong hoac loi, bo qua")
            continue

        base_id = _slugify(fname)
        dataset_id = base_id
        counter = 2
        while dataset_id in used_ids:
            dataset_id = base_id + "-" + str(counter)
            counter += 1
        used_ids.add(dataset_id)

        idx = len(datasets)
        icon = TAB_ICONS[idx % len(TAB_ICONS)]
        color = TAB_COLORS[idx % len(TAB_COLORS)]

        display = _display_name(fname)
        datasets.append({
            "id": dataset_id,
            "name": display,
            "icon": icon,
            "color": color,
            "data": rows,
            "count": len(rows),
            "source": fname,
            "type": "main",
            "group": "fixpy",
        })
        print("   [OK] " + fname + " -> tab '" + display
              + "' (" + str(len(rows)) + " cau)")

    return datasets


# =================================================================
#  BUILD JS OVERRIDE (CẬP NHẬT LOAD PREVIEW TRƯỚC, DATA ĐẦY ĐỦ SAU)
# =================================================================
def build_js_override(ids_js, datasets_meta_json):
    L = []
    add = L.append

    add("")
    add("<script>")
    add("/* FIX.PY - Lazy load preview + full data tu JSON (Co thong bao loading) */")
    add("(function() {")
    add("    'use strict';")
    add("    var NEW_IDS = " + ids_js + ";")
    add("")

    add("    window.FIXPY_DATASETS = {};")
    add("    window.__fixpyFullLoaded = false;")
    add("    window.__fixpyMeta = " + datasets_meta_json + ";")
    add("    window.__fixpyPendingSwitch = null;")

    add("    /* Hàm hiển thị thông báo trực quan */")
    add("    function showFixToast(msg, isError, duration) {")
    add("        var existing = document.getElementById('fixToastBanner');")
    add("        if (existing) existing.remove();")
    add("        var toast = document.createElement('div');")
    add("        toast.id = 'fixToastBanner';")
    add("        toast.style.cssText = 'position:fixed; bottom:24px; right:24px; z-index:999999; background:' + (isError ? '#dc2626' : '#2563eb') + '; color:#fff; padding:12px 20px; border-radius:12px; font-size:14px; font-weight:600; box-shadow:0 6px 20px rgba(0,0,0,0.25); display:flex; align-items:center; gap:8px; transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1);';")
    add("        toast.innerHTML = '<i class=\"fas ' + (isError ? 'fa-exclamation-circle' : 'fa-spinner fa-spin') + '\"></i><span>' + msg + '</span>';")
    add("        document.body.appendChild(toast);")
    add("        if (duration) {")
    add("            setTimeout(function() {")
    add("                toast.style.opacity = '0';")
    add("                setTimeout(function() { toast.remove(); }, 300);")
    add("            }, duration);")
    add("        }")
    add("    }")

    add("    /* Hiển thị thông báo đang tải ngầm ban đầu */")
    add("    showFixToast('Đang tải dữ liệu trang web...', false, null);")

    add("    /* 1. LOAD NHANH PREVIEW (1/10 data) TRUOC DE GIAO DIEN HIEN THI NGAY */")
    add("    (function() {")
    add("        fetch('data/fixpy_preview.json?t=' + Math.floor(Date.now() / 60000))")
    add("            .then(function(r) { return r.ok ? r.json() : {}; })")
    add("            .then(function(d) {")
    add("                if (!window.__fixpyFullLoaded) {")
    add("                    window.FIXPY_DATASETS = d || {};")
    add("                }")
    add("                console.log('[fix.py] preview loaded');")
    add("                if (typeof window.__fixpyOnDataReady === 'function') {")
    add("                    window.__fixpyOnDataReady();")
    add("                }")
    add("            })")
    add("            .catch(function(e) {")
    add("                console.error('[fix.py] preview load error:', e);")
    add("            });")
    add("    })();")
    add("")

    add("    /* 2. LOAD NGẦM TOÀN BỘ DỮ LIỆU ĐẦY ĐỦ PHÍA SAU */")
    add("    (function() {")
    add("        fetch('data/fixpy_datasets.json?t=' + Math.floor(Date.now() / 60000))")
    add("            .then(function(r) { return r.ok ? r.json() : {}; })")
    add("            .then(function(d) {")
    add("                window.FIXPY_DATASETS = d || {};")
    add("                window.__fixpyFullLoaded = true;")
    add("                console.log('[fix.py] FULL data loaded');")
    add("                ")
    add("                /* Nếu người dùng đã bấm chuyển tab trước đó, giờ load xong thì tự động chuyển và thông báo thành công */")
    add("                if (window.__fixpyPendingSwitch) {")
    add("                    var targetId = window.__fixpyPendingSwitch;")
    add("                    window.__fixpyPendingSwitch = null;")
    add("                    if (typeof window.__switchRawData === 'function') {")
    add("                        window.__switchRawData(targetId);")
    add("                        if (typeof applyFilter === 'function') applyFilter();")
    add("                        if (typeof updateResultCount === 'function') updateResultCount();")
    add("                    }")
    add("                }")
    add("                showFixToast('Đã sẵn sàng toàn bộ dữ liệu!', false, 2500);")
    add("            })")
    add("            .catch(function(e) {")
    add("                console.error('[fix.py] full data load error:', e);")
    add("                showFixToast('Lỗi tải dữ liệu đầy đủ!', true, 4000);")
    add("            });")
    add("    })();")
    add("")

    add("    window.__findByHskStt = function(hskTarget, sttTarget) {")
    add("        function _normH(hsk) {")
    add("            if (!hsk) return '';")
    add("            var s = String(hsk).toUpperCase().trim();")
    add("            s = s.replace(/\\([^)]*\\)/g, '').trim();")
    add("            s = s.replace(/\\s+/g, '');")
    add("            var m = s.match(/^HSK(\\d+)(?:[-–](\\d+))?$/);")
    add("            if (!m) return s;")
    add("            var from = parseInt(m[1], 10);")
    add("            var to = m[2] ? parseInt(m[2], 10) : from;")
    add("            if (from >= 7 || to >= 7) return 'HSK7-9';")
    add("            return 'HSK' + from;")
    add("        }")
    add("        var pool = (typeof RAW_DATA !== 'undefined' && Array.isArray(RAW_DATA))")
    add("                   ? RAW_DATA : [];")
    add("        var target = _normH(hskTarget);")
    add("        return pool.filter(function(r) {")
    add("            var rh = _normH(r.hsk);")
    add("            if (rh !== target) return false;")
    add("            if (sttTarget === null) return true;")
    add("            var sttStr = (r.stt_original != null && String(r.stt_original).trim() !== '')")
    add("                       ? String(r.stt_original).trim()")
    add("                       : String(r.stt || '').replace(/^[^0-9]*-/, '');")
    add("            var n = parseInt(sttStr, 10);")
    add("            if (isNaN(n)) return false;")
    add("            return n >= sttTarget;")
    add("        });")
    add("    };")
    add("")
    add("    function patchSwitchRawData() {")
    add("        if (window.__fixPySwitchPatched) return;")
    add("        var origSwitch = window.__switchRawData;")
    add("        if (typeof origSwitch !== 'function') {")
    add("            setTimeout(patchSwitchRawData, 100);")
    add("            return;")
    add("        }")
    add("        window.__switchRawData = function(datasetId) {")
    add("            if (window.FIXPY_DATASETS && window.FIXPY_DATASETS[datasetId]) {")
    add("                /* Nếu file full chưa tải xong mà người dùng bấm đổi tab */")
    add("                if (!window.__fixpyFullLoaded && datasetId !== 'tonghop') {")
    add("                    window.__fixpyPendingSwitch = datasetId;")
    add("                    showFixToast('Đang tải dữ liệu đầy đủ, vui lòng đợi giây lát...', false, null);")
    add("                    RAW_DATA = window.FIXPY_DATASETS[datasetId].data || [];")
    add("                    CURRENT_DATASET = datasetId;")
    add("                    return true;")
    add("                }")
    add("                RAW_DATA = window.FIXPY_DATASETS[datasetId].data || [];")
    add("                CURRENT_DATASET = datasetId;")
    add("                return true;")
    add("            }")
    add("            return origSwitch.apply(this, arguments);")
    add("        };")
    add("        window.__fixPySwitchPatched = true;")
    add("    }")
    add("    patchSwitchRawData();")
    add("")

    add("    window.__fixpyOnDataReady = function() {")
    add("        var curDs = (typeof CURRENT_DATASET !== 'undefined') ? CURRENT_DATASET : 'tonghop';")
    add("        if (window.FIXPY_DATASETS && window.FIXPY_DATASETS[curDs]) {")
    add("            if (typeof applyFilter === 'function') applyFilter();")
    add("            if (typeof updateResultCount === 'function') updateResultCount();")
    add("        }")
    add("    };")
    add("")

    add("    function patchMarkActive() {")
    add("        if (window.__fixPyMarkPatched) return;")
    add("        window.markCurrentDatasetActive = function() {")
    add("            var cur = (typeof CURRENT_DATASET !== 'undefined')")
    add("                      ? CURRENT_DATASET : 'tonghop';")
    add("            document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {")
    add("                b.classList.remove('active');")
    add("            });")
    add("            if (cur === 'tonghop') {")
    add("                var tonghopBtn = document.querySelector('.ds-btn[data-dataset=\"tonghop\"]');")
    add("                if (tonghopBtn) tonghopBtn.classList.add('active');")
    add("                return;")
    add("            }")
    add("            if (window.FIXPY_DATASETS && window.FIXPY_DATASETS[cur]) {")
    add("                var fxBtn = document.querySelector('.ds-btn[data-dataset=\"' + cur + '\"]');")
    add("                if (fxBtn) fxBtn.classList.add('active');")
    add("                return;")
    add("            }")
    add("            var subBtn = document.querySelector('.ds-sub-btn[data-dataset=\"' + cur + '\"]');")
    add("            if (subBtn) subBtn.classList.add('active');")
    add("            var cnBtn = document.querySelector('.ds-btn[data-dataset-group=\"chuyen-nganh\"]');")
    add("            if (cnBtn && subBtn) cnBtn.classList.add('active');")
    add("        };")
    add("        window.__fixPyMarkPatched = true;")
    add("    }")
    add("")

    add("    function patchGetLimitedData() {")
    add("        if (window.__fixPyLimitedPatched) return;")
    add("        var origGet = window.getLimitedData")
    add("                    || (typeof getLimitedData !== 'undefined' ? getLimitedData : null);")
    add("        if (typeof origGet !== 'function') return;")
    add("        window.getLimitedData = function() {")
    add("            var currentDs = (typeof CURRENT_DATASET !== 'undefined')")
    add("                            ? CURRENT_DATASET : 'tonghop';")
    add("            if (currentDs === 'tonghop') {")
    add("                return origGet.apply(this, arguments);")
    add("            }")
    add("            if (!window.FIXPY_DATASETS || !window.FIXPY_DATASETS[currentDs]) {")
    add("                return origGet.apply(this, arguments);")
    add("            }")
    add("            var info = (typeof getTierInfo === 'function')")
    add("                       ? getTierInfo() : {};")
    add("            if (info.tier === 'active') {")
    add("                return RAW_DATA;")
    add("            }")
    add("            var override = window.__onboardingOverride;")
    add("            if (override && Array.isArray(override) && override.length > 0")
    add("                && typeof state !== 'undefined' && state")
    add("                && !state.search && !state.hsk && !state.subject) {")
    add("                var currentStts = {};")
    add("                RAW_DATA.forEach(function(r) { currentStts[r.stt] = true; });")
    add("                var filtered = override.filter(function(r) {")
    add("                    return currentStts[r.stt];")
    add("                });")
    add("                if (filtered.length > 0) {")
    add("                    var max = info.maxQuestions || 60;")
    add("                    return filtered.slice(0, max);")
    add("                }")
    add("            }")
    add("            var max2 = info.maxQuestions || 60;")
    add("            return RAW_DATA.slice(0, max2);")
    add("        };")
    add("        window.__fixPyLimitedPatched = true;")
    add("    }")
    add("")

    add("    window.__fixpyParseHskStt = function(rawQuery) {")
    add("        if (!rawQuery) return null;")
    add("        var m = rawQuery.toLowerCase().match(/^hsk\\s*(7[-\\s]*9|\\d+)\\s*(?:(\\d+)(?:\\s+(\\d+))?)?$/);")
    add("        if (!m) return null;")
    add("        var hskNum = m[1].replace(/\\s+/g, '');")
    add("        if (hskNum === '7' || hskNum === '8' || hskNum === '9') hskNum = '7-9';")
    add("        var startStt = m[2] ? parseInt(m[2], 10) : null;")
    add("        var endStt;")
    add("        if (m[3]) {")
    add("            endStt = parseInt(m[3], 10);")
    add("        } else {")
    add("            endStt = null;")
    add("        }")
    add("        if (startStt !== null && endStt !== null && endStt < startStt) {")
    add("            var tmp = startStt; startStt = endStt; endStt = tmp;")
    add("        }")
    add("        return {")
    add("            hsk: (hskNum === '7-9') ? 'HSK7-9' : ('HSK' + hskNum),")
    add("            hskNum: hskNum,")
    add("            startStt: startStt,")
    add("            endStt: endStt")
    add("        };")
    add("    };")
    add("")

    add("    window.__fixpyFilterByHskStt = function(parsed) {")
    add("        var pool = window.__findByHskStt(parsed.hsk, null);")
    add("        if (parsed.startStt === null) return pool;")
    add("        if (parsed.endStt === null) {")
    add("            return pool.filter(function(r) {")
    add("                var sttStr = (r.stt_original != null && String(r.stt_original).trim() !== '')")
    add("                           ? String(r.stt_original).trim()")
    add("                           : String(r.stt || '').replace(/^[^0-9]*-/, '');")
    add("                var n = parseInt(sttStr, 10);")
    add("                if (isNaN(n)) return false;")
    add("                return n >= parsed.startStt;")
    add("            });")
    add("        }")
    add("        return pool.filter(function(r) {")
    add("            var sttStr = (r.stt_original != null && String(r.stt_original).trim() !== '')")
    add("                       ? String(r.stt_original).trim()")
    add("                       : String(r.stt || '').replace(/^[^0-9]*-/, '');")
    add("            var n = parseInt(sttStr, 10);")
    add("            if (isNaN(n)) return false;")
    add("            return n >= parsed.startStt && n <= parsed.endStt;")
    add("        });")
    add("    };")
    add("")
    
    add("    function patchApplyFilter() {")
    add("        if (window.__fixPyApplyFilterPatched) return;")
    add("        var origApply = window.applyFilter;")
    add("        if (typeof origApply !== 'function') {")
    add("            setTimeout(patchApplyFilter, 100);")
    add("            return;")
    add("        }")
    add("        window.applyFilter = function() {")
    add("            var curDs = (typeof CURRENT_DATASET !== 'undefined')")
    add("                        ? CURRENT_DATASET : 'tonghop';")
    add("            if (curDs === 'tonghop') {")
    add("                return origApply.apply(this, arguments);")
    add("            }")
    add("            if (!window.FIXPY_DATASETS || !window.FIXPY_DATASETS[curDs]) {")
    add("                return origApply.apply(this, arguments);")
    add("            }")
    add("            var si = document.getElementById('searchInput');")
    add("            var raw = si ? si.value.trim() : '';")
    add("            var parsed = window.__fixpyParseHskStt(raw);")
    add("            if (!parsed) {")
    add("                return origApply.apply(this, arguments);")
    add("            }")
    add("            var result = window.__fixpyFilterByHskStt(parsed);")
    add("            var hskNum = parsed.hskNum;")
    add("            var startStt = parsed.startStt;")
    add("            var endStt = parsed.endStt;")
    add("            try {")
    add("                filtered = result;")
    add("            } catch(e) {")
    add("                window.filtered = result;")
    add("            }")
    add("            if (typeof render === 'function') render(true);")
    add("            if (typeof updateResultCount === 'function') updateResultCount();")
    add("            if (typeof updateFilterUI === 'function') updateFilterUI();")
    add("            var clearBtn = document.getElementById('clearSearchBtn');")
    add("            if (clearBtn) clearBtn.classList.add('show');")
    add("            if (typeof showSearchToast === 'function') {")
    add("                var hskDisplay = (hskNum === '7-9') ? '7-9' : hskNum;")
    add("                var msg;")
    add("                if (startStt === null) {")
    add("                    msg = 'HSK' + hskDisplay + ': ' + result.length + ' cau';")
    add("                } else if (endStt === null) {")
    add("                    msg = 'HSK' + hskDisplay + ' tu cau ' + startStt + ': ' + result.length + ' ket qua';")
    add("                } else if (startStt === endStt) {")
    add("                    msg = 'HSK' + hskDisplay + ' cau ' + startStt + ': ' + result.length + ' ket qua';")
    add("                } else {")
    add("                    msg = 'HSK' + hskDisplay + ' cau ' + startStt + '->' + endStt + ': ' + result.length + ' ket qua';")
    add("                }")
    add("                showSearchToast(msg);")
    add("            }")
    add("        };")
    add("        window.__fixPyApplyFilterPatched = true;")
    add("    }")
    add("")

    add("    function patchPfApplyFilter() {")
    add("        if (window.__fixPyPfApplyFilterPatched) return;")
    add("        var origPfApply = window.pfApplyFilter;")
    add("        if (typeof origPfApply !== 'function') {")
    add("            setTimeout(patchPfApplyFilter, 100);")
    add("            return;")
    add("        }")
    add("        window.pfApplyFilter = function() {")
    add("            var curDs = (typeof CURRENT_DATASET !== 'undefined')")
    add("                        ? CURRENT_DATASET : 'tonghop';")
    add("            if (curDs === 'tonghop') {")
    add("                return origPfApply.apply(this, arguments);")
    add("            }")
    add("            if (!window.FIXPY_DATASETS || !window.FIXPY_DATASETS[curDs]) {")
    add("                return origPfApply.apply(this, arguments);")
    add("            }")
    add("            var si = document.getElementById('pfSearchInput');")
    add("            var raw = si ? si.value.trim() : '';")
    add("            var parsed = window.__fixpyParseHskStt(raw);")
    add("            if (!parsed) {")
    add("                return origPfApply.apply(this, arguments);")
    add("            }")
    add("            var si2 = document.getElementById('searchInput');")
    add("            if (si2) si2.value = raw;")
    add("            if (typeof state !== 'undefined' && state) {")
    add("                state.search = raw.toLowerCase();")
    add("            }")
    add("            var result = window.__fixpyFilterByHskStt(parsed);")
    add("            try {")
    add("                filtered = result;")
    add("            } catch(e) {")
    add("                window.filtered = result;")
    add("            }")
    add("            if (typeof pfBuildQuickNav === 'function') pfBuildQuickNav();")
    add("            if (typeof pfUpdateFilterUI === 'function') pfUpdateFilterUI();")
    add("            var clearBtn = document.getElementById('pfClearSearchBtn');")
    add("            if (clearBtn) clearBtn.classList.add('show');")
    add("            if (result.length > 0) {")
    add("                if (typeof loadPracticeFull === 'function') {")
    add("                    loadPracticeFull(result[0].stt);")
    add("                }")
    add("            } else {")
    add("                var pfViEl = document.getElementById('pfVi');")
    add("                if (pfViEl) pfViEl.textContent = 'Khong tim thay cau nao';")
    add("                var pfCounter = document.getElementById('pfCounter');")
    add("                if (pfCounter) pfCounter.textContent = 'Cau 0 / 0';")
    add("                var pfTags = document.getElementById('pfTags');")
    add("                if (pfTags) pfTags.innerHTML = '';")
    add("                var pfPrev = document.getElementById('pfPrevBtn');")
    add("                if (pfPrev) pfPrev.disabled = true;")
    add("                var pfNext = document.getElementById('pfNextBtn');")
    add("                if (pfNext) pfNext.disabled = true;")
    add("            }")
    add("        };")
    add("        window.__fixPyPfApplyFilterPatched = true;")
    add("    }")
    add("")
    
    add("    function bindTab(dsId) {")
    add("        /* ⭐ FIX_CONFLICT: Bỏ qua nút chuyen-nganh — không clone */")
    add("        if (dsId === 'chuyen-nganh') return;")
    add("        var btn = document.querySelector('.ds-btn[data-dataset=\"' + dsId + '\"]');")
    add("        if (btn && btn.getAttribute('data-dataset-group') === 'chuyen-nganh') return;")
    add("        if (!btn) return;")
    add("        if (btn.__fixPyBound) return;")
    add("        var cloned = btn.cloneNode(true);")
    add("        btn.parentNode.replaceChild(cloned, btn);")
    add("        cloned.__fixPyBound = true;")
    add("        cloned.addEventListener('click', function(e) {")
    add("            /* FIX_CONFLICT: bỏ stopImmediatePropagation */")
    add("            e.stopPropagation();")
    add("            var sub = document.getElementById('dsSubWrap');")
    add("            if (sub) sub.style.display = 'none';")
    add("            document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {")
    add("                b.classList.remove('active');")
    add("            });")
    add("            this.classList.add('active');")
    add("            if (typeof window.__switchRawData === 'function') {")
    add("                window.__switchRawData(dsId);")
    add("            }")
    add("            if (typeof state !== 'undefined' && state) {")
    add("                state.search = '';")
    add("                state.hsk = '';")
    add("                state.subject = '';")
    add("            }")
    add("            try {")
    add("                var si = document.getElementById('searchInput');")
    add("                var hf = document.getElementById('hskFilter');")
    add("                var sf = document.getElementById('subjectFilter');")
    add("                if (si) si.value = '';")
    add("                if (hf) hf.value = '';")
    add("                if (sf) sf.value = '';")
    add("                var cb = document.getElementById('clearSearchBtn');")
    add("                if (cb) cb.classList.remove('show');")
    add("            } catch(err) {}")
    add("            var savedTopics = null;")
    add("            if (typeof loadOnboardingSelection === 'function') {")
    add("                try {")
    add("                    var saved = loadOnboardingSelection();")
    add("                    if (saved && saved.topics && saved.topics.length > 0) {")
    add("                        savedTopics = saved.topics;")
    add("                    }")
    add("                } catch(e) {}")
    add("            }")
    add("            try {")
    add("                if (typeof buildFilters === 'function') buildFilters();")
    add("                if (typeof applyFilter === 'function') applyFilter();")
    add("                if (typeof updateResultCount === 'function') updateResultCount();")
    add("                if (savedTopics && savedTopics.length > 0")
    add("                    && typeof applyOnboardingSelection === 'function') {")
    add("                    try {")
    add("                        var cfg = (typeof getOnboardingConfig === 'function')")
    add("                                  ? getOnboardingConfig() : null;")
    add("                        if (cfg) {")
    add("                            var saved2 = loadOnboardingSelection();")
    add("                            window.__onboardingAutoPicked = saved2 ? !!saved2.auto_picked : false;")
    add("                            applyOnboardingSelection(savedTopics, false);")
    add("                        }")
    add("                    } catch(e2) {}")
    add("                }")
    add("                document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {")
    add("                    b.classList.remove('active');")
    add("                });")
    add("                this.classList.add('active');")
    add("            } catch(err) {}")
    add("            setTimeout(function() {")
    add("                var mainEl = document.getElementById('mainContent');")
    add("                if (mainEl) {")
    add("                    var yOffset = mainEl.getBoundingClientRect().top")
    add("                                + window.scrollY - 100;")
    add("                    window.scrollTo({ top: yOffset, behavior: 'smooth' });")
    add("                }")
    add("            }, 100);")
    add("        }, false); /* FIX_CONFLICT: bỏ capture */")
    add("    }")
    add("")

    add("    function patchApplyOnboarding() {")
    add("        if (window.__fixPyApplyOnbPatched) return;")
    add("        var origApply = window.applyOnboardingSelection")
    add("                      || (typeof applyOnboardingSelection !== 'undefined'")
    add("                          ? applyOnboardingSelection : null);")
    add("        if (typeof origApply !== 'function') return;")
    add("        window.applyOnboardingSelection = function(topics, scrollTop) {")
    add("            var currentDs = (typeof CURRENT_DATASET !== 'undefined')")
    add("                            ? CURRENT_DATASET : 'tonghop';")
    add("            if (!window.FIXPY_DATASETS || !window.FIXPY_DATASETS[currentDs]) {")
    add("                return origApply.apply(this, arguments);")
    add("            }")
    add("            var cfg = (typeof getOnboardingConfig === 'function')")
    add("                      ? getOnboardingConfig() : null;")
    add("            if (!cfg) return;")
    add("            var maxQ = cfg.max_questions;")
    add("            var isUnlimitedQ = (maxQ === -1 || maxQ === Infinity);")
    add("            var allowedHsk;")
    add("            if (cfg.hsk_allowed && Array.isArray(cfg.hsk_allowed) && cfg.hsk_allowed.length > 0) {")
    add("                allowedHsk = cfg.hsk_allowed.map(function(n) { return 'HSK' + n; });")
    add("            } else {")
    add("                allowedHsk = (typeof getAllowedHskList === 'function')")
    add("                             ? getAllowedHskList()")
    add("                             : ['HSK1','HSK2','HSK3','HSK4','HSK5','HSK6'];")
    add("            }")
    add("            var pool = RAW_DATA.filter(function(r) {")
    add("                if (allowedHsk.indexOf(r.hsk) === -1) return false;")
    add("                var s = (r.subject || '').trim();")
    add("                return topics.indexOf(s) !== -1;")
    add("            });")
    add("            pool.sort(function(a, b) {")
    add("                return (parseInt(a.stt) || 0) - (parseInt(b.stt) || 0);")
    add("            });")
    add("            var final = [];")
    add("            if (isUnlimitedQ) {")
    add("                final = pool.slice();")
    add("            } else {")
    add("                var maxPerTopic = (typeof getMaxPerTopic === 'function')")
    add("                                 ? getMaxPerTopic(maxQ, RAW_DATA)")
    add("                                 : Math.max(1, Math.ceil(maxQ / Math.max(1, topics.length)));")
    add("                var topicCount = {};")
    add("                var perHsk = Math.ceil(maxQ / allowedHsk.length);")
    add("                var hskCount = {};")
    add("                allowedHsk.forEach(function(h) { hskCount[h] = 0; });")
    add("                for (var i = 0; i < pool.length && final.length < maxQ; i++) {")
    add("                    var r = pool[i];")
    add("                    var s = (r.subject || '').trim() || '__no_subject__';")
    add("                    if ((topicCount[s] || 0) >= maxPerTopic) continue;")
    add("                    if (r.hsk && hskCount[r.hsk] !== undefined && hskCount[r.hsk] >= perHsk) continue;")
    add("                    final.push(r);")
    add("                    topicCount[s] = (topicCount[s] || 0) + 1;")
    add("                    if (r.hsk && hskCount[r.hsk] !== undefined) hskCount[r.hsk]++;")
    add("                }")
    add("                if (final.length < maxQ) {")
    add("                    var usedIds = {};")
    add("                    final.forEach(function(r) { usedIds[r.stt] = true; });")
    add("                    for (var p = 0; p < pool.length && final.length < maxQ; p++) {")
    add("                        var rp = pool[p];")
    add("                        if (usedIds[rp.stt]) continue;")
    add("                        var sp = (rp.subject || '').trim() || '__no_subject__';")
    add("                        if ((topicCount[sp] || 0) >= maxPerTopic) continue;")
    add("                        final.push(rp);")
    add("                        usedIds[rp.stt] = true;")
    add("                        topicCount[sp] = (topicCount[sp] || 0) + 1;")
    add("                    }")
    add("                }")
    add("                if (final.length > maxQ) final = final.slice(0, maxQ);")
    add("            }")
    add("            final.sort(function(a, b) {")
    add("                return (parseInt(a.stt) || 0) - (parseInt(b.stt) || 0);")
    add("            });")
    add("            window.__onboardingOverride = final;")
    add("            if (typeof state !== 'undefined' && state) {")
    add("                state.search = '';")
    add("                state.hsk = '';")
    add("                state.subject = '';")
    add("            }")
    add("            try {")
    add("                var si = document.getElementById('searchInput');")
    add("                if (si) si.value = '';")
    add("                var cb = document.getElementById('clearSearchBtn');")
    add("                if (cb) cb.classList.remove('show');")
    add("            } catch(e) {}")
    add("            if (typeof applyFilter === 'function') applyFilter();")
    add("            if (typeof updateResultCount === 'function') updateResultCount();")
    add("            if (typeof showOnboardingActiveBanner === 'function') {")
    add("                showOnboardingActiveBanner(topics, final.length);")
    add("            }")
    add("            if (scrollTop) {")
    add("                setTimeout(function() {")
    add("                    var mainEl = document.getElementById('mainContent');")
    add("                    if (mainEl) {")
    add("                        var yOffset = mainEl.getBoundingClientRect().top")
    add("                                    + window.scrollY - 100;")
    add("                        window.scrollTo({ top: yOffset, behavior: 'smooth' });")
    add("                    }")
    add("                }, 200);")
    add("            }")
    add("        };")
    add("        window.__fixPyApplyOnbPatched = true;")
    add("    }")
    add("")

    add("    function bindAll() {")
    add("        patchSwitchRawData();")
    add("        patchGetLimitedData();")
    add("        patchApplyOnboarding();")
    add("        patchApplyFilter();")
    add("        patchPfApplyFilter();")
    add("        NEW_IDS.forEach(bindTab);")
    add("        patchMarkActive();")
    add("        bindFixedTabs();")
    add("    }")
    add("    if (document.readyState === 'loading') {")
    add("        document.addEventListener('DOMContentLoaded', bindAll);")
    add("    } else {")
    add("        bindAll();")
    add("    }")
    add("")
    add("    var _timer = null;")
    add("    var observer = new MutationObserver(function() {")
    add("        clearTimeout(_timer);")
    add("        _timer = setTimeout(bindAll, 200);")
    add("    });")
    add("    /* FIX_CONFLICT: chỉ observe .ds-main-row */")
    add("    var _dsRow = document.querySelector('.ds-main-row');")
    add("    if (_dsRow) {")
    add("        observer.observe(_dsRow, { childList: true });")
    add("    }")
    add("")
    add("    /* === BIND LAI 2 TAB GOC (tonghop + chuyen-nganh) === */")
    add("    function bindFixedTabs() {")
    add("        var tonghopBtn = document.querySelector('.ds-btn[data-dataset=\"tonghop\"]');")
    add("        if (tonghopBtn && !tonghopBtn.__fixedBind) {")
    add("            tonghopBtn.__fixedBind = true;")
    add("            tonghopBtn.addEventListener('click', function(e) {")
    add("                e.stopPropagation();")
    add("                var sub = document.getElementById('dsSubWrap');")
    add("                if (sub) sub.style.display = 'none';")
    add("                document.querySelectorAll('.ds-btn, .ds-sub-btn').forEach(function(b) {")
    add("                    b.classList.remove('active');")
    add("                });")
    add("                this.classList.add('active');")
    add("                if (typeof window.__switchRawData === 'function') {")
    add("                    window.__switchRawData('tonghop');")
    add("                }")
    add("                if (typeof state !== 'undefined' && state) {")
    add("                    state.search = '';")
    add("                    state.hsk = '';")
    add("                    state.subject = '';")
    add("                }")
    add("                try {")
    add("                    var si = document.getElementById('searchInput');")
    add("                    var hf = document.getElementById('hskFilter');")
    add("                    var sf = document.getElementById('subjectFilter');")
    add("                    if (si) si.value = '';")
    add("                    if (hf) hf.value = '';")
    add("                    if (sf) sf.value = '';")
    add("                } catch(err) {}")
    add("                try {")
    add("                    if (typeof buildFilters === 'function') buildFilters();")
    add("                    if (typeof applyFilter === 'function') applyFilter();")
    add("                    if (typeof updateResultCount === 'function') updateResultCount();")
    add("                } catch(err) {}")
    add("            }, true);")
    add("        }")
    
    add("    }")
    add("    setTimeout(bindFixedTabs, 1500);")
    add("    setInterval(bindFixedTabs, 2000);")
    add("")
    add("    console.log('[fix.py] Da bind ' + NEW_IDS.length + ' tab:', NEW_IDS);")
    add("})();")
    add("</script>")

    return "\n".join(L)



# =================================================================
#  BUILD CSS LAYOUT
# =================================================================
def build_layout_css(new_datasets, add_vocab):
    css_lines = []
    css_lines.append("")
    css_lines.append("/* FIX.PY: AUTO-FIT LAYOUT */")
    css_lines.append("@media (max-width: 768px) {")
    css_lines.append("    .ds-main-row {")
    css_lines.append("        grid-template-columns: repeat(2, minmax(0, 1fr) ) !important;")
    css_lines.append("        gap: .5rem !important;")
    css_lines.append("    }")
    css_lines.append("}")
    css_lines.append("@media (min-width: 769px) {")
    css_lines.append("    .ds-main-row {")
    css_lines.append("        grid-template-columns: repeat(4, minmax(0, 1fr) ) !important;")
    css_lines.append("        gap: .55rem !important;")
    css_lines.append("    }")
    css_lines.append("}")

    css_lines.append("")
    css_lines.append("/* GRID DEU CHO TAB CON CHUYEN NGANH */")
    css_lines.append(".ds-sub-grid {")
    css_lines.append("    display: grid !important;")
    css_lines.append("    grid-template-columns: repeat(2, minmax(0, 1fr) ) !important;")
    css_lines.append("    gap: .55rem !important;")
    css_lines.append("    align-items: stretch !important;")
    css_lines.append("}")
    css_lines.append("@media (min-width: 600px) {")
    css_lines.append("    .ds-sub-grid { grid-template-columns: repeat(3, minmax(0, 1fr) ) !important; }")
    css_lines.append("}")
    css_lines.append("@media (min-width: 900px) {")
    css_lines.append("    .ds-sub-grid { grid-template-columns: repeat(4, minmax(0, 1fr) ) !important; }")
    css_lines.append("}")
    css_lines.append(".ds-sub-btn {")
    css_lines.append("    width: 100% !important;")
    css_lines.append("    min-width: 0 !important;")
    css_lines.append("    max-width: 100% !important;")
    css_lines.append("    height: 100% !important;")
    css_lines.append("    min-height: 44px !important;")
    css_lines.append("    padding: .55rem .7rem !important;")
    css_lines.append("    justify-content: flex-start !important;")
    css_lines.append("    border-radius: 12px !important;")
    css_lines.append("    font-size: clamp(.68rem, 1.9vw, .82rem) !important;")
    css_lines.append("    white-space: normal !important;")
    css_lines.append("    word-break: break-word !important;")
    css_lines.append("    overflow-wrap: anywhere !important;")
    css_lines.append("    line-height: 1.25 !important;")
    css_lines.append("    text-align: left !important;")
    css_lines.append("}")
    css_lines.append(".ds-sub-btn span {")
    css_lines.append("    flex: 1 1 auto !important;")
    css_lines.append("    min-width: 0 !important;")
    css_lines.append("    display: -webkit-box !important;")
    css_lines.append("    -webkit-line-clamp: 2 !important;")
    css_lines.append("    -webkit-box-orient: vertical !important;")
    css_lines.append("    overflow: hidden !important;")
    css_lines.append("}")

    for ds in new_datasets:
        i = ds["id"]
        sel = '.ds-btn[data-dataset="' + i + '"]'
        css_lines.append("")
        css_lines.append("/* Style cho tab " + i + " */")
        css_lines.append(sel + " {")
        css_lines.append("    background: var(--surface) !important;")
        css_lines.append("    border-color: var(--border) !important;")
        css_lines.append("    color: var(--text) !important;")
        css_lines.append("}")
        css_lines.append(sel + " i:first-child { color: var(--primary) !important; }")
        css_lines.append(sel + ":hover {")
        css_lines.append("    border-color: var(--primary) !important;")
        css_lines.append("    background: var(--primary-light) !important;")
        css_lines.append("}")
        css_lines.append(sel + ".active {")
        css_lines.append("    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;")
        css_lines.append("    color: #fff !important;")
        css_lines.append("    border-color: transparent !important;")
        css_lines.append("    box-shadow: 0 4px 12px rgba(124, 58, 237, .35) !important;")
        css_lines.append("}")
        css_lines.append(sel + ".active i:first-child { color: #fff !important; }")
        css_lines.append('[data-theme="dark"] ' + sel + " {")
        css_lines.append("    background: var(--surface) !important;")
        css_lines.append("    border-color: var(--border) !important;")
        css_lines.append("}")
        css_lines.append('[data-theme="dark"] ' + sel + ".active {")
        css_lines.append("    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;")
        css_lines.append("    border-color: transparent !important;")
        css_lines.append("}")

    if add_vocab:
        css_lines.append("")
        css_lines.append("/* VOCAB PREMIUM CSS */")
        css_lines.append(build_vocab_css(VOCAB_ID))
        css_lines.append(VOCAB_WARNING_CSS)

    return "\n".join(css_lines) + "\n"


# =================================================================
#  MAIN (GHI CẢ 2 FILE: FULL VÀ PREVIEW)
# =================================================================
def main():
    print("=" * 62)
    print("[fix.py] Auto-scan data/ -> them tab rieng cho moi file")
    print("=" * 62)

    if not os.path.isfile(INDEX_HTML):
        print("[X] Khong thay " + INDEX_HTML + ". Chay convert.py truoc.")
        sys.exit(1)

    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    datasets = scan_data_dir()

    vocab_data = []
    vocab_real_path = None
    if HAS_VOCAB_MODULE:
        print("")
        print("[VOCAB] Kiem tra file tu vung: " + VOCAB_FILE)
        vocab_real_path = _find_file_safe(VOCAB_FILE)
        if vocab_real_path:
            print("[VOCAB] Tim thay: " + os.path.basename(vocab_real_path))
            vocab_data = read_vocab_excel(vocab_real_path)
            if not vocab_data:
                print("[VOCAB] [!] File rong hoac loi")
        else:
            print("[VOCAB] Khong co file tu vung - bo qua")

    all_new = []
    for ds in datasets:
        marker = 'data-dataset="' + ds["id"] + '"'
        if marker not in html:
            all_new.append(ds)
        else:
            print("   [skip] '" + ds["id"] + "' da co trong HTML")

    vocab_exists_in_html = 'data-dataset="' + VOCAB_ID + '"' in html
    add_vocab = bool(vocab_data) and not vocab_exists_in_html

    _need_data_rewrite = bool(vocab_data) or bool(datasets)
    _need_patch_html = bool(all_new) or add_vocab

    # Chuẩn bị dữ liệu để ghi ra file JSON
    datasets_dict = {}
    if vocab_data:
        datasets_dict[VOCAB_ID] = {
            "id": VOCAB_ID,
            "name": VOCAB_LABEL,
            "icon": "fa-book",
            "color": "#f59e0b",
            "data": vocab_data,
            "count": len(vocab_data),
            "source": (os.path.basename(vocab_real_path)
                       if vocab_real_path else "tu_vung_hsk.xlsx"),
            "type": "premium",
            "group": "fixpy",
        }

    for ds in datasets:
        datasets_dict[ds["id"]] = ds

    for ds in all_new:
        datasets_dict[ds["id"]] = ds

    if _need_data_rewrite or _need_patch_html:
        _data_dir = "data"
        os.makedirs(_data_dir, exist_ok=True)
        
        # 1. Ghi file full 20MB
        _fixpy_path = os.path.join(_data_dir, "fixpy_datasets.json")
        with open(_fixpy_path, "w", encoding="utf-8") as _f:
            json.dump(datasets_dict, _f, ensure_ascii=False, separators=(",", ":"))
        _size_kb = os.path.getsize(_fixpy_path) / 1024
        print(f"   [OK] Ghi data/fixpy_datasets.json ({_size_kb:.1f} KB)")

        # 2. Ghi file preview siêu nhẹ (chỉ lấy 1/10 data ban đầu)
        _preview_dict = {}
        for _ds_id, _ds in datasets_dict.items():
            _full = _ds.get("data", [])
            _n = max(1, len(_full) // 10)
            _preview_dict[_ds_id] = {
                "id": _ds["id"],
                "name": _ds["name"],
                "icon": _ds["icon"],
                "color": _ds["color"],
                "count": _ds["count"],
                "source": _ds["source"],
                "type": _ds.get("type", "main"),
                "group": _ds.get("group", "fixpy"),
                "data": _full[:_n],
                "preview": True,
            }

        _preview_path = os.path.join("data", "fixpy_preview.json")
        with open(_preview_path, "w", encoding="utf-8") as _f:
            json.dump(_preview_dict, _f, ensure_ascii=False, separators=(",", ":"))
        _prev_kb = os.path.getsize(_preview_path) / 1024
        print(f"   [OK] Ghi data/fixpy_preview.json ({_prev_kb:.1f} KB - Load nhanh)")

    if not _need_patch_html and not _need_data_rewrite:
        print("")
        print("[fix.py] Tat ca da co - khong can patch HTML.")
        return

    # CASE A: Tab da co -> chi ghi lai data JSON, khong patch HTML
    if not _need_patch_html and _need_data_rewrite:
        print("")
        print("[fix.py] Tab da co san -> CHI ghi lai data JSON (khong patch HTML)")
        print("")
        print("=" * 62)
        print("[fix.py] Chay patch_buttons.py de cover 4 nut...")
        print("=" * 62)
        try:
            _here = os.path.dirname(os.path.abspath(__file__))
            if _here not in sys.path:
                sys.path.insert(0, _here)
            from patch_buttons import patch_all_buttons
            _ok = patch_all_buttons(INDEX_HTML)
            print("[fix.py] patch_buttons.py -> " + ("THANH CONG" if _ok else "THAT BAI"))
        except Exception as _e:
            print("[fix.py] Loi patch_buttons: " + str(_e))
        return

    print("")
    print("[fix.py] Se them:")
    for ds in all_new:
        print("   - [tab] " + ds["name"] + " (" + str(ds["count"]) + " cau)")
    if add_vocab:
        print("   - [PREMIUM] " + VOCAB_LABEL + " (" + str(len(vocab_data)) + " tu)")

    print("")
    print("[PATCH 2] Them button tabs...")
    new_btns = ""
    for ds in all_new:
        label = ds["name"]
        new_btns += (
            '\n        <button class="ds-btn ds-btn-primary" '
            'data-dataset="' + ds["id"] + '">\n'
            '            <i class="fas ' + ds["icon"] + '"></i>\n'
            '            <span>' + _js_str(label) + '</span>\n'
            '        </button>'
        )

    if add_vocab:
        new_btns += build_vocab_tab_html(VOCAB_ID, VOCAB_LABEL)

    pat_tonghop = re.compile(
        r'(<button[^>]*class="[^"]*ds-btn[^"]*"[^>]*data-dataset="tonghop"[^>]*>.*?</button>)',
        re.MULTILINE | re.DOTALL
    )
    html, n = pat_tonghop.subn(
        lambda m: m.group(1) + new_btns,
        html, count=1
    )

    if n > 0:
        print("   [OK] Da chen button (sau 'Tong hop')")
    else:
        print("   [!] Khong thay nut 'tonghop' -> fallback truoc 'chuyen-nganh'")
        pat_before_cn = re.compile(
            r'(\s*)(<button\s+class="[^"]*ds-btn[^"]*"\s+[^>]*data-dataset-group="chuyen-nganh")',
            re.MULTILINE
        )
        html, n = pat_before_cn.subn(
            lambda m: m.group(1) + new_btns + '\n        ' + m.group(2),
            html, count=1
        )
        if n == 0:
            print("[X] Khong tim thay ca nut 'tonghop' lan 'chuyen-nganh'")
            sys.exit(1)
        print("   [OK] Da chen button (fallback)")

    print("")
    print("[PATCH 3] CSS layout...")
    css = build_layout_css(all_new, add_vocab)
    pat_style = re.compile(r'(\s*)(</style>)', re.MULTILINE)
    html, n = pat_style.subn(
        lambda m: m.group(1) + css + m.group(1) + m.group(2),
        html, count=1
    )
    if n == 0:
        print("   [!] Khong tim thay </style>")
    else:
        print("   [OK] Da inject CSS")

    print("")
    print("[PATCH 4] JS binding...")

    ids_js = json.dumps([ds["id"] for ds in all_new])

    datasets_meta = {}
    for _id, _ds in datasets_dict.items():
        datasets_meta[_id] = {
            "id": _ds["id"],
            "name": _ds["name"],
            "icon": _ds["icon"],
            "color": _ds["color"],
            "count": _ds["count"],
            "source": _ds["source"],
            "type": _ds.get("type", "main"),
            "group": _ds.get("group", "fixpy"),
        }

    datasets_json = _escape_json_for_script(datasets_meta)

    js = build_js_override(ids_js, datasets_json)

    if add_vocab:
        js += '\n<script>\n'
        js += build_vocab_js_override(VOCAB_ID)
        js += '\n' + build_vocab_js_patch()
        js += '\n</script>\n'

    modal_html = ""
    if add_vocab:
        modal_html = build_vocab_modal_html()

    pat_body = re.compile(r'(\s*)(</body>)', re.MULTILINE)
    html, n = pat_body.subn(
        lambda m: m.group(1) + modal_html + '\n' + js + m.group(1) + m.group(2),
        html, count=1
    )
    if n == 0:
        print("[X] Khong tim thay </body>")
        sys.exit(1)
    print("   [OK] Da inject JS + modal")

    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(INDEX_HTML) / 1024

    print("")
    print("=" * 62)
    print("[fix.py] HOAN TAT! Da patch " + INDEX_HTML)
    print("[fix.py] Kich thuoc HTML: " + str(round(size_kb, 1)) + " KB")

    if all_new:
        print("[fix.py] Tab thuong da them:")
        for ds in all_new:
            print("   - " + ds["name"] + " (" + str(ds["count"]) + " cau)")

    if add_vocab:
        print("[fix.py] Tab Tu vung PREMIUM: " + str(len(vocab_data)) + " tu")

    print("[fix.py] Layout: PC 4 cot - Mobile 2 cot")
    print("=" * 62)

    print("")
    print("=" * 62)
    print("[fix.py] Chay patch_buttons.py de cover 4 nut...")
    print("=" * 62)
    try:
        _here = os.path.dirname(os.path.abspath(__file__))
        if _here not in sys.path:
            sys.path.insert(0, _here)

        from patch_buttons import patch_all_buttons
        _ok = patch_all_buttons(INDEX_HTML)
        if _ok:
            print("[fix.py] patch_buttons.py -> THANH CONG")
        else:
            print("[fix.py] patch_buttons.py -> THAT BAI (tra ve False)")
    except ImportError as _e:
        print("[fix.py] Khong tim thay patch_buttons.py: " + str(_e))
        print("[fix.py] Bo qua buoc nay")
    except Exception as _e:
        print("[fix.py] Loi khi chay patch_buttons.py: " + str(_e))
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
