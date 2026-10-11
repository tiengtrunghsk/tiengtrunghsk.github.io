# -*- coding: utf-8 -*-
"""
Module GỘP: Auth + Firebase + Admin panel + Trial + Renewal (QR ngân hàng).
Hỗ trợ 3 tier: demo / trial / active (bao gồm gói vĩnh viễn).
Đọc config từ file JSON bên ngoài (config.json).

✅ RTDB PRESENCE (2026-09):
   - Track user online qua Firebase Realtime Database (KHÔNG tốn Firestore quota)
   - onDisconnect tự động xóa khi tắt tab
   - Heartbeat 2 phút/lần
   - Admin xem được danh sách user online realtime

FIX (2026-09):
- Sửa lỗi dropdown user menu không bấm được trên desktop
- Thêm banner cảnh báo gia hạn 3 mức
- Dropdown mặc định mở, nhớ trạng thái đóng trong sessionStorage
- Chèn User Online section vào Admin Panel
- Fix typo HTML trong dropdown (stylerop, downfas, renew-b|adge)
"""

import json


# ═══════════════════════════════════════════════════════════════
# CSS
# ═══════════════════════════════════════════════════════════════
def build_accounts_css():
    return r"""
/* ============ USER MENU ============ */
.user-menu{position:relative}
.user-avatar{width:38px;height:38px;border-radius:50%;border:2px solid var(--border);cursor:pointer;object-fit:cover;transition:.15s;display:block;}
.user-avatar:hover{border-color:var(--primary);transform:scale(1.05)}
.user-dropdown{
    position:absolute;
    top:calc(100% + .5rem);
    right:0;
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:var(--radius);
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    padding:.5rem;
    min-width:290px;
    display:none;
    z-index:200;
}
.user-dropdown.show{display:block}

/* ═══════════════════════════════════════════════════════════════
   MŨI TÊN TAM GIÁC — Chỉ lên avatar (nút mở dropdown)
   ═══════════════════════════════════════════════════════════════ */
.user-dropdown::before{
    content:'';
    position:absolute;
    top:-9px;
    right:20px;
    width:0;
    height:0;
    border-left:9px solid transparent;
    border-right:9px solid transparent;
    border-bottom:9px solid var(--border);
    pointer-events:none;
}
.user-dropdown::after{
    content:'';
    position:absolute;
    top:-7px;
    right:22px;
    width:0;
    height:0;
    border-left:7px solid transparent;
    border-right:7px solid transparent;
    border-bottom:7px solid var(--surface);
    pointer-events:none;
}
.user-info{padding:.75rem;border-bottom:1px solid var(--border);margin-bottom:.5rem}
.user-info .name{font-weight:700;font-size:.9rem;color:var(--text);margin-bottom:.2rem}
.user-info .email{font-size:.75rem;color:var(--text-3);word-break:break-all}
.user-info .role{display:inline-block;margin-top:.4rem;padding:.15rem .5rem;background:var(--primary-light);color:var(--primary-dark);border-radius:50px;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.3px;}
.user-info .role.admin{background:var(--amber-light);color:#92400e}
.user-info .role.subadmin{background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff}
.dropdown-item{display:flex;align-items:center;gap:.5rem;width:100%;padding:.65rem .75rem;border:none;border-radius:var(--radius-sm);background:transparent;color:var(--text);font-size:.85rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;text-align:left;text-decoration:none;}
.dropdown-item:hover{background:var(--surface-2)}
.dropdown-item.danger{color:var(--danger)}
.dropdown-item.danger:hover{background:var(--danger-light)}

/* ============ DROPDOWN: NÚT GIA HẠN ============ */
.dropdown-renew{
    display:flex;align-items:center;justify-content:center;gap:.5rem;
    width:100%;padding:.75rem 1rem;margin:.4rem 0;
    border:none;border-radius:12px;
    background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 50%,#a855f7 100%);
    color:#fff;font-size:.9rem;font-weight:800;cursor:pointer;
    transition:all .25s ease;font-family:inherit;
    text-transform:uppercase;letter-spacing:.5px;
    box-shadow:0 4px 14px rgba(124,58,237,.35), 0 0 0 0 rgba(139,92,246,.6);
    position:relative;overflow:hidden;
    animation:renewPulse 2.5s infinite;
}
.dropdown-renew::before{
    content:'';position:absolute;top:0;left:-100%;
    width:100%;height:100%;
    background:linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent);
    animation:renewShine 3s infinite;
}
.dropdown-renew:hover,.dropdown-renew:active{
    transform:translateY(-2px) scale(1.02);
    box-shadow:0 8px 24px rgba(124,58,237,.5), 0 0 0 4px rgba(139,92,246,.25);
}
.dropdown-renew i{font-size:1rem;position:relative;z-index:2;color:#e0f2fe;}
.dropdown-renew i.fa-gem{color:#67e8f9;text-shadow:0 0 8px rgba(103,232,249,.7);}
.dropdown-renew span{position:relative;z-index:2;}
@keyframes renewPulse{
    0%,100%{box-shadow:0 4px 14px rgba(124,58,237,.35), 0 0 0 0 rgba(139,92,246,.6);}
    50%{box-shadow:0 4px 18px rgba(139,92,246,.55), 0 0 0 6px rgba(139,92,246,0);}
}
@keyframes renewShine{0%{left:-100%;}50%,100%{left:100%;}}

.dropdown-renew .renew-badge{
    position:absolute;top:-6px;right:-4px;
    background:linear-gradient(135deg,#fbbf24,#f59e0b);
    color:#1e1b4b;font-size:.55rem;font-weight:900;
    padding:.15rem .45rem;border-radius:50px;
    letter-spacing:.5px;
    box-shadow:0 2px 8px rgba(251,191,36,.6);
    animation:renewBadgeBlink 1.5s infinite;
    border:1.5px solid #fef3c7;
    z-index:3;
}
@keyframes renewBadgeBlink{
    0%,100%{transform:scale(1);opacity:1;}
    50%{transform:scale(1.15);opacity:.85;}
}
.dropdown-renew.urgent{
    background:linear-gradient(135deg,#7f1d1d 0%,#b91c1c 50%,#dc2626 100%);
    animation:renewUrgent 1.2s infinite;
}
@keyframes renewUrgent{
    0%,100%{box-shadow:0 4px 14px rgba(220,38,38,.6), 0 0 0 0 rgba(220,38,38,.7);}
    50%{box-shadow:0 4px 18px rgba(220,38,38,.8), 0 0 0 8px rgba(220,38,38,0);}
}
.dropdown-forever{
    background:linear-gradient(135deg,#7c2d12 0%,#b91c1c 50%,#dc2626 100%) !important;
    box-shadow:0 4px 14px rgba(220,38,38,.45) !important;
    animation:foreverPulse2 2s infinite !important;
}
.dropdown-forever i.fa-crown{color:#fde68a !important;text-shadow:0 0 8px rgba(253,230,138,.8) !important;}
@keyframes foreverPulse2{
    0%,100%{box-shadow:0 4px 14px rgba(220,38,38,.45), 0 0 0 0 rgba(220,38,38,.6);}
    50%{box-shadow:0 4px 18px rgba(220,38,38,.7), 0 0 0 6px rgba(220,38,38,0);}
}

/* ============ USER DETAILS ============ */
.user-details{padding:.6rem .75rem .75rem;border-bottom:1px solid var(--border);margin-bottom:.5rem;display:flex;flex-direction:column;gap:.6rem;}
.detail-row{display:flex;align-items:flex-start;gap:.65rem;}
.detail-icon{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;background:var(--surface-2);color:var(--text-2);transition:.2s;}
.detail-icon.ok{background:rgba(22,163,74,.12);color:var(--success);}
.detail-icon.warn{background:rgba(245,158,11,.15);color:#d97706;}
.detail-icon.urgent{background:rgba(220,38,38,.15);color:var(--danger);}
.detail-icon.permanent{background:var(--primary-light);color:var(--primary-dark);}
.detail-icon.trial{background:linear-gradient(135deg,rgba(245,158,11,.15),rgba(251,191,36,.2));color:#d97706;}
.detail-icon.expired{background:rgba(220,38,38,.25);color:var(--danger);}
.detail-content{flex:1;min-width:0;}
.detail-label{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.3px;color:var(--text-3);margin-bottom:.15rem;}
.detail-value{font-size:.85rem;font-weight:700;color:var(--text);line-height:1.3;word-break:break-word;}
.detail-value.ok{color:var(--success);}
.detail-value.warn{color:#d97706;}
.detail-value.urgent{color:var(--danger);}
.detail-value.permanent{color:var(--primary-dark);}
.detail-value.trial{color:#d97706;}
.detail-value.expired{color:var(--danger);text-decoration:line-through;}
.detail-sub{font-size:.7rem;color:var(--text-3);margin-top:.15rem;line-height:1.35;}
.detail-sub b{color:var(--text-2);font-weight:700;}
.progress-track{width:100%;height:6px;background:var(--surface-2);border-radius:50px;overflow:hidden;border:1px solid var(--border);}
.progress-bar{height:100%;border-radius:50px;transition:width .4s ease, background .3s ease;background:linear-gradient(90deg, #16a34a, #22c55e);}
.progress-bar.ok{background:linear-gradient(90deg, #16a34a, #22c55e);}
.progress-bar.warn{background:linear-gradient(90deg, #f59e0b, #fbbf24);}
.progress-bar.urgent{background:linear-gradient(90deg, #dc2626, #ef4444);}

.btn-login-header{display:flex;align-items:center;gap:.4rem;padding:.55rem 1rem;border-radius:50px;background:var(--primary);color:#fff;border:none;font-size:.85rem;font-weight:700;cursor:pointer;transition:.15s;font-family:inherit;box-shadow:0 4px 12px rgba(37,99,235,.3);white-space:nowrap;}
.btn-login-header:hover,.btn-login-header:active{background:var(--primary-dark);transform:translateY(-1px)}

/* ============ LOGIN MODAL ============ */
.login-modal{position:fixed;inset:0;background:rgba(15,23,42,.8);backdrop-filter:blur(6px);z-index:3000;display:none;align-items:center;justify-content:center;padding:1.5rem;animation:fadeIn .2s;}
.login-modal.show{display:flex}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.login-box{background:#fff;border-radius:20px;padding:2.5rem 2rem;max-width:440px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.3);text-align:center;position:relative;animation:slideUp .3s cubic-bezier(.34,1.56,.64,1);}
@keyframes slideUp{from{transform:translateY(30px) scale(.95);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.login-close{position:absolute;top:12px;right:12px;width:34px;height:34px;border-radius:50%;border:none;background:#f1f5f9;color:#475569;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:.15s;}
.login-close:hover{background:#fee2e2;color:#dc2626}
.login-logo{width:70px;height:70px;background:linear-gradient(135deg,#4f46e5,#7c3aed);border-radius:20px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:2rem;margin:0 auto 1.5rem;box-shadow:0 8px 20px rgba(124,58,237,.35);}
.login-box h2{font-size:1.4rem;color:#0f172a;margin-bottom:.5rem;font-weight:700}
.login-box p{color:#64748b;font-size:.9rem;margin-bottom:2rem;line-height:1.5}
.btn-google{display:flex;align-items:center;justify-content:center;gap:.75rem;width:100%;padding:.9rem 1.5rem;border-radius:50px;border:2px solid #e2e8f0;background:#fff;color:#0f172a;font-size:1rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;}
.btn-google:hover{border-color:#7c3aed;background:#faf5ff;transform:translateY(-1px);box-shadow:0 4px 12px rgba(124,58,237,.15)}
.btn-google img{width:22px;height:22px}
.login-error{background:#fee2e2;color:#dc2626;padding:.85rem 1rem;border-radius:10px;font-size:.85rem;margin-top:1rem;display:none;text-align:left;line-height:1.4;}
.login-error.show{display:block}
.login-footer{margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid #e2e8f0;font-size:.78rem;color:#94a3b8;line-height:1.5}

/* ============ ADMIN MODAL ============ */
.admin-modal{position:fixed;inset:0;background:rgba(15,23,42,.75);backdrop-filter:blur(4px);z-index:3000;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s;}
.admin-modal.show{display:flex}
.admin-box{background:var(--surface);border-radius:20px;width:100%;max-width:960px;max-height:calc(100vh - 2rem);overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.3);display:flex;flex-direction:column;}
.admin-header{padding:1.25rem 1.5rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;}
.admin-header h2{font-size:1.15rem;color:var(--text);display:flex;align-items:center;gap:.5rem;font-weight:700}
.admin-header h2 i{color:var(--amber)}
.admin-header-actions{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.admin-body{padding:1.25rem 1.5rem;overflow-y:auto;flex:1}

/* ============ SUMMARY BAR (TỔNG USER/ADMIN) ============ */
.admin-summary-bar{
    display:flex;align-items:center;gap:1.25rem;
    padding:.75rem 1rem;margin-bottom:1rem;
    background:linear-gradient(135deg, rgba(59,130,246,.08), rgba(245,158,11,.06));
    border:1px solid var(--border);border-radius:12px;flex-wrap:wrap;
}
.admin-summary-bar .summary-item{display:flex;align-items:center;gap:.5rem;font-size:.88rem;}
.admin-summary-bar .summary-item i{font-size:1.1rem;}
.admin-summary-bar .summary-label{color:var(--text-2);font-weight:700;text-transform:uppercase;font-size:.72rem;letter-spacing:.4px;}
.admin-summary-bar .summary-value{
    font-weight:900;font-size:1.15rem;
    background:var(--surface);
    padding:.15rem .65rem;border-radius:8px;
    border:1px solid var(--border);
    min-width:38px;text-align:center;line-height:1.2;
}
.admin-summary-bar #summaryTotalUsers{color:#2563eb;}
[data-theme="dark"] .admin-summary-bar #summaryTotalUsers{color:#93c5fd;}
.admin-summary-bar #summaryTotalAdmins{color:#d97706;}
[data-theme="dark"] .admin-summary-bar #summaryTotalAdmins{color:#fcd34d;}

/* Search box */
.admin-search-wrap{position:relative;margin-bottom:1rem;}
.admin-search-wrap i{position:absolute;left:.85rem;top:50%;transform:translateY(-50%);color:var(--text-3);font-size:.9rem;pointer-events:none;}
.admin-search{width:100%;padding:.7rem .85rem .7rem 2.4rem;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.88rem;outline:none;transition:.15s;font-family:inherit;}
.admin-search:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(37,99,235,.15)}
.admin-search-clear{position:absolute;right:.6rem;top:50%;transform:translateY(-50%);width:24px;height:24px;border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;font-size:.75rem;display:none;align-items:center;justify-content:center;transition:.15s;}
.admin-search-clear.show{display:flex}
.admin-search-clear:hover{background:var(--danger-light);color:var(--danger)}

/* Filter buttons */
.admin-filter-row{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1rem;}
.admin-filter-btn{padding:.35rem .75rem;border-radius:50px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);font-size:.75rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;display:inline-flex;align-items:center;gap:.3rem;white-space:nowrap;}
.admin-filter-btn:hover{border-color:var(--primary);color:var(--primary);}
.admin-filter-btn.active{background:var(--primary);color:#fff;border-color:var(--primary);box-shadow:0 2px 8px rgba(37,99,235,.3);}
.admin-filter-btn .count{background:rgba(0,0,0,.08);padding:.05rem .4rem;border-radius:50px;font-size:.68rem;font-weight:700;min-width:18px;text-align:center;}
.admin-filter-btn.active .count{background:rgba(255,255,255,.35);}

/* ═══════════════════════════════════════════════════════════
   COLLAPSIBLE SECTIONS
   ═══════════════════════════════════════════════════════════ */
.admin-section{
    margin-top:1.5rem;
    border:1px solid var(--border);
    border-radius:14px;
    background:var(--surface);
    overflow:hidden;
    transition:box-shadow .25s ease, border-color .25s ease;
}
.admin-section:hover{
    border-color:rgba(37,99,235,.35);
    box-shadow:0 4px 16px rgba(15,23,42,.06);
}
[data-theme="dark"] .admin-section:hover{
    border-color:rgba(96,165,250,.35);
    box-shadow:0 4px 16px rgba(0,0,0,.35);
}
.admin-section-head{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:.75rem;
    padding:.85rem 1rem;
    background:linear-gradient(135deg, rgba(37,99,235,.04), rgba(124,58,237,.03));
    border-bottom:1px solid var(--border);
    flex-wrap:wrap;
    transition:background .25s ease, border-color .25s ease;
    user-select:none;
}
[data-theme="dark"] .admin-section-head{
    background:linear-gradient(135deg, rgba(37,99,235,.08), rgba(124,58,237,.06));
}
.admin-section.collapsed .admin-section-head{
    border-bottom-color:transparent;
}
.admin-section-head .ash-left{
    display:flex;
    align-items:center;
    gap:.6rem;
    min-width:0;
    flex:1;
}
.admin-section-head .ash-icon{
    width:32px;
    height:32px;
    border-radius:9px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:.85rem;
    flex-shrink:0;
    background:var(--primary-light);
    color:var(--primary-dark);
    transition:.2s;
}
.admin-section-head .ash-icon.amber{background:var(--amber-light);color:#92400e;}
.admin-section-head .ash-icon.violet{background:rgba(124,58,237,.12);color:#7c3aed;}
.admin-section-head .ash-icon.slate{background:var(--surface-2);color:var(--text-2);}
.admin-section-head .ash-text{
    display:flex;
    flex-direction:column;
    gap:.15rem;
    min-width:0;
}
.admin-section-head .ash-title{
    font-weight:800;
    font-size:.9rem;
    color:var(--text);
    line-height:1.2;
    display:flex;
    align-items:center;
    gap:.4rem;
    flex-wrap:wrap;
}
.admin-section-head .ash-subtitle{
    font-size:.72rem;
    color:var(--text-3);
    line-height:1.3;
    display:flex;
    align-items:center;
    gap:.4rem;
    flex-wrap:wrap;
}
.admin-section-head .ash-subtitle .chip{
    display:inline-flex;
    align-items:center;
    gap:.25rem;
    padding:.1rem .45rem;
    border-radius:50px;
    font-size:.68rem;
    font-weight:700;
    background:var(--surface-2);
    color:var(--text-2);
}
.admin-section-head .ash-subtitle .chip.primary{background:var(--primary-light);color:var(--primary-dark);}
.admin-section-head .ash-subtitle .chip.warn{background:var(--amber-light);color:#92400e;}
.admin-section-head .ash-subtitle .chip.danger{background:var(--danger-light);color:var(--danger);}
.admin-section-head .ash-subtitle .chip.ok{background:rgba(22,163,74,.12);color:var(--success);}
.admin-section-head .ash-actions{
    display:flex;
    align-items:center;
    gap:.35rem;
    flex-shrink:0;
}
.admin-toggle-btn{
    width:34px;
    height:34px;
    border-radius:9px;
    border:1.5px solid var(--border);
    background:var(--surface);
    color:var(--text-2);
    cursor:pointer;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    font-size:.85rem;
    transition:all .2s ease;
    font-family:inherit;
    padding:0;
    position:relative;
}
.admin-toggle-btn:hover{
    background:var(--primary-light);
    color:var(--primary-dark);
    border-color:var(--primary);
    transform:translateY(-1px);
}
.admin-toggle-btn:active{
    transform:translateY(0) scale(.96);
}
.admin-toggle-btn i{
    transition:transform .25s ease;
    display:inline-block;
}
.admin-toggle-btn.active{
    background:var(--primary-light);
    color:var(--primary-dark);
    border-color:var(--primary);
}
.admin-toggle-btn:not(.active){
    background:var(--surface-2);
    color:var(--text-3);
}
.admin-toggle-btn:not(.active):hover{
    background:var(--danger-light);
    color:var(--danger);
    border-color:var(--danger);
}
.admin-section-body{
    display:grid;
    grid-template-rows:1fr;
    transition:grid-template-rows .3s ease, opacity .25s ease;
    opacity:1;
}
.admin-section.collapsed .admin-section-body{
    grid-template-rows:0fr;
    opacity:0;
}
.admin-section-body > .admin-section-inner{
    overflow:hidden;
    padding:1rem;
    min-height:0;
    transition:padding .3s ease;
}
.admin-section.collapsed .admin-section-body > .admin-section-inner{
    padding-top:0;
    padding-bottom:0;
}
.admin-section.has-pending .admin-section-head{
    background:linear-gradient(135deg, rgba(245,158,11,.14), rgba(251,191,36,.06));
    border-bottom-color:rgba(245,158,11,.4);
}
.admin-section.has-pending .ash-icon.amber{
    animation:bellRing 1.5s infinite;
    color:#dc2626;
    background:rgba(220,38,38,.12);
}
@keyframes bellRing{
    0%,100%{transform:rotate(0);}
    10%,30%{transform:rotate(-12deg);}
    20%,40%{transform:rotate(12deg);}
    50%{transform:rotate(0);}
}
#pendingRenewalsBadge.pulse,
.chip.pulse{
    display:inline-block;padding:.05rem .5rem;
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;border-radius:50px;
    font-weight:900;font-size:.72rem;
    animation:pendingPulse 1.5s infinite;
    box-shadow:0 2px 8px rgba(220,38,38,.5);
    min-width:22px;text-align:center;
}
@keyframes pendingPulse{
    0%,100%{transform:scale(1);box-shadow:0 2px 8px rgba(220,38,38,.5);}
    50%{transform:scale(1.15);box-shadow:0 4px 14px rgba(220,38,38,.8);}
}
.admin-section-body .no-data{
    padding:2rem 1rem;
    text-align:center;
    color:var(--text-3);
    font-size:.85rem;
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:.5rem;
}
.admin-section-body .no-data i{
    font-size:1.75rem;
    opacity:.4;
}

/* ============ ADD USER FORM ============ */
.add-user-form{background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius-sm);padding:1rem;margin-bottom:1rem;display:none;}
.add-user-form.show{display:block}
.add-user-form h3{font-size:.85rem;color:var(--text);margin-bottom:.75rem;font-weight:700}
.form-group{margin-bottom:.75rem}
.form-group label{display:block;font-size:.75rem;font-weight:600;color:var(--text-2);margin-bottom:.3rem}
.form-group input,.form-group select{width:100%;padding:.6rem .85rem;border-radius:8px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.85rem;outline:none;transition:.15s;font-family:inherit;}
.form-group input:focus,.form-group select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(37,99,235,.15)}
.form-actions{display:flex;gap:.5rem;justify-content:flex-end;margin-top:.75rem}
.btn{padding:.55rem 1rem;border-radius:8px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.82rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;display:inline-flex;align-items:center;gap:.35rem;}
.btn:hover{background:var(--surface-2)}
.btn:disabled{opacity:.5;cursor:not-allowed;}
.btn.primary{background:var(--primary);color:#fff;border-color:var(--primary)}
.btn.primary:hover{background:var(--primary-dark)}
.btn-add{padding:.45rem .85rem;border-radius:8px;border:none;background:var(--primary);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:.35rem;transition:.15s;font-family:inherit;}
.btn-add:hover{background:var(--primary-dark)}

/* ============ USER LIST ============ */
.user-list{display:flex;flex-direction:column;gap:.5rem}
.user-row{display:flex;align-items:center;gap:.75rem;padding:.75rem;background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius-sm);transition:.15s;}
.user-row:hover{border-color:var(--primary)}
.user-row .u-info{flex:1;min-width:0}
.user-row .u-name{font-weight:700;font-size:.88rem;color:var(--text);margin-bottom:.15rem}
.user-row .u-email{font-size:.75rem;color:var(--text-3);word-break:break-all}
.user-row .u-role{padding:.15rem .5rem;border-radius:50px;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.3px;white-space:nowrap;}
.user-row .u-role.admin{background:var(--amber-light);color:#92400e}
.user-row .u-role.user{background:var(--primary-light);color:var(--primary-dark)}
.user-row .u-role.super{background:linear-gradient(135deg, #f59e0b, #d97706);color:#fff;box-shadow:0 2px 6px rgba(245,158,11,.4);}
.user-row .u-role.subadmin{background:linear-gradient(135deg, #06b6d4, #0891b2);color:#fff;box-shadow:0 2px 6px rgba(6,182,212,.4);}
.user-row .u-role.perm{background:linear-gradient(135deg,#dc2626,#7c2d12);color:#fde68a;box-shadow:0 2px 6px rgba(220,38,38,.4);}
.user-row .u-role.trial{background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#1e1b4b;box-shadow:0 2px 6px rgba(245,158,11,.4);}
.user-row .u-actions{display:flex;gap:.3rem}
.u-btn{width:32px;height:32px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.8rem;transition:.15s;}
.u-btn:hover{background:var(--surface-2);color:var(--primary);border-color:var(--primary)}
.u-btn.danger:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger)}
.u-btn.history{background:rgba(124,58,237,.1);color:#7c3aed;border-color:rgba(124,58,237,.35);}
.u-btn.history:hover{background:#7c3aed;color:#fff;border-color:#7c3aed;transform:scale(1.08);}
.u-btn.expiry{background:rgba(245,158,11,.1);color:#d97706;border-color:rgba(245,158,11,.4);}
.u-btn.expiry:hover{background:var(--amber);color:#fff;border-color:var(--amber);transform:scale(1.08);}
.u-btn.expiry.urgent{background:rgba(220,38,38,.15);color:var(--danger);border-color:rgba(220,38,38,.5);animation:expiryPulse 2s infinite;}
.u-btn:disabled{opacity:.35;cursor:not-allowed}
@keyframes expiryPulse{0%,100%{box-shadow:0 0 0 0 rgba(220,38,38,.4);}50%{box-shadow:0 0 0 6px rgba(220,38,38,0);}}

.admin-close{width:34px;height:34px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.9rem;transition:.15s;}
.admin-close:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger)}

/* ============ LOGS ============ */
.logs-list{max-height:280px;overflow-y:auto;background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.5rem;}
.log-item{display:flex;gap:.5rem;padding:.4rem .5rem;font-size:.75rem;color:var(--text-2);border-bottom:1px solid var(--border);}
.log-item:last-child{border-bottom:none}
.log-item .log-time{color:var(--text-3);flex-shrink:0;font-family:monospace;font-size:.7rem}
.log-item .log-msg{flex:1;word-break:break-word}
.u-last-login{font-size:.68rem;color:var(--text-3);display:flex;align-items:center;gap:.25rem;margin-top:.2rem;}
.u-last-login.active{color:var(--success);}
.u-last-login.recent{color:var(--primary);}
.u-expiry{font-size:.68rem;font-weight:600;display:inline-flex;align-items:center;gap:.25rem;margin-top:.2rem;padding:.15rem .45rem;border-radius:50px;cursor:pointer;transition:.15s;}
.u-expiry:hover{opacity:.8;}
.u-expiry.permanent{background:rgba(148,163,184,.15);color:var(--text-3);}
.u-expiry.permanent.perm{background:rgba(220,38,38,.15);color:#dc2626;}
.u-expiry.ok{background:rgba(22,163,74,.12);color:var(--success);}
.u-expiry.warn{background:rgba(245,158,11,.15);color:#92400e;}
.u-expiry.urgent{background:rgba(220,38,38,.15);color:var(--danger);}
.u-expiry.expired{background:rgba(220,38,38,.25);color:#fff;text-decoration:line-through;}

/* ============ EDIT MODALS ============ */
.edit-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(4px);z-index:4000;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s;}
.edit-modal.show{display:flex}
.edit-box{background:var(--surface);border-radius:20px;width:100%;max-width:420px;box-shadow:0 20px 60px rgba(0,0,0,.4);padding:1.5rem;position:relative;animation:slideUp .3s cubic-bezier(.34,1.56,.64,1);}
.edit-box h2{font-size:1.1rem;color:var(--text);font-weight:700;display:flex;align-items:center;gap:.5rem;margin-bottom:1.25rem;}
.edit-box h2 i{color:var(--primary);}
.edit-close{position:absolute;top:12px;right:12px;width:32px;height:32px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text-2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.85rem;transition:.15s;}
.edit-close:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger)}
.edit-user-info{padding:.75rem;background:var(--surface-2);border-radius:10px;margin-bottom:1rem;border:1px solid var(--border);}
.edit-user-info .eu-name{font-weight:700;font-size:.9rem;color:var(--text);margin-bottom:.2rem}
.edit-user-info .eu-email{font-size:.75rem;color:var(--text-3);word-break:break-all}
.quick-expiry-btns{display:grid;grid-template-columns:repeat(3,1fr);gap:.4rem;margin-bottom:1rem;}
.quick-expiry-btn{padding:.5rem .4rem;border-radius:8px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);font-size:.72rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;display:flex;flex-direction:column;align-items:center;gap:.2rem;white-space:nowrap;}
.quick-expiry-btn:hover{background:var(--primary-light);border-color:var(--primary);color:var(--primary-dark);transform:translateY(-1px);}
.quick-expiry-btn.danger:hover{background:var(--danger-light);border-color:var(--danger);color:var(--danger);}

/* ============ IMPORT MODAL ============ */
.import-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(4px);z-index:3500;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s;}
.import-modal.show{display:flex}
.import-box{background:var(--surface);border-radius:20px;width:100%;max-width:900px;max-height:calc(100vh - 2rem);box-shadow:0 20px 60px rgba(0,0,0,.4);display:flex;flex-direction:column;overflow:hidden;}
.import-header{padding:1.25rem 1.5rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;}
.import-header h2{font-size:1.15rem;color:var(--text);display:flex;align-items:center;gap:.5rem;font-weight:700;}
.import-header h2 i{color:#16a34a;}
.import-body{padding:1.25rem 1.5rem;overflow-y:auto;flex:1;min-height:0;}
.import-summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:.6rem;margin-bottom:1rem;}
.import-stat{padding:.65rem .85rem;border-radius:10px;text-align:center;border:1px solid var(--border);background:var(--surface-2);}
.import-stat .num{font-size:1.5rem;font-weight:800;line-height:1;margin-bottom:.25rem;}
.import-stat .label{font-size:.7rem;color:var(--text-3);text-transform:uppercase;font-weight:600;}
.import-stat.ok .num{color:var(--success);}
.import-stat.update .num{color:var(--primary);}
.import-stat.warn .num{color:var(--amber);}
.import-stat.err .num{color:var(--danger);}
.import-preview-wrap{max-height:400px;overflow-y:auto;border:1px solid var(--border);border-radius:10px;background:var(--surface-2);}
.import-table{width:100%;border-collapse:collapse;font-size:.82rem;}
.import-table th{padding:.6rem .8rem;text-align:left;background:var(--surface);color:var(--text-2);font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.3px;border-bottom:2px solid var(--border);position:sticky;top:0;z-index:2;}
.import-table td{padding:.55rem .8rem;color:var(--text);border-bottom:1px solid var(--border);word-break:break-word;}
.import-table tr:last-child td{border-bottom:none;}
.import-table tr.row-error{background:rgba(220,38,38,.08);}
.import-table tr.row-warn{background:rgba(245,158,11,.08);}
.import-table tr.row-new{background:rgba(22,163,74,.05);}
.import-table tr.row-update{background:rgba(37,99,235,.05);}
.import-table .status-badge{display:inline-flex;align-items:center;gap:.3rem;padding:.2rem .5rem;border-radius:50px;font-size:.68rem;font-weight:700;white-space:nowrap;}
.import-table .status-badge.ok{background:rgba(22,163,74,.15);color:var(--success);}
.import-table .status-badge.update{background:rgba(37,99,235,.15);color:var(--primary);}
.import-table .status-badge.warn{background:rgba(245,158,11,.15);color:#92400e;}
.import-table .status-badge.err{background:rgba(220,38,38,.15);color:var(--danger);}
.import-table .role-badge{display:inline-block;padding:.15rem .5rem;border-radius:50px;font-size:.68rem;font-weight:700;text-transform:uppercase;}
.import-table .role-badge.admin{background:var(--amber-light);color:#92400e;}
.import-table .role-badge.user{background:var(--primary-light);color:var(--primary-dark);}
.import-options{display:flex;gap:1rem;margin-top:1rem;flex-wrap:wrap;}
.import-options label{display:flex;align-items:center;gap:.4rem;font-size:.82rem;font-weight:600;color:var(--text-2);cursor:pointer;user-select:none;}
.import-options input[type="checkbox"]{width:16px;height:16px;accent-color:var(--primary);cursor:pointer;}
.import-info{margin-top:1rem;padding:.65rem .85rem;border-radius:10px;background:var(--primary-light);color:var(--primary-dark);font-size:.78rem;line-height:1.6;display:flex;align-items:flex-start;gap:.5rem;}
.import-info i{margin-top:.15rem;flex-shrink:0;}
.import-footer{padding:1rem 1.5rem;border-top:1px solid var(--border);display:flex;gap:.5rem;justify-content:flex-end;align-items:center;background:var(--surface);}

/* ═══════════════════════════════════════════════════════════════
   ⏰ EXPIRY BANNER — Cảnh báo gia hạn 3 mức
   ═══════════════════════════════════════════════════════════════ */
.expiry-banner{
    display:flex;
    align-items:center;
    gap:clamp(.6rem,1.2vw,1rem);
    padding:clamp(.7rem,1.4vw,1rem) clamp(.8rem,1.5vw,1.15rem);
    margin-bottom:1rem;
    border-radius:var(--radius);
    flex-wrap:wrap;
    position:relative;
    overflow:hidden;
    animation:expirySlideDown .35s cubic-bezier(.34,1.56,.64,1);
    box-shadow:0 6px 20px rgba(0,0,0,.08);
    background:linear-gradient(135deg,#fef3c7,#fde68a);
    border:1.5px solid #f59e0b;
}
[data-theme="dark"] .expiry-banner{
    background:linear-gradient(135deg,rgba(245,158,11,.2),rgba(245,158,11,.3));
    border-color:#f59e0b;
}
@keyframes expirySlideDown{
    from{opacity:0;transform:translateY(-12px);}
    to{opacity:1;transform:translateY(0);}
}
.expiry-banner.urgent{
    background:linear-gradient(135deg,#fed7aa,#fdba74);
    border-color:#ea580c;
    animation:expirySlideDown .35s cubic-bezier(.34,1.56,.64,1),
              pulseUrgent 2.5s ease-in-out infinite;
}
[data-theme="dark"] .expiry-banner.urgent{
    background:linear-gradient(135deg,rgba(234,88,12,.25),rgba(234,88,12,.35));
    border-color:#ea580c;
}
@keyframes pulseUrgent{
    0%,100%{box-shadow:0 6px 20px rgba(234,88,12,.25);}
    50%{box-shadow:0 6px 28px rgba(234,88,12,.55);}
}
.expiry-banner.expired{
    background:linear-gradient(135deg,#fecaca,#fca5a5);
    border-color:#dc2626;
    animation:expirySlideDown .35s cubic-bezier(.34,1.56,.64,1),
              pulseExpired 1.8s ease-in-out infinite;
}
[data-theme="dark"] .expiry-banner.expired{
    background:linear-gradient(135deg,rgba(220,38,38,.3),rgba(220,38,38,.4));
    border-color:#dc2626;
}
@keyframes pulseExpired{
    0%,100%{box-shadow:0 6px 20px rgba(220,38,38,.3);}
    50%{box-shadow:0 6px 28px rgba(220,38,38,.6);}
}
.expiry-banner-icon{
    width:40px;
    height:40px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-shrink:0;
    font-size:1.1rem;
    color:#fff;
    box-shadow:0 4px 12px rgba(0,0,0,.15);
    background:linear-gradient(135deg,#f59e0b,#d97706);
}
.expiry-banner.urgent .expiry-banner-icon{
    background:linear-gradient(135deg,#ea580c,#c2410c);
    animation:expiryIconShake 2s ease-in-out infinite;
}
@keyframes expiryIconShake{
    0%,100%{transform:rotate(0deg);}
    25%{transform:rotate(-8deg);}
    75%{transform:rotate(8deg);}
}
.expiry-banner.expired .expiry-banner-icon{
    background:linear-gradient(135deg,#dc2626,#991b1b);
    animation:expiryIconShake 1.5s ease-in-out infinite;
}
.expiry-banner-text{
    flex:1 1 200px;
    min-width:0;
}
.expiry-banner-text .title{
    font-weight:800;
    font-size:clamp(.86rem,1vw,.96rem);
    color:#92400e;
    margin-bottom:.15rem;
    line-height:1.3;
}
.expiry-banner.urgent .expiry-banner-text .title{color:#9a3412;}
.expiry-banner.expired .expiry-banner-text .title{color:#7f1d1d;}
[data-theme="dark"] .expiry-banner-text .title{color:#fcd34d;}
[data-theme="dark"] .expiry-banner.urgent .expiry-banner-text .title{color:#fdba74;}
[data-theme="dark"] .expiry-banner.expired .expiry-banner-text .title{color:#fca5a5;}
.expiry-banner-text .desc{
    font-size:clamp(.72rem,.88vw,.82rem);
    color:#78350f;
    line-height:1.5;
}
.expiry-banner.urgent .expiry-banner-text .desc{color:#7c2d12;}
.expiry-banner.expired .expiry-banner-text .desc{color:#7f1d1d;}
[data-theme="dark"] .expiry-banner-text .desc{color:#fde68a;}
[data-theme="dark"] .expiry-banner.urgent .expiry-banner-text .desc{color:#fed7aa;}
[data-theme="dark"] .expiry-banner.expired .expiry-banner-text .desc{color:#fecaca;}
.expiry-banner-text b{
    font-weight:900;
    font-size:1.08em;
    color:#dc2626;
}
[data-theme="dark"] .expiry-banner-text b{color:#fef08a;}
.expiry-banner-btn{
    padding:clamp(.5rem,.9vw,.62rem) clamp(.85rem,1.3vw,1.1rem);
    border-radius:50px;
    border:none;
    background:linear-gradient(135deg,#f59e0b,#d97706);
    color:#fff;
    font-size:clamp(.74rem,.88vw,.84rem);
    font-weight:800;
    cursor:pointer;
    font-family:inherit;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:.4rem;
    white-space:nowrap;
    transition:transform .15s,box-shadow .2s,background .2s;
    box-shadow:0 4px 14px rgba(245,158,11,.45);
    text-transform:uppercase;
    letter-spacing:.3px;
}
.expiry-banner-btn:hover{
    transform:translateY(-1px) scale(1.03);
    box-shadow:0 6px 20px rgba(245,158,11,.65);
}
.expiry-banner.urgent .expiry-banner-btn{
    background:linear-gradient(135deg,#ea580c,#c2410c);
    box-shadow:0 4px 14px rgba(234,88,12,.5);
    animation:renewUrgent 1.2s infinite;
}
.expiry-banner.expired .expiry-banner-btn{
    background:linear-gradient(135deg,#7f1d1d,#b91c1c);
    box-shadow:0 4px 14px rgba(220,38,38,.5);
    animation:renewUrgent 1.2s infinite;
}
@media (max-width:600px){
    .expiry-banner{
        padding:.65rem .75rem;
        gap:.55rem;
    }
    .expiry-banner-icon{
        width:34px;
        height:34px;
        font-size:.95rem;
    }
    .expiry-banner-btn{
        width:100%;
        margin-top:.2rem;
    }
}

/* ============ RENEWAL MODAL ============ */
.renewal-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(6px);z-index:3500;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s;overflow-y:auto;}
.renewal-modal.show{display:flex}
.renewal-box{background:var(--surface);border-radius:20px;width:100%;max-width:560px;max-height:calc(100vh - 2rem);box-shadow:0 20px 60px rgba(0,0,0,.4);display:flex;flex-direction:column;overflow:hidden;animation:slideUp .3s cubic-bezier(.34,1.56,.64,1);}
.renewal-header{padding:1.25rem 1.5rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;gap:1rem;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;}
.renewal-header h2{font-size:1.15rem;font-weight:800;display:flex;align-items:center;gap:.5rem;color:#fff;margin:0;}
.renewal-header h2 i{color:#67e8f9;text-shadow:0 0 10px rgba(103,232,249,.8);}
.renewal-header .subtitle{font-size:.78rem;opacity:.9;margin-top:.15rem;}
.renewal-close{width:34px;height:34px;border-radius:50%;border:none;background:rgba(255,255,255,.2);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1rem;transition:.15s;flex-shrink:0;}
.renewal-close:hover{background:rgba(255,255,255,.35)}
.renewal-body{padding:1.5rem;overflow-y:auto;flex:1;}
.renewal-current{padding:.85rem 1rem;border-radius:12px;background:linear-gradient(135deg, rgba(79,70,229,.08), rgba(124,58,237,.08));border:1px solid rgba(124,58,237,.25);margin-bottom:1.25rem;display:flex;align-items:center;gap:.75rem;}
.renewal-current .rc-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.15rem;flex-shrink:0;}
.renewal-current.warn .rc-icon{background:var(--amber);}
.renewal-current.expired .rc-icon{background:var(--danger);}
.renewal-current .rc-info{flex:1;min-width:0;}
.renewal-current .rc-title{font-weight:800;font-size:.9rem;color:var(--text);margin-bottom:.15rem;}
.renewal-current .rc-desc{font-size:.75rem;color:var(--text-2);line-height:1.4;}
.renewal-current .rc-desc b{color:#7c3aed;}
.renewal-section-title{font-size:.72rem;font-weight:800;color:var(--text-3);text-transform:uppercase;letter-spacing:.5px;margin-bottom:.6rem;display:flex;align-items:center;gap:.35rem;}
.package-grid{display:grid;grid-template-columns:1fr;gap:.6rem;margin-bottom:1.25rem;}
@media(min-width:480px){.package-grid{grid-template-columns:1fr 1fr 1fr;}}
.package-card{padding:.9rem .75rem;border-radius:12px;border:2px solid var(--border);background:var(--surface);cursor:pointer;transition:.2s;text-align:center;position:relative;user-select:none;}
.package-card:hover{border-color:#7c3aed;transform:translateY(-2px);}
.package-card.selected{border-color:#7c3aed;background:linear-gradient(135deg, rgba(79,70,229,.08), rgba(124,58,237,.08));box-shadow:0 6px 20px rgba(124,58,237,.25);}
.package-card .pkg-label{font-weight:800;font-size:.95rem;color:var(--text);margin-bottom:.3rem;}
.package-card .pkg-price{font-weight:900;font-size:1.25rem;color:#7c3aed;line-height:1;margin-bottom:.25rem;}
.package-card .pkg-unit{font-size:.68rem;color:var(--text-3);font-weight:600;}
.package-card .pkg-save{position:absolute;top:-8px;right:-4px;background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;font-size:.6rem;font-weight:800;padding:.15rem .45rem;border-radius:50px;text-transform:uppercase;letter-spacing:.3px;box-shadow:0 2px 6px rgba(22,163,74,.4);}
.package-card .pkg-popular{position:absolute;top:-8px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#1e1b4b;font-size:.6rem;font-weight:800;padding:.15rem .5rem;border-radius:50px;text-transform:uppercase;letter-spacing:.3px;white-space:nowrap;box-shadow:0 2px 6px rgba(245,158,11,.4);}
.package-card[data-pkg="forever"]{background:linear-gradient(135deg, #fef3c7, #fde68a);border-color:#f59e0b;position:relative;}
.package-card[data-pkg="forever"]:hover{border-color:#d97706;transform:translateY(-3px) scale(1.02);box-shadow:0 12px 28px rgba(245,158,11,.4);}
.package-card[data-pkg="forever"].selected{background:linear-gradient(135deg, #fbbf24, #f59e0b);border-color:#b45309;box-shadow:0 8px 24px rgba(245,158,11,.5);}
.package-card[data-pkg="forever"] .pkg-label{color:#78350f;font-weight:900;}
.package-card[data-pkg="forever"] .pkg-price{background:linear-gradient(135deg,#dc2626,#b91c1c);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;font-size:1.4rem;font-weight:900;}
.package-card[data-pkg="forever"] .pkg-unit{color:#92400e;font-weight:700;}
.package-card[data-pkg="forever"].selected .pkg-label,
.package-card[data-pkg="forever"].selected .pkg-unit{color:#fff;}
.package-card[data-pkg="forever"].selected .pkg-price{-webkit-text-fill-color:#fff;background:none;color:#fff;}
.package-card[data-pkg="forever"]::before{
    content:'💎 VĨNH VIỄN';
    position:absolute;top:-10px;left:50%;transform:translateX(-50%);
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;font-size:.6rem;font-weight:900;
    padding:.2rem .6rem;border-radius:50px;
    letter-spacing:.5px;white-space:nowrap;
    box-shadow:0 4px 12px rgba(124,58,237,.5);
    animation:foreverPulse 1.8s infinite;z-index:3;
}
@keyframes foreverPulse{
    0%,100%{transform:translateX(-50%) scale(1);box-shadow:0 4px 12px rgba(124,58,237,.5);}
    50%{transform:translateX(-50%) scale(1.08);box-shadow:0 6px 18px rgba(124,58,237,.8);}
}
.qr-wrap{display:flex;flex-direction:column;align-items:center;gap:.75rem;padding:1rem;background:linear-gradient(135deg,#f0f4f8,#e2e8f0);border-radius:14px;border:1.5px dashed var(--border);}
.qr-img{width:220px;height:220px;background:#fff;padding:.5rem;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,.15);}
.qr-wrap .qr-hint{font-size:.75rem;color:var(--text-2);text-align:center;line-height:1.5;max-width:300px;}
.qr-wrap .qr-hint b{color:#7c3aed;}
.bank-info{padding:.9rem 1rem;border-radius:12px;background:var(--surface-2);border:1px solid var(--border);display:flex;flex-direction:column;gap:.55rem;}
.bank-row{display:flex;justify-content:space-between;align-items:center;gap:.75rem;font-size:.82rem;}
.bank-row .br-label{color:var(--text-3);font-weight:600;flex-shrink:0;}
.bank-row .br-value{color:var(--text);font-weight:700;word-break:break-all;text-align:right;}
.bank-row .br-value.code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--danger);font-size:.95rem;background:rgba(220,38,38,.08);padding:.15rem .5rem;border-radius:6px;letter-spacing:1px;}
.copy-btn{width:28px;height:28px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text-2);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:.75rem;transition:.15s;margin-left:.4rem;}
.copy-btn:hover{background:var(--primary-light);color:var(--primary-dark);border-color:var(--primary);}
.copy-btn.copied{background:var(--success);color:#fff;border-color:var(--success);}
.payment-steps{display:flex;flex-direction:column;gap:.5rem;padding:.85rem 1rem;border-radius:12px;background:linear-gradient(135deg, rgba(124,58,237,.08), rgba(124,58,237,.03));border:1px solid rgba(124,58,237,.25);}
.payment-steps .step{display:flex;gap:.6rem;font-size:.8rem;color:var(--text-2);line-height:1.5;align-items:flex-start;}
.payment-steps .step .num{width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:800;flex-shrink:0;margin-top:.05rem;}
.payment-steps .step b{color:var(--text);}
.renewal-actions{display:flex;gap:.6rem;justify-content:flex-end;padding-top:1rem;border-top:1px solid var(--border);}
.renewal-btn{padding:.7rem 1.2rem;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.85rem;font-weight:700;cursor:pointer;transition:.15s;font-family:inherit;display:inline-flex;align-items:center;gap:.4rem;text-decoration:none;}
.renewal-btn:hover{background:var(--surface-2);}
.renewal-btn.primary{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-color:#7c3aed;box-shadow:0 4px 12px rgba(124,58,237,.3);}
.renewal-btn.success{background:var(--success);color:#fff;border-color:var(--success);box-shadow:0 4px 12px rgba(22,163,74,.3);}
.renewal-btn:disabled{opacity:.5;cursor:not-allowed;}
.renewal-success{text-align:center;padding:2rem 1rem;display:flex;flex-direction:column;align-items:center;gap:1rem;}
.renewal-success .icon{width:70px;height:70px;border-radius:50%;background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;display:flex;align-items:center;justify-content:center;font-size:2rem;box-shadow:0 8px 24px rgba(22,163,74,.4);animation:successPop .5s cubic-bezier(.34,1.56,.64,1);}
@keyframes successPop{0%{transform:scale(0);}70%{transform:scale(1.15);}100%{transform:scale(1);}}
.renewal-success h3{font-size:1.15rem;font-weight:800;color:var(--text);margin:0;}
.renewal-success p{font-size:.85rem;color:var(--text-2);line-height:1.6;max-width:340px;margin:0;}
.renewal-success .info-box{padding:.65rem 1rem;border-radius:10px;background:var(--surface-2);border:1px solid var(--border);font-size:.78rem;color:var(--text-2);display:flex;align-items:center;gap:.5rem;text-align:left;}
.renewal-admin-row{display:flex;flex-direction:column;gap:.5rem;padding:.85rem;border-radius:10px;background:var(--surface-2);border:1px solid var(--border);margin-bottom:.5rem;}
.renewal-admin-row .rar-head{display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap;align-items:flex-start;}
.renewal-admin-row .rar-email{font-weight:800;font-size:.88rem;color:var(--text);word-break:break-all;}
.renewal-admin-row .rar-sub{font-size:.72rem;color:var(--text-3);margin-top:.15rem;}
.renewal-admin-row .rar-pkg{text-align:right;}
.renewal-admin-row .rar-amount{font-weight:900;font-size:1.05rem;color:#7c3aed;line-height:1;}
.renewal-admin-row .rar-pkg-label{font-size:.7rem;color:var(--text-3);margin-top:.15rem;}
.renewal-admin-row .rar-foot{display:flex;justify-content:space-between;align-items:center;gap:.5rem;padding-top:.5rem;border-top:1px solid var(--border);flex-wrap:wrap;}
.renewal-admin-row .rar-code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.78rem;color:var(--danger);background:rgba(220,38,38,.08);padding:.15rem .5rem;border-radius:6px;letter-spacing:.5px;font-weight:800;}
.renewal-admin-row .rar-status{display:inline-flex;align-items:center;gap:.25rem;padding:.2rem .5rem;border-radius:50px;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.3px;}
.renewal-admin-row .rar-status.pending{background:rgba(37,99,235,.15);color:#2563eb;}
.renewal-admin-row .rar-status.user_paid{background:rgba(245,158,11,.18);color:#d97706;}
.renewal-admin-row .rar-status.confirmed{background:rgba(22,163,74,.15);color:#16a34a;}
.renewal-admin-row .rar-actions{display:flex;gap:.35rem;align-items:center;flex-wrap:wrap;}

/* ============ RENEWAL HISTORY ============ */
.renewal-history-item{display:flex;flex-direction:column;gap:.4rem;padding:.85rem;margin-bottom:.5rem;background:var(--surface-2);border:1px solid var(--border);border-radius:10px;transition:.15s;}
.renewal-history-item:hover{border-color:#7c3aed}
.renewal-history-item .rh-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem;flex-wrap:wrap;}
.renewal-history-item .rh-pkg{font-weight:800;font-size:.88rem;color:var(--text);}
.renewal-history-item .rh-amount{font-weight:900;font-size:1rem;color:#7c3aed;white-space:nowrap;}
.renewal-history-item .rh-date{font-size:.72rem;color:var(--text-3);display:flex;align-items:center;gap:.3rem;margin-top:.15rem;}
.renewal-history-item .rh-code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.75rem;color:var(--danger);background:rgba(220,38,38,.08);padding:.15rem .5rem;border-radius:6px;letter-spacing:.5px;font-weight:700;display:inline-block;margin-top:.15rem;}
.renewal-history-item .rh-status{display:inline-flex;align-items:center;gap:.25rem;padding:.2rem .55rem;border-radius:50px;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.3px;white-space:nowrap;}
.renewal-history-item .rh-status.confirmed{background:rgba(22,163,74,.15);color:var(--success);}
.renewal-history-item .rh-status.user_paid{background:rgba(245,158,11,.18);color:#d97706;}
.renewal-history-item .rh-status.pending{background:rgba(37,99,235,.15);color:#2563eb;}
.renewal-history-item .rh-status.cancelled{background:rgba(148,163,184,.15);color:var(--text-3);}
.renewal-history-item .rh-status.rejected{background:rgba(220,38,38,.15);color:var(--danger);}
.renewal-history-item .rh-foot{display:flex;justify-content:space-between;align-items:center;gap:.5rem;flex-wrap:wrap;padding-top:.4rem;border-top:1px solid var(--border);font-size:.72rem;color:var(--text-3);}
.renewal-history-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:.5rem;padding:.75rem;background:var(--surface-2);border-radius:10px;border:1px solid var(--border);margin-bottom:1rem;}
.renewal-history-stats .rhs-item{text-align:center;}
.renewal-history-stats .rhs-label{font-size:.7rem;color:var(--text-3);text-transform:uppercase;font-weight:700;letter-spacing:.3px;}
.renewal-history-stats .rhs-value{font-size:1.1rem;font-weight:900;color:var(--primary);line-height:1.2;margin-top:.15rem;}
.renewal-history-stats .rhs-value.amount{color:var(--success);}
.admin-renewal-history-list{max-height:480px;overflow-y:auto;padding-right:.25rem;}
.admin-renewals-tabs{display:flex;gap:.4rem;margin-bottom:.75rem;flex-wrap:wrap;}

/* ============ ADMIN PERMISSIONS ============ */
.permission-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(4px);z-index:4000;display:none;align-items:center;justify-content:center;padding:1rem;animation:fadeIn .2s;}
.permission-modal.show{display:flex}
.permission-box{background:var(--surface);border-radius:20px;width:100%;max-width:520px;box-shadow:0 20px 60px rgba(0,0,0,.4);padding:1.5rem;position:relative;animation:slideUp .3s cubic-bezier(.34,1.56,.64,1);max-height:calc(100vh - 2rem);overflow-y:auto;}
.permission-box h2{font-size:1.1rem;color:var(--text);font-weight:700;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;}
.permission-box h2 i{color:#06b6d4;}
.permission-list{display:flex;flex-direction:column;gap:.5rem;margin-bottom:1.25rem;}
.permission-item{display:flex;align-items:center;justify-content:space-between;gap:.75rem;padding:.7rem .85rem;border-radius:10px;background:var(--surface-2);border:1px solid var(--border);transition:.15s;}
.permission-item:hover{border-color:#06b6d4}
.permission-item .pi-info{flex:1;min-width:0;}
.permission-item .pi-name{font-weight:700;font-size:.85rem;color:var(--text);margin-bottom:.1rem;}
.permission-item .pi-desc{font-size:.72rem;color:var(--text-3);line-height:1.4;}
.permission-item .pi-toggle{position:relative;width:44px;height:24px;flex-shrink:0;}
.permission-item .pi-toggle input{opacity:0;width:0;height:0;position:absolute;}
.permission-item .pi-slider{position:absolute;inset:0;background:var(--border);border-radius:50px;cursor:pointer;transition:.3s;}
.permission-item .pi-slider::before{content:'';position:absolute;width:18px;height:18px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.3s;box-shadow:0 1px 3px rgba(0,0,0,.2);}
.permission-item .pi-toggle input:checked + .pi-slider{background:linear-gradient(135deg,#06b6d4,#0891b2);}
.permission-item .pi-toggle input:checked + .pi-slider::before{transform:translateX(20px);}
.permission-item .pi-toggle input:disabled + .pi-slider{opacity:.5;cursor:not-allowed;}
.permission-note{padding:.65rem .85rem;border-radius:10px;background:rgba(6,182,212,.08);border:1px solid rgba(6,182,212,.25);font-size:.78rem;color:var(--text-2);line-height:1.5;display:flex;align-items:flex-start;gap:.5rem;margin-bottom:1rem;}
.permission-note i{color:#06b6d4;margin-top:.1rem;flex-shrink:0;}

/* ============ RESPONSIVE ============ */
@media (max-width:600px){
    .admin-section-head{padding:.75rem .85rem;}
    .admin-section-head .ash-title{font-size:.85rem;}
    .admin-section-head .ash-icon{width:28px;height:28px;font-size:.78rem;}
    .admin-section-body > .admin-section-inner{padding:.75rem;}
    .admin-toggle-btn{width:32px;height:32px;}
}

/* ═══════════════════════════════════════════════════════════════
   FIX: Dropdown user menu không bấm được trên desktop
   ═══════════════════════════════════════════════════════════════ */
@media (min-width:769px){
    .header-inner{
        overflow:visible !important;
    }
    .sticky-top{
        overflow:visible !important;
    }
    .header-actions{
        z-index:500 !important;
    }
    .user-menu{
        position:relative;
        z-index:501 !important;
    }
    .user-dropdown{
        z-index:1000 !important;
    }
}

/* ═══════════════════════════════════════════════════════════════
   🆕 USER DATA CHANGED TOAST
   ═══════════════════════════════════════════════════════════════ */
.user-changed-toast {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(-100px);
    padding: .9rem 1.5rem;
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: #fff;
    border-radius: 50px;
    font-size: .9rem;
    font-weight: 800;
    font-family: inherit;
    box-shadow: 0 12px 40px rgba(22, 163, 74, .5), 0 4px 12px rgba(0, 0, 0, .15);
    z-index: 10000;
    opacity: 0;
    transition: opacity .3s ease, transform .4s cubic-bezier(.34, 1.56, .64, 1);
    pointer-events: none;
    display: flex;
    align-items: center;
    gap: .6rem;
    max-width: 90vw;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.user-changed-toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}
.user-changed-toast i {
    font-size: 1.2rem;
    animation: successPop .5s cubic-bezier(.34, 1.56, .64, 1);
}
.user-changed-toast.expired {
    background: linear-gradient(135deg, #dc2626, #b91c1c);
    box-shadow: 0 12px 40px rgba(220, 38, 38, .5), 0 4px 12px rgba(0, 0, 0, .15);
}
.user-changed-toast.info {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    box-shadow: 0 12px 40px rgba(124, 58, 237, .5), 0 4px 12px rgba(0, 0, 0, .15);
}
"""


# ═══════════════════════════════════════════════════════════════
# HTML
# ═══════════════════════════════════════════════════════════════
def build_accounts_html():
    return r"""
<div class="login-modal" id="loginModal">
    <div class="login-box">
        <button class="login-close" id="loginClose"><i class="fas fa-times"></i></button>
        <div class="login-logo"><i class="fas fa-gem"></i></div>
        <h2>Đăng nhập để mở khóa</h2>
        <p>Đăng nhập bằng Google để sử dụng <b>toàn bộ câu</b>, tất cả bộ lọc HSK1-6, chủ đề đầy đủ, luyện viết không giới hạn và nhiều tính năng khác.</p>
        <button class="btn-google" id="googleLoginBtn">
            <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="Google">
            Đăng nhập bằng Google
        </button>
        <div class="login-error" id="loginError"></div>
        <div class="login-footer">
            <i class="fas fa-shield-alt"></i> Tài khoản mới được <b>tặng miễn phí <span id="trialDaysText">3</span> ngày</b> dùng thử.
        </div>
    </div>
</div>

<div class="edit-modal" id="changeNameModal">
    <div class="edit-box">
        <button class="edit-close" id="changeNameClose"><i class="fas fa-times"></i></button>
        <h2><i class="fas fa-user-edit"></i> Đổi tên hiển thị</h2>
        <div class="edit-user-info">
            <div class="eu-name" id="changeNameCurrent">-</div>
            <div class="eu-email" id="changeNameEmail">-</div>
        </div>
        <div class="form-group">
            <label>Tên mới</label>
            <input type="text" id="changeNameInput" placeholder="Nhập tên mới..." maxlength="50">
        </div>
        <div class="form-actions">
            <button class="btn" id="changeNameCancel">Hủy</button>
            <button class="btn primary" id="changeNameConfirm"><i class="fas fa-check"></i> Lưu</button>
        </div>
    </div>
</div>

<div class="edit-modal" id="editExpiryModal">
    <div class="edit-box">
        <button class="edit-close" id="editExpiryClose"><i class="fas fa-times"></i></button>
        <h2><i class="fas fa-calendar-edit"></i> Chỉnh hạn sử dụng</h2>
        <div class="edit-user-info">
            <div class="eu-name" id="editExpiryName">-</div>
            <div class="eu-email" id="editExpiryEmail">-</div>
        </div>
        <div class="quick-expiry-btns">
            <button class="quick-expiry-btn" onclick="setQuickExpiry(7)"><i class="fas fa-calendar-plus"></i> +7 ngày</button>
            <button class="quick-expiry-btn" onclick="setQuickExpiry(30)"><i class="fas fa-calendar-plus"></i> +30 ngày</button>
            <button class="quick-expiry-btn" onclick="setQuickExpiry(90)"><i class="fas fa-calendar-plus"></i> +90 ngày</button>
            <button class="quick-expiry-btn" onclick="setQuickExpiry(180)"><i class="fas fa-calendar-plus"></i> +6 tháng</button>
            <button class="quick-expiry-btn" onclick="setQuickExpiry(365)"><i class="fas fa-calendar-plus"></i> +1 năm</button>
            <button class="quick-expiry-btn danger" onclick="setQuickExpiryPermanent()"><i class="fas fa-infinity"></i> Vĩnh viễn</button>
        </div>
        <div class="form-group">
            <label>Hoặc chọn ngày cụ thể</label>
            <input type="date" id="editExpiryInput">
        </div>
        <div class="form-actions">
            <button class="btn" id="editExpiryCancel">Hủy</button>
            <button class="btn primary" id="editExpiryConfirm"><i class="fas fa-check"></i> Lưu</button>
        </div>
    </div>
</div>

<div class="renewal-modal" id="renewalModal">
    <div class="renewal-box">
        <div class="renewal-header">
            <div>
                <h2><i class="fas fa-gem"></i> Gia hạn tài khoản</h2>
                <div class="subtitle">Chọn gói phù hợp và thanh toán</div>
            </div>
            <button class="renewal-close" id="renewalClose"><i class="fas fa-times"></i></button>
        </div>
        <div class="renewal-body" id="renewalBody"></div>
    </div>
</div>

<div class="edit-modal" id="renewalHistoryModal">
    <div class="edit-box" style="max-width:600px">
        <button class="edit-close" id="renewalHistoryClose"><i class="fas fa-times"></i></button>
        <h2><i class="fas fa-history"></i> Lịch sử gia hạn</h2>
        <div id="renewalHistoryList" style="max-height:65vh;overflow-y:auto;margin-top:1rem;">
            <div class="no-data" style="padding:2rem 1rem;text-align:center;color:var(--text-3)">
                <i class="fas fa-spinner fa-pulse"></i> Đang tải...
            </div>
        </div>
    </div>
</div>

<div class="import-modal" id="importModal">
    <div class="import-box">
        <div class="import-header">
            <h2><i class="fas fa-file-import"></i> Import danh sách user</h2>
            <button class="admin-close" id="importClose"><i class="fas fa-times"></i></button>
        </div>
        <div class="import-body">
            <div class="import-summary" id="importSummary"></div>
            <div class="import-preview-wrap">
                <table class="import-table">
                    <thead>
                        <tr>
                            <th style="width:45px">#</th>
                            <th>Email</th>
                            <th>Tên</th>
                            <th style="width:80px">Vai trò</th>
                            <th style="width:110px">Hạn dùng</th>
                            <th style="width:130px">Trạng thái</th>
                        </tr>
                    </thead>
                    <tbody id="importTableBody"></tbody>
                </table>
            </div>
            <div class="import-options">
                <label><input type="checkbox" id="importSkipDuplicates"> Bỏ qua user đã tồn tại (không update)</label>
                <label><input type="checkbox" id="importSkipInvalid" checked> Bỏ qua dòng không hợp lệ</label>
            </div>
            <div class="import-info">
                <i class="fas fa-info-circle"></i>
                <div>
                    File Excel cần có cột: <b>email</b> (bắt buộc), <b>name</b> (tùy chọn), <b>expiresAt</b> (tùy chọn).
                    <br>• <b>email</b>: bắt buộc, phải hợp lệ
                    <br>• <b>name</b>: nếu thiếu sẽ lấy phần trước @ của email
                    <br>• <b>expiresAt</b>: định dạng <b>YYYY-MM-DD</b>, để trống = vĩnh viễn
                    <br><b>⚠️ Lưu ý:</b> Chỉ import <b>user</b>, KHÔNG import admin.
                </div>
            </div>
        </div>
        <div class="import-footer">
            <button class="btn" id="importCancelBtn">Hủy</button>
            <button class="btn primary" id="importConfirmBtn"><i class="fas fa-check"></i> Import <span id="importCount">0</span> user</button>
        </div>
    </div>
</div>

<div class="permission-modal" id="permissionModal">
    <div class="permission-box">
        <button class="edit-close" id="permissionClose"><i class="fas fa-times"></i></button>
        <h2><i class="fas fa-user-shield"></i> Phân quyền Admin</h2>
        <div class="edit-user-info">
            <div class="eu-name" id="permissionName">-</div>
            <div class="eu-email" id="permissionEmail">-</div>
        </div>
        <div class="permission-note">
            <i class="fas fa-info-circle"></i>
            <div>Admin thường <b>mặc định có toàn quyền</b> (xem/thêm/xóa user, chỉnh hạn, duyệt gia hạn, import/export, xem log). Chỉ <b>Quản lý Admin</b> là dành riêng cho Super Admin.</div>
        </div>
        <div class="permission-list" id="permissionList"></div>
        <div class="form-actions">
            <button class="btn" id="permissionCancel">Hủy</button>
            <button class="btn primary" id="permissionSave"><i class="fas fa-check"></i> Lưu quyền</button>
        </div>
    </div>
</div>

<div class="admin-modal" id="adminModal">
    <div class="admin-box">
        <div class="admin-header">
            <h2><i class="fas fa-shield-alt"></i> Quản lý tài khoản</h2>
            <div class="admin-header-actions">
                <button class="btn" id="exportExcelBtn" title="Xuất danh sách USER ra Excel"><i class="fas fa-file-export"></i> Export</button>
                <button class="btn" id="importExcelBtn" title="Import từ Excel (chỉ import user)"><i class="fas fa-file-import"></i> Import</button>
                <input type="file" id="importFileInput" accept=".xlsx,.xls,.csv" style="display:none">
                <button class="btn" id="refreshUsersBtn" title="Làm mới"><i class="fas fa-sync-alt"></i></button>
                <button class="admin-close" id="adminClose"><i class="fas fa-times"></i></button>
            </div>
        </div>
        <div class="admin-body">

            <div class="admin-summary-bar" id="adminSummaryBar">
                <div class="summary-item">
                    <i class="fas fa-users" style="color:#3b82f6"></i>
                    <span class="summary-label">Tổng User:</span>
                    <span class="summary-value" id="summaryTotalUsers">0</span>
                </div>
                <div class="summary-item" id="summaryAdminItem" style="display:none">
                    <i class="fas fa-shield-alt" style="color:#f59e0b"></i>
                    <span class="summary-label">Tổng Admin:</span>
                    <span class="summary-value" id="summaryTotalAdmins">0</span>
                </div>
            </div>

            <div class="admin-search-wrap">
                <i class="fas fa-search"></i>
                <input type="text" class="admin-search" id="adminSearchInput" placeholder="Tìm kiếm theo email hoặc tên...">
                <button class="admin-search-clear" id="adminSearchClear"><i class="fas fa-times"></i></button>
            </div>

            <div class="admin-filter-row" id="adminFilterRow">
                <button class="admin-filter-btn active" data-filter="all"><i class="fas fa-users"></i> Tất cả <span class="count" id="filterCountAll">0</span></button>
                <button class="admin-filter-btn" data-filter="user"><i class="fas fa-user"></i> User <span class="count" id="filterCountUser">0</span></button>
                <button class="admin-filter-btn" data-filter="admin"><i class="fas fa-shield-alt"></i> Admin <span class="count" id="filterCountAdmin">0</span></button>
                <button class="admin-filter-btn" data-filter="trial"><i class="fas fa-gift"></i> Trial <span class="count" id="filterCountTrial">0</span></button>
                <button class="admin-filter-btn" data-filter="expiring"><i class="fas fa-clock"></i> Sắp hết hạn <span class="count" id="filterCountExpiring">0</span></button>
                <button class="admin-filter-btn" data-filter="expired"><i class="fas fa-exclamation-circle"></i> Hết hạn <span class="count" id="filterCountExpired">0</span></button>
                <button class="admin-filter-btn" data-filter="permanent"><i class="fas fa-crown"></i> Vĩnh viễn <span class="count" id="filterCountPermanent">0</span></button>
            </div>

            <div class="admin-section" id="adminRenewalsSection">
                <div class="admin-section-head">
                    <div class="ash-left">
                        <div class="ash-icon amber"><i class="fas fa-clock"></i></div>
                        <div class="ash-text">
                            <div class="ash-title"><span>Yêu cầu gia hạn</span></div>
                            <div class="ash-subtitle">
                                <span class="chip warn"><i class="fas fa-hourglass-half"></i> <span id="pendingRenewalsBadge">0</span> chờ</span>
                                <span class="chip ok"><i class="fas fa-check-circle"></i> <span id="confirmedRenewalsBadge">0</span> đã xác nhận</span>
                            </div>
                        </div>
                    </div>
                    <div class="ash-actions">
                        <button class="btn" id="refreshRenewalsBtn" style="padding:.4rem .7rem;font-size:.75rem" title="Làm mới"><i class="fas fa-sync-alt"></i></button>
                        <button class="admin-toggle-btn active" id="toggleRenewalsBtn" title="Ẩn khung yêu cầu gia hạn"><i class="fas fa-eye"></i></button>
                    </div>
                </div>
                <div class="admin-section-body">
                    <div class="admin-section-inner">
                        <div class="admin-renewals-tabs">
                            <button class="admin-filter-btn active" data-renewal-tab="pending" onclick="setRenewalTab('pending')">
                                <i class="fas fa-hourglass-half"></i> Đang chờ <span class="count" id="pendingCountTab">0</span>
                            </button>
                            <button class="admin-filter-btn" data-renewal-tab="confirmed" onclick="setRenewalTab('confirmed')">
                                <i class="fas fa-check-circle"></i> Đã xác nhận <span class="count" id="confirmedCountTab">0</span>
                            </button>
                        </div>
                        <div class="renewals-list" id="renewalsList">
                            <div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="admin-section" id="adminUsersSection">
                <div class="admin-section-head">
                    <div class="ash-left">
                        <div class="ash-icon"><i class="fas fa-users"></i></div>
                        <div class="ash-text">
                            <div class="ash-title"><span>Danh sách tài khoản</span></div>
                            <div class="ash-subtitle">
                                <span class="chip primary"><i class="fas fa-user"></i> <span id="adminUserCount">0</span> user</span>
                            </div>
                        </div>
                    </div>
                    <div class="ash-actions">
                        <button class="btn-add" id="showAddUserBtn"><i class="fas fa-plus"></i> Thêm</button>
                        <button class="admin-toggle-btn active" id="toggleUsersBtn" title="Ẩn danh sách tài khoản"><i class="fas fa-eye"></i></button>
                    </div>
                </div>
                <div class="admin-section-body">
                    <div class="admin-section-inner">
                        <div class="add-user-form" id="addUserForm">
                            <h3>Thêm tài khoản mới</h3>
                            <div class="form-group">
                                <label>Email Google</label>
                                <input type="email" id="newUserEmail" placeholder="user@gmail.com">
                            </div>
                            <div class="form-group">
                                <label>Tên hiển thị</label>
                                <input type="text" id="newUserName" placeholder="Nguyễn Văn A">
                            </div>
                            <div class="form-group">
                                <label>Vai trò</label>
                                <select id="newUserRole">
                                    <option value="user">User (chỉ học)</option>
                                    <option value="admin">Admin (quản trị)</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label>Hạn sử dụng (để trống = vĩnh viễn)</label>
                                <input type="date" id="newUserExpires">
                            </div>
                            <div class="form-actions">
                                <button class="btn" id="cancelAddUser">Hủy</button>
                                <button class="btn primary" id="confirmAddUser"><i class="fas fa-check"></i> Thêm</button>
                            </div>
                        </div>
                        <div class="user-list" id="userList">
                            <div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="admin-section" id="adminLogsSection">
                <div class="admin-section-head">
                    <div class="ash-left">
                        <div class="ash-icon slate"><i class="fas fa-history"></i></div>
                        <div class="ash-text">
                            <div class="ash-title"><span>Lịch sử đăng nhập</span></div>
                            <div class="ash-subtitle">
                                <span class="chip"><i class="fas fa-list"></i> 30 gần nhất</span>
                            </div>
                        </div>
                    </div>
                    <div class="ash-actions">
                        <button class="admin-toggle-btn active" id="toggleLogsBtn" title="Ẩn lịch sử đăng nhập"><i class="fas fa-eye"></i></button>
                    </div>
                </div>
                <div class="admin-section-body">
                    <div class="admin-section-inner">
                        <div class="logs-list" id="logsList">
                            <div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="admin-section collapsed" id="adminRenewalHistorySection">
                <div class="admin-section-head">
                    <div class="ash-left">
                        <div class="ash-icon violet"><i class="fas fa-receipt"></i></div>
                        <div class="ash-text">
                            <div class="ash-title"><span>Lịch sử gia hạn</span></div>
                            <div class="ash-subtitle">
                                <span class="chip"><i class="fas fa-database"></i> Tất cả giao dịch</span>
                            </div>
                        </div>
                    </div>
                    <div class="ash-actions">
                        <button class="btn" id="refreshRenewalHistoryBtn" style="padding:.4rem .7rem;font-size:.75rem" title="Làm mới"><i class="fas fa-sync-alt"></i></button>
                        <button class="admin-toggle-btn" id="toggleRenewalHistoryBtn" title="Hiện lịch sử gia hạn"><i class="fas fa-eye-slash"></i></button>
                    </div>
                </div>
                <div class="admin-section-body">
                    <div class="admin-section-inner">
                        <div class="admin-renewal-history-list" id="adminRenewalHistoryList">
                            <div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 👥 USER ONLINE — main.py tự chèn qua placeholder -->
            <!-- __ADMIN_ONLINE_SECTION__ -->

            <!-- 📊 QUOTA DASHBOARD — main.py tự chèn qua placeholder -->
            <!-- __ADMIN_QUOTA_SECTION__ -->

        </div>
    </div>
</div>
"""


def build_user_dropdown_html():
    return r"""
<div class="user-dropdown show" id="userDropdown">
    <div class="user-info">
        <div class="name" id="userName">-</div>
        <div class="email" id="userEmail">-</div>
        <span class="role" id="userRole">user</span>
    </div>
    <div class="user-details" id="userDetails" style="display:none">
        <div class="detail-row" id="expiryRow">
            <div class="detail-icon" id="expiryIconWrap">
                <i class="fas fa-calendar-check" id="expiryIcon"></i>
            </div>
            <div class="detail-content">
                <div class="detail-label">Hạn sử dụng</div>
                <div class="detail-value" id="expiryValue">-</div>
                <div class="detail-sub" id="expirySub"></div>
            </div>
        </div>
        <div class="detail-progress" id="expiryProgressWrap" style="display:none">
            <div class="progress-track">
                <div class="progress-bar" id="expiryProgressBar"></div>
            </div>
        </div>
    </div>
    <button class="dropdown-item" id="changeNameBtn">
        <i class="fas fa-user-edit"></i> Đổi tên hiển thị
    </button>
    <button class="dropdown-item" id="openAdminBtn" style="display:none">
        <i class="fas fa-shield-alt"></i> Quản lý tài khoản
    </button>
    <button class="dropdown-item" id="renewalHistoryBtn">
        <i class="fas fa-history"></i> Lịch sử gia hạn
    </button>

    <!-- 💬 Preview chat gần nhất -->
    <div class="dropdown-chat-preview" id="dropdownChatPreview" onclick="window.__chatOpen && window.__chatOpen()">
        <div class="dcp-head">
            <div class="dcp-title">
                <i class="fas fa-comments"></i> Tin nhắn gần nhất
                <span class="dcp-badge" id="dcpBadge" style="display:none">0</span>
            </div>
            <div class="dcp-time" id="dcpTime"></div>
        </div>
        <div class="dcp-msg" id="dcpMsg">Chưa có tin nhắn. Bấm để bắt đầu chat với Admin.</div>
    </div>

    <!-- 💬 Nút Chat -->
    <button class="dropdown-item" id="chatSupportBtn" onclick="window.__chatOpen && window.__chatOpen()">
        <i class="fas fa-comments" style="color:#4f46e5;"></i> Chat với Admin
    </button>

    <button class="dropdown-renew" id="dropdownRenewBtn" style="display:none">
        <i class="fas fa-gem"></i>
        <span>Gia hạn tài khoản</span>
        <span class="renew-badge">VIP</span>
    </button>
    <button class="dropdown-renew dropdown-forever" id="dropdownForeverBtn" style="display:none">
        <i class="fas fa-crown"></i>
        <span>Sở hữu vĩnh viễn</span>
        <span class="renew-badge" style="background:linear-gradient(135deg,#dc2626,#b91c1c)">HOT</span>
    </button>
    <button class="dropdown-item danger" id="logoutBtn">
        <i class="fas fa-sign-out-alt"></i> Đăng xuất
    </button>
</div>
"""


def build_renewal_html():
    return ""


# ═══════════════════════════════════════════════════════════════
# JS
# ═══════════════════════════════════════════════════════════════
def build_accounts_js(config):
    js = r"""
/* ============ CONFIG INJECTED ============ */
var TRIAL_DAYS = __TRIAL_DAYS__;
var TRIAL_MAX_QUESTIONS = __TRIAL_MAX_QUESTIONS__;
var TRIAL_MAX_HSK = __TRIAL_MAX_HSK__;
var TRIAL_UNLIMITED_WRITING = __TRIAL_UNLIMITED_WRITING__;
var BANK_CONFIG = __BANK_CONFIG__;
var PACKAGES = __PACKAGES__;
var RENEWAL_SUPPORT_ZALO = "__RENEWAL_SUPPORT_ZALO__";

/* ⭐ TELEGRAM CONFIG */
var TELEGRAM_BOT_TOKEN = "__TELEGRAM_BOT_TOKEN__";
var TELEGRAM_CHAT_ID   = "__TELEGRAM_CHAT_ID__";

/* ============ STATE ============ */
var currentUser = null;
var isDemo = true;
var auth, db;
var usersCache = [];
var lastLoginMap = {};
var importRows = [];
var editingEmail = null;
var editingExpiryEmail = null;
var appInitialized = false;
var renewalSelectedPkg = null;
var renewalCurrentReq = null;
var renewalListener = null;

var userWatcher = null;

/* Search & Filter state */
var adminSearchQuery = '';
var adminCurrentFilter = 'all';
var editingPermissionEmail = null;

/* Renewals tab state */
var renewalTab = 'pending';
var pendingRenewalsData = [];
var confirmedRenewalsData = [];

/* Admin permissions definition */
var ADMIN_PERMISSIONS = [
    { key: 'canViewUsers',      name: 'Xem danh sách user',   desc: 'Xem thông tin tất cả tài khoản user' },
    { key: 'canEditExpiry',     name: 'Chỉnh hạn sử dụng',    desc: 'Thay đổi ngày hết hạn của user' },
    { key: 'canRenew',          name: 'Duyệt gia hạn',        desc: 'Xác nhận/từ chối yêu cầu gia hạn của user' },
    { key: 'canAddUser',        name: 'Thêm user mới',        desc: 'Tạo tài khoản user mới' },
    { key: 'canDeleteUser',     name: 'Xóa user',             desc: 'Xóa tài khoản user khỏi hệ thống' },
    { key: 'canImportExport',   name: 'Import/Export Excel',  desc: 'Nhập/xuất danh sách user' },
    { key: 'canViewLogs',       name: 'Xem lịch sử đăng nhập', desc: 'Xem log đăng nhập của user' },
    { key: 'canManageAdmin',    name: 'Quản lý Admin',        desc: 'Thêm/xóa/phân quyền admin khác (chỉ Super Admin)' }
];

var DEFAULT_ADMIN_PERMS = {
    canViewUsers: true,
    canEditExpiry: true,
    canRenew: true,
    canAddUser: true,
    canDeleteUser: true,
    canImportExport: true,
    canViewLogs: true,
    canManageAdmin: false
};

/* ============ HELPERS ============ */
function escapeHtml(s) {
    if (s == null) return '';
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}
function escapeJs(s) {
    if (s == null) return '';
    return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/"/g,'\\"');
}
function isSuperAdmin() {
    if (!currentUser || currentUser.role !== 'admin') return false;
    var email = (currentUser.email || '').toLowerCase().trim();
    return email === SUPER_ADMIN.toLowerCase().trim();
}
function isHiddenAdmin() {
    if (!currentUser || currentUser.role !== 'admin') return false;
    return !isSuperAdmin();
}
function isSubAdmin() {
    if (!currentUser || currentUser.role !== 'admin') return false;
    if (isSuperAdmin()) return false;
    return currentUser.isSubAdmin === true || currentUser.permissions !== undefined;
}
function hasPermission(permKey) {
    if (!currentUser || currentUser.role !== 'admin') return false;
    if (isSuperAdmin()) return true;
    var perms = currentUser.permissions || {};
    if (perms[permKey] === undefined) {
        return DEFAULT_ADMIN_PERMS[permKey] === true;
    }
    return perms[permKey] === true;
}

function showUserChangedToast(message, type) {
    var old = document.getElementById('userChangedToast');
    if (old) old.remove();

    var toast = document.createElement('div');
    toast.id = 'userChangedToast';
    toast.className = 'user-changed-toast' + (type ? ' ' + type : '');
    toast.innerHTML = '<i class="fas fa-' +
        (type === 'expired' ? 'exclamation-triangle' :
         type === 'info' ? 'info-circle' : 'check-circle') +
        '"></i><span>' + message + '</span>';
    document.body.appendChild(toast);

    requestAnimationFrame(function() {
        toast.classList.add('show');
    });

    setTimeout(function() {
        toast.classList.remove('show');
        setTimeout(function() { if (toast.parentNode) toast.remove(); }, 400);
    }, 4000);
}

/* ============ TIER STATE ============ */
function publishTierState() {
    if (!currentUser) {
        window.APP_TIER = 'demo';
        window.APP_LIMITS = {
            maxQuestions: (typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 25,
            maxHSK: (typeof DEMO_HSK_MAX === 'number') ? DEMO_HSK_MAX : 3,
            unlimitedWriting: false, isTrial: false, email: null
        };
        _refreshDatasetLockUI();
        return;
    }
    if (currentUser.role === 'admin') {
        window.APP_TIER = 'active';
        window.APP_LIMITS = { maxQuestions: Infinity, maxHSK: 6, unlimitedWriting: true, isTrial: false, email: currentUser.email };
        _refreshDatasetLockUI();
        return;
    }
    var tier = currentUser.tier || 'active';
    if (tier === 'trial') {
        window.APP_TIER = 'trial';
        window.APP_LIMITS = {
            maxQuestions: currentUser.trialMaxQuestions || TRIAL_MAX_QUESTIONS || 50,
            maxHSK: currentUser.trialMaxHSK || TRIAL_MAX_HSK || 5,
            unlimitedWriting: true, isTrial: true, email: currentUser.email
        };
    } else if (tier === 'expired') {
        window.APP_TIER = 'expired';
        window.APP_LIMITS = {
            maxQuestions: (typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 25,
            maxHSK: (typeof DEMO_HSK_MAX === 'number') ? DEMO_HSK_MAX : 3,
            unlimitedWriting: false, isTrial: false, email: currentUser.email
        };
    } else {
        window.APP_TIER = 'active';
        window.APP_LIMITS = { maxQuestions: Infinity, maxHSK: 6, unlimitedWriting: true, isTrial: false, email: currentUser.email };
    }
    _refreshDatasetLockUI();
}

function _refreshDatasetLockUI() {
    if (typeof initDatasetSelector === 'function') {
        try { initDatasetSelector(); } catch(e) {}
    }
    if (typeof pfBuildDatasetSelect === 'function') {
        try { pfBuildDatasetSelect(); } catch(e) {}
    }
    if (typeof CURRENT_DATASET !== 'undefined' && CURRENT_DATASET !== 'tonghop') {
        var canAccess = (window.APP_TIER === 'active');
        if (!canAccess) {
            try {
                if (typeof window.__switchRawData === 'function') {
                    window.__switchRawData('tonghop');
                }
                if (typeof applyFilter === 'function') applyFilter();
                if (typeof markCurrentDatasetActive === 'function') {
                    markCurrentDatasetActive();
                }
            } catch(e) {}
        }
    }
}

/* ============ FIREBASE INIT ============ */
try {
    firebase.initializeApp(FIREBASE_CONFIG);
    auth = firebase.auth();
    db = firebase.firestore();
    auth.onAuthStateChanged(handleAuthChange);
} catch(e) {
    console.error('Firebase init error:', e);
    enterDemoMode();
}

/* ═══════════════════════════════════════════════════════════════
   👥 RTDB PRESENCE — Track user online MIỄN PHÍ
   ═══════════════════════════════════════════════════════════════ */
function startRTDBPresence() {
    if (!currentUser || !currentUser.email) return;
    if (typeof firebase === 'undefined' || typeof firebase.database !== 'function') {
        console.warn('⚠️ RTDB chưa bật — bỏ qua presence');
        return;
    }

    try {
        var emailKey = encodeURIComponent(currentUser.email.toLowerCase());
        var ref = firebase.database().ref('presence/' + emailKey);

        ref.onDisconnect().remove();

        ref.set({
            at: Date.now(),
            email: currentUser.email,
            name: currentUser.name || currentUser.email.split('@')[0],
            role: currentUser.role || 'user'
        }).catch(function(e) { console.warn('RTDB presence set:', e); });

        if (window.__presenceTimer) clearInterval(window.__presenceTimer);
        window.__presenceTimer = setInterval(function() {
            if (document.hidden) return;
            if (!currentUser) return;
            ref.update({ at: Date.now() }).catch(function(){});
        }, 120000);

        if (!window.__presenceFocusHandler) {
            window.__presenceFocusHandler = function() {
                if (!document.hidden && currentUser && window.__presenceRef) {
                    window.__presenceRef.update({ at: Date.now() }).catch(function(){});
                }
            };
            window.addEventListener('focus', window.__presenceFocusHandler);
        }

        window.__presenceRef = ref;
        console.log('👥 RTDB presence started for:', currentUser.email);
    } catch(e) {
        console.warn('startRTDBPresence error:', e);
    }
}

function stopRTDBPresence() {
    if (window.__presenceRef) {
        try { window.__presenceRef.remove(); } catch(e) {}
        window.__presenceRef = null;
    }
    if (window.__presenceTimer) {
        clearInterval(window.__presenceTimer);
        window.__presenceTimer = null;
    }
    console.log('👥 RTDB presence stopped');
}

/* ============ AUTH STATE ============ */
async function handleAuthChange(user) {
    if (!user) {
        resetAppState();

        publishTierState();
        applyUserUI();
        enterDemoMode();

        if (typeof buildFilters === 'function') buildFilters();
        if (typeof applyFilter === 'function') applyFilter();
        if (typeof updateResultCount === 'function') updateResultCount();
        if (typeof markCurrentDatasetActive === 'function') markCurrentDatasetActive();

        if (typeof maybeShowOnboarding === 'function') {
            setTimeout(maybeShowOnboarding, 300);
        }
        if (typeof favUpdateLockState === 'function') favUpdateLockState();
        return;
    }

    var email = (user.email || '').toLowerCase();
    var cacheKey = 'user_cache_' + email;
    var cached = null;
    try { cached = JSON.parse(localStorage.getItem(cacheKey) || 'null'); } catch(e) {}

    if (cached && cached.expires > Date.now() && cached.data) {
        currentUser = cached.data;
        isDemo = false;

        if (currentUser.role !== 'admin' && !currentUser.isPermanent && currentUser.expiresAt) {
            var expDate = getExpiryDate(currentUser.expiresAt);
            if (expDate && !isNaN(expDate.getTime())) {
                var isExpired = expDate.getTime() < Date.now();
                currentUser.isExpiredOnly = isExpired;
                if (isExpired) currentUser.tier = 'expired';
            }
        }

        /* ═══ CHECK DEVICE LIMIT ═══ */
        try {
            if (window.__dvlCheckAndRegister && currentUser && currentUser.email) {
                var _dvlResult = await window.__dvlCheckAndRegister(currentUser.email);

                if (_dvlResult && _dvlResult.needsVerify) {
                    var _vEmail = currentUser.email;
                    var _vExpire = _dvlResult.expireAt || (Date.now() + 300000);

                    if (window.__dvlSendVerifyEmail) {
                        window.__dvlSendVerifyEmail(_vEmail, _dvlResult.token);
                    }
                    if (window.__dvlShowVerifyModal) {
                        window.__dvlShowVerifyModal(_vEmail, _vExpire);
                    }
                    return;
                }
            }
        } catch(_dvlErr) {
            console.warn('[DVL] Register error:', _dvlErr);
        }
        /* ═══ END CHECK DEVICE ═══ */

        publishTierState();
        applyUserUI();
        logLogin(currentUser);

        if (!appInitialized) {
            initApp();
            appInitialized = true;
        } else {
            if (typeof refreshApp === 'function') refreshApp();
        }

        if (typeof buildFilters === 'function') buildFilters();
        if (typeof applyFilter === 'function') applyFilter();
        if (typeof updateResultCount === 'function') updateResultCount();
        if (typeof markCurrentDatasetActive === 'function') markCurrentDatasetActive();
        if (typeof favUpdateLockState === 'function') favUpdateLockState();

        if (typeof window.removeOnboardingBannerIfNeeded === 'function') {
            window.removeOnboardingBannerIfNeeded();
        }

        watchCurrentUser();
        startRTDBPresence();
        setTimeout(function() { verifyCurrentUserBackground(); }, 2000);
        return;
    }

    try {
        var docRef = db.collection('allowed_users').doc(email);
        var doc = await docRef.get({ source: 'server' });

        if (!doc.exists) {
            var registered = await grantTrialIfNew(user, null);
            if (registered) {
                doc = await docRef.get({ source: 'server' });
                setTimeout(function() {
                    var trialDays = (typeof TRIAL_DAYS === 'number' && TRIAL_DAYS > 0) ? TRIAL_DAYS : 3;
                    var trialDate = new Date(Date.now() + trialDays * 86400000);
                    alert('🎉 Chào mừng bạn!\n\n' +
                          '💎 Bạn được tặng MIỄN PHÍ ' + trialDays + ' ngày sử dụng.\n\n' +
                          '📚 Trong thời gian dùng thử:\n' +
                          '   • ' + (TRIAL_MAX_QUESTIONS || 50) + ' câu đầu tiên\n' +
                          '   • HSK1-' + (TRIAL_MAX_HSK || 5) + '\n' +
                          '   • Nghe + Luyện viết KHÔNG giới hạn\n\n' +
                          '📅 Hạn dùng: ' + trialDate.toLocaleDateString('vi-VN') + '\n\n' +
                          'Chúc bạn học tốt! 🎓');
                }, 600);
            } else {
                await auth.signOut();
                showLoginError('Tài khoản <b>' + email + '</b> chưa được cấp quyền.');
                enterDemoMode();
                return;
            }
        }

        var data = doc.data() || {};

        var userTier = 'active';
        if (data.role === 'admin') userTier = 'active';
        else if (data.tier === 'trial' || data.isTrial === true) userTier = 'trial';

        var userData = {
            email: email,
            name: data.name || user.displayName || email.split('@')[0],
            role: data.role || 'user',
            photo: user.photoURL || '',
            expiresAt: data.expiresAt || null,
            isTrial: data.isTrial || false,
            isExpiredOnly: false,
            isPermanent: data.isPermanent || false,
            tier: userTier,
            trialMaxQuestions: data.trialMaxQuestions || TRIAL_MAX_QUESTIONS,
            trialMaxHSK: data.trialMaxHSK || TRIAL_MAX_HSK,
            isSubAdmin: data.isSubAdmin || false,
            permissions: data.permissions || null,
            currentPackage: data.currentPackage || null,
            currentPackageDays: data.currentPackageDays || 0
        };

        currentUser = userData;

        var isExpiredUser = false;

        if (currentUser.role !== 'admin' && !currentUser.isPermanent) {
            if (currentUser.expiresAt) {
                var expDate2 = getExpiryDate(currentUser.expiresAt);
                if (expDate2 && !isNaN(expDate2.getTime())) {
                    isExpiredUser = expDate2.getTime() < Date.now();

                    if (isExpiredUser && (currentUser.isTrial || currentUser.tier === 'trial')) {
                        try {
                            db.collection('allowed_users').doc(email).update({
                                tier: 'expired',
                                isTrial: false,
                                expiredAt: firebase.firestore.FieldValue.serverTimestamp()
                            });
                        } catch(e) {}
                    }
                }
            }
        }

        if (isExpiredUser) {
            isDemo = false;
            currentUser.isExpiredOnly = true;
            currentUser.tier = 'expired';
            currentUser.isTrial = false;
        } else {
            isDemo = false;
            currentUser.isExpiredOnly = false;
        }

        try {
            localStorage.setItem(cacheKey, JSON.stringify({
                data: currentUser,
                expires: Date.now() + 12 * 60 * 60 * 1000
            }));
        } catch(e) {}

        /* ═══ CHECK DEVICE LIMIT ═══ */
        try {
            if (window.__dvlCheckAndRegister && currentUser && currentUser.email) {
                var _dvlResult2 = await window.__dvlCheckAndRegister(currentUser.email);

                if (_dvlResult2 && _dvlResult2.needsVerify) {
                    var _vEmail2 = currentUser.email;
                    var _vExpire2 = _dvlResult2.expireAt || (Date.now() + 300000);

                    if (window.__dvlSendVerifyEmail) {
                        window.__dvlSendVerifyEmail(_vEmail2, _dvlResult2.token);
                    }
                    if (window.__dvlShowVerifyModal) {
                        window.__dvlShowVerifyModal(_vEmail2, _vExpire2);
                    }
                    return;
                }
            }
        } catch(_dvlErr2) {
            console.warn('[DVL] Register error:', _dvlErr2);
        }
        /* ═══ END CHECK DEVICE ═══ */

        publishTierState();
        applyUserUI();
        logLogin(currentUser);

        if (!appInitialized) {
            initApp();
            appInitialized = true;
        } else {
            if (typeof refreshApp === 'function') refreshApp();
        }

        if (typeof buildFilters === 'function') buildFilters();
        if (typeof applyFilter === 'function') applyFilter();
        if (typeof updateResultCount === 'function') updateResultCount();
        if (typeof markCurrentDatasetActive === 'function') markCurrentDatasetActive();

        if (typeof window.removeOnboardingBannerIfNeeded === 'function') {
            window.removeOnboardingBannerIfNeeded();
        }

        if (typeof maybeShowOnboarding === 'function') {
            setTimeout(maybeShowOnboarding, 500);
        }
        if (typeof favUpdateLockState === 'function') favUpdateLockState();
        if (typeof favRefreshUI === 'function') favRefreshUI();

        watchCurrentUser();
        startRTDBPresence();

    } catch(e) {
        console.error('Auth check error:', e);
        isDemo = true;
        enterDemoMode();
    }
}
/* ═══════════════════════════════════════════════════════════════
   🔄 REALTIME WATCHER
   ═══════════════════════════════════════════════════════════════ */
function watchCurrentUser() {
    if (!currentUser || !db) return;

    if (userWatcher) {
        try { userWatcher(); } catch(e) {}
        userWatcher = null;
    }

    var email = currentUser.email;
    if (!email) return;

    console.log('👁 Watching user changes for:', email);

    userWatcher = db.collection('allowed_users').doc(email).onSnapshot(function(doc) {
        if (!doc.exists) return;
        var data = doc.data();
        if (!data) return;

        var oldExpiryMs = null;
        if (currentUser.expiresAt) {
            var od = getExpiryDate(currentUser.expiresAt);
            if (od) oldExpiryMs = od.getTime();
        }

        var newExpiryMs = null;
        if (data.expiresAt) {
            var nd = getExpiryDate(data.expiresAt);
            if (nd) newExpiryMs = nd.getTime();
        }

        var oldPermanent = currentUser.isPermanent || false;
        var newPermanent = data.isPermanent || false;
        var oldRole = currentUser.role;
        var newRole = data.role || 'user';
        var oldName = currentUser.name;
        var newName = data.name || currentUser.name;

        if (oldExpiryMs === newExpiryMs
            && oldPermanent === newPermanent
            && oldRole === newRole
            && oldName === newName) {
            return;
        }

        console.log('🔄 User data changed:', {
            oldExpiry: oldExpiryMs, newExpiry: newExpiryMs,
            oldPermanent: oldPermanent, newPermanent: newPermanent
        });

        currentUser.expiresAt = data.expiresAt || null;
        currentUser.isPermanent = newPermanent;
        currentUser.name = newName;
        currentUser.role = newRole;
        currentUser.tier = data.tier || 'active';
        if (data.permissions) currentUser.permissions = data.permissions;
        if (data.isSubAdmin !== undefined) currentUser.isSubAdmin = data.isSubAdmin;

        if (currentUser.role !== 'admin' && currentUser.expiresAt && !currentUser.isPermanent) {
            var expDate = getExpiryDate(currentUser.expiresAt);
            if (expDate && !isNaN(expDate.getTime())) {
                var isExpired = expDate.getTime() < Date.now();
                currentUser.isExpiredOnly = isExpired;
                isDemo = isExpired;
                if (isExpired) currentUser.tier = 'expired';
                else if (currentUser.tier === 'expired') currentUser.tier = 'active';
            }
        } else {
            currentUser.isExpiredOnly = false;
            isDemo = false;
        }

        try { localStorage.removeItem('user_cache_' + email); } catch(e) {}
        try {
            localStorage.setItem('user_cache_' + email, JSON.stringify({
                data: currentUser, expires: Date.now() + 12 * 60 * 60 * 1000
            }));
        } catch(e) {}

        publishTierState();
        applyUserUI();
        if (typeof refreshApp === 'function') refreshApp();

        if (typeof window.favRefreshUI === 'function') window.favRefreshUI();

        if (newPermanent && !oldPermanent) {
            showUserChangedToast('💎 Tài khoản đã được kích hoạt VĨNH VIỄN!', 'success');
        } else if (newExpiryMs && oldExpiryMs && newExpiryMs > oldExpiryMs) {
            var newDate = new Date(newExpiryMs).toLocaleDateString('vi-VN');
            showUserChangedToast('🎉 Tài khoản đã được gia hạn đến ' + newDate, 'success');
        } else if (newExpiryMs && !oldExpiryMs) {
            var d2 = new Date(newExpiryMs).toLocaleDateString('vi-VN');
            showUserChangedToast('🎉 Tài khoản đã được gia hạn đến ' + d2, 'success');
        } else if (newRole !== oldRole) {
            showUserChangedToast('ℹ️ Vai trò đã đổi thành: ' + newRole, 'info');
        }

    }, function(err) {
        console.warn('User watcher error:', err);
    });
}
/* ═══════════════════════════════════════════════════════════════
   🔍 VERIFY BACKGROUND — Fetch server sau 2s
   ═══════════════════════════════════════════════════════════════ */
function verifyCurrentUserBackground() {
    if (!currentUser || !db) return;
    var email = currentUser.email;
    if (!email) return;

    db.collection('allowed_users').doc(email).get({ source: 'server' })
        .then(function(doc) {
            if (!doc.exists) return;
            var data = doc.data();
            if (!data) return;

            var oldExpiry = currentUser.expiresAt ? getExpiryDate(currentUser.expiresAt) : null;
            var newExpiry = data.expiresAt ? getExpiryDate(data.expiresAt) : null;

            var oldMs = oldExpiry ? oldExpiry.getTime() : 0;
            var newMs = newExpiry ? newExpiry.getTime() : 0;
            var oldPerm = currentUser.isPermanent || false;
            var newPerm = data.isPermanent || false;

            if (oldMs !== newMs || oldPerm !== newPerm) {
                console.log('🔄 Background verify found changes — refreshing');
                currentUser.expiresAt = data.expiresAt || null;
                currentUser.isPermanent = newPerm;
                currentUser.role = data.role || currentUser.role;
                currentUser.name = data.name || currentUser.name;
                currentUser.tier = data.tier || 'active';
                if (data.permissions) currentUser.permissions = data.permissions;
                if (data.isSubAdmin !== undefined) currentUser.isSubAdmin = data.isSubAdmin;

                if (currentUser.role !== 'admin' && currentUser.expiresAt && !currentUser.isPermanent) {
                    var expDate = getExpiryDate(currentUser.expiresAt);
                    if (expDate && !isNaN(expDate.getTime())) {
                        var isExpired = expDate.getTime() < Date.now();
                        currentUser.isExpiredOnly = isExpired;
                        isDemo = isExpired;
                        if (isExpired) currentUser.tier = 'expired';
                        else if (currentUser.tier === 'expired') currentUser.tier = 'active';
                    }
                } else {
                    currentUser.isExpiredOnly = false;
                    isDemo = false;
                }

                try { localStorage.removeItem('user_cache_' + email); } catch(e) {}
                try {
                    localStorage.setItem('user_cache_' + email, JSON.stringify({
                        data: currentUser, expires: Date.now() + 12 * 60 * 60 * 1000
                    }));
                } catch(e) {}

                publishTierState();
                applyUserUI();
                if (typeof refreshApp === 'function') refreshApp();
            }
        })
        .catch(function(err) {
            console.warn('Background verify error:', err);
        });
}
function getDaysRemaining(userData) {
    if (!userData || !userData.expiresAt) return null;
    if (userData.role === 'admin') return null;
    if (userData.isPermanent) return null;
    var expDate = getExpiryDate(userData.expiresAt);
    if (!expDate) return null;
    return Math.ceil((expDate.getTime() - Date.now()) / (24 * 60 * 60 * 1000));
}

/* ============ TRIAL ============ */
async function grantTrialIfNew(user, userData) {
    if (!user || !user.email) return false;
    var email = user.email.toLowerCase();
    var userRef = db.collection('allowed_users').doc(email);

    try {
        var result = await db.runTransaction(async function(transaction) {
            var doc = await transaction.get(userRef);
            if (doc.exists) {
                var data = doc.data() || {};
                if (data.registeredAt || data.expiresAt || data.role === 'admin') {
                    return { granted: false, reason: 'already_exists' };
                }
            }
            var days = (typeof TRIAL_DAYS === 'number' && TRIAL_DAYS > 0) ? TRIAL_DAYS : 3;
            var expiresAt = new Date(Date.now() + days * 86400000);
            expiresAt.setHours(23, 59, 59, 0);
            transaction.set(userRef, {
                email: email,
                name: (userData && userData.name) ? userData.name : (user.displayName || email.split('@')[0]),
                role: 'user',
                expiresAt: firebase.firestore.Timestamp.fromDate(expiresAt),
                registeredAt: firebase.firestore.FieldValue.serverTimestamp(),
                isTrial: true, trialDays: days,
                trialStartedAt: firebase.firestore.FieldValue.serverTimestamp(),
                tier: 'trial',
                trialMaxQuestions: (typeof TRIAL_MAX_QUESTIONS === 'number') ? TRIAL_MAX_QUESTIONS : 50,
                trialMaxHSK: (typeof TRIAL_MAX_HSK === 'number') ? TRIAL_MAX_HSK : 5
            });
            return { granted: true, expiresAt: expiresAt };
        });
        return result.granted;
    } catch (e) {
        console.error('❌ Grant trial error:', e);
        return false;
    }
}

function enterDemoMode() {
    isDemo = true;
    currentUser = null;
    publishTierState();
    applyUserUI();
    if (!appInitialized) { initApp(); appInitialized = true; }
    else { if (typeof refreshApp === 'function') refreshApp(); }
    if ($('loadingScreen')) $('loadingScreen').classList.add('hidden');
    if ($('stickyTop')) $('stickyTop').style.display = 'block';
    if ($('fabGroup')) $('fabGroup').style.display = 'flex';
    if ($('mainContent')) $('mainContent').style.display = 'block';
}

/* ═══════════════════════════════════════════════════════════════
   ⏰ RENDER BANNER CẢNH BÁO GIA HẠN
   ═══════════════════════════════════════════════════════════════ */
function renderExpiryBanner() {
    var banner = $('expiryBanner');
    if (!banner) return;

    if (!currentUser) {
        banner.style.display = 'none';
        return;
    }
    if (currentUser.role === 'admin' || currentUser.isPermanent) {
        banner.style.display = 'none';
        return;
    }
    if (!currentUser.expiresAt) {
        banner.style.display = 'none';
        return;
    }

    var expDate = getExpiryDate(currentUser.expiresAt);
    if (!expDate || isNaN(expDate.getTime())) {
        banner.style.display = 'none';
        return;
    }

    var now = Date.now();
    var daysLeft = Math.ceil((expDate.getTime() - now) / (24 * 60 * 60 * 1000));
    var expDateStr = expDate.toLocaleDateString('vi-VN');
    var tier = currentUser.tier || 'active';

    if (daysLeft > 7) {
        banner.style.display = 'none';
        return;
    }

    var isExpired = daysLeft <= 0;
    var isUrgent  = !isExpired && daysLeft <= 3;

    banner.classList.remove('urgent', 'expired');
    if (isExpired) {
        banner.classList.add('expired');
    } else if (isUrgent) {
        banner.classList.add('urgent');
    }

    var iconWrap = $('expiryBannerIcon') || banner.querySelector('.expiry-banner-icon');
    if (iconWrap) {
        if (isExpired) {
            iconWrap.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
        } else if (isUrgent) {
            iconWrap.innerHTML = '<i class="fas fa-exclamation-circle"></i>';
        } else {
            iconWrap.innerHTML = '<i class="fas fa-hourglass-half"></i>';
        }
    }

    var titleEl = $('expiryBannerTitle') || banner.querySelector('.expiry-banner-text .title');
    if (titleEl) {
        if (isExpired) {
            titleEl.innerHTML = '❌ Tài khoản đã HẾT HẠN!';
        } else if (isUrgent) {
            titleEl.innerHTML = '🔥 Chỉ còn ' + daysLeft + ' ngày!';
        } else if (tier === 'trial') {
            titleEl.innerHTML = '🎁 Trial còn ' + daysLeft + ' ngày';
        } else {
            titleEl.innerHTML = '⏰ Tài khoản sắp hết hạn';
        }
    }

    var descEl = $('expiryBannerDesc') || banner.querySelector('.expiry-banner-text .desc');
    if (descEl) {
        if (isExpired) {
            descEl.innerHTML = 'Đã hết hạn vào <b>' + expDateStr + '</b> (' +
                Math.abs(daysLeft) + ' ngày trước). Bạn đang ở chế độ giới hạn — ' +
                'gia hạn ngay để mở khóa toàn bộ!';
        } else if (isUrgent) {
            descEl.innerHTML = 'Tài khoản sẽ hết hạn vào <b>' + expDateStr + '</b> — ' +
                'chỉ còn <b>' + daysLeft + ' ngày</b>. Gia hạn ngay để không bị gián đoạn!';
        } else if (tier === 'trial') {
            descEl.innerHTML = 'Còn <b>' + daysLeft + ' ngày</b> dùng thử (đến <b>' +
                expDateStr + '</b>). Nâng cấp để mở khóa toàn bộ nội dung!';
        } else {
            descEl.innerHTML = 'Còn <b>' + daysLeft + ' ngày</b> sử dụng (đến <b>' +
                expDateStr + '</b>). Gia hạn sớm để yên tâm học tập!';
        }
    }

    var contactBtn = $('expiryContactBtn') || banner.querySelector('.expiry-banner-btn');
    if (contactBtn) {
        if (isExpired) {
            contactBtn.innerHTML = '<i class="fas fa-gem"></i> Gia hạn ngay';
        } else if (isUrgent) {
            contactBtn.innerHTML = '<i class="fas fa-gem"></i> Gia hạn ngay';
        } else {
            contactBtn.innerHTML = '<i class="fas fa-gem"></i> Gia hạn';
        }
        contactBtn.onclick = function(e) {
            e.preventDefault();
            if (typeof openRenewalModal === 'function') openRenewalModal();
        };
    }

    banner.style.display = 'flex';
}

/* ═══════════════════════════════════════════════════════════════
   ✅ ĐỒNG BỘ TRẠNG THÁI DROPDOWN USER MENU
   ═══════════════════════════════════════════════════════════════ */
function applyUserDropdownState() {
    var dd = $('userDropdown');
    if (!dd) return;

    if (isDemo && !currentUser) {
        dd.classList.remove('show');
        return;
    }

    var closedFlag = null;
    try { closedFlag = sessionStorage.getItem('userDropdownClosed'); } catch(_e) {}

    if (closedFlag === '1') {
        dd.classList.remove('show');
    } else {
        dd.classList.add('show');
    }
}

/* ============ USER UI ============ */
function applyUserUI() {
    var demoBadge = $('demoBadge');
    var headerLoginBtn = $('headerLoginBtn');
    var userMenu = $('userMenu');

    renderExpiryBanner();

    /* ⭐ Update nút gia hạn trong dropdown */
    var renewBtn = $('dropdownRenewBtn');
    if (renewBtn) {
        var showRenew = currentUser
                        && currentUser.role !== 'admin'
                        && !currentUser.isPermanent
                        && currentUser.tier !== 'trial';
        renewBtn.style.display = showRenew ? 'flex' : 'none';
        if (showRenew) {
            var rDaysLeft = getDaysRemaining(currentUser);
            var isUrgent = (rDaysLeft !== null && rDaysLeft <= 3);
            renewBtn.classList.toggle('urgent', isUrgent);
            var rBadge = renewBtn.querySelector('.renew-badge');
            if (rBadge) {
                if (rDaysLeft !== null && rDaysLeft <= 0) rBadge.textContent = 'HẾT HẠN';
                else if (rDaysLeft !== null && rDaysLeft <= 3) rBadge.textContent = 'GẤP';
                else rBadge.textContent = 'VIP';
            }
        }
    }

    var foreverBtn = $('dropdownForeverBtn');
    if (foreverBtn) {
        var showForever = currentUser
                          && currentUser.role !== 'admin'
                          && !currentUser.isPermanent;
        foreverBtn.style.display = showForever ? 'flex' : 'none';
    }

    /* ═══════════════════════════════════════════════════════════════
       ⭐ PHÂN BIỆT: Guest / Expired / Active
       ═══════════════════════════════════════════════════════════════ */
    var hasFirebaseUser = false;
    try {
        hasFirebaseUser = !!(auth && auth.currentUser);
    } catch(e) {}

    var isRealGuest = !currentUser && !hasFirebaseUser;
    var isExpiredUser = currentUser && currentUser.isExpiredOnly === true;

    if (isRealGuest) {
        /* ═══════════════════════════════════════════════════════════
           ⭐ GUEST — Chưa login
           ═══════════════════════════════════════════════════════════ */
        if (demoBadge) demoBadge.style.display = 'flex';
        if (headerLoginBtn) headerLoginBtn.style.display = 'flex';
        if (userMenu) userMenu.style.display = 'none';
        if ($('demoBanner')) $('demoBanner').style.display = 'flex';
        if ($('userDetails')) $('userDetails').style.display = 'none';

    } else if (isExpiredUser) {
        /* ═══════════════════════════════════════════════════════════
           ⭐ EXPIRED — Đã login nhưng hết hạn
           ⭐ FIX: ẨN #demoBanner — chỉ hiện #expiryBanner (đỏ full-width)
           ═══════════════════════════════════════════════════════════ */
        if (demoBadge) demoBadge.style.display = 'none';
        if (headerLoginBtn) headerLoginBtn.style.display = 'none';
        if (userMenu) userMenu.style.display = 'block';
        if ($('demoBanner')) $('demoBanner').style.display = 'none';   // ⬅️ ĐÃ SỬA: flex → none

        /* ⭐ User info */
        if ($('userName')) $('userName').textContent = currentUser.name;
        if ($('userEmail')) $('userEmail').textContent = currentUser.email;
        if ($('userRole')) {
            var roleText = currentUser.role;
            var roleCls = 'role';
            if (currentUser.role === 'admin') {
                if (isSuperAdmin()) { roleText = 'super admin'; roleCls += ' admin'; }
                else if (isSubAdmin()) { roleText = 'sub admin'; roleCls += ' subadmin'; }
                else { roleText = 'admin'; roleCls += ' admin'; }
            }
            $('userRole').textContent = roleText;
            $('userRole').className = roleCls;
        }

        /* ⭐ Avatar với màu đỏ (báo hiệu expired) */
        var avatar = $('userAvatar');
        if (avatar) {
            if (currentUser.photo) {
                avatar.src = currentUser.photo;
            } else {
                avatar.src = 'data:image/svg+xml;utf8,' + encodeURIComponent(
                    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' +
                    '<rect fill="#dc2626" width="100" height="100"/>' +
                    '<text x="50" y="65" font-size="45" fill="#fff" text-anchor="middle" ' +
                    'font-family="sans-serif" font-weight="bold">' +
                    (currentUser.name || '?').charAt(0).toUpperCase() +
                    '</text></svg>'
                );
            }
        }

        /* ⭐ User details — hiện "Đã hết hạn" */
        if ($('userDetails')) $('userDetails').style.display = 'flex';

        var expiryValue = $('expiryValue');
        var expirySub = $('expirySub');
        var expiryIcon = $('expiryIcon');
        var expiryIconWrap = $('expiryIconWrap');
        var progressWrap = $('expiryProgressWrap');

        if (expiryValue) {
            expiryValue.textContent = 'Đã hết hạn';
            expiryValue.className = 'detail-value expired';
        }

        if (expirySub && currentUser.expiresAt) {
            var d = getExpiryDate(currentUser.expiresAt);
            if (d && !isNaN(d.getTime())) {
                var daysAgo = Math.floor((Date.now() - d.getTime()) / (24 * 60 * 60 * 1000));
                expirySub.innerHTML = 'Hết hạn: <b>' + d.toLocaleDateString('vi-VN') + '</b><br>' +
                    'Đã hết hạn ' + daysAgo + ' ngày trước';
            }
        }

        if (expiryIcon) expiryIcon.className = 'fas fa-calendar-times';
        if (expiryIconWrap) expiryIconWrap.className = 'detail-icon expired';
        if (progressWrap) progressWrap.style.display = 'none';

        /* ⭐ Hiện nút "Gia hạn" trong dropdown */
        if (renewBtn) renewBtn.style.display = 'flex';
        if (foreverBtn) foreverBtn.style.display = 'flex';

        /* ⭐ Ẩn admin button */
        if ($('openAdminBtn')) {
            $('openAdminBtn').style.display = currentUser.role === 'admin' ? 'flex' : 'none';
        }

        applyUserDropdownState();

    } else {
        /* ═══════════════════════════════════════════════════════════
           ⭐ ACTIVE — Đang hoạt động bình thường
           ═══════════════════════════════════════════════════════════ */
        if (demoBadge) demoBadge.style.display = 'none';
        if (headerLoginBtn) headerLoginBtn.style.display = 'none';
        if (userMenu) userMenu.style.display = 'block';
        if ($('demoBanner')) $('demoBanner').style.display = 'none';

        if ($('userName')) $('userName').textContent = currentUser.name;
        if ($('userEmail')) $('userEmail').textContent = currentUser.email;
        if ($('userRole')) {
            var roleText2 = currentUser.role;
            var roleCls2 = 'role';
            if (currentUser.role === 'admin') {
                if (isSuperAdmin()) { roleText2 = 'super admin'; roleCls2 += ' admin'; }
                else if (isSubAdmin()) { roleText2 = 'sub admin'; roleCls2 += ' subadmin'; }
                else { roleText2 = 'admin'; roleCls2 += ' admin'; }
            }
            $('userRole').textContent = roleText2;
            $('userRole').className = roleCls2;
        }

        if ($('openAdminBtn')) {
            $('openAdminBtn').style.display = currentUser.role === 'admin' ? 'flex' : 'none';
        }

        /* ⭐ Avatar bình thường (màu tím) */
        var avatar2 = $('userAvatar');
        if (avatar2) {
            if (currentUser.photo) {
                avatar2.src = currentUser.photo;
            } else {
                avatar2.src = 'data:image/svg+xml;utf8,' + encodeURIComponent(
                    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' +
                    '<rect fill="#7c3aed" width="100" height="100"/>' +
                    '<text x="50" y="65" font-size="45" fill="#fff" text-anchor="middle" ' +
                    'font-family="sans-serif" font-weight="bold">' +
                    (currentUser.name || '?').charAt(0).toUpperCase() +
                    '</text></svg>'
                );
            }
        }

        updateUserDetails();
        applyUserDropdownState();
    }

    /* ═══ Update chip HSK/Subject với tier limited ═══ */
    var hskChip = $('hskChip');
    var subjectChip = $('subjectChip');
    if (hskChip && subjectChip) {
        var limited = isDemo || isExpiredUser || (currentUser && currentUser.tier === 'expired');
        if (limited) {
            hskChip.classList.add('demo-limited');
            subjectChip.classList.add('demo-limited');
        } else {
            hskChip.classList.remove('demo-limited');
            subjectChip.classList.remove('demo-limited');
        }
    }

    if (typeof updateDemoRemaining === 'function') updateDemoRemaining();

    var toggleFocusBtn = $('toggleFocusBtn');
    if (toggleFocusBtn) {
        toggleFocusBtn.style.display = (isDemo || isExpiredUser) ? 'none' : 'flex';
    }

    if (isDemo || isExpiredUser) {
        document.body.classList.remove('hide-floating');
    }

    if (typeof window.favUpdateLockState === 'function') window.favUpdateLockState();

/* ⭐ Update banner theo tier (demo / expired) */
    if (typeof updateDemoBannerByTier === 'function') {
        updateDemoBannerByTier();
    }

    /* ⭐ Refresh lại filter HSK/Subject theo tier mới */
    if (typeof buildFilters === 'function') {
        try { buildFilters(); } catch(e) {}
    }
    if (typeof pfBuildFilterOptions === 'function') {
        try { pfBuildFilterOptions(); } catch(e) {}
    }

    /* ⭐ Refresh lock state cho dataset tabs */
    if (typeof markCurrentDatasetActive === 'function') {
        try { markCurrentDatasetActive(); } catch(e) {}
    }
}

function updateDemoBannerByTier() {
    var banner = $('demoBanner');
    if (!banner) return;

    var btn = $('demoBannerBtn');
    var btnText = $('demoBannerBtnText');
    var titleEl = $('demoBannerTitle');
    var descEl = $('demoBannerDesc');
    var iconEl = banner.querySelector('.demo-banner-icon');

    var hasFirebaseUser = false;
    try {
        hasFirebaseUser = !!(auth && auth.currentUser);
    } catch(e) {}

    var isRealGuest = !currentUser && !hasFirebaseUser;
    var isExpiredUser = currentUser && currentUser.isExpiredOnly === true;

    // ⭐ FIX: XÓA BANNER "Tài khoản đã hết hạn 28/9/2026"
    // Banner #demoBanner CHỈ hiện cho GUEST chưa login.
    // Khi expired → ẩn hoàn toàn, chỉ dùng #expiryBanner.
    if (isExpiredUser) {
        banner.style.display = 'none';
        return;
    }

    if (!isRealGuest) {
        banner.style.display = 'none';
        return;
    }

    /* ═══════════════════════════════════════════════════════════════
       ⭐ GUEST → Nút "Đăng nhập bằng Gmail"
       ═══════════════════════════════════════════════════════════════ */
    banner.style.display = 'flex';

    var remaining = (typeof getDemoRemaining === 'function') ? getDemoRemaining() : 100;

    if (titleEl) titleEl.innerHTML = 'Đăng nhập miễn phí để mở khóa toàn bộ';
    if (descEl) {
        descEl.innerHTML = 'Đăng nhập bằng <b>Gmail</b> để xem <b>toàn bộ kho câu</b>, ' +
            'không giới hạn nghe và luyện viết.<br>' +
            'Nghe + Luyện viết còn lại hôm nay: ' +
            '<b id="demoRemainingText" style="color:#16a34a">' + remaining + '</b> lượt.';
    }
    if (btnText) btnText.textContent = 'Đăng nhập bằng Gmail';
    if (btn) {
        var icon = btn.querySelector('i');
        if (icon) icon.className = 'fas fa-sign-in-alt';
        btn.onclick = function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (typeof showLoginModal === 'function') showLoginModal();
        };
    }
    if (iconEl) iconEl.innerHTML = '<i class="fas fa-gift"></i>';
    banner.style.background = '';
    banner.style.borderColor = '';
}
function updateUserDetails() {
    var detailsEl = $('userDetails');
    if (!detailsEl) return;
    if (isDemo || !currentUser) { detailsEl.style.display = 'none'; return; }
    detailsEl.style.display = 'flex';
    var expiryValue = $('expiryValue');
    var expirySub = $('expirySub');
    var expiryIcon = $('expiryIcon');
    var expiryIconWrap = $('expiryIconWrap');
    var progressWrap = $('expiryProgressWrap');
    var progressBar = $('expiryProgressBar');
    if (!expiryValue || !expirySub) return;
    if (currentUser.role === 'admin') {
        expiryValue.textContent = 'Vĩnh viễn';
        expiryValue.className = 'detail-value permanent';
        expirySub.textContent = isSuperAdmin() ? 'Super Admin' : (isSubAdmin() ? 'Sub Admin' : 'Quản trị viên');
        if (expiryIcon) expiryIcon.className = 'fas fa-infinity';
        if (expiryIconWrap) expiryIconWrap.className = 'detail-icon permanent';
        if (progressWrap) progressWrap.style.display = 'none';
        return;
    }
    if (currentUser.isPermanent) {
        expiryValue.textContent = '💎 Vĩnh viễn';
        expiryValue.className = 'detail-value permanent';
        expirySub.innerHTML = 'Đã sở hữu <b>gói vĩnh viễn</b> — không bao giờ hết hạn';
        if (expiryIcon) expiryIcon.className = 'fas fa-crown';
        if (expiryIconWrap) expiryIconWrap.className = 'detail-icon permanent';
        if (progressWrap) progressWrap.style.display = 'none';
        return;
    }
    if (!currentUser.expiresAt) {
        expiryValue.textContent = 'Vĩnh viễn';
        expiryValue.className = 'detail-value permanent';
        expirySub.textContent = 'Không giới hạn thời gian';
        if (expiryIcon) expiryIcon.className = 'fas fa-infinity';
        if (expiryIconWrap) expiryIconWrap.className = 'detail-icon permanent';
        if (progressWrap) progressWrap.style.display = 'none';
        return;
    }
    var expDate = getExpiryDate(currentUser.expiresAt);
    if (!expDate || isNaN(expDate.getTime())) { expiryValue.textContent = '-'; expirySub.textContent = ''; return; }
    var now = Date.now();
    var daysLeft = Math.ceil((expDate.getTime() - now) / (24 * 60 * 60 * 1000));
    var dateStr = expDate.toLocaleDateString('vi-VN');
    var tier = currentUser.tier || 'active';
    expiryValue.className = 'detail-value';
    if (expiryIconWrap) expiryIconWrap.className = 'detail-icon';
    if (daysLeft < 0) {
        expiryValue.textContent = 'Đã hết hạn';
        expiryValue.classList.add('expired');
        expirySub.innerHTML = 'Ngày hết hạn: <b>' + dateStr + '</b><br>Đã hết hạn ' + Math.abs(daysLeft) + ' ngày trước';
        if (expiryIcon) expiryIcon.className = 'fas fa-calendar-times';
        if (expiryIconWrap) expiryIconWrap.classList.add('expired');
        if (progressWrap) progressWrap.style.display = 'none';
    } else if (daysLeft <= 3) {
        expiryValue.textContent = 'Còn ' + daysLeft + ' ngày';
        expiryValue.classList.add('urgent');
        expirySub.innerHTML = (tier === 'trial' ? '🎁 Trial: ' : '') + 'Hạn: <b>' + dateStr + '</b>';
        if (expiryIcon) expiryIcon.className = 'fas fa-exclamation-circle';
        if (expiryIconWrap) expiryIconWrap.classList.add('urgent');
        if (progressWrap) { progressWrap.style.display = 'block'; progressBar.className = 'progress-bar urgent'; progressBar.style.width = '90%'; }
    } else if (daysLeft <= 7) {
        expiryValue.textContent = 'Còn ' + daysLeft + ' ngày';
        expiryValue.classList.add('warn');
        expirySub.innerHTML = (tier === 'trial' ? '🎁 Trial: ' : '') + 'Hạn: <b>' + dateStr + '</b>';
        if (expiryIcon) expiryIcon.className = 'fas fa-clock';
        if (expiryIconWrap) expiryIconWrap.classList.add('warn');
        if (progressWrap) { progressWrap.style.display = 'block'; progressBar.className = 'progress-bar warn'; progressBar.style.width = '70%'; }
    } else {
        expiryValue.textContent = 'Còn ' + daysLeft + ' ngày';
        expiryValue.className = 'detail-value ' + (tier === 'trial' ? 'trial' : 'ok');
        expirySub.innerHTML = (tier === 'trial' ? '🎁 Trial: ' : '') + 'Hạn: <b>' + dateStr + '</b>';
        if (expiryIcon) expiryIcon.className = 'fas fa-calendar-check';
        if (expiryIconWrap) expiryIconWrap.classList.add(tier === 'trial' ? 'trial' : 'ok');
        if (progressWrap) { progressWrap.style.display = 'block'; progressBar.className = 'progress-bar ok'; progressBar.style.width = '30%'; }
    }
}

/* ============ LOGIN UI ============ */
window.showLoginModal = function() {
    $('loginModal').classList.add('show');
    $('loginError').classList.remove('show');
};
function hideLoginModal() { $('loginModal').classList.remove('show'); }
function showLoginError(msg) {
    var el = $('loginError');
    el.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ' + msg;
    el.classList.add('show');
}

function logLogin(u) {
    try {
        var today = new Date().toDateString();
        var logKey = 'login_log_' + u.email;
        if (localStorage.getItem(logKey) === today) return;
        db.collection('login_logs').add({
            email: u.email, name: u.name, role: u.role,
            time: firebase.firestore.FieldValue.serverTimestamp(),
            userAgent: navigator.userAgent.substring(0, 100)
        }).then(function() { try { localStorage.setItem(logKey, today); } catch(e) {} }).catch(function(){});
    } catch(e) {}
}

/* ============ ADMIN SEARCH & FILTER ============ */
function filterUsers(items) {
    var query = adminSearchQuery.toLowerCase().trim();
    var filter = adminCurrentFilter;
    var now = Date.now();
    return items.filter(function(u) {
        if (query) {
            var email = (u.email || '').toLowerCase();
            var name = (u.name || '').toLowerCase();
            if (email.indexOf(query) === -1 && name.indexOf(query) === -1) return false;
        }
        if (filter === 'all') return true;
        if (filter === 'user') return u.role !== 'admin';
        if (filter === 'admin') return u.role === 'admin';
        if (filter === 'trial') return u.role !== 'admin' && (u.tier === 'trial' || u.isTrial);
        if (filter === 'permanent') return u.role !== 'admin' && u.isPermanent;
        if (filter === 'expiring') {
            if (u.role === 'admin' || u.isPermanent || !u.expiresAt) return false;
            var d = getExpiryDate(u.expiresAt);
            if (!d || isNaN(d.getTime())) return false;
            var daysLeft = Math.ceil((d.getTime() - now) / 86400000);
            return daysLeft >= 0 && daysLeft <= 7;
        }
        if (filter === 'expired') {
            if (u.role === 'admin' || u.isPermanent || !u.expiresAt) return false;
            var d2 = getExpiryDate(u.expiresAt);
            if (!d2 || isNaN(d2.getTime())) return false;
            return d2.getTime() < now;
        }
        return true;
    });
}

function getUserSortStatus(u, now) {
    if (u.role === 'admin') return 0;
    if (u.isPermanent || !u.expiresAt) return 0;
    var d = getExpiryDate(u.expiresAt);
    if (!d || isNaN(d.getTime())) return 0;
    var daysLeft = Math.ceil((d.getTime() - now) / (24 * 60 * 60 * 1000));
    if (daysLeft < 0) return 2;
    if (daysLeft <= 7) return 1;
    return 0;
}

function sortUsersForDisplay(items) {
    var myEmail = (currentUser && currentUser.email ? currentUser.email.toLowerCase() : '');
    var now = Date.now();

    return items.slice().sort(function(a, b) {
        var aEmail = (a.email || '').toLowerCase();
        var bEmail = (b.email || '').toLowerCase();

        var aIsMe = (aEmail === myEmail);
        var bIsMe = (bEmail === myEmail);
        if (aIsMe && !bIsMe) return -1;
        if (!aIsMe && bIsMe) return 1;

        var aGroup = a.role === 'admin' ? 1 : 2;
        var bGroup = b.role === 'admin' ? 1 : 2;
        if (aGroup !== bGroup) return aGroup - bGroup;

        if (aGroup === 2) {
            var aStatus = getUserSortStatus(a, now);
            var bStatus = getUserSortStatus(b, now);
            if (aStatus !== bStatus) return aStatus - bStatus;
        }

        var aLast = lastLoginMap[aEmail] ? lastLoginMap[aEmail].getTime() : 0;
        var bLast = lastLoginMap[bEmail] ? lastLoginMap[bEmail].getTime() : 0;
        if (aLast !== bLast) return bLast - aLast;

        return aEmail.localeCompare(bEmail);
    });
}

function updateFilterCounts(items) {
    var now = Date.now();
    var counts = { all: 0, user: 0, admin: 0, trial: 0, expiring: 0, expired: 0, permanent: 0 };
    var hidden = isHiddenAdmin();
    var myEmail = (currentUser && currentUser.email ? currentUser.email.toLowerCase() : '');
    items.forEach(function(u) {
        var uEmail = (u.email || '').toLowerCase();
        if (hidden && u.role === 'admin' && uEmail !== myEmail) return;
        counts.all++;
        if (u.role === 'admin') counts.admin++;
        else {
            counts.user++;
            if (u.tier === 'trial' || u.isTrial) counts.trial++;
            if (u.isPermanent) counts.permanent++;
            if (u.expiresAt && !u.isPermanent) {
                var d = getExpiryDate(u.expiresAt);
                if (d && !isNaN(d.getTime())) {
                    var daysLeft = Math.ceil((d.getTime() - now) / 86400000);
                    if (daysLeft < 0) counts.expired++;
                    else if (daysLeft <= 7) counts.expiring++;
                }
            }
        }
    });
    var map = { all: 'filterCountAll', user: 'filterCountUser', admin: 'filterCountAdmin',
                trial: 'filterCountTrial', expiring: 'filterCountExpiring',
                expired: 'filterCountExpired', permanent: 'filterCountPermanent' };
    Object.keys(map).forEach(function(k) {
        var el = $(map[k]);
        if (el) el.textContent = counts[k];
    });
}

window.setAdminFilter = function(filter) {
    adminCurrentFilter = filter;
    document.querySelectorAll('.admin-filter-btn').forEach(function(btn) {
        if (btn.dataset.filter) btn.classList.toggle('active', btn.dataset.filter === filter);
    });
    renderUsers(usersCache);
};

/* ═══════════════════════════════════════════════════════════════
   🔒 OPEN RENEWAL MODAL
   ═══════════════════════════════════════════════════════════════ */
window.openRenewalModal = async function() {
    if (!currentUser) { showLoginModal(); return; }
    if (currentUser.role === 'admin') { alert('Admin có hạn vĩnh viễn, không cần gia hạn!'); return; }
    if (currentUser.isPermanent) { alert('💎 Bạn đã sở hữu gói VĨNH VIỄN!\n\nKhông cần gia hạn thêm.'); return; }

    try {
        var existingSnap = await db.collection('renewal_requests')
            .where('email', '==', currentUser.email)
            .where('status', 'in', ['pending', 'user_paid'])
            .orderBy('createdAt', 'desc')
            .limit(1)
            .get();

        if (!existingSnap.empty) {
            var oldReq = existingSnap.docs[0];
            var oldData = oldReq.data();
            var oldCreated = oldData.createdAt ? oldData.createdAt.toDate() : new Date();
            var hoursAgo = Math.floor((Date.now() - oldCreated.getTime()) / 3600000);

            var statusText = oldData.status === 'user_paid' ? 'Chờ admin xác nhận' : 'Chờ chuyển khoản';
            var confirmMsg = '⚠️ Bạn đang có 1 lệnh gia hạn CHƯA hoàn tất:\n\n' +
                '• Gói: ' + (oldData.packageLabel || oldData.package) + '\n' +
                '• Số tiền: ' + formatMoney(oldData.amount) + 'đ\n' +
                '• Mã: ' + oldData.transferCode + '\n' +
                '• Tạo cách đây: ' + hoursAgo + ' giờ\n' +
                '• Trạng thái: ' + statusText + '\n\n' +
                '👉 Bạn KHÔNG THỂ tạo lệnh mới khi lệnh cũ chưa xử lý.\n\n' +
                'Bạn có muốn HỦY lệnh cũ để tạo lệnh mới không?';

            if (!confirm(confirmMsg)) {
                return;
            }

            await db.collection('renewal_requests').doc(oldReq.id).update({
                status: 'cancelled',
                cancelledAt: firebase.firestore.FieldValue.serverTimestamp(),
                cancelledBy: 'user_replace',
                cancelReason: 'User hủy để tạo lệnh mới'
            });

            alert('✅ Đã hủy lệnh cũ. Bạn có thể tạo lệnh mới.');
        }
    } catch(e) {
        console.error('Check existing renewal error:', e);
    }

    renewalSelectedPkg = null;
    renewalCurrentReq = null;
    renderRenewalStep1();
    $('renewalModal').classList.add('show');
    if ($('userDropdown')) $('userDropdown').classList.remove('show');
};

window.closeRenewalModal = function() {
    $('renewalModal').classList.remove('show');
    if (renewalListener) { try { renewalListener(); } catch(e) {} renewalListener = null; }
};

function renderRenewalStep1() {
    var daysLeft = getDaysRemaining(currentUser);
    var isExpired = daysLeft !== null && daysLeft <= 0;
    var isWarn = daysLeft !== null && daysLeft > 0 && daysLeft <= 7;
    var tier = currentUser.tier || 'active';
    var currentCls = isExpired ? 'expired' : (isWarn ? 'warn' : '');
    var currentIcon = isExpired ? 'fa-exclamation-triangle' : (isWarn ? 'fa-hourglass-half' : 'fa-gem');
    var currentTitle = isExpired ? 'Tài khoản đã hết hạn' : (tier === 'trial' ? '🎁 Đang dùng bản Trial' : (isWarn ? 'Sắp hết hạn' : 'Tài khoản đang hoạt động'));
    var currentDesc = '';
    if (daysLeft === null) currentDesc = 'Vĩnh viễn, không cần gia hạn';
    else if (isExpired) currentDesc = 'Đã hết hạn <b>' + Math.abs(daysLeft) + ' ngày</b> trước.';
    else if (tier === 'trial') currentDesc = 'Trial còn <b>' + daysLeft + ' ngày</b>. Nâng cấp để mở khóa toàn bộ!';
    else currentDesc = 'Còn <b>' + daysLeft + ' ngày</b> sử dụng.';

    var packagesHtml = '';
    var permanentPkg = null;
    var normalPackages = [];
    PACKAGES.forEach(function(p) {
        if (p.permanent) permanentPkg = p;
        else normalPackages.push(p);
    });
    normalPackages.forEach(function(p) {
        var saveHtml = p.save ? '<div class="pkg-save">' + escapeHtml(p.save) + '</div>' : '';
        var popularHtml = p.popular ? '<div class="pkg-popular">⭐ Phổ biến</div>' : '';
        packagesHtml += '<div class="package-card" data-pkg="' + p.id + '" onclick="selectPackage(\'' + p.id + '\')">' +
            popularHtml + saveHtml +
            '<div class="pkg-label">' + escapeHtml(p.label) + '</div>' +
            '<div class="pkg-price">' + formatMoney(p.amount) + '</div>' +
            '<div class="pkg-unit">VNĐ</div></div>';
    });
    if (permanentPkg) {
        packagesHtml += '<div style="grid-column:1/-1;margin-top:.5rem;padding-top:.75rem;border-top:2px dashed var(--border);">' +
            '<div class="renewal-section-title" style="justify-content:center;color:#dc2626;font-size:.78rem;margin-bottom:.6rem">' +
                '<i class="fas fa-crown"></i> Gói đặc biệt — sở hữu mãi mãi</div>' +
            '<div class="package-card" data-pkg="' + permanentPkg.id + '" onclick="selectPackage(\'' + permanentPkg.id + '\')" style="padding:1.2rem 1rem;">' +
                '<div class="pkg-label" style="font-size:1.15rem;">💎 ' + escapeHtml(permanentPkg.label) + '</div>' +
                '<div class="pkg-price" style="font-size:1.6rem;margin:.5rem 0;">' + formatMoney(permanentPkg.amount) + 'đ</div>' +
                '<div class="pkg-unit" style="font-size:.75rem;">' + escapeHtml(permanentPkg.save || 'Dùng mãi mãi — Không lo hết hạn') + '</div></div></div>';
    }
    $('renewalBody').innerHTML =
        '<div class="renewal-current ' + currentCls + '">' +
            '<div class="rc-icon"><i class="fas ' + currentIcon + '"></i></div>' +
            '<div class="rc-info"><div class="rc-title">' + currentTitle + '</div>' +
            '<div class="rc-desc">' + currentDesc + '</div></div></div>' +
        '<div class="renewal-section-title"><i class="fas fa-box"></i> Chọn gói gia hạn</div>' +
        '<div class="package-grid">' + packagesHtml + '</div>' +
        '<div class="renewal-actions">' +
            '<button class="renewal-btn" onclick="closeRenewalModal()">Hủy</button>' +
            '<button class="renewal-btn primary" id="renewalNextBtn" disabled onclick="goToPayment()"><i class="fas fa-arrow-right"></i> Tiếp tục</button>' +
        '</div>';
}

window.selectPackage = function(pkgId) {
    renewalSelectedPkg = PACKAGES.find(function(p) { return p.id === pkgId; });
    document.querySelectorAll('.package-card').forEach(function(c) {
        c.classList.toggle('selected', c.dataset.pkg === pkgId);
    });
    var btn = $('renewalNextBtn');
    if (btn) btn.disabled = false;
};

async function goToPayment() {
    if (!renewalSelectedPkg) return;

    try {
        var checkSnap = await db.collection('renewal_requests')
            .where('email', '==', currentUser.email)
            .where('status', 'in', ['pending', 'user_paid'])
            .limit(1)
            .get();

        if (!checkSnap.empty) {
            alert('⚠️ Bạn vẫn còn 1 lệnh gia hạn chưa xử lý.\n\nVui lòng hủy lệnh cũ trước khi tạo lệnh mới.');
            closeRenewalModal();
            return;
        }
    } catch(e) {
        console.error('Double-check error:', e);
    }

    var transferCode = generateTransferCode();
    var amount = renewalSelectedPkg.amount;
    var btn = $('renewalNextBtn');
    if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang tạo...'; }
    try {
        var reqData = {
            email: currentUser.email, name: currentUser.name,
            package: renewalSelectedPkg.id, packageLabel: renewalSelectedPkg.label,
            amount: amount, days: renewalSelectedPkg.days,
            transferCode: transferCode, status: 'pending', method: 'manual',
            createdAt: firebase.firestore.FieldValue.serverTimestamp()
        };
        if (renewalSelectedPkg.permanent) reqData.isPermanent = true;
        var reqRef = await db.collection('renewal_requests').add(reqData);
        renewalCurrentReq = { id: reqRef.id, code: transferCode };
    } catch(e) {
        alert('❌ Lỗi tạo yêu cầu: ' + e.message);
        if (btn) { btn.disabled = false; btn.innerHTML = '<i class="fas fa-arrow-right"></i> Tiếp tục'; }
        return;
    }
    renderPaymentScreen();
    listenRenewalRequest(renewalCurrentReq.id);
}

function renderPaymentScreen() {
    var pkg = renewalSelectedPkg;
    var code = renewalCurrentReq.code;
    var amount = pkg.amount;
    var qrUrl = 'https://img.vietqr.io/image/' + BANK_CONFIG.bank_id + '-' + BANK_CONFIG.account_no + '-compact2.png' +
                '?amount=' + amount + '&addInfo=' + encodeURIComponent(code) + '&accountName=' + encodeURIComponent(BANK_CONFIG.account_name);
    var durationText = pkg.permanent ? '<b style="color:#dc2626">💎 VĨNH VIỄN</b>' : pkg.days + ' ngày';
    $('renewalBody').innerHTML =
        '<div class="renewal-current">' +
            '<div class="rc-icon"><i class="fas fa-shopping-cart"></i></div>' +
            '<div class="rc-info"><div class="rc-title">Gói ' + escapeHtml(pkg.label) + '</div>' +
            '<div class="rc-desc">Số tiền: <b>' + formatMoney(amount) + ' VNĐ</b> · ' + durationText + '</div></div></div>' +
        '<div class="renewal-section-title"><i class="fas fa-qrcode"></i> Quét mã để thanh toán</div>' +
        '<div class="qr-wrap">' +
            '<img class="qr-img" src="' + qrUrl + '" alt="QR" onerror="this.style.display=\'none\'">' +
            '<div class="qr-hint">Mở app ngân hàng, quét QR để chuyển khoản. Hoặc chuyển thủ công theo thông tin bên dưới.</div></div>' +
        '<div class="bank-info">' +
            '<div class="bank-row"><span class="br-label">Ngân hàng</span><span class="br-value">' + escapeHtml(BANK_CONFIG.bank_name) + '</span></div>' +
            '<div class="bank-row"><span class="br-label">Số TK</span><span class="br-value">' + escapeHtml(BANK_CONFIG.account_no) +
                '<button class="copy-btn" onclick="copyText(\'' + escapeJs(BANK_CONFIG.account_no) + '\', this)"><i class="fas fa-copy"></i></button></span></div>' +
            '<div class="bank-row"><span class="br-label">Chủ TK</span><span class="br-value">' + escapeHtml(BANK_CONFIG.account_name) + '</span></div>' +
            '<div class="bank-row"><span class="br-label">Số tiền</span><span class="br-value code">' + formatMoney(amount) + 'đ</span></div>' +
            '<div class="bank-row"><span class="br-label">Nội dung</span><span class="br-value code">' + escapeHtml(code) +
                '<button class="copy-btn" onclick="copyText(\'' + escapeJs(code) + '\', this)"><i class="fas fa-copy"></i></button></span></div></div>' +
        '<div class="payment-steps">' +
            '<div class="step"><span class="num">1</span><div>Chuyển <b>' + formatMoney(amount) + ' VNĐ</b> đến STK trên</div></div>' +
            '<div class="step"><span class="num">2</span><div>Ghi đúng nội dung: <b>' + escapeHtml(code) + '</b></div></div>' +
            '<div class="step"><span class="num">3</span><div>Nhấn nút <b>"Tôi đã thanh toán"</b></div></div>' +
            '<div class="step"><span class="num">4</span><div>Chờ admin xác nhận trong <b>1-5 phút</b></div></div>' +
            '<div class="step" style="color:#dc2626;font-weight:700"><span class="num" style="background:linear-gradient(135deg,#dc2626,#b91c1c)">!</span><div>Lệnh sẽ <b>tự động hủy sau 24h</b> nếu admin không xác nhận</div></div></div>' +
        '<div class="renewal-actions">' +
            '<button class="renewal-btn" onclick="cancelRenewal()"><i class="fas fa-times"></i> Hủy</button>' +
            '<button class="renewal-btn success" id="renewalConfirmBtn" onclick="userConfirmPaid()"><i class="fas fa-check"></i> Tôi đã thanh toán</button></div>';
}

window.copyText = function(text, btn) {
    var done = function() {
        btn.classList.add('copied');
        btn.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(function() { btn.classList.remove('copied'); btn.innerHTML = '<i class="fas fa-copy"></i>'; }, 1500);
    };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done);
    else {
        var ta = document.createElement('textarea'); ta.value = text;
        document.body.appendChild(ta); ta.select(); document.execCommand('copy');
        document.body.removeChild(ta); done();
    }
};

window.userConfirmPaid = async function() {
    if (!renewalCurrentReq) return;
    var btn = $('renewalConfirmBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang gửi...';
    try {
        var _reqData = null;
        try {
            var _snap = await db.collection('renewal_requests').doc(renewalCurrentReq.id).get();
            if (_snap.exists) _reqData = _snap.data();
        } catch(_e) {}
        await db.collection('renewal_requests').doc(renewalCurrentReq.id).update({
            userConfirmedAt: firebase.firestore.FieldValue.serverTimestamp(),
            status: 'user_paid'
        });
        if (_reqData && typeof window.notifyTelegramUserPaid === 'function') {
            try {
                window.notifyTelegramUserPaid({
                    email: _reqData.email || currentUser.email,
                    name: _reqData.name || currentUser.name,
                    amount: _reqData.amount, package: _reqData.package,
                    packageLabel: _reqData.packageLabel, days: _reqData.days,
                    isPermanent: _reqData.isPermanent || false,
                    transferCode: _reqData.transferCode
                });
            } catch(_te) {}
        }
        renderPendingConfirm();
    } catch(e) {
        alert('❌ Lỗi: ' + e.message);
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-check"></i> Tôi đã thanh toán';
    }
};

function renderPendingConfirm() {
    var zaloUrl = RENEWAL_SUPPORT_ZALO ? 'https://zalo.me/' + RENEWAL_SUPPORT_ZALO.replace(/\D/g, '') : '#';
    $('renewalBody').innerHTML =
        '<div class="renewal-success">' +
            '<div class="icon" style="background:linear-gradient(135deg,#4f46e5,#7c3aed);box-shadow:0 8px 24px rgba(124,58,237,.4)">' +
                '<i class="fas fa-hourglass-half"></i></div>' +
            '<h3>Đang chờ xác nhận</h3>' +
            '<p>Admin sẽ kiểm tra và xác nhận trong <b>1-5 phút</b>.</p>' +
            '<div class="info-box" style="border-color:#dc2626;background:rgba(220,38,38,.08)">' +
                '<i class="fas fa-exclamation-triangle" style="color:#dc2626"></i>' +
                '<div><b>Lưu ý:</b> Nếu admin không xác nhận trong <b>24 giờ</b>, lệnh sẽ tự động bị hủy.</div></div>' +
            '<div class="info-box"><i class="fas fa-info-circle" style="color:#7c3aed"></i>' +
                '<div>Nếu sau <b>10 phút</b> chưa được gia hạn, liên hệ Zalo kèm mã: <b>' + escapeHtml(renewalCurrentReq.code) + '</b></div></div>' +
            '<div style="display:flex;gap:.5rem;flex-wrap:wrap;justify-content:center;margin-top:.5rem">' +
                '<a class="renewal-btn" href="' + zaloUrl + '" target="_blank" rel="noopener"><i class="fas fa-comment-dots"></i> Liên hệ Zalo</a>' +
                '<button class="renewal-btn primary" onclick="closeRenewalModal()"><i class="fas fa-check"></i> Đóng</button></div></div>';
}

function listenRenewalRequest(reqId) {
    if (renewalListener) { try { renewalListener(); } catch(e) {} }
    renewalListener = db.collection('renewal_requests').doc(reqId).onSnapshot(function(doc) {
        if (!doc.exists) return;
        var data = doc.data();
        if (data.status === 'confirmed') {
            showRenewalSuccess(data);
            if (renewalListener) { try { renewalListener(); } catch(e) {} renewalListener = null; }
            refreshCurrentUser();
        } else if (data.status === 'expired') {
            showRenewalExpired();
            if (renewalListener) { try { renewalListener(); } catch(e) {} renewalListener = null; }
        } else if (data.status === 'cancelled') {
            if (renewalListener) { try { renewalListener(); } catch(e) {} renewalListener = null; }
        }
    });
}

function showRenewalExpired() {
    $('renewalBody').innerHTML =
        '<div class="renewal-success">' +
            '<div class="icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c);box-shadow:0 8px 24px rgba(220,38,38,.4)">' +
                '<i class="fas fa-clock"></i></div>' +
            '<h3>⏰ Lệnh đã hết hạn</h3>' +
            '<p>Lệnh gia hạn này đã quá <b>24 giờ</b> mà admin chưa xác nhận nên đã bị hủy tự động.</p>' +
            '<div class="info-box"><i class="fas fa-info-circle" style="color:#7c3aed"></i>' +
                '<div>Bạn có thể tạo lệnh mới. Nếu đã chuyển tiền, vui lòng liên hệ Zalo kèm mã giao dịch.</div></div>' +
            '<div style="display:flex;gap:.5rem;flex-wrap:wrap;justify-content:center;margin-top:.5rem">' +
                '<button class="renewal-btn" onclick="closeRenewalModal()"><i class="fas fa-times"></i> Đóng</button>' +
                '<button class="renewal-btn primary" onclick="closeRenewalModal(); setTimeout(openRenewalModal, 300)"><i class="fas fa-redo"></i> Tạo lệnh mới</button></div></div>';
}

function showRenewalSuccess(data) {
    var newExpiry = '';
    if (data.newExpiresAt) {
        try {
            var d = data.newExpiresAt.toDate ? data.newExpiresAt.toDate() : new Date(data.newExpiresAt.seconds * 1000);
            newExpiry = d.toLocaleDateString('vi-VN');
        } catch(e) {}
    }
    var isPermanent = data.isPermanent || false;
    $('renewalBody').innerHTML =
        '<div class="renewal-success">' +
            '<div class="icon"><i class="fas fa-' + (isPermanent ? 'crown' : 'gem') + '"></i></div>' +
            '<h3>🎉 ' + (isPermanent ? 'Kích hoạt VĨNH VIỄN thành công!' : 'Gia hạn thành công!') + '</h3>' +
            '<p>' + (isPermanent ? 'Bạn đã sở hữu <b>gói VĨNH VIỄN</b>. Tài khoản không bao giờ hết hạn! 💎'
                                 : 'Tài khoản đã được gia hạn thêm <b>' + data.days + ' ngày</b>.') + '</p>' +
            (newExpiry ? '<div class="info-box"><i class="fas fa-calendar-check" style="color:var(--success)"></i><div>Hạn mới: <b>' + newExpiry + '</b></div></div>' : '') +
            '<button class="renewal-btn primary" onclick="closeRenewalModal();location.reload()" style="margin-top:.5rem"><i class="fas fa-check"></i> Hoàn tất</button></div>';
}

window.cancelRenewal = async function() {
    if (renewalCurrentReq) {
        try {
            await db.collection('renewal_requests').doc(renewalCurrentReq.id).update({
                status: 'cancelled',
                cancelledAt: firebase.firestore.FieldValue.serverTimestamp(),
                cancelledBy: 'user'
            });
        } catch(e) {}
    }
    closeRenewalModal();
};

function generateTransferCode() {
    var rand = Math.random().toString(36).substring(2, 6).toUpperCase();
    var ts = Date.now().toString(36).slice(-4).toUpperCase();
    return 'HN' + ts + rand;
}
function formatMoney(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }

async function refreshCurrentUser() {
    if (!currentUser) return;
    try {
        var doc = await db.collection('allowed_users').doc(currentUser.email).get({ source: 'server' });
        if (!doc.exists) return;
        var data = doc.data();
        currentUser.expiresAt = data.expiresAt || null;
        currentUser.name = data.name || currentUser.name;
        currentUser.isPermanent = data.isPermanent || false;
        if (data.tier) currentUser.tier = data.tier;
        if (data.permissions) currentUser.permissions = data.permissions;
        if (data.isSubAdmin !== undefined) currentUser.isSubAdmin = data.isSubAdmin;

        if (currentUser.role !== 'admin' && currentUser.expiresAt && !currentUser.isPermanent) {
            var expDate = getExpiryDate(currentUser.expiresAt);
            if (expDate && !isNaN(expDate.getTime())) {
                var isExpired = expDate.getTime() < Date.now();
                currentUser.isExpiredOnly = isExpired;
                isDemo = isExpired;
                if (isExpired) currentUser.tier = 'expired';
            }
        } else if (currentUser.role === 'admin' || !currentUser.expiresAt || currentUser.isPermanent) {
            currentUser.isExpiredOnly = false;
            isDemo = false;
        }
        try { localStorage.removeItem('user_cache_' + currentUser.email); } catch(e) {}
        try {
            localStorage.setItem('user_cache_' + currentUser.email, JSON.stringify({
                data: currentUser, expires: Date.now() + 12 * 60 * 60 * 1000
            }));
        } catch(e) {}
        publishTierState();
        if (typeof applyUserUI === 'function') applyUserUI();
    } catch(e) { console.error('refreshCurrentUser error:', e); }
}

/* ═══════════════════════════════════════════════════════════════
   ⏰ AUTO-EXPIRE
   ═══════════════════════════════════════════════════════════════ */
async function autoExpireOldRenewals() {
    if (!db) return;
    try {
        var cutoff = new Date(Date.now() - 24 * 60 * 60 * 1000);
        var snap = await db.collection('renewal_requests')
            .where('status', 'in', ['pending', 'user_paid'])
            .where('createdAt', '<', firebase.firestore.Timestamp.fromDate(cutoff))
            .limit(50)
            .get();

        if (snap.empty) return;

        var batch = db.batch();
        var count = 0;
        snap.forEach(function(doc) {
            batch.update(doc.ref, {
                status: 'expired',
                expiredAt: firebase.firestore.FieldValue.serverTimestamp(),
                expireReason: 'Quá 24h không được xác nhận'
            });
            count++;
        });

        await batch.commit();
        console.log('[Auto-expire] Đã hủy ' + count + ' lệnh gia hạn quá 24h');
    } catch(e) {
        console.error('[Auto-expire] Lỗi:', e);
    }
}

function scheduleAutoExpire() {
    setTimeout(autoExpireOldRenewals, 10000);
    setInterval(autoExpireOldRenewals, 60 * 60 * 1000);
}

/* ============ LỊCH SỬ GIA HẠN (USER) ============ */
window.openRenewalHistory = async function() {
    if (!currentUser) { showLoginModal(); return; }
    var titleEl = document.querySelector('#renewalHistoryModal h2');
    if (titleEl) titleEl.innerHTML = '<i class="fas fa-history"></i> Lịch sử gia hạn';
    var listEl = $('renewalHistoryList');
    listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';
    $('renewalHistoryModal').classList.add('show');

    try {
        var snapshot = await db.collection('renewal_requests')
            .where('email', '==', currentUser.email)
            .orderBy('createdAt', 'desc').limit(50).get();

        if (snapshot.empty) {
            listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:var(--text-3)">' +
                '<i class="fas fa-inbox" style="font-size:2rem;margin-bottom:.75rem;display:block;opacity:.5"></i>' +
                'Bạn chưa có giao dịch gia hạn nào</div>';
            return;
        }

        var html = '';
        snapshot.forEach(function(doc) {
            var d = doc.data();
            html += buildHistoryItemHtml(d, false);
        });
        listEl.innerHTML = html;
    } catch(e) {
        console.error('Lỗi load lịch sử:', e);
        listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:#dc2626">' +
            '<i class="fas fa-exclamation-triangle"></i> Lỗi tải dữ liệu: ' + escapeHtml(e.message) + '</div>';
    }
};

window.openUserRenewalHistory = async function(email) {
    if (!currentUser || currentUser.role !== 'admin') {
        alert('Chỉ admin mới có quyền xem lịch sử gia hạn!');
        return;
    }
    var user = usersCache.find(function(u) { return u.email === email; });
    var userName = user ? (user.name || email.split('@')[0]) : email.split('@')[0];
    var titleEl = document.querySelector('#renewalHistoryModal h2');
    if (titleEl) titleEl.innerHTML = '<i class="fas fa-history"></i> Lịch sử gia hạn — ' + escapeHtml(userName);
    var listEl = $('renewalHistoryList');
    listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';
    $('renewalHistoryModal').classList.add('show');

    try {
        var snapshot = await db.collection('renewal_requests')
            .where('email', '==', email.toLowerCase())
            .orderBy('createdAt', 'desc').limit(100).get();

        if (snapshot.empty) {
            listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:var(--text-3)">' +
                '<i class="fas fa-inbox" style="font-size:2rem;margin-bottom:.75rem;display:block;opacity:.5"></i>' +
                'User này chưa có giao dịch gia hạn nào</div>';
            return;
        }

        var totalAmount = 0, totalConfirmed = 0, totalPending = 0, totalRejected = 0, totalExpired = 0;
        snapshot.forEach(function(doc) {
            var d = doc.data();
            if (d.status === 'confirmed') { totalAmount += (d.amount || 0); totalConfirmed++; }
            else if (d.status === 'pending' || d.status === 'user_paid') totalPending++;
            else if (d.status === 'rejected') totalRejected++;
            else if (d.status === 'expired') totalExpired++;
        });

        var statsHtml = '<div class="renewal-history-stats">' +
            '<div class="rhs-item"><div class="rhs-label">Tổng chi tiêu</div><div class="rhs-value amount">' + formatMoney(totalAmount) + 'đ</div></div>' +
            '<div class="rhs-item"><div class="rhs-label">Số giao dịch</div><div class="rhs-value">' + snapshot.size + '</div></div>' +
            '<div class="rhs-item"><div class="rhs-label">Đã xác nhận</div><div class="rhs-value" style="color:var(--success)">' + totalConfirmed + '</div></div>' +
            '<div class="rhs-item"><div class="rhs-label">Chờ / Hủy / Hết hạn</div><div class="rhs-value" style="color:#f59e0b">' + totalPending + ' / ' + totalRejected + ' / ' + totalExpired + '</div></div></div>';

        var html = statsHtml;
        snapshot.forEach(function(doc) {
            var d = doc.data();
            html += buildHistoryItemHtml(d, true);
        });
        listEl.innerHTML = html;
    } catch(e) {
        console.error('Lỗi load lịch sử:', e);
        listEl.innerHTML = '<div class="no-data" style="padding:2rem 1rem;text-align:center;color:#dc2626">' +
            '<i class="fas fa-exclamation-triangle"></i> Lỗi tải dữ liệu: ' + escapeHtml(e.message) + '</div>';
    }
};

function buildHistoryItemHtml(d, showAdminInfo) {
    var created = d.createdAt ? d.createdAt.toDate() : null;
    var createdStr = created ? created.toLocaleString('vi-VN') : 'Không rõ';

    var statusMap = {
        'pending':   { text: '⏱ Chờ chuyển khoản', cls: 'pending' },
        'user_paid': { text: '⏳ Chờ xác nhận',     cls: 'user_paid' },
        'confirmed': { text: '✅ Đã xác nhận',      cls: 'confirmed' },
        'cancelled': { text: '🚫 Đã hủy',           cls: 'cancelled' },
        'rejected':  { text: '❌ Bị từ chối',       cls: 'rejected' },
        'expired':   { text: '⏰ Hết hạn (24h)',    cls: 'rejected' }
    };
    var st = statusMap[d.status] || { text: d.status || 'Không rõ', cls: 'pending' };
    var isPermanent = d.isPermanent || d.package === 'forever' || d.days >= 36500;

    var confirmInfo = '';
    if (d.confirmedAt) {
        var cf = d.confirmedAt.toDate ? d.confirmedAt.toDate() : null;
        if (cf) confirmInfo = '<div class="rh-date"><i class="fas fa-check-circle" style="color:#16a34a"></i> Xác nhận: ' + cf.toLocaleString('vi-VN') + (showAdminInfo && d.confirmedBy ? ' — bởi <b>' + escapeHtml(d.confirmedBy) + '</b>' : '') + '</div>';
    } else if (d.userConfirmedAt) {
        var ucf = d.userConfirmedAt.toDate ? d.userConfirmedAt.toDate() : null;
        if (ucf) confirmInfo = '<div class="rh-date"><i class="fas fa-clock" style="color:#f59e0b"></i> User xác nhận: ' + ucf.toLocaleString('vi-VN') + '</div>';
    } else if (d.rejectedAt) {
        var rj = d.rejectedAt.toDate ? d.rejectedAt.toDate() : null;
        if (rj) confirmInfo = '<div class="rh-date"><i class="fas fa-times-circle" style="color:#dc2626"></i> Từ chối: ' + rj.toLocaleString('vi-VN') + (d.rejectReason ? ' — ' + escapeHtml(d.rejectReason) : '') + '</div>';
    } else if (d.expiredAt) {
        var ex = d.expiredAt.toDate ? d.expiredAt.toDate() : null;
        if (ex) confirmInfo = '<div class="rh-date"><i class="fas fa-clock" style="color:#dc2626"></i> Hết hạn tự động: ' + ex.toLocaleString('vi-VN') + (d.expireReason ? ' — ' + escapeHtml(d.expireReason) : '') + '</div>';
    } else if (d.cancelledAt) {
        var cn = d.cancelledAt.toDate ? d.cancelledAt.toDate() : null;
        if (cn) confirmInfo = '<div class="rh-date"><i class="fas fa-ban" style="color:#94a3b8"></i> Hủy: ' + cn.toLocaleString('vi-VN') + (d.cancelledBy ? ' — ' + escapeHtml(d.cancelledBy) : '') + '</div>';
    }

    var newExpiryInfo = '';
    if (d.newExpiresAt) {
        var ne = d.newExpiresAt.toDate ? d.newExpiresAt.toDate() : null;
        if (ne) newExpiryInfo = '<div class="rh-date"><i class="fas fa-calendar-check" style="color:#16a34a"></i> Hạn mới: <b>' + ne.toLocaleDateString('vi-VN') + '</b></div>';
    }
    if (isPermanent) {
        newExpiryInfo += '<div class="rh-date"><i class="fas fa-crown" style="color:#dc2626"></i> <b>VĨNH VIỄN</b></div>';
    }

    return '<div class="renewal-history-item">' +
        '<div class="rh-head">' +
            '<div>' +
                '<div class="rh-pkg">' + escapeHtml(d.packageLabel || d.package || 'Gói') + (showAdminInfo && d.email ? ' — ' + escapeHtml(d.email) : '') + '</div>' +
                '<div class="rh-date"><i class="fas fa-clock"></i> ' + createdStr + '</div>' +
            '</div>' +
            '<div class="rh-amount">' + formatMoney(d.amount || 0) + 'đ</div>' +
        '</div>' +
        '<div><span class="rh-code">' + escapeHtml(d.transferCode || '—') + '</span></div>' +
        '<div class="rh-foot">' +
            '<span class="rh-status ' + st.cls + '">' + st.text + '</span>' +
            '<span>' + (isPermanent ? 'Vĩnh viễn' : (d.days || 0) + ' ngày') + '</span>' +
        '</div>' + confirmInfo + newExpiryInfo +
    '</div>';
}

/* ============ ADMIN PERMISSIONS UI ============ */
window.openPermissionModal = function(email) {
    if (!isSuperAdmin()) { alert('Chỉ Super Admin mới có quyền phân quyền!'); return; }
    var user = usersCache.find(function(u) { return u.email === email; });
    if (!user) return alert('Không tìm thấy user!');
    if (user.role !== 'admin') return alert('Chỉ phân quyền cho admin!');
    editingPermissionEmail = email;
    $('permissionName').textContent = user.name || email.split('@')[0];
    $('permissionEmail').textContent = email;
    var perms = user.permissions || {};
    var html = '';
    ADMIN_PERMISSIONS.forEach(function(p) {
        var value = (perms[p.key] === undefined) ? (DEFAULT_ADMIN_PERMS[p.key] === true) : (perms[p.key] === true);
        var checked = value ? 'checked' : '';
        var disabled = p.key === 'canManageAdmin' ? 'disabled' : '';
        html += '<div class="permission-item">' +
            '<div class="pi-info"><div class="pi-name">' + escapeHtml(p.name) + '</div>' +
            '<div class="pi-desc">' + escapeHtml(p.desc) + '</div></div>' +
            '<label class="pi-toggle"><input type="checkbox" data-perm="' + p.key + '" ' + checked + ' ' + disabled + '>' +
            '<span class="pi-slider"></span></label></div>';
    });
    $('permissionList').innerHTML = html;
    $('permissionModal').classList.add('show');
};

window.closePermissionModal = function() {
    $('permissionModal').classList.remove('show');
    editingPermissionEmail = null;
};

window.savePermissions = async function() {
    if (!editingPermissionEmail || !isSuperAdmin()) return;
    var perms = {};
    $('permissionList').querySelectorAll('input[data-perm]').forEach(function(cb) {
        perms[cb.dataset.perm] = cb.checked;
    });
    try {
        await db.collection('allowed_users').doc(editingPermissionEmail).update({
            permissions: perms, isSubAdmin: true
        });
        try { localStorage.removeItem('user_cache_' + editingPermissionEmail); } catch(e) {}
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        $('permissionModal').classList.remove('show');
        alert('✅ Đã lưu quyền!');
        loadUsers(true);
    } catch(e) { alert('❌ Lỗi: ' + e.message); }
};

/* ============ ADMIN PANEL INIT ============ */
function initAdminPanel() {
    if ($('openAdminBtn')) $('openAdminBtn').addEventListener('click', function() {
        $('userDropdown').classList.remove('show');
        try { sessionStorage.setItem('userDropdownClosed', '1'); } catch(_e) {}
        openAdminPanel();
    });
    if ($('adminClose')) $('adminClose').addEventListener('click', function() { $('adminModal').classList.remove('show'); });
    if ($('adminModal')) $('adminModal').addEventListener('click', function(e) { if (e.target === this) $('adminModal').classList.remove('show'); });
    if ($('refreshUsersBtn')) $('refreshUsersBtn').addEventListener('click', function() {
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        loadUsers(true);
    });
    if ($('exportExcelBtn')) $('exportExcelBtn').addEventListener('click', doExportExcel);
    if ($('importExcelBtn')) $('importExcelBtn').addEventListener('click', function() { $('importFileInput').click(); });
    if ($('importFileInput')) $('importFileInput').addEventListener('change', handleImportFileSelect);
    if ($('importClose')) $('importClose').addEventListener('click', function() { $('importModal').classList.remove('show'); importRows = []; });
    if ($('importCancelBtn')) $('importCancelBtn').addEventListener('click', function() { $('importModal').classList.remove('show'); importRows = []; });
    if ($('importModal')) $('importModal').addEventListener('click', function(e) { if (e.target === this) { $('importModal').classList.remove('show'); importRows = []; } });
    if ($('importConfirmBtn')) $('importConfirmBtn').addEventListener('click', doImport);

    if ($('showAddUserBtn')) $('showAddUserBtn').addEventListener('click', function() {
        $('addUserForm').classList.toggle('show');
        if ($('addUserForm').classList.contains('show')) $('newUserEmail').focus();
    });
    if ($('cancelAddUser')) $('cancelAddUser').addEventListener('click', function() {
        $('addUserForm').classList.remove('show');
        $('newUserEmail').value = ''; $('newUserName').value = '';
        $('newUserRole').value = 'user'; $('newUserExpires').value = '';
    });
    if ($('confirmAddUser')) $('confirmAddUser').addEventListener('click', doAddUser);

    if ($('adminSearchInput')) {
        $('adminSearchInput').addEventListener('input', function() {
            adminSearchQuery = this.value;
            var clearBtn = $('adminSearchClear');
            if (clearBtn) clearBtn.classList.toggle('show', this.value.length > 0);
            renderUsers(usersCache);
        });
    }
    if ($('adminSearchClear')) {
        $('adminSearchClear').addEventListener('click', function() {
            $('adminSearchInput').value = '';
            adminSearchQuery = '';
            this.classList.remove('show');
            renderUsers(usersCache);
        });
    }

    document.querySelectorAll('.admin-filter-btn[data-filter]').forEach(function(btn) {
        btn.addEventListener('click', function() {
            setAdminFilter(this.dataset.filter);
        });
    });

    if ($('refreshRenewalsBtn')) $('refreshRenewalsBtn').addEventListener('click', function() { loadRenewals(); });
    if ($('refreshRenewalHistoryBtn')) $('refreshRenewalHistoryBtn').addEventListener('click', function() { loadAdminRenewalHistory(); });

    function bindSectionToggle(btnId, sectionId, label) {
        var btn = $(btnId);
        var sec = $(sectionId);
        if (!btn || !sec) return;

        function syncState() {
            var isVisible = !sec.classList.contains('collapsed');
            var icon = btn.querySelector('i');
            if (icon) icon.className = isVisible ? 'fas fa-eye' : 'fas fa-eye-slash';
            btn.classList.toggle('active', isVisible);
            btn.title = (isVisible ? 'Ẩn ' : 'Hiện ') + (label || 'khung');
        }

        syncState();

        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            sec.classList.toggle('collapsed');
            syncState();
        });
    }

    bindSectionToggle('toggleRenewalsBtn', 'adminRenewalsSection', 'khung yêu cầu gia hạn');
    bindSectionToggle('toggleUsersBtn', 'adminUsersSection', 'danh sách tài khoản');
    bindSectionToggle('toggleLogsBtn', 'adminLogsSection', 'lịch sử đăng nhập');
    bindSectionToggle('toggleRenewalHistoryBtn', 'adminRenewalHistorySection', 'lịch sử gia hạn');

    if ($('permissionClose')) $('permissionClose').addEventListener('click', closePermissionModal);
    if ($('permissionCancel')) $('permissionCancel').addEventListener('click', closePermissionModal);
    if ($('permissionSave')) $('permissionSave').addEventListener('click', savePermissions);
    if ($('permissionModal')) $('permissionModal').addEventListener('click', function(e) { if (e.target === this) closePermissionModal(); });
}

async function doAddUser() {
    if (!isSuperAdmin() && !hasPermission('canAddUser')) {
        alert('Bạn không có quyền thêm user!');
        return;
    }
    var email = $('newUserEmail').value.trim().toLowerCase();
    var name = $('newUserName').value.trim();
    var role = $('newUserRole').value;
    var expiresVal = $('newUserExpires').value;

    if (!email || !email.includes('@')) { alert('Email không hợp lệ'); return; }
    if (!name) name = email.split('@')[0];
    if (role === 'admin' && !isSuperAdmin()) { alert('⚠️ Chỉ Super Admin mới có quyền thêm admin!'); return; }

    try {
        var docRef = db.collection('allowed_users').doc(email);
        var doc = await docRef.get();
        if (doc.exists) { alert('Email này đã tồn tại!'); return; }

        var setData = {
            email: email, name: name, role: role, tier: 'active',
            addedAt: firebase.firestore.FieldValue.serverTimestamp(),
            addedBy: currentUser.email
        };
        if (role === 'admin') {
            setData.isSubAdmin = true;
            setData.permissions = Object.assign({}, DEFAULT_ADMIN_PERMS);
        }
        if (expiresVal && role !== 'admin') {
            var d = new Date(expiresVal + 'T23:59:59');
            if (!isNaN(d.getTime())) setData.expiresAt = firebase.firestore.Timestamp.fromDate(d);
        } else if (role !== 'admin') {
            setData.isPermanent = true;
        }
        await docRef.set(setData);
        $('addUserForm').classList.remove('show');
        $('newUserEmail').value = ''; $('newUserName').value = '';
        $('newUserRole').value = 'user'; $('newUserExpires').value = '';
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        loadUsers(true);
    } catch(e) { alert('Lỗi: ' + e.message); }
}

function openAdminPanel() {
    if (!currentUser || currentUser.role !== 'admin') return;
    $('adminModal').classList.add('show');

    var canIE = isSuperAdmin() || hasPermission('canImportExport');
    if ($('exportExcelBtn')) $('exportExcelBtn').style.display = canIE ? 'inline-flex' : 'none';
    if ($('importExcelBtn')) $('importExcelBtn').style.display = canIE ? 'inline-flex' : 'none';

    var canAdd = isSuperAdmin() || hasPermission('canAddUser');
    if ($('showAddUserBtn')) $('showAddUserBtn').style.display = canAdd ? 'inline-flex' : 'none';

    loadUsers(false);
    loadLogs();
    loadRenewals();
    loadAdminRenewalHistory();
}

function loadUsers(forceRefresh) {
    var cacheKey = 'admin_users_cache';
    if (forceRefresh) { try { localStorage.removeItem(cacheKey); } catch(e) {} }

    if (!forceRefresh) {
        try {
            var cached = JSON.parse(localStorage.getItem(cacheKey) || 'null');
            if (cached && cached.expires > Date.now() && cached.data && Array.isArray(cached.data)) {
                usersCache = cached.data;
                renderUsers(usersCache);
                renderAdminStats();
                loadLastLoginMap();
                return;
            }
        } catch(e) { try { localStorage.removeItem(cacheKey); } catch(e2) {} }
    }

    $('userList').innerHTML = '<div class="no-data"><i class="fas fa-spinner fa-pulse"></i><span>Đang tải...</span></div>';
    db.collection('allowed_users').get().then(function(snapshot) {
        usersCache = [];
        snapshot.forEach(function(doc) {
            var data = doc.data() || {};
            usersCache.push({
                email: doc.id,
                name: data.name || '',
                role: data.role || 'user',
                expiresAt: data.expiresAt || null,
                tier: data.tier || 'active',
                isTrial: data.isTrial || false,
                isPermanent: data.isPermanent || false,
                isSubAdmin: data.isSubAdmin || false,
                permissions: data.permissions || null
            });
        });
        usersCache.sort(function(a, b) { return (a.email || '').localeCompare(b.email || ''); });
        try {
            localStorage.setItem(cacheKey, JSON.stringify({ data: usersCache, expires: Date.now() + 5 * 60 * 1000 }));
        } catch(e) {}
        renderUsers(usersCache);
        renderAdminStats();
        return loadLastLoginMap();
    }).catch(function(err) {
        $('userList').innerHTML = '<div class="no-data" style="color:#dc2626"><i class="fas fa-exclamation-triangle"></i><span>Lỗi: ' + err.message + '</span></div>';
    });
}

function loadLastLoginMap() {
    var hidden = isHiddenAdmin();
    var myEmail = (currentUser && currentUser.email ? currentUser.email.toLowerCase() : '');
    return db.collection('login_logs').orderBy('time', 'desc').limit(500).get().then(function(snapshot) {
        lastLoginMap = {};
        snapshot.forEach(function(doc) {
            var d = doc.data();
            var email = (d.email || '').toLowerCase();
            if (hidden && d.role === 'admin' && email !== myEmail) return;
            if (!lastLoginMap[email] && d.time) lastLoginMap[email] = d.time.toDate();
        });
        renderUsers(usersCache);
    }).catch(function() {});
}

function renderAdminStats() {
    var usersOnly = usersCache.filter(function(u) { return u.role !== 'admin'; });
    var users = usersOnly.length;
    var admins = usersCache.length - users;

    var summaryUsers = $('summaryTotalUsers');
    if (summaryUsers) summaryUsers.textContent = users;

    var summaryAdminItem = $('summaryAdminItem');
    var summaryAdmins = $('summaryTotalAdmins');
    if (summaryAdminItem && summaryAdmins) {
        if (isSuperAdmin()) {
            summaryAdminItem.style.display = 'flex';
            summaryAdmins.textContent = admins;
        } else {
            summaryAdminItem.style.display = 'none';
        }
    }

    var adminUserCountEl = $('adminUserCount');
    if (adminUserCountEl) adminUserCountEl.textContent = users;
    updateFilterCounts(usersCache);
}

function renderUsers(items) {
    var list = $('userList');
    var hidden = isHiddenAdmin();
    var superAdmin = isSuperAdmin();
    var myEmail = (currentUser && currentUser.email ? currentUser.email.toLowerCase() : '');

    var displayItems = items;
    if (hidden) {
        displayItems = items.filter(function(u) {
            var uEmail = (u.email || '').toLowerCase();
            if (u.role === 'admin' && uEmail !== myEmail) return false;
            return true;
        });
    }
    displayItems = filterUsers(displayItems);
    displayItems = sortUsersForDisplay(displayItems);

    if (!displayItems.length) {
        var msg = adminSearchQuery ? 'Không tìm thấy kết quả cho "' + escapeHtml(adminSearchQuery) + '"' : 'Không có user nào';
        list.innerHTML = '<div class="no-data"><i class="fas fa-search"></i><span>' + msg + '</span></div>';
        return;
    }

    var now = Date.now();
    var day7 = 7 * 24 * 60 * 60 * 1000;
    var day30 = 30 * 24 * 60 * 60 * 1000;

    list.innerHTML = displayItems.map(function(u) {
        var isMe = u.email === currentUser.email;
        var isAdmin = u.role === 'admin';
        var targetIsSuper = (u.email || '').toLowerCase() === SUPER_ADMIN.toLowerCase();
        var targetIsSubAdmin = isAdmin && u.isSubAdmin && !targetIsSuper;
        var canModifyAdmin = superAdmin && isAdmin && !isMe && !targetIsSuper;

        var roleBtn = isAdmin
            ? (canModifyAdmin
                ? '<button class="u-btn" onclick="changeRole(\'' + escapeJs(u.email) + '\', \'user\')" title="Hạ xuống User"><i class="fas fa-user"></i></button>'
                : '<button class="u-btn" disabled title="Không thể hạ quyền"><i class="fas fa-user"></i></button>')
            : (superAdmin
                ? '<button class="u-btn" onclick="changeRole(\'' + escapeJs(u.email) + '\', \'admin\')" title="Nâng lên Admin"><i class="fas fa-shield-alt"></i></button>'
                : '<button class="u-btn" disabled title="Chỉ Super Admin"><i class="fas fa-shield-alt"></i></button>');

        var permBtn = '';
        if (superAdmin && targetIsSubAdmin) {
            permBtn = '<button class="u-btn" style="background:rgba(6,182,212,.1);color:#06b6d4;border-color:rgba(6,182,212,.4);" onclick="openPermissionModal(\'' + escapeJs(u.email) + '\')" title="Phân quyền"><i class="fas fa-user-shield"></i></button>';
        }

        var canDelete = superAdmin || hasPermission('canDeleteUser');
        var deleteBtn = isMe
            ? '<button class="u-btn danger" disabled title="Không thể tự xóa"><i class="fas fa-trash"></i></button>'
            : (targetIsSuper
                ? '<button class="u-btn danger" disabled title="Không thể xóa Super Admin"><i class="fas fa-trash"></i></button>'
                : (isAdmin
                    ? (canModifyAdmin
                        ? '<button class="u-btn danger" onclick="deleteUser(\'' + escapeJs(u.email) + '\')" title="Xóa"><i class="fas fa-trash"></i></button>'
                        : '<button class="u-btn danger" disabled title="Chỉ Super Admin"><i class="fas fa-trash"></i></button>')
                    : (canDelete
                        ? '<button class="u-btn danger" onclick="deleteUser(\'' + escapeJs(u.email) + '\')" title="Xóa"><i class="fas fa-trash"></i></button>'
                        : '<button class="u-btn danger" disabled title="Không có quyền xóa"><i class="fas fa-trash"></i></button>')));

        var expiryBtn = '';
        if (!isAdmin) {
            var btnCls = 'u-btn expiry';
            var tooltip = 'Chỉnh hạn sử dụng';
            if (u.isPermanent) tooltip = 'Chỉnh hạn (Vĩnh viễn 💎)';
            else if (u.expiresAt) {
                var d = getExpiryDate(u.expiresAt);
                if (d && !isNaN(d.getTime())) {
                    var daysLeftExp = Math.ceil((d.getTime() - Date.now()) / (24 * 60 * 60 * 1000));
                    tooltip = 'Chỉnh hạn (còn ' + Math.max(0, daysLeftExp) + ' ngày)';
                    if (daysLeftExp <= 7) btnCls += ' urgent';
                }
            } else tooltip = 'Chỉnh hạn (Vĩnh viễn)';
            expiryBtn = '<button class="' + btnCls + '" onclick="openEditExpiry(\'' + escapeJs(u.email) + '\')" title="' + escapeHtml(tooltip) + '"><i class="fas fa-calendar-alt"></i></button>';
        }

        var historyBtn = '';
        if (!targetIsSuper || isMe) {
            historyBtn = '<button class="u-btn history" onclick="openUserRenewalHistory(\'' + escapeJs(u.email) + '\')" title="Xem lịch sử gia hạn"><i class="fas fa-history"></i></button>';
        }

        var last = lastLoginMap[(u.email || '').toLowerCase()];
        var lastLoginHtml = last
            ? '<div class="u-last-login ' + ((now - last.getTime()) <= day7 ? 'active' : ((now - last.getTime()) <= day30 ? 'recent' : '')) + '"><i class="fas fa-clock"></i> ' + formatTimeDiff(now - last.getTime()) + '</div>'
            : '<div class="u-last-login"><i class="fas fa-times-circle"></i> Chưa đăng nhập</div>';

        var expiryHtml = '';
        if (isAdmin) expiryHtml = '<div class="u-expiry permanent"><i class="fas fa-infinity"></i> Vĩnh viễn</div>';
        else if (u.isPermanent) expiryHtml = '<div class="u-expiry permanent perm" onclick="openEditExpiry(\'' + escapeJs(u.email) + '\')"><i class="fas fa-crown"></i> 💎 Vĩnh viễn</div>';
        else if (!u.expiresAt) expiryHtml = '<div class="u-expiry permanent" onclick="openEditExpiry(\'' + escapeJs(u.email) + '\')"><i class="fas fa-infinity"></i> Vĩnh viễn</div>';
        else {
            var expDate = getExpiryDate(u.expiresAt);
            if (expDate && !isNaN(expDate.getTime())) {
                var daysLeft = Math.ceil((expDate.getTime() - now) / (24 * 60 * 60 * 1000));
                var expCls = 'ok', expIcon = 'fa-calendar-check', expText = 'Còn ' + daysLeft + ' ngày';
                if (daysLeft < 0) { expCls = 'expired'; expIcon = 'fa-calendar-times'; expText = 'Hết hạn ' + Math.abs(daysLeft) + ' ngày'; }
                else if (daysLeft === 0) { expCls = 'urgent'; expIcon = 'fa-exclamation-circle'; expText = 'Hết hạn hôm nay'; }
                else if (daysLeft <= 3) { expCls = 'urgent'; expIcon = 'fa-exclamation-circle'; }
                else if (daysLeft <= 7) { expCls = 'warn'; expIcon = 'fa-clock'; }
                var tierPrefix = (u.tier === 'trial' || u.isTrial) ? '🎁 ' : '';
                expiryHtml = '<div class="u-expiry ' + expCls + '" onclick="openEditExpiry(\'' + escapeJs(u.email) + '\')"><i class="fas ' + expIcon + '"></i> ' + tierPrefix + expText + ' • ' + expDate.toLocaleDateString('vi-VN') + '</div>';
            }
        }

        var roleBadge;
        if (isAdmin) {
            if (targetIsSuper) roleBadge = '<span class="u-role super">👑 super</span>';
            else if (targetIsSubAdmin) roleBadge = '<span class="u-role subadmin">🛡 sub</span>';
            else roleBadge = '<span class="u-role admin">admin</span>';
        } else if (u.isPermanent) {
            roleBadge = '<span class="u-role perm">💎 perm</span>';
        } else if (u.tier === 'trial' || u.isTrial) {
            roleBadge = '<span class="u-role trial">🎁 trial</span>';
        } else {
            roleBadge = '<span class="u-role user">user</span>';
        }

        return '<div class="user-row" data-email="' + escapeHtml(u.email) + '">' +
            '<div class="u-info">' +
                '<div class="u-name">' + escapeHtml(u.name || u.email.split('@')[0]) + (isMe ? ' <span style="color:#94a3b8;font-size:.7rem">(bạn)</span>' : '') + '</div>' +
                '<div class="u-email">' + escapeHtml(u.email) + '</div>' +
                lastLoginHtml + expiryHtml +
            '</div>' + roleBadge +
            '<div class="u-actions">' + historyBtn + permBtn + expiryBtn + roleBtn + deleteBtn + '</div>' +
        '</div>';
    }).join('');
}

window.changeRole = async function(email, newRole) {
    var target = usersCache.find(function(u) { return u.email === email; });
    if (!target) return alert('Không tìm thấy user!');
    var isMe = email === currentUser.email;
    var isAdmin = target.role === 'admin';
    var superAdmin = isSuperAdmin();
    var targetIsSuper = (email || '').toLowerCase() === SUPER_ADMIN.toLowerCase();
    if (isMe && newRole === 'user') return alert('⚠️ Không thể tự hạ quyền!');
    if (targetIsSuper) return alert('⚠️ Không thể thay đổi Super Admin!');
    if (isAdmin && newRole === 'user' && !superAdmin) return alert('⚠️ Chỉ Super Admin!');
    if (!isAdmin && newRole === 'admin' && !superAdmin) return alert('⚠️ Chỉ Super Admin!');
    var action = newRole === 'admin' ? 'NÂNG LÊN ADMIN' : 'HẠ XUỐNG USER';
    if (!confirm(action + ' cho:\n\n' + email + ' ?')) return;
    try {
        var updateData = { role: newRole };
        if (newRole === 'admin') {
            updateData.isSubAdmin = true;
            updateData.permissions = Object.assign({}, DEFAULT_ADMIN_PERMS);
        } else {
            updateData.isSubAdmin = false;
            updateData.permissions = null;
        }
        await db.collection('allowed_users').doc(email).update(updateData);
        try { localStorage.removeItem('user_cache_' + email); } catch(e) {}
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        loadUsers(true);
    } catch(e) { alert('Lỗi: ' + e.message); }
};

window.deleteUser = async function(email) {
    if (!isSuperAdmin() && !hasPermission('canDeleteUser')) {
        alert('Bạn không có quyền xóa user!');
        return;
    }
    var target = usersCache.find(function(u) { return u.email === email; });
    if (!target) return alert('Không tìm thấy user!');
    var isMe = email === currentUser.email;
    var isAdmin = target.role === 'admin';
    var superAdmin = isSuperAdmin();
    var targetIsSuper = (email || '').toLowerCase() === SUPER_ADMIN.toLowerCase();
    if (isMe) return alert('⚠️ Không thể tự xóa!');
    if (targetIsSuper) return alert('⚠️ Không thể xóa Super Admin!');
    if (isAdmin && !superAdmin) return alert('⚠️ Chỉ Super Admin!');
    if (!confirm('⚠️ XÓA\n\n' + email + '\n\nNgười này sẽ không đăng nhập được nữa.\n\nTiếp tục?')) return;
    try {
        await db.collection('allowed_users').doc(email).delete();
        try { localStorage.removeItem('user_cache_' + email); } catch(e) {}
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        loadUsers(true);
    } catch(e) { alert('Lỗi: ' + e.message); }
};

function loadLogs() {
    if (!isSuperAdmin() && !hasPermission('canViewLogs')) {
        var logsSection = $('adminLogsSection');
        if (logsSection) logsSection.style.display = 'none';
        return;
    }
    var logsSection = $('adminLogsSection');
    if (logsSection) logsSection.style.display = '';
    db.collection('login_logs').orderBy('time', 'desc').limit(30).get().then(function(snapshot) {
        if (snapshot.empty) {
            $('logsList').innerHTML = '<div class="no-data"><i class="fas fa-inbox"></i><span>Chưa có log</span></div>';
            return;
        }
        var html = '';
        snapshot.forEach(function(doc) {
            var d = doc.data();
            var time = d.time ? new Date(d.time.toDate()).toLocaleString('vi-VN') : 'N/A';
            html += '<div class="log-item"><span class="log-time">' + time + '</span><span class="log-msg"><b>' + escapeHtml(d.name || d.email) + '</b> (' + escapeHtml(d.role || 'user') + ')</span></div>';
        });
        $('logsList').innerHTML = html;
    }).catch(function(err) {
        $('logsList').innerHTML = '<div class="no-data" style="color:#dc2626"><i class="fas fa-exclamation-triangle"></i><span>Lỗi: ' + err.message + '</span></div>';
    });
}

function buildRenewalRowHtml(d, isPending) {
    var created = d.createdAt ? d.createdAt.toDate() : new Date();
    var timeStr = formatTimeDiff(Date.now() - created.getTime());
    var isPermanent = d.isPermanent || d.package === 'forever' || d.days >= 36500;
    var canApprove = isSuperAdmin() || hasPermission('canRenew');

    var hoursOld = Math.floor((Date.now() - created.getTime()) / 3600000);
    var hoursLeft = Math.max(0, 24 - hoursOld);

    var statusCls, statusText;
    if (d.status === 'user_paid') { statusCls = 'user_paid'; statusText = '⏳ Chờ xác nhận'; }
    else if (d.status === 'pending') { statusCls = 'pending'; statusText = '⏱ Chờ CK'; }
    else { statusCls = 'confirmed'; statusText = '✅ Đã xác nhận'; }

    var actionBtns = '';
    if (isPending) {
        actionBtns = canApprove
            ? '<button class="btn primary" style="padding:.4rem .75rem;font-size:.75rem" onclick="approveRenewal(\'' + escapeJs(d._id) + '\')"><i class="fas fa-check"></i> Xác nhận</button>' +
              '<button class="btn" style="padding:.4rem .65rem;font-size:.75rem" onclick="rejectRenewal(\'' + escapeJs(d._id) + '\')"><i class="fas fa-times"></i></button>'
            : '<span style="font-size:.72rem;color:var(--text-3)">Không có quyền duyệt</span>';
    } else {
        var confirmedBy = d.confirmedBy ? 'bởi <b>' + escapeHtml(d.confirmedBy) + '</b>' : '';
        var confirmedTime = d.confirmedAt ? (d.confirmedAt.toDate ? d.confirmedAt.toDate().toLocaleString('vi-VN') : '') : '';
        actionBtns = '<span style="font-size:.7rem;color:var(--text-3)">' + confirmedTime + ' ' + confirmedBy + '</span>' +
                     '<button class="btn" style="padding:.35rem .65rem;font-size:.72rem" onclick="openUserRenewalHistory(\'' + escapeJs(d.email) + '\')"><i class="fas fa-history"></i></button>';
    }

    var newExpiryInfo = '';
    if (d.newExpiresAt) {
        var ne = d.newExpiresAt.toDate ? d.newExpiresAt.toDate() : null;
        if (ne) newExpiryInfo = '<div class="rar-sub" style="color:#16a34a"><i class="fas fa-calendar-check"></i> Hạn mới: <b>' + ne.toLocaleDateString('vi-VN') + '</b></div>';
    }
    if (isPermanent) {
        newExpiryInfo = '<div class="rar-sub" style="color:#dc2626"><i class="fas fa-crown"></i> <b>💎 VĨNH VIỄN</b></div>';
    }

    var timeWarnHtml = '';
    if (isPending && hoursLeft <= 6) {
        timeWarnHtml = '<div class="rar-sub" style="color:#dc2626;font-weight:700"><i class="fas fa-exclamation-triangle"></i> Còn ' + hoursLeft + 'h sẽ tự động hủy!</div>';
    } else if (isPending) {
        timeWarnHtml = '<div class="rar-sub" style="color:#f59e0b"><i class="fas fa-clock"></i> Còn ' + hoursLeft + 'h trước khi hết hạn</div>';
    }

    return '<div class="renewal-admin-row">' +
        '<div class="rar-head">' +
            '<div>' +
                '<div class="rar-email">' + escapeHtml(d.name || d.email) + '</div>' +
                '<div class="u-email">' + escapeHtml(d.email) + '</div>' +
                '<div class="rar-sub"><i class="fas fa-clock"></i> ' + timeStr + '</div>' +
                newExpiryInfo +
                timeWarnHtml +
            '</div>' +
            '<div class="rar-pkg">' +
                '<div class="rar-amount">' + formatMoney(d.amount) + 'đ</div>' +
                '<div class="rar-pkg-label">' + escapeHtml(d.packageLabel || d.package) +
                    (isPermanent ? ' · <b style="color:#dc2626">💎 VĨNH VIỄN</b>' : ' · ' + d.days + ' ngày') +
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="rar-foot">' +
            '<div>Mã: <span class="rar-code">' + escapeHtml(d.transferCode) + '</span></div>' +
            '<div class="rar-actions">' +
                '<span class="rar-status ' + statusCls + '">' + statusText + '</span>' +
                actionBtns +
            '</div>' +
        '</div>' +
    '</div>';
}

function loadRenewals() {
    if (!isSuperAdmin() && !hasPermission('canRenew')) {
        var renewalsSection = $('adminRenewalsSection');
        if (renewalsSection) renewalsSection.style.display = 'none';
        return;
    }
    var renewalsSection = $('adminRenewalsSection');
    if (renewalsSection) renewalsSection.style.display = '';

    var listEl = $('renewalsList');

    db.collection('renewal_requests').orderBy('createdAt', 'desc').limit(200).get().then(function(snapshot) {
        pendingRenewalsData = [];
        confirmedRenewalsData = [];
        snapshot.forEach(function(doc) {
            var d = doc.data();
            var item = Object.assign({ _id: doc.id }, d);
            if (d.status === 'pending' || d.status === 'user_paid') pendingRenewalsData.push(item);
            else if (d.status === 'confirmed') confirmedRenewalsData.push(item);
        });

        var pBadge = $('pendingRenewalsBadge');
        if (pBadge) {
            pBadge.textContent = pendingRenewalsData.length;
            pBadge.classList.toggle('pulse', pendingRenewalsData.length > 0);
        }
        var cBadge = $('confirmedRenewalsBadge');
        if (cBadge) cBadge.textContent = confirmedRenewalsData.length;
        var pTab = $('pendingCountTab');
        if (pTab) pTab.textContent = pendingRenewalsData.length;
        var cTab = $('confirmedCountTab');
        if (cTab) cTab.textContent = confirmedRenewalsData.length;

        var section = $('adminRenewalsSection');
        if (section) {
            section.classList.toggle('has-pending', pendingRenewalsData.length > 0);
        }
        if (pendingRenewalsData.length > 0 && renewalTab === 'confirmed') {
            renewalTab = 'pending';
        }
        document.querySelectorAll('[data-renewal-tab]').forEach(function(btn) {
            btn.classList.toggle('active', btn.dataset.renewalTab === renewalTab);
        });

        renderRenewalsList();

        if (pendingRenewalsData.length > 0 && section && !window.__hasScrolledToRenewals) {
            window.__hasScrolledToRenewals = true;
            setTimeout(function() {
                section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 500);
        }
    }).catch(function(err) {
        if (listEl) listEl.innerHTML = '<div class="no-data" style="color:#dc2626"><i class="fas fa-exclamation-triangle"></i><span>Lỗi: ' + escapeHtml(err.message) + '</span></div>';
    });
}

function renderRenewalsList() {
    var listEl = $('renewalsList');
    if (!listEl) return;
    var items = (renewalTab === 'pending') ? pendingRenewalsData : confirmedRenewalsData;
    var isPending = (renewalTab === 'pending');

    if (items.length === 0) {
        listEl.innerHTML = '<div class="no-data"><i class="fas fa-inbox"></i><span>' +
            (isPending ? 'Không có yêu cầu nào đang chờ' : 'Chưa có giao dịch nào đã xác nhận') + '</span></div>';
        return;
    }
    var html = '';
    items.forEach(function(d) { html += buildRenewalRowHtml(d, isPending); });
    listEl.innerHTML = html;
}

window.setRenewalTab = function(tab) {
    renewalTab = tab;
    document.querySelectorAll('[data-renewal-tab]').forEach(function(btn) {
        btn.classList.toggle('active', btn.dataset.renewalTab === tab);
    });
    renderRenewalsList();
};

window.loadRenewals = loadRenewals;

function loadPendingRenewals() { loadRenewals(); }
function loadConfirmedRenewals() { loadRenewals(); }

function loadAdminRenewalHistory() {
    if (!isSuperAdmin() && !hasPermission('canRenew')) {
        var histSection = $('adminRenewalHistorySection');
        if (histSection) histSection.style.display = 'none';
        return;
    }
    var histSection = $('adminRenewalHistorySection');
    if (histSection) histSection.style.display = '';

    var listEl = $('adminRenewalHistoryList');
    if (!listEl) return;

    db.collection('renewal_requests').orderBy('createdAt', 'desc').limit(100).get().then(function(snapshot) {
        if (snapshot.empty) {
            listEl.innerHTML = '<div class="no-data"><i class="fas fa-inbox"></i><span>Chưa có giao dịch nào</span></div>';
            return;
        }
        var html = '';
        snapshot.forEach(function(doc) {
            var d = doc.data();
            html += buildHistoryItemHtml(d, true);
        });
        listEl.innerHTML = html;
    }).catch(function(err) {
        listEl.innerHTML = '<div class="no-data" style="color:#dc2626"><i class="fas fa-exclamation-triangle"></i><span>Lỗi: ' + escapeHtml(err.message) + '</span></div>';
    });
}

window.approveRenewal = async function(reqId) {
    if (!isSuperAdmin() && !hasPermission('canRenew')) {
        alert('Bạn không có quyền duyệt gia hạn!');
        return;
    }
    if (!confirm('Xác nhận đã nhận tiền và gia hạn?')) return;
    try {
        var reqDoc = await db.collection('renewal_requests').doc(reqId).get();
        if (!reqDoc.exists) return alert('Không tìm thấy yêu cầu!');
        var req = reqDoc.data();

        if (req.status === 'expired') {
            alert('⚠️ Lệnh này đã hết hạn (quá 24h). Không thể xác nhận.');
            loadRenewals();
            return;
        }

        var isPermanent = (req.package === 'forever') || (req.days >= 36500) || req.isPermanent;
        var userDoc = await db.collection('allowed_users').doc(req.email).get();
        var currentExpiry = null;
        if (userDoc.exists) {
            var ud = userDoc.data();
            if (ud.expiresAt) currentExpiry = getExpiryDate(ud.expiresAt);
        }
        var updateData = { isTrial: false, tier: 'active', lastRenewalAt: firebase.firestore.FieldValue.serverTimestamp() };
        var reqUpdateData = { status: 'confirmed', confirmedAt: firebase.firestore.FieldValue.serverTimestamp(), confirmedBy: currentUser.email };
        var message = '';
        var _newExpiryStr = '';

        if (isPermanent) {
            updateData.expiresAt = null;
            updateData.isPermanent = true;
            updateData.permanentSince = firebase.firestore.FieldValue.serverTimestamp();
            reqUpdateData.newExpiresAt = null;
            reqUpdateData.isPermanent = true;
            message = '💎 Đã kích hoạt VĨNH VIỄN cho:\n\n' + req.email;
        } else {
            var now = new Date();
            var baseDate = (currentExpiry && currentExpiry > now) ? currentExpiry : now;
            var newExpiry = new Date(baseDate.getTime() + req.days * 24 * 60 * 60 * 1000);
            updateData.expiresAt = firebase.firestore.Timestamp.fromDate(newExpiry);
            updateData.isPermanent = false;
            reqUpdateData.newExpiresAt = firebase.firestore.Timestamp.fromDate(newExpiry);
            reqUpdateData.isPermanent = false;
            _newExpiryStr = newExpiry.toLocaleDateString('vi-VN');
            message = '✅ Đã gia hạn ' + req.days + ' ngày cho:\n' + req.email + '\n\nHạn mới: ' + _newExpiryStr;
        }
        await db.collection('allowed_users').doc(req.email).update(updateData);
        await db.collection('renewal_requests').doc(reqId).update(reqUpdateData);

        if (typeof window.notifyTelegramAdminConfirmed === 'function') {
            try {
                window.notifyTelegramAdminConfirmed({
                    email: req.email, name: req.name, amount: req.amount,
                    package: req.package, packageLabel: req.packageLabel,
                    days: req.days, isPermanent: isPermanent
                }, _newExpiryStr);
            } catch(_te) {}
        }
        try { localStorage.removeItem('user_cache_' + req.email); } catch(e) {}
        alert(message);
        loadRenewals();
        loadAdminRenewalHistory();
        loadUsers(true);
    } catch(e) { alert('❌ Lỗi: ' + e.message); }
};

window.rejectRenewal = async function(reqId) {
    if (!isSuperAdmin() && !hasPermission('canRenew')) {
        alert('Bạn không có quyền duyệt gia hạn!');
        return;
    }
    var reason = prompt('Lý do từ chối (tùy chọn):', '');
    if (reason === null) return;
    try {
        await db.collection('renewal_requests').doc(reqId).update({
            status: 'rejected',
            rejectedAt: firebase.firestore.FieldValue.serverTimestamp(),
            rejectedBy: currentUser.email,
            rejectReason: reason || ''
        });
        loadRenewals();
    } catch(e) { alert('❌ Lỗi: ' + e.message); }
};

window.openEditExpiry = function(email) {
    var user = usersCache.find(function(u) { return u.email === email; });
    if (!user) return alert('Không tìm thấy user!');
    if (user.role === 'admin') return alert('Admin có hạn vĩnh viễn!');
    editingExpiryEmail = email;
    $('editExpiryName').textContent = user.name || email.split('@')[0];
    $('editExpiryEmail').textContent = email;
    if (user.isPermanent) $('editExpiryInput').value = '';
    else if (user.expiresAt) {
        var d = getExpiryDate(user.expiresAt);
        $('editExpiryInput').value = (d && !isNaN(d.getTime())) ? formatDate(d) : '';
    } else $('editExpiryInput').value = '';
    $('editExpiryModal').classList.add('show');
};
window.setQuickExpiry = function(days) {
    var d = new Date();
    d.setDate(d.getDate() + days);
    d.setHours(23, 59, 59);
    $('editExpiryInput').value = formatDate(d);
};
window.setQuickExpiryPermanent = function() { $('editExpiryInput').value = ''; };

async function doUpdateExpiry() {
    if (!editingExpiryEmail) return;
    var dateVal = $('editExpiryInput').value;
    var updateData = {};
    if (dateVal) {
        var d = new Date(dateVal + 'T23:59:59');
        if (isNaN(d.getTime())) return alert('Ngày không hợp lệ!');
        updateData.expiresAt = firebase.firestore.Timestamp.fromDate(d);
        updateData.isPermanent = false;
    } else {
        updateData.expiresAt = null;
        updateData.isPermanent = true;
    }
    var btn = $('editExpiryConfirm');
    btn.disabled = true;
    var originalHtml = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang lưu...';
    try {
        await db.collection('allowed_users').doc(editingExpiryEmail).update(updateData);
        try { localStorage.removeItem('user_cache_' + editingExpiryEmail); } catch(e) {}
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        $('editExpiryModal').classList.remove('show');
        alert(dateVal ? '✅ Đã cập nhật hạn đến ' + new Date(dateVal).toLocaleDateString('vi-VN') : '💎 Đã đặt thành vĩnh viễn');
        loadUsers(true);
    } catch(err) { alert('❌ Lỗi: ' + err.message); }
    finally { btn.disabled = false; btn.innerHTML = originalHtml; }
}

async function doChangeName() {
    if (!editingEmail) return;
    var newName = $('changeNameInput').value.trim();
    if (!newName) return alert('Tên không được để trống!');
    if (newName.length > 50) return alert('Tên quá dài!');
    var btn = $('changeNameConfirm');
    btn.disabled = true;
    var originalHtml = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang lưu...';
    try {
        await db.collection('allowed_users').doc(editingEmail).update({ name: newName });
        try { localStorage.removeItem('user_cache_' + editingEmail); } catch(e) {}
        try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
        if (currentUser && currentUser.email === editingEmail) {
            currentUser.name = newName;
            $('userName').textContent = newName;
        }
        $('changeNameModal').classList.remove('show');
        alert('✅ Đã đổi tên!');
        if ($('adminModal').classList.contains('show')) loadUsers(true);
    } catch(err) { alert('❌ Lỗi: ' + err.message); }
    finally { btn.disabled = false; btn.innerHTML = originalHtml; }
}

function doExportExcel() {
    if (!isSuperAdmin() && !hasPermission('canImportExport')) {
        alert('Bạn không có quyền Export!');
        return;
    }
    var usersOnly = usersCache.filter(function(u) { return u.role !== 'admin'; });
    if (!usersOnly.length) return alert('Không có user nào để export!');
    try {
        var wb = XLSX.utils.book_new();
        var now = Date.now();
        var COLUMNS = [
            { header: 'STT', width: 6 }, { header: 'email', width: 35 },
            { header: 'name', width: 25 }, { header: 'expiresAt', width: 14 },
            { header: 'Trạng thái', width: 22 }
        ];
        var aoa = [COLUMNS.map(function(c) { return c.header; })];
        usersOnly.forEach(function(u) {
            var expDate = getExpiryDate(u.expiresAt);
            var expStr = '', statusStr = '';
            if (u.isPermanent || !expDate) statusStr = '💎 Vĩnh viễn';
            else {
                expStr = formatDate(expDate);
                var daysLeft = Math.ceil((expDate.getTime() - now) / (24 * 60 * 60 * 1000));
                var prefix = (u.tier === 'trial' || u.isTrial) ? '🎁 Trial ' : '';
                if (daysLeft < 0) statusStr = '❌ Hết hạn ' + Math.abs(daysLeft) + ' ngày';
                else if (daysLeft <= 3) statusStr = prefix + '🔴 Còn ' + daysLeft + ' ngày';
                else if (daysLeft <= 7) statusStr = prefix + '🟡 Còn ' + daysLeft + ' ngày';
                else statusStr = prefix + '🟢 Còn ' + daysLeft + ' ngày';
            }
            aoa.push(['', u.email || '', u.name || '', expStr, statusStr]);
        });
        var ws = XLSX.utils.aoa_to_sheet(aoa);
        ws['!cols'] = COLUMNS.map(function(c) { return { wch: c.width }; });
        XLSX.utils.book_append_sheet(wb, ws, 'Users');
        var today = new Date();
        var dateStr = today.getFullYear() + String(today.getMonth() + 1).padStart(2, '0') + String(today.getDate()).padStart(2, '0');
        XLSX.writeFile(wb, 'users_export_' + dateStr + '.xlsx');
    } catch(err) { alert('❌ Lỗi export: ' + err.message); }
}

function handleImportFileSelect(e) {
    var file = e.target.files[0];
    if (!file) return;
    var reader = new FileReader();
    reader.onload = function(evt) {
        try {
            var data = new Uint8Array(evt.target.result);
            var workbook = XLSX.read(data, { type: 'array' });
            var sheet = workbook.Sheets[workbook.SheetNames[0]];
            var rows = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '' });
            processImport(rows);
        } catch(err) { alert('❌ Lỗi đọc file: ' + err.message); }
        e.target.value = '';
    };
    reader.readAsArrayBuffer(file);
}

function processImport(rows) {
    if (!rows || rows.length < 2) return alert('❌ File rỗng!');
    var headerRowIdx = -1;
    for (var i = 0; i < Math.min(5, rows.length); i++) {
        var r = rows[i].map(function(c) { return String(c || '').toLowerCase().trim(); });
        if (r.indexOf('email') !== -1) { headerRowIdx = i; break; }
    }
    if (headerRowIdx === -1) return alert('❌ Không tìm thấy cột "email"!');

    var header = rows[headerRowIdx].map(function(c) { return String(c || '').toLowerCase().trim(); });
    var emailCol = header.indexOf('email');
    var nameCol = header.indexOf('name');
    var expCol = header.indexOf('expiresat');

    var existingUserMap = {}, existingAdminSet = {};
    usersCache.forEach(function(u) {
        var email = (u.email || '').toLowerCase();
        if (u.role === 'admin') existingAdminSet[email] = true;
        else existingUserMap[email] = u;
    });

    importRows = [];
    var seenInFile = {};

    for (var i = headerRowIdx + 1; i < rows.length; i++) {
        var row = rows[i];
        if (!row || row.length === 0) continue;
        var email = emailCol >= 0 ? String(row[emailCol] || '').trim().toLowerCase() : '';
        var name = nameCol >= 0 ? String(row[nameCol] || '').trim() : '';
        var expRaw = expCol >= 0 ? row[expCol] : '';
        if (!email && !name) continue;
        if (existingAdminSet[email]) continue;

        var status = 'ok', reason = '';
        var isUpdate = !!existingUserMap[email];
        if (!email) { status = 'error'; reason = 'Thiếu email'; }
        else if (!email.includes('@')) { status = 'error'; reason = 'Email không hợp lệ'; }
        else if (seenInFile[email]) { status = 'error'; reason = 'Trùng trong file'; }
        else seenInFile[email] = true;

        if (!name && email.indexOf('@') > 0) name = email.split('@')[0];

        var expDate = null, expStr = '';
        if (expRaw) {
            var raw = expRaw;
            if (typeof raw === 'number' && raw > 25569) {
                var d = new Date((raw - 25569) * 86400 * 1000);
                if (!isNaN(d.getTime())) { expDate = d; expStr = formatDate(d); }
            } else {
                var s = String(raw).trim();
                var m = s.match(/^(\d{4})[-\/](\d{1,2})[-\/](\d{1,2})$/);
                if (m) {
                    var d2 = new Date(parseInt(m[1]), parseInt(m[2]) - 1, parseInt(m[3]), 23, 59, 59);
                    if (!isNaN(d2.getTime())) { expDate = d2; expStr = formatDate(d2); }
                } else {
                    var d3 = new Date(s);
                    if (!isNaN(d3.getTime())) { expDate = d3; expStr = formatDate(d3); }
                    else if (status === 'ok') { status = 'warn'; reason = 'Ngày không hợp lệ'; }
                }
            }
        }
        importRows.push({
            rowNum: i + 1, email: email, name: name, role: 'user',
            expDate: expDate, expStr: expStr, status: status, reason: reason, isUpdate: isUpdate
        });
    }

    if (importRows.length === 0) return alert('❌ Không có dòng hợp lệ!');
    renderImportPreview();
    $('importModal').classList.add('show');
}

function renderImportPreview() {
    var tbody = $('importTableBody');
    var html = '';
    var countOk = 0, countUpdate = 0, countWarn = 0, countErr = 0;
    importRows.forEach(function(r) {
        var rowCls = '', statusHtml = '';
        if (r.status === 'ok' && r.isUpdate) { rowCls = 'row-update'; statusHtml = '<span class="status-badge update"><i class="fas fa-sync-alt"></i> Cập nhật</span>'; countUpdate++; }
        else if (r.status === 'ok') { rowCls = 'row-new'; statusHtml = '<span class="status-badge ok"><i class="fas fa-plus"></i> Thêm mới</span>'; countOk++; }
        else if (r.status === 'warn') { rowCls = 'row-warn'; statusHtml = '<span class="status-badge warn">' + escapeHtml(r.reason) + '</span>'; countWarn++; }
        else { rowCls = 'row-error'; statusHtml = '<span class="status-badge err">' + escapeHtml(r.reason) + '</span>'; countErr++; }
        var expDisplay = r.expStr
            ? '<span style="color:#16a34a;font-size:.7rem;font-weight:600;">' + r.expStr + '</span>'
            : '<span style="color:#dc2626;font-size:.7rem;font-weight:600;">💎 Vĩnh viễn</span>';
        html += '<tr class="' + rowCls + '"><td>' + r.rowNum + '</td><td><b>' + escapeHtml(r.email) + '</b></td><td>' + escapeHtml(r.name) + '</td><td><span class="role-badge user">user</span></td><td>' + expDisplay + '</td><td>' + statusHtml + '</td></tr>';
    });
    tbody.innerHTML = html;
    $('importSummary').innerHTML =
        '<div class="import-stat"><div class="num">' + importRows.length + '</div><div class="label">Tổng</div></div>' +
        '<div class="import-stat ok"><div class="num">' + countOk + '</div><div class="label">Thêm mới</div></div>' +
        '<div class="import-stat update"><div class="num">' + countUpdate + '</div><div class="label">Cập nhật</div></div>' +
        '<div class="import-stat warn"><div class="num">' + countWarn + '</div><div class="label">Cảnh báo</div></div>' +
        '<div class="import-stat err"><div class="num">' + countErr + '</div><div class="label">Lỗi</div></div>';
    var totalImportable = countOk + countUpdate + countWarn;
    if ($('importCount')) $('importCount').textContent = totalImportable;
    if ($('importConfirmBtn')) $('importConfirmBtn').disabled = totalImportable === 0;
}

async function doImport() {
    if (!isSuperAdmin() && !hasPermission('canImportExport')) {
        alert('Bạn không có quyền Import!');
        return;
    }
    var skipDuplicates = $('importSkipDuplicates').checked;
    var skipInvalid = $('importSkipInvalid').checked;
    var toImport = importRows.filter(function(r) {
        if (r.status === 'error') return false;
        if (r.status === 'warn' && skipInvalid) return false;
        if (r.isUpdate && skipDuplicates) return false;
        return true;
    });
    if (toImport.length === 0) return alert('⚠️ Không có user nào để import!');

    var totalNew = toImport.filter(function(r) { return !r.isUpdate; }).length;
    var totalUpdate = toImport.filter(function(r) { return r.isUpdate; }).length;
    if (!confirm('📥 IMPORT ' + toImport.length + ' TÀI KHOẢN?\n\n• Thêm mới: ' + totalNew + '\n• Cập nhật: ' + totalUpdate)) return;

    var btn = $('importConfirmBtn');
    var originalHTML = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang import...';

    var success = 0, failed = 0;
    var BATCH_SIZE = 400;
    for (var i = 0; i < toImport.length; i += BATCH_SIZE) {
        var chunk = toImport.slice(i, i + BATCH_SIZE);
        var batch = db.batch();
        chunk.forEach(function(r) {
            var ref = db.collection('allowed_users').doc(r.email);
            var data = { email: r.email, name: r.name, role: 'user', tier: 'active', addedBy: currentUser.email };
            if (!r.isUpdate) {
                data.addedAt = firebase.firestore.FieldValue.serverTimestamp();
                data.importedFromExcel = true;
            } else data.updatedAt = firebase.firestore.FieldValue.serverTimestamp();
            if (r.expDate) {
                data.expiresAt = firebase.firestore.Timestamp.fromDate(r.expDate);
                data.isPermanent = false;
            } else {
                data.expiresAt = null;
                data.isPermanent = true;
            }
            batch.set(ref, data, { merge: true });
        });
        try { await batch.commit(); success += chunk.length; }
        catch(err) { failed += chunk.length; console.error(err); }
    }

    btn.disabled = false;
    btn.innerHTML = originalHTML;
    importRows = [];
    try { localStorage.removeItem('admin_users_cache'); } catch(e) {}
    toImport.forEach(function(r) { try { localStorage.removeItem('user_cache_' + r.email); } catch(e) {} });
    alert('✅ Import xong!\n\n✓ Thành công: ' + success + (failed ? '\n✗ Thất bại: ' + failed : ''));
    $('importModal').classList.remove('show');
    loadUsers(true);
}

/* ============ DATE HELPERS ============ */
function getExpiryDate(expiresAt) {
    if (!expiresAt) return null;
    try {
        var ea = expiresAt;
        if (typeof ea.toDate === 'function') return ea.toDate();
        if (ea.seconds) return new Date(ea.seconds * 1000);
        return new Date(ea);
    } catch(e) { return null; }
}
function formatDate(d) {
    if (!d) return '';
    return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
}
function formatTimeDiff(ms) {
    if (ms < 60000) return 'Vừa xong';
    if (ms < 3600000) return Math.floor(ms / 60000) + ' phút trước';
    if (ms < 86400000) return Math.floor(ms / 3600000) + ' giờ trước';
    if (ms < 2592000000) return Math.floor(ms / 86400000) + ' ngày trước';
    return Math.floor(ms / 2592000000) + ' tháng trước';
}
/* ═══════════════════════════════════════════════════════════════
   🔄 RESET APP STATE — Gọi khi logout để xóa sạch state cũ
   ═══════════════════════════════════════════════════════════════ */
function resetAppState() {
    console.log('🔄 [resetAppState] Đang reset state sau logout...');

    /* 1. Reset biến toàn cục */
    currentUser = null;
    isDemo = true;
    usersCache = [];
    lastLoginMap = [];
    importRows = [];
    editingEmail = null;
    editingExpiryEmail = null;
    renewalSelectedPkg = null;
    renewalCurrentReq = null;
    renewalTab = 'pending';
    pendingRenewalsData = [];
    confirmedRenewalsData = [];
    adminSearchQuery = '';
    adminCurrentFilter = 'all';
    editingPermissionEmail = null;

    /* 2. Hủy watchers & listeners */
    if (userWatcher) {
        try { userWatcher(); } catch(e) {}
        userWatcher = null;
    }
    if (renewalListener) {
        try { renewalListener(); } catch(e) {}
        renewalListener = null;
    }
    stopRTDBPresence();

    /* 3. Xóa override onboarding */
    window.__onboardingOverride = null;
    window.__onboardingAutoPicked = false;

    /* 4. Xóa các banner động */
    var bannersToRemove = [
        'vocabWarningBanner',
        'onboardingActiveBanner',
        'userChangedToast',
        'tagToast'
    ];
    bannersToRemove.forEach(function(id) {
        var el = document.getElementById(id);
        if (el) el.remove();
    });

    /* 5. Ẩn tất cả banner chính */
    ['demoBanner', 'expiryBanner'].forEach(function(id) {
        var el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });

    /* 6. Reset APP_TIER / APP_LIMITS về demo */
    window.APP_TIER = 'demo';
    window.APP_LIMITS = {
        maxQuestions: (typeof DEMO_LIMIT === 'number') ? DEMO_LIMIT : 25,
        maxHSK: (typeof DEMO_HSK_MAX === 'number') ? DEMO_HSK_MAX : 3,
        unlimitedWriting: false,
        isTrial: false,
        email: null
    };

    /* 7. Reset dropdown user về trạng thái mặc định */
    try {
        sessionStorage.removeItem('userDropdownClosed');
        sessionStorage.removeItem('fabClosed');
        sessionStorage.removeItem('session_start');
    } catch(e) {}

    /* 8. Reset bộ lọc & search */
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
    } catch(e) {}

    /* 9. Đóng tất cả modal đang mở */
    var modals = document.querySelectorAll(
        '.admin-modal, .edit-modal, .renewal-modal, .import-modal, ' +
        '.permission-modal, .voice-modal, .writer-modal, .practice-full-modal, ' +
        '.onboarding-modal, .login-modal'
    );
    modals.forEach(function(m) { m.classList.remove('show'); });

    document.body.classList.remove('practice-full-open');
    document.body.style.overflow = '';

    /* 10. Ẩn user menu, hiện nút login */
    var userMenu = document.getElementById('userMenu');
    var headerLoginBtn = document.getElementById('headerLoginBtn');
    var demoBadge = document.getElementById('demoBadge');
    if (userMenu) userMenu.style.display = 'none';
    if (headerLoginBtn) headerLoginBtn.style.display = 'flex';
    if (demoBadge) demoBadge.style.display = 'flex';

    console.log('✅ [resetAppState] Hoàn tất reset');
}
/* ============ INIT AUTH UI ============ */
function initAuthUI() {
    if ($('headerLoginBtn')) $('headerLoginBtn').addEventListener('click', showLoginModal);
    if ($('loginClose')) $('loginClose').addEventListener('click', hideLoginModal);
    if ($('loginModal')) $('loginModal').addEventListener('click', function(e) { if (e.target === this) hideLoginModal(); });

    if ($('googleLoginBtn')) {
        $('googleLoginBtn').addEventListener('click', async function() {
            var btn = this;
            var originalHtml = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang đăng nhập...';

            var provider = new firebase.auth.GoogleAuthProvider();
            provider.setCustomParameters({ prompt: 'select_account' });

            try {
                var result = await auth.signInWithPopup(provider);
                if (result && result.user) {
                    hideLoginModal();
                }
            } catch (e) {
                console.error('Login error:', e);

                if (e.code === 'auth/popup-closed-by-user' ||
                    e.code === 'auth/cancelled-popup-request') {
                    // Im lặng
                }
                else if (e.code === 'auth/popup-blocked') {
                    showLoginError(
                        '<b>Trình duyệt đã chặn popup đăng nhập.</b><br>' +
                        'Vui lòng <b>cho phép popup</b> cho trang này rồi thử lại.<br>' +
                        '<span style="font-size:.8em;opacity:.8">' +
                        '(Thường ở biểu tượng 🔒/⚠️ cạnh thanh địa chỉ → Popups → Allow)' +
                        '</span>'
                    );
                }
                else if (e.code === 'auth/web-storage-unsupported' ||
                         (e.message && e.message.indexOf('missing initial state') !== -1)) {
                    showLoginError(
                        '<b>Trình duyệt đang chặn storage cần thiết.</b><br>' +
                        'Vui lòng:<br>' +
                        '• Tắt chế độ ẩn danh (nếu đang dùng)<br>' +
                        '• Cho phép <b>cookie bên thứ ba</b> cho Google<br>' +
                        '• Hoặc thử trình duyệt khác (Chrome/Edge mới nhất)'
                    );
                }
                else {
                    showLoginError('Lỗi đăng nhập: <b>' + (e.code || e.message) + '</b>');
                }
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalHtml;
            }
        });
    }

    /* ═══════════════════════════════════════════════════════════
       🔥 LOGOUT — XÓA TOÀN BỘ CACHE + STOP PRESENCE
       ═══════════════════════════════════════════════════════════ */
    /* ═══════════════════════════════════════════════════════════
       🔥 LOGOUT — RESET STATE + XÓA CACHE + STOP PRESENCE
       ═══════════════════════════════════════════════════════════ */
    if ($('logoutBtn')) {
        $('logoutBtn').addEventListener('click', function() {
            if (!confirm('Đăng xuất?')) return;

            try {
                /* ⭐ BƯỚC 1: Reset toàn bộ state */
                resetAppState();

                /* ⭐ BƯỚC 2: Xóa cache user hiện tại */
                var oldEmail = currentUser && currentUser.email;
                if (oldEmail) {
                    localStorage.removeItem('user_cache_' + oldEmail);
                }

                /* ⭐ BƯỚC 3: Xóa TẤT CẢ cache user_cache_* và admin_users_cache */
                var keysToRemove = [];
                for (var i = 0; i < localStorage.length; i++) {
                    var k = localStorage.key(i);
                    if (k && (k.indexOf('user_cache_') === 0 || k === 'admin_users_cache')) {
                        keysToRemove.push(k);
                    }
                }
                keysToRemove.forEach(function(k) {
                    try { localStorage.removeItem(k); } catch(e) {}
                });

                /* ⭐ BƯỚC 4: Xóa login log */
                if (oldEmail) {
                    try { localStorage.removeItem('login_log_' + oldEmail); } catch(e) {}
                }

                console.log('✅ Đã xóa', keysToRemove.length, 'cache keys khi đăng xuất');
            } catch(e) {
                console.warn('Lỗi khi xóa cache:', e);
            }

            /* ⭐ BƯỚC 5: Sign out Firebase → trigger handleAuthChange(null) */
            auth.signOut();
        });
    }

    if ($('userAvatar')) {
        $('userAvatar').addEventListener('click', function(e) {
            e.stopPropagation();
            var dd = $('userDropdown');
            if (!dd) return;
            var willOpen = !dd.classList.contains('show');
            dd.classList.toggle('show');
            try { sessionStorage.setItem('userDropdownClosed', willOpen ? '0' : '1'); } catch(_e) {}
        });
    }
    document.addEventListener('click', function(e) {
        var dd = $('userDropdown');
        if (dd && !dd.contains(e.target) && $('userAvatar') && !$('userAvatar').contains(e.target)) {
            dd.classList.remove('show');
            try { sessionStorage.setItem('userDropdownClosed', '1'); } catch(_e) {}
        }
    });

    if ($('changeNameBtn')) {
        $('changeNameBtn').addEventListener('click', function() {
            $('userDropdown').classList.remove('show');
            try { sessionStorage.setItem('userDropdownClosed', '1'); } catch(_e) {}
            if (!currentUser) return;
            editingEmail = currentUser.email;
            $('changeNameCurrent').textContent = currentUser.name;
            $('changeNameEmail').textContent = currentUser.email;
            $('changeNameInput').value = currentUser.name;
            $('changeNameModal').classList.add('show');
            setTimeout(function() { $('changeNameInput').focus(); }, 100);
        });
    }
    if ($('changeNameClose')) $('changeNameClose').addEventListener('click', function() { $('changeNameModal').classList.remove('show'); });
    if ($('changeNameCancel')) $('changeNameCancel').addEventListener('click', function() { $('changeNameModal').classList.remove('show'); });
    if ($('changeNameModal')) $('changeNameModal').addEventListener('click', function(e) { if (e.target === this) $('changeNameModal').classList.remove('show'); });
    if ($('changeNameConfirm')) $('changeNameConfirm').addEventListener('click', doChangeName);

    if ($('editExpiryClose')) $('editExpiryClose').addEventListener('click', function() { $('editExpiryModal').classList.remove('show'); });
    if ($('editExpiryCancel')) $('editExpiryCancel').addEventListener('click', function() { $('editExpiryModal').classList.remove('show'); });
    if ($('editExpiryModal')) $('editExpiryModal').addEventListener('click', function(e) { if (e.target === this) $('editExpiryModal').classList.remove('show'); });
    if ($('editExpiryConfirm')) $('editExpiryConfirm').addEventListener('click', doUpdateExpiry);

    if ($('renewalClose')) $('renewalClose').addEventListener('click', closeRenewalModal);
    if ($('renewalModal')) $('renewalModal').addEventListener('click', function(e) { if (e.target === this) closeRenewalModal(); });
    if ($('dropdownRenewBtn')) $('dropdownRenewBtn').addEventListener('click', function(e) { e.preventDefault(); openRenewalModal(); });
    if ($('expiryRenewBtn')) $('expiryRenewBtn').addEventListener('click', function(e) { e.preventDefault(); openRenewalModal(); });

    if ($('dropdownForeverBtn')) {
        $('dropdownForeverBtn').addEventListener('click', function(e) {
            e.preventDefault();
            $('userDropdown').classList.remove('show');
            try { sessionStorage.setItem('userDropdownClosed', '1'); } catch(_e) {}
            openRenewalModal();
            setTimeout(function() {
                if (typeof selectPackage === 'function') selectPackage('forever');
            }, 150);
        });
    }

    if ($('renewalHistoryClose')) $('renewalHistoryClose').addEventListener('click', function() { $('renewalHistoryModal').classList.remove('show'); });
    if ($('renewalHistoryModal')) $('renewalHistoryModal').addEventListener('click', function(e) { if (e.target === this) $('renewalHistoryModal').classList.remove('show'); });
    if ($('renewalHistoryBtn')) {
        $('renewalHistoryBtn').addEventListener('click', function() {
            $('userDropdown').classList.remove('show');
            try { sessionStorage.setItem('userDropdownClosed', '1'); } catch(_e) {}
            openRenewalHistory();
        });
    }

    initAdminPanel();
    scheduleAutoExpire();
}

/* ============ TIMEOUT FALLBACK ============ */
setTimeout(function() {
    if (!appInitialized) {
        console.warn('Auth timeout, entering demo mode');
        enterDemoMode();
    }
}, 5000);

/* ═══════════════════════════════════════════════════════════════
   📱 TELEGRAM NOTIFICATION
   ═══════════════════════════════════════════════════════════════ */
function _telegramSendMessage(text) {
    if (!TELEGRAM_BOT_TOKEN || !TELEGRAM_CHAT_ID || TELEGRAM_CHAT_ID === '-0') {
        console.warn('[Telegram] Chưa cấu hình bot_token / chat_id hợp lệ');
        console.warn('[Telegram] Token:', TELEGRAM_BOT_TOKEN ? 'OK' : 'MISSING');
        console.warn('[Telegram] Chat ID:', TELEGRAM_CHAT_ID || 'MISSING');
        return Promise.reject('not_configured');
    }

    var url = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage';

    return fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            chat_id: TELEGRAM_CHAT_ID,
            text: text,
            parse_mode: 'HTML',
            disable_web_page_preview: true
        })
    })
    .then(function(r) {
        return r.json();
    })
    .then(function(data) {
        if (!data.ok) {
            console.error('[Telegram] ❌ API error:', data.description);
            throw new Error(data.description || 'Telegram API error');
        }
        console.log('[Telegram] ✅ Đã gửi tin nhắn thành công');
        return data;
    })
    .catch(function(err) {
        console.error('[Telegram] ❌ Lỗi gửi:', err);
        throw err;
    });
}

window.notifyTelegramUserPaid = function(req) {
    if (!req) return Promise.resolve();

    var isPermanent = req.isPermanent || false;
    var amountStr = String(req.amount || 0).replace(/\B(?=(\d{3})+(?!\d))/g, '.');

    var text = '💰 <b>USER ĐÃ THANH TOÁN</b>\n\n' +
        '👤 <b>' + escapeHtml(req.name || req.email) + '</b>\n' +
        '📧 ' + escapeHtml(req.email) + '\n' +
        '💵 <b>' + amountStr + 'đ</b>\n' +
        '📦 ' + escapeHtml(req.packageLabel || req.package) +
            (isPermanent ? ' <b>(💎 VĨNH VIỄN)</b>' : ' (' + req.days + ' ngày)') + '\n' +
        '🔑 Mã: <code>' + escapeHtml(req.transferCode || '—') + '</code>\n\n' +
        '⏳ Vui lòng kiểm tra và xác nhận trong trang quản trị.';

    return _telegramSendMessage(text);
};

window.notifyTelegramAdminConfirmed = function(req, newExpiryStr) {
    if (!req) return Promise.resolve();

    var isPermanent = req.isPermanent || false;
    var amountStr = String(req.amount || 0).replace(/\B(?=(\d{3})+(?!\d))/g, '.');

    var text = '✅ <b>ĐÃ XÁC NHẬN GIA HẠN</b>\n\n' +
        '👤 <b>' + escapeHtml(req.name || req.email) + '</b>\n' +
        '📧 ' + escapeHtml(req.email) + '\n' +
        '💵 ' + amountStr + 'đ\n' +
        '📦 ' + escapeHtml(req.packageLabel || req.package) + '\n' +
        (isPermanent
            ? '💎 <b>KÍCH HOẠT VĨNH VIỄN</b>'
            : '📅 Hạn mới: <b>' + escapeHtml(newExpiryStr || '?') + '</b>') + '\n\n' +
        '🎉 User đã được gia hạn thành công.';

    return _telegramSendMessage(text);
};

window.testTelegram = function() {
    console.log('[Telegram] Test started...');
    console.log('[Telegram] Token:', TELEGRAM_BOT_TOKEN ? TELEGRAM_BOT_TOKEN.substring(0, 15) + '...' : '❌ MISSING');
    console.log('[Telegram] Chat ID:', TELEGRAM_CHAT_ID || '❌ MISSING');
    return _telegramSendMessage('🧪 <b>Test Telegram</b>\n\nBot đang hoạt động tốt! ✅\n\nThời gian: ' + new Date().toLocaleString('vi-VN'))
        .then(function() {
            alert('✅ Đã gửi test! Kiểm tra Telegram.');
        })
        .catch(function(err) {
            alert('❌ Lỗi gửi test: ' + err.message + '\n\nXem F12 Console để biết chi tiết.');
        });
};
"""

    # Inject config
    js = js.replace("__TRIAL_DAYS__", str(config.get("trial_days", 3)))
    js = js.replace("__TRIAL_MAX_QUESTIONS__", str(config.get("trial_max_questions", 50)))
    js = js.replace("__TRIAL_MAX_HSK__", str(config.get("trial_max_hsk", 5)))
    js = js.replace("__TRIAL_UNLIMITED_WRITING__",
                    "true" if config.get("trial_unlimited_writing", True) else "false")
    js = js.replace("__BANK_CONFIG__", json.dumps(config.get("bank_config", {}), ensure_ascii=False))
    js = js.replace("__PACKAGES__", json.dumps(config.get("packages", []), ensure_ascii=False))
    js = js.replace("__RENEWAL_SUPPORT_ZALO__", config.get("renewal_support_zalo", ""))

    telegram_token = config.get("telegram_bot_token", "") or ""
    telegram_chat_id = config.get("telegram_chat_id", "") or ""
    telegram_token_escaped = telegram_token.replace("\\", "\\\\").replace('"', '\\"')
    telegram_chat_id_escaped = str(telegram_chat_id).replace("\\", "\\\\").replace('"', '\\"')
    js = js.replace("__TELEGRAM_BOT_TOKEN__", telegram_token_escaped)
    js = js.replace("__TELEGRAM_CHAT_ID__", telegram_chat_id_escaped)
    # ⭐ Ẩn banner trùng lặp khi ở tab Từ vựng Premium
    js += r"""


/* ⭐ Ẩn #expiryBanner khi #vocabWarningBanner đang hiện (tránh trùng) */
(function hideExpiryWhenMerged() {
    function sync() {
        var merged = document.getElementById('vocabWarningBanner');
        var expiry = document.getElementById('expiryBanner');
        if (!expiry) return;
        if (merged && merged.offsetParent !== null) {
            expiry.style.display = 'none';
        }
    }
    setInterval(sync, 500);
})();

"""

    return js

def build_renewal_js(config=None):
    return ""


def build_renewal_css():
    return ""


def build_all_auth(config):
    """
    config: dict đã load từ JSON.
    Trả về tuple (css, html, js).
    """
    css = build_accounts_css()
    html = build_accounts_html()
    js = build_accounts_js(config)

    trial_days = config.get("trial_days", 3)
    html = html.replace(
        '<span id="trialDaysText">3</span>',
        '<span id="trialDaysText">' + str(trial_days) + '</span>'
    )
    return css, html, js
