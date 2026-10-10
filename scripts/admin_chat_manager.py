# -*- coding: utf-8 -*-
"""Admin Chat Manager"""


def build_admin_chat_css():
    return r"""
.acm-modal{
    position:fixed;inset:0;
    background:rgba(15,23,42,.75);
    backdrop-filter:blur(6px);
    z-index:5000;
    display:none;
    align-items:center;justify-content:center;
    padding:1rem;
    pointer-events:none;
}
.acm-modal.show{display:flex;pointer-events:auto;}

.acm-box{
    background:#fff;
    border-radius:20px;
    width:100%;
    max-width:960px;
    height:min(85vh, 800px);
    display:flex;flex-direction:column;overflow:hidden;
    box-shadow:0 30px 80px rgba(0,0,0,.4);
    animation:acmSlideIn .3s cubic-bezier(.34,1.56,.64,1);
}
@keyframes acmSlideIn{
    from{opacity:0;transform:scale(.9) translateY(30px);}
    to{opacity:1;transform:scale(1) translateY(0);}
}
[data-theme="dark"] .acm-box{
    background:#1e293b;
    box-shadow:0 30px 80px rgba(0,0,0,.8);
}

.acm-header{
    padding:1rem 1.25rem;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    display:flex;align-items:center;gap:1rem;
    flex-shrink:0;
}
.acm-header h3{
    font-size:1.05rem;font-weight:800;
    margin:0;flex:1;
    display:flex;align-items:center;gap:.5rem;
}
.acm-header h3 i{font-size:1.2rem;}
.acm-header-back{
    width:36px;height:36px;border-radius:50%;
    border:none;background:rgba(255,255,255,.2);
    color:#fff;cursor:pointer;
    display:none;align-items:center;justify-content:center;
    font-size:1rem;flex-shrink:0;transition:.15s;
}
.acm-header-back.show{display:flex;}
.acm-header-back:hover{background:rgba(255,255,255,.35);transform:scale(1.05);}
.acm-close{
    width:36px;height:36px;border-radius:50%;
    border:none;background:rgba(255,255,255,.2);
    color:#fff;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    font-size:1rem;flex-shrink:0;transition:.15s;
}
.acm-close:hover{background:rgba(255,255,255,.35);transform:scale(1.05);}

.acm-bulk-toggle{
    width:36px;height:36px;border-radius:50%;
    border:none;background:rgba(255,255,255,.2);
    color:#fff;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    font-size:.95rem;flex-shrink:0;transition:.15s;
}
.acm-bulk-toggle:hover{
    background:rgba(255,255,255,.35);
    transform:scale(1.05);
}
.acm-bulk-toggle.active{
    background:rgba(251,191,36,.5);
    box-shadow:0 0 0 3px rgba(251,191,36,.3);
}

.acm-stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(120px,1fr));
    gap:.5rem;
    padding:.75rem 1.25rem;
    background:#f8fafc;
    border-bottom:1px solid #e2e8f0;
    flex-shrink:0;
}
[data-theme="dark"] .acm-stats{background:#0f172a;border-color:#334155;}
.acm-stat{
    padding:.5rem .75rem;
    background:#fff;
    border-radius:10px;
    border:1px solid #e2e8f0;
    text-align:center;
    transition:.15s;
    cursor:pointer;
}
[data-theme="dark"] .acm-stat{background:#1e293b;border-color:#334155;}
.acm-stat:hover{border-color:#4f46e5;transform:translateY(-2px);box-shadow:0 4px 12px rgba(79,70,229,.15);}
.acm-stat.active{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-color:transparent;}
.acm-stat .acm-stat-value{
    font-size:1.35rem;font-weight:900;line-height:1;
    color:#4f46e5;display:block;margin-bottom:.15rem;
}
.acm-stat.active .acm-stat-value{color:#fff;}
.acm-stat .acm-stat-label{
    font-size:.65rem;text-transform:uppercase;
    letter-spacing:.4px;color:#64748b;font-weight:700;
}
.acm-stat.active .acm-stat-label{color:rgba(255,255,255,.9);}
[data-theme="dark"] .acm-stat .acm-stat-label{color:#94a3b8;}
.acm-stat[data-filter="online"] .acm-stat-value{color:#16a34a;}
.acm-stat[data-filter="online"].active{background:linear-gradient(135deg,#16a34a,#22c55e);}
.acm-stat[data-filter="online"].active .acm-stat-value{color:#fff;}

.acm-search{
    padding:.75rem 1.25rem;
    background:#fff;
    border-bottom:1px solid #e2e8f0;
    flex-shrink:0;
    display:flex;gap:.5rem;align-items:center;
}
[data-theme="dark"] .acm-search{background:#1e293b;border-color:#334155;}
.acm-search-input{
    flex:1;min-width:0;
    padding:.55rem 1rem;
    border-radius:50px;
    border:1.5px solid #e2e8f0;
    background:#f8fafc;
    color:#0f172a;
    font-size:.85rem;font-family:inherit;outline:none;
    transition:.15s;
}
[data-theme="dark"] .acm-search-input{
    background:#0f172a;color:#f1f5f9;border-color:#334155;
}
.acm-search-input:focus{border-color:#4f46e5;box-shadow:0 0 0 3px rgba(79,70,229,.1);}
.acm-refresh-btn{
    width:40px;height:40px;border-radius:10px;
    border:none;background:#eff6ff;color:#4f46e5;
    cursor:pointer;display:flex;align-items:center;justify-content:center;
    font-size:.9rem;flex-shrink:0;transition:.15s;
}
.acm-refresh-btn:hover{background:#4f46e5;color:#fff;transform:rotate(180deg);}
.acm-refresh-btn.spinning{animation:acmSpin .6s linear infinite;}
@keyframes acmSpin{to{transform:rotate(360deg);}}

.acm-bulk-toolbar{
    display:none;
    padding:.65rem 1.25rem;
    background:linear-gradient(135deg, #eff6ff, #e0e7ff);
    border-bottom:1px solid #c7d2fe;
    flex-shrink:0;
    align-items:center;
    gap:.75rem;
    flex-wrap:wrap;
}
.acm-bulk-toolbar.show{display:flex;}
[data-theme="dark"] .acm-bulk-toolbar{
    background:linear-gradient(135deg, rgba(79,70,229,.15), rgba(124,58,237,.1));
    border-color:rgba(124,58,237,.3);
}
.acm-bulk-info{
    flex:1;
    min-width:0;
    font-size:.82rem;
    font-weight:700;
    color:#4f46e5;
    display:flex;
    align-items:center;
    gap:.35rem;
}
[data-theme="dark"] .acm-bulk-info{color:#a5b4fc;}
.acm-bulk-count{
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    padding:.15rem .55rem;
    border-radius:50px;
    font-weight:900;
    font-size:.85rem;
    min-width:28px;
    text-align:center;
}
.acm-bulk-btn{
    padding:.5rem 1rem;
    border-radius:9px;
    border:none;
    font-size:.8rem;
    font-weight:800;
    cursor:pointer;
    font-family:inherit;
    display:inline-flex;
    align-items:center;
    gap:.35rem;
    transition:.15s;
    white-space:nowrap;
}
.acm-bulk-btn.primary{
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    box-shadow:0 3px 10px rgba(79,70,229,.35);
}
.acm-bulk-btn.primary:hover{
    transform:translateY(-1px);
    box-shadow:0 5px 14px rgba(79,70,229,.5);
}
.acm-bulk-btn.primary:disabled{
    opacity:.4;
    cursor:not-allowed;
    transform:none;
}
.acm-bulk-btn.ghost{
    background:rgba(255,255,255,.7);
    color:#4f46e5;
    border:1.5px solid rgba(79,70,229,.35);
}
.acm-bulk-btn.ghost:hover{
    background:#fff;
    border-color:#4f46e5;
}
[data-theme="dark"] .acm-bulk-btn.ghost{
    background:rgba(30,41,59,.6);
    color:#a5b4fc;
    border-color:rgba(124,58,237,.4);
}

.acm-user-checkbox{
    width:24px;height:24px;flex-shrink:0;
    display:none;
    align-items:center;justify-content:center;
    cursor:pointer;
}
body.acm-bulk-mode .acm-user-checkbox{display:flex;}
.acm-user-checkbox input{
    width:20px;height:20px;
    accent-color:#4f46e5;
    cursor:pointer;
    margin:0;
}

.acm-user.selected{
    border-color:#4f46e5;
    background:linear-gradient(90deg, rgba(79,70,229,.08), rgba(124,58,237,.05));
    box-shadow:0 2px 12px rgba(79,70,229,.15);
}
[data-theme="dark"] .acm-user.selected{
    background:linear-gradient(90deg, rgba(79,70,229,.2), rgba(124,58,237,.12));
}

.acm-select-all-row{
    display:none;
    padding:.5rem .85rem;
    background:#fff;
    border:1.5px dashed #c7d2fe;
    border-radius:10px;
    margin-bottom:.5rem;
    align-items:center;
    gap:.5rem;
    font-size:.8rem;
    font-weight:700;
    color:#4f46e5;
    cursor:pointer;
    transition:.15s;
}
body.acm-bulk-mode .acm-select-all-row{display:flex;}
.acm-select-all-row:hover{
    background:#eff6ff;
    border-color:#4f46e5;
}
[data-theme="dark"] .acm-select-all-row{
    background:#1e293b;
    border-color:rgba(124,58,237,.3);
    color:#a5b4fc;
}
.acm-select-all-row input{
    width:20px;height:20px;
    accent-color:#4f46e5;
    cursor:pointer;
    margin:0;
}

.acm-list{
    flex:1;min-height:0;overflow-y:auto;
    padding:.75rem 1.25rem;
    background:#f8fafc;
}
[data-theme="dark"] .acm-list{background:#0f172a;}

.acm-user{
    display:flex;align-items:center;gap:.75rem;
    padding:.75rem .85rem;
    background:#fff;
    border:1px solid #e2e8f0;
    border-radius:12px;
    margin-bottom:.5rem;
    transition:.15s;
    position:relative;
}
[data-theme="dark"] .acm-user{background:#1e293b;border-color:#334155;}
.acm-user:hover{border-color:#4f46e5;box-shadow:0 2px 8px rgba(79,70,229,.15);transform:translateX(2px);}
.acm-user.has-unread{border-color:#dc2626;background:linear-gradient(90deg,rgba(220,38,38,.05),transparent);}
.acm-user.no-thread{opacity:.85;}

.acm-user-avatar{
    width:44px;height:44px;border-radius:50%;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    display:flex;align-items:center;justify-content:center;
    font-weight:800;font-size:1rem;flex-shrink:0;
    position:relative;
}
.acm-user-avatar.online::after{
    content:'';position:absolute;bottom:0;right:0;
    width:12px;height:12px;border-radius:50%;
    background:#16a34a;border:2px solid #fff;
    animation:acmPulse 2s infinite;
}
[data-theme="dark"] .acm-user-avatar.online::after{border-color:#1e293b;}
@keyframes acmPulse{
    0%,100%{box-shadow:0 0 0 2px rgba(22,163,74,.3);}
    50%{box-shadow:0 0 0 5px rgba(22,163,74,.1);}
}
.acm-user-avatar.no-thread{
    background:linear-gradient(135deg,#94a3b8,#64748b);
}

.acm-user-info{flex:1;min-width:0;}
.acm-user-name{
    font-weight:800;font-size:.88rem;
    color:#0f172a;margin-bottom:.15rem;
    overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
    display:flex;align-items:center;gap:.35rem;
}
[data-theme="dark"] .acm-user-name{color:#f1f5f9;}
.acm-user-name .acm-tier{
    font-size:.55rem;font-weight:700;
    padding:.1rem .4rem;border-radius:50px;
    text-transform:uppercase;letter-spacing:.3px;
}
.acm-user-name .acm-tier.active{background:#dcfce7;color:#166534;}
.acm-user-name .acm-tier.trial{background:#fef3c7;color:#92400e;}
.acm-user-name .acm-tier.demo{background:#e0e7ff;color:#3730a3;}
.acm-user-name .acm-tier.admin{background:linear-gradient(135deg,#fbbf24,#f59e0b);color:#fff;}
.acm-user-name .acm-tier.expired{background:#fee2e2;color:#991b1b;}

.acm-user-email{
    font-size:.72rem;color:#64748b;
    overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
    margin-bottom:.1rem;
}
.acm-user-preview{
    font-size:.75rem;color:#94a3b8;
    overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
    font-style:italic;
}
.acm-user-preview b{color:#4f46e5;font-style:normal;font-weight:700;}
[data-theme="dark"] .acm-user-preview{color:#64748b;}

.acm-user-meta{
    display:flex;flex-direction:column;align-items:flex-end;
    gap:.3rem;flex-shrink:0;
}
.acm-user-time{
    font-size:.68rem;color:#94a3b8;white-space:nowrap;
}
.acm-user-time.online-now{
    color:#16a34a;
    font-weight:800;
    animation:acmOnlinePulse 2s ease-in-out infinite;
}
@keyframes acmOnlinePulse{
    0%,100%{opacity:1;}
    50%{opacity:.6;}
}
.acm-user-time.recent-login{
    color:#4f46e5;
    font-weight:700;
}
[data-theme="dark"] .acm-user-time.online-now{color:#22c55e;}
[data-theme="dark"] .acm-user-time.recent-login{color:#a5b4fc;}

.acm-user-badge{
    min-width:22px;height:22px;padding:0 .4rem;
    border-radius:50px;
    background:#dc2626;color:#fff;
    font-size:.65rem;font-weight:900;
    display:flex;align-items:center;justify-content:center;
    animation:acmBadgeBounce .8s infinite;
}
@keyframes acmBadgeBounce{
    0%,100%{transform:scale(1);}
    50%{transform:scale(1.15);}
}

.acm-user-actions{
    display:flex;gap:.3rem;flex-shrink:0;margin-left:.5rem;
}
.acm-user-btn{
    width:32px;height:32px;border-radius:8px;
    border:none;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    font-size:.8rem;transition:.15s;
    background:#f1f5f9;color:#64748b;
}
.acm-user-btn:hover{transform:scale(1.1);}
.acm-user-btn.chat{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;}
.acm-user-btn.chat:hover{box-shadow:0 4px 12px rgba(79,70,229,.4);}
.acm-user-btn.history{background:#eff6ff;color:#4f46e5;}
.acm-user-btn.history:hover{background:#4f46e5;color:#fff;box-shadow:0 4px 12px rgba(79,70,229,.4);}

.acm-user-btn.delete-history{
    background:#fef2f2;
    color:#dc2626;
}
.acm-user-btn.delete-history:hover{
    background:#dc2626;
    color:#fff;
    box-shadow:0 4px 12px rgba(220,38,38,.4);
    transform:scale(1.1);
}

.acm-empty{
    display:flex;flex-direction:column;
    align-items:center;justify-content:center;
    padding:3rem 1.5rem;text-align:center;
    color:#94a3b8;gap:.75rem;
}
.acm-empty i{font-size:3rem;opacity:.3;}
.acm-empty .acm-empty-title{
    font-size:.95rem;font-weight:700;color:#475569;
}
[data-theme="dark"] .acm-empty .acm-empty-title{color:#cbd5e1;}
.acm-empty .acm-empty-desc{font-size:.8rem;max-width:300px;line-height:1.5;}

.acm-loading{
    display:flex;align-items:center;justify-content:center;
    padding:3rem;color:#94a3b8;gap:.5rem;
    font-size:.85rem;
}

.acm-history{
    display:none;
    flex:1;min-height:0;overflow-y:auto;
    padding:1rem 1.25rem;
    background:#f8fafc;
}
.acm-history.show{display:block;}
[data-theme="dark"] .acm-history{background:#0f172a;}

.acm-hist-header{
    display:flex;align-items:center;gap:1rem;
    padding:1rem;
    background:#fff;
    border-radius:12px;
    margin-bottom:1rem;
    border:1px solid #e2e8f0;
}
[data-theme="dark"] .acm-hist-header{background:#1e293b;border-color:#334155;}
.acm-hist-avatar{
    width:60px;height:60px;border-radius:50%;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    display:flex;align-items:center;justify-content:center;
    font-weight:900;font-size:1.5rem;flex-shrink:0;
    position:relative;
}
.acm-hist-info{flex:1;min-width:0;}
.acm-hist-name{
    font-size:1.1rem;font-weight:900;
    color:#0f172a;margin-bottom:.2rem;
    display:flex;align-items:center;gap:.4rem;
    flex-wrap:wrap;
}
[data-theme="dark"] .acm-hist-name{color:#f1f5f9;}
.acm-hist-email{
    font-size:.8rem;color:#64748b;margin-bottom:.3rem;
}
.acm-hist-meta{
    font-size:.7rem;color:#94a3b8;
    display:flex;flex-wrap:wrap;gap:.75rem;
}

.acm-hist-filters{
    display:flex;gap:.4rem;flex-wrap:wrap;
    margin-bottom:1rem;
}
.acm-hist-filter{
    padding:.35rem .85rem;
    border-radius:50px;
    border:1.5px solid #e2e8f0;
    background:#fff;color:#64748b;
    font-size:.75rem;font-weight:700;
    cursor:pointer;transition:.15s;
    font-family:inherit;
    display:inline-flex;align-items:center;gap:.3rem;
}
[data-theme="dark"] .acm-hist-filter{background:#1e293b;border-color:#334155;color:#94a3b8;}
.acm-hist-filter:hover{border-color:#4f46e5;color:#4f46e5;}
.acm-hist-filter.active{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-color:transparent;}

.acm-timeline{
    position:relative;
    padding-left:2rem;
}
.acm-timeline::before{
    content:'';
    position:absolute;
    left:8px;top:0;bottom:0;
    width:2px;
    background:linear-gradient(180deg,#4f46e5,#7c3aed,#a855f7);
    opacity:.3;
}

.acm-tl-item{
    position:relative;
    margin-bottom:1rem;
    padding:.75rem 1rem;
    background:#fff;
    border-radius:10px;
    border-left:3px solid #4f46e5;
    transition:.15s;
}
[data-theme="dark"] .acm-tl-item{background:#1e293b;border-color:#4f46e5;}
.acm-tl-item:hover{box-shadow:0 4px 12px rgba(79,70,229,.1);transform:translateX(2px);}

.acm-tl-item::before{
    content:'';
    position:absolute;
    left:-1.65rem;top:1rem;
    width:12px;height:12px;border-radius:50%;
    background:#4f46e5;
    border:2px solid #fff;
    box-shadow:0 0 0 3px rgba(79,70,229,.15);
}
[data-theme="dark"] .acm-tl-item::before{border-color:#1e293b;}

.acm-tl-item[data-type="login"]{border-left-color:#16a34a;}
.acm-tl-item[data-type="login"]::before{background:#16a34a;box-shadow:0 0 0 3px rgba(22,163,74,.15);}
.acm-tl-item[data-type="logout"]{border-left-color:#94a3b8;}
.acm-tl-item[data-type="logout"]::before{background:#94a3b8;box-shadow:0 0 0 3px rgba(148,163,184,.15);}
.acm-tl-item[data-type="chat"]{border-left-color:#4f46e5;}
.acm-tl-item[data-type="chat"]::before{background:#4f46e5;box-shadow:0 0 0 3px rgba(79,70,229,.15);}
.acm-tl-item[data-type="renewal"]{border-left-color:#f59e0b;}
.acm-tl-item[data-type="renewal"]::before{background:#f59e0b;box-shadow:0 0 0 3px rgba(245,158,11,.15);}
.acm-tl-item[data-type="favorite"]{border-left-color:#dc2626;}
.acm-tl-item[data-type="favorite"]::before{background:#dc2626;box-shadow:0 0 0 3px rgba(220,38,38,.15);}
.acm-tl-item[data-type="practice"]{border-left-color:#7c3aed;}
.acm-tl-item[data-type="practice"]::before{background:#7c3aed;box-shadow:0 0 0 3px rgba(124,58,237,.15);}
.acm-tl-item[data-type="admin"]{border-left-color:#0ea5e9;}
.acm-tl-item[data-type="admin"]::before{background:#0ea5e9;box-shadow:0 0 0 3px rgba(14,165,233,.15);}

.acm-tl-head{
    display:flex;align-items:center;
    justify-content:space-between;gap:.5rem;
    margin-bottom:.3rem;
}
.acm-tl-title{
    font-size:.85rem;font-weight:800;
    color:#0f172a;
    display:flex;align-items:center;gap:.35rem;
}
[data-theme="dark"] .acm-tl-title{color:#f1f5f9;}
.acm-tl-icon{
    width:20px;height:20px;border-radius:50%;
    background:#eff6ff;color:#4f46e5;
    display:flex;align-items:center;justify-content:center;
    font-size:.65rem;flex-shrink:0;
}
.acm-tl-item[data-type="login"] .acm-tl-icon{background:#dcfce7;color:#16a34a;}
.acm-tl-item[data-type="logout"] .acm-tl-icon{background:#f1f5f9;color:#64748b;}
.acm-tl-item[data-type="renewal"] .acm-tl-icon{background:#fef3c7;color:#d97706;}
.acm-tl-item[data-type="favorite"] .acm-tl-icon{background:#fee2e2;color:#dc2626;}
.acm-tl-item[data-type="practice"] .acm-tl-icon{background:#ede9fe;color:#7c3aed;}
.acm-tl-item[data-type="admin"] .acm-tl-icon{background:#e0f2fe;color:#0284c7;}

.acm-tl-time{
    font-size:.7rem;color:#94a3b8;
    white-space:nowrap;flex-shrink:0;
}
.acm-tl-body{
    font-size:.8rem;color:#475569;
    line-height:1.5;padding-left:1.6rem;
}
[data-theme="dark"] .acm-tl-body{color:#cbd5e1;}
.acm-tl-body b{color:#4f46e5;font-weight:700;}
.acm-tl-body code{
    background:#f1f5f9;color:#dc2626;
    padding:.1rem .35rem;border-radius:4px;
    font-size:.75rem;
}
[data-theme="dark"] .acm-tl-body code{background:#0f172a;color:#f87171;}

@media (max-width:768px){
    .acm-modal{
        padding:0;
        align-items:flex-end;
        height:100vh;
        height:100dvh;
    }
    .acm-box{
        max-width:100%;
        height:92vh;
        height:92dvh;
        max-height:calc(100vh - 8px);
        max-height:calc(100dvh - 8px);
        border-radius:20px 20px 0 0;
        animation:acmSlideUp .3s cubic-bezier(.34,1.56,.64,1);
    }
    @keyframes acmSlideUp{
        from{transform:translateY(100%);}
        to{transform:translateY(0);}
    }
    .acm-stats{
        grid-template-columns:repeat(2,1fr);
        padding:.6rem .85rem;
    }
    .acm-list{padding:.6rem .85rem;}
    .acm-search{padding:.6rem .85rem;}
    .acm-user{padding:.65rem .7rem;flex-wrap:wrap;}
    .acm-user-avatar{width:40px;height:40px;font-size:.9rem;}
    .acm-header{padding:.85rem 1rem;}
    .acm-header h3{font-size:.95rem;}
    .acm-user-actions{width:100%;justify-content:flex-end;margin-top:.4rem;margin-left:0;}
    .acm-history{padding:.75rem;}
    .acm-hist-header{padding:.75rem;}
    .acm-hist-avatar{width:48px;height:48px;font-size:1.2rem;}
    .acm-timeline{padding-left:1.5rem;}
    .acm-tl-item{padding:.6rem .75rem;}
}

.acm-confirm-overlay{
    position:fixed;inset:0;
    background:rgba(15,23,42,.8);
    backdrop-filter:blur(4px);
    z-index:6000;
    display:none;
    align-items:center;justify-content:center;
    padding:1rem;
}
.acm-confirm-overlay.show{display:flex;}
.acm-confirm-box{
    background:#fff;
    border-radius:16px;
    max-width:420px;
    width:100%;
    padding:1.5rem;
    box-shadow:0 20px 60px rgba(0,0,0,.4);
    animation:acmSlideIn .3s cubic-bezier(.34,1.56,.64,1);
    text-align:center;
}
[data-theme="dark"] .acm-confirm-box{background:#1e293b;}
.acm-confirm-icon{
    width:60px;height:60px;border-radius:50%;
    background:linear-gradient(135deg,#fef2f2,#fee2e2);
    color:#dc2626;
    display:flex;align-items:center;justify-content:center;
    font-size:1.6rem;
    margin:0 auto 1rem;
}
[data-theme="dark"] .acm-confirm-icon{background:rgba(220,38,38,.2);}
.acm-confirm-title{
    font-size:1.05rem;font-weight:800;
    color:#0f172a;margin-bottom:.5rem;
}
[data-theme="dark"] .acm-confirm-title{color:#f1f5f9;}
.acm-confirm-desc{
    font-size:.85rem;color:#64748b;
    line-height:1.5;margin-bottom:1.25rem;
}
[data-theme="dark"] .acm-confirm-desc{color:#94a3b8;}
.acm-confirm-desc b{color:#dc2626;font-weight:800;}
.acm-confirm-actions{
    display:flex;gap:.5rem;justify-content:center;
    flex-wrap:wrap;
}
.acm-confirm-btn{
    padding:.6rem 1.2rem;
    border-radius:10px;
    border:1.5px solid #e2e8f0;
    background:#fff;
    color:#0f172a;
    font-size:.85rem;font-weight:700;
    cursor:pointer;font-family:inherit;
    display:inline-flex;align-items:center;gap:.4rem;
    transition:.15s;
}
.acm-confirm-btn:hover{background:#f8fafc;}
.acm-confirm-btn.danger{
    background:linear-gradient(135deg,#dc2626,#b91c1c);
    color:#fff;border-color:#dc2626;
    box-shadow:0 4px 12px rgba(220,38,38,.3);
}
.acm-confirm-btn.danger:hover{
    box-shadow:0 6px 18px rgba(220,38,38,.5);
    transform:translateY(-1px);
}
.acm-confirm-btn:disabled{opacity:.5;cursor:not-allowed;}
[data-theme="dark"] .acm-confirm-btn{
    background:#334155;color:#f1f5f9;border-color:#475569;
}

.acm-bulk-compose{
    position:fixed;inset:0;
    background:rgba(15,23,42,.8);
    backdrop-filter:blur(4px);
    z-index:6100;
    display:none;
    align-items:center;justify-content:center;
    padding:1rem;
}
.acm-bulk-compose.show{display:flex;}
.acm-bulk-compose-box{
    background:#fff;
    border-radius:18px;
    max-width:560px;
    width:100%;
    max-height:90vh;
    display:flex;flex-direction:column;
    box-shadow:0 20px 60px rgba(0,0,0,.4);
    animation:acmSlideIn .3s cubic-bezier(.34,1.56,.64,1);
    overflow:hidden;
}
[data-theme="dark"] .acm-bulk-compose-box{background:#1e293b;}
.acm-bulk-compose-header{
    padding:1rem 1.25rem;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    display:flex;align-items:center;gap:.75rem;
    flex-shrink:0;
}
.acm-bulk-compose-header h3{
    font-size:1rem;font-weight:800;
    margin:0;flex:1;
    display:flex;align-items:center;gap:.4rem;
}
.acm-bulk-compose-close{
    width:32px;height:32px;border-radius:50%;
    border:none;background:rgba(255,255,255,.2);
    color:#fff;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    font-size:.9rem;flex-shrink:0;
    transition:.15s;
}
.acm-bulk-compose-close:hover{background:rgba(255,255,255,.35);}
.acm-bulk-compose-body{
    padding:1.25rem;
    overflow-y:auto;
    flex:1;
    min-height:0;
}
.acm-bulk-label{
    font-size:.72rem;
    font-weight:800;
    color:#64748b;
    text-transform:uppercase;
    letter-spacing:.4px;
    margin-bottom:.4rem;
    display:flex;
    align-items:center;
    gap:.35rem;
}
[data-theme="dark"] .acm-bulk-label{color:#94a3b8;}
.acm-bulk-textarea{
    width:100%;
    min-height:130px;
    max-height:280px;
    padding:.85rem 1rem;
    border-radius:12px;
    border:1.5px solid #e2e8f0;
    background:#f8fafc;
    color:#0f172a;
    font-size:.9rem;
    font-family:inherit;
    line-height:1.5;
    outline:none;
    resize:vertical;
    transition:.15s;
}
.acm-bulk-textarea:focus{
    border-color:#4f46e5;
    box-shadow:0 0 0 3px rgba(79,70,229,.1);
}
[data-theme="dark"] .acm-bulk-textarea{
    background:#0f172a;
    color:#f1f5f9;
    border-color:#334155;
}
.acm-bulk-charcount{
    text-align:right;
    font-size:.72rem;
    color:#94a3b8;
    margin-top:.35rem;
}
.acm-bulk-templates{
    display:flex;
    gap:.35rem;
    flex-wrap:wrap;
    margin-top:.65rem;
}
.acm-bulk-template{
    padding:.35rem .75rem;
    border-radius:50px;
    border:1.5px solid #e2e8f0;
    background:#fff;
    color:#4f46e5;
    font-size:.72rem;
    font-weight:700;
    cursor:pointer;
    font-family:inherit;
    transition:.15s;
}
.acm-bulk-template:hover{
    background:#4f46e5;
    color:#fff;
    border-color:#4f46e5;
}
[data-theme="dark"] .acm-bulk-template{
    background:#334155;
    color:#a5b4fc;
    border-color:#475569;
}
[data-theme="dark"] .acm-bulk-template:hover{
    background:#4f46e5;
    color:#fff;
}
.acm-bulk-recipients{
    margin-top:1rem;
    padding:.75rem;
    border-radius:10px;
    background:#f8fafc;
    border:1px solid #e2e8f0;
    max-height:140px;
    overflow-y:auto;
}
[data-theme="dark"] .acm-bulk-recipients{
    background:#0f172a;
    border-color:#334155;
}
.acm-bulk-recipient-tag{
    display:inline-block;
    padding:.2rem .55rem;
    margin:.15rem;
    border-radius:50px;
    background:#e0e7ff;
    color:#3730a3;
    font-size:.7rem;
    font-weight:700;
}
[data-theme="dark"] .acm-bulk-recipient-tag{
    background:rgba(124,58,237,.25);
    color:#ddd6fe;
}
.acm-bulk-compose-footer{
    padding:1rem 1.25rem;
    border-top:1px solid #e2e8f0;
    display:flex;
    gap:.5rem;
    justify-content:flex-end;
    flex-shrink:0;
    background:#fff;
}
[data-theme="dark"] .acm-bulk-compose-footer{
    background:#1e293b;
    border-color:#334155;
}
.acm-bulk-send-btn{
    padding:.7rem 1.4rem;
    border-radius:10px;
    border:none;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    color:#fff;
    font-size:.85rem;
    font-weight:800;
    cursor:pointer;
    font-family:inherit;
    display:inline-flex;
    align-items:center;
    gap:.4rem;
    transition:.15s;
    box-shadow:0 4px 12px rgba(124,58,237,.35);
}
.acm-bulk-send-btn:hover{
    transform:translateY(-1px);
    box-shadow:0 6px 18px rgba(124,58,237,.5);
}
.acm-bulk-send-btn:disabled{
    opacity:.5;
    cursor:not-allowed;
    transform:none;
}
.acm-bulk-progress{
    display:none;
    padding:.75rem 1.25rem;
    background:linear-gradient(90deg, #eff6ff, #e0e7ff);
    border-top:1px solid #c7d2fe;
    flex-shrink:0;
}
.acm-bulk-progress.show{display:block;}
.acm-bulk-progress-text{
    font-size:.78rem;
    font-weight:700;
    color:#4f46e5;
    margin-bottom:.4rem;
    display:flex;
    justify-content:space-between;
    gap:.5rem;
}
.acm-bulk-progress-bar{
    height:6px;
    background:#c7d2fe;
    border-radius:50px;
    overflow:hidden;
}
.acm-bulk-progress-fill{
    height:100%;
    background:linear-gradient(90deg,#4f46e5,#7c3aed);
    border-radius:50px;
    transition:width .3s ease;
    width:0%;
}
"""


def build_admin_chat_html():
    return r"""
<div class="acm-modal" id="acmModal">
    <div class="acm-box">

        <div class="acm-header" id="acmHeaderList">
            <h3><i class="fas fa-users-cog"></i> Quản lý Chat — Tất cả User</h3>
            <button class="acm-bulk-toggle" id="acmBulkToggle" type="button" title="Chọn nhiều user để gửi hàng loạt">
                <i class="fas fa-check-square"></i>
            </button>
            <button class="acm-close" id="acmClose" type="button" title="Đóng">
                <i class="fas fa-times"></i>
            </button>
        </div>

        <div class="acm-stats" id="acmStats">
            <div class="acm-stat active" data-filter="all" id="acmStatAll">
                <span class="acm-stat-value" id="acmCountAll">0</span>
                <span class="acm-stat-label">Tất cả</span>
            </div>
            <div class="acm-stat" data-filter="online" id="acmStatOnline">
                <span class="acm-stat-value" id="acmCountOnline">0</span>
                <span class="acm-stat-label">Online</span>
            </div>
            <div class="acm-stat" data-filter="unread" id="acmStatUnread">
                <span class="acm-stat-value" id="acmCountUnread">0</span>
                <span class="acm-stat-label">Chưa đọc</span>
            </div>
            <div class="acm-stat" data-filter="has-thread" id="acmStatHasThread">
                <span class="acm-stat-value" id="acmCountHasThread">0</span>
                <span class="acm-stat-label">Có tin nhắn</span>
            </div>
            <div class="acm-stat" data-filter="no-thread" id="acmStatNoThread">
                <span class="acm-stat-value" id="acmCountNoThread">0</span>
                <span class="acm-stat-label">Chưa nhắn</span>
            </div>
        </div>

        <div class="acm-search" id="acmSearchBar">
            <input type="text" class="acm-search-input" id="acmSearchInput"
                   placeholder="Tìm theo tên hoặc email..." autocomplete="off">
            <button class="acm-refresh-btn" id="acmRefreshBtn" type="button" title="Làm mới">
                <i class="fas fa-sync-alt"></i>
            </button>
        </div>

        <div class="acm-bulk-toolbar" id="acmBulkToolbar">
            <div class="acm-bulk-info">
                <i class="fas fa-check-circle"></i>
                Đã chọn: <span class="acm-bulk-count" id="acmBulkCount">0</span> user
            </div>
            <button class="acm-bulk-btn ghost" type="button" id="acmBulkSelectAll">
                <i class="fas fa-check-double"></i> Chọn tất cả
            </button>
            <button class="acm-bulk-btn ghost" type="button" id="acmBulkClear">
                <i class="fas fa-times"></i> Bỏ chọn
            </button>
            <button class="acm-bulk-btn primary" type="button" id="acmBulkSend" disabled>
                <i class="fas fa-paper-plane"></i> Gửi hàng loạt
            </button>
        </div>

        <div class="acm-list" id="acmList">
            <div class="acm-loading">
                <i class="fas fa-spinner fa-pulse"></i>
                <span>Đang tải danh sách user...</span>
            </div>
        </div>

        <div class="acm-header" id="acmHeaderHistory" style="display:none;">
            <button class="acm-header-back show" id="acmHistoryBack" type="button" title="Quay lại">
                <i class="fas fa-arrow-left"></i>
            </button>
            <h3><i class="fas fa-history"></i> Lịch sử hoạt động</h3>
            <button class="acm-close" id="acmCloseHistory" type="button" title="Đóng">
                <i class="fas fa-times"></i>
            </button>
        </div>

        <div class="acm-history" id="acmHistory">
            <div class="acm-loading">
                <i class="fas fa-spinner fa-pulse"></i>
                <span>Đang tải lịch sử...</span>
            </div>
        </div>

    </div>
</div>

<div class="acm-confirm-overlay" id="acmConfirmDelete">
    <div class="acm-confirm-box">
        <div class="acm-confirm-icon">
            <i class="fas fa-trash-alt"></i>
        </div>
        <div class="acm-confirm-title">Xoá lịch sử chat?</div>
        <div class="acm-confirm-desc" id="acmConfirmDesc">
            Toàn bộ tin nhắn sẽ bị xoá vĩnh viễn và <b>không thể khôi phục</b>.
        </div>
        <div class="acm-confirm-actions">
            <button class="acm-confirm-btn" type="button" id="acmConfirmCancel">
                <i class="fas fa-times"></i> Huỷ
            </button>
            <button class="acm-confirm-btn danger" type="button" id="acmConfirmOk">
                <i class="fas fa-trash-alt"></i> Xoá vĩnh viễn
            </button>
        </div>
    </div>
</div>

<div class="acm-bulk-compose" id="acmBulkCompose">
    <div class="acm-bulk-compose-box">
        <div class="acm-bulk-compose-header">
            <h3><i class="fas fa-bullhorn"></i> Nhắn tin hàng loạt</h3>
            <button class="acm-bulk-compose-close" type="button" id="acmBulkComposeClose">
                <i class="fas fa-times"></i>
            </button>
        </div>
        <div class="acm-bulk-compose-body">
            <div class="acm-bulk-label">
                <i class="fas fa-users"></i> Người nhận (<span id="acmBulkRecipientCount">0</span>)
            </div>
            <div class="acm-bulk-recipients" id="acmBulkRecipientsList"></div>

            <div class="acm-bulk-label" style="margin-top:1rem;">
                <i class="fas fa-comment-dots"></i> Nội dung tin nhắn
            </div>
            <textarea class="acm-bulk-textarea" id="acmBulkTextarea"
                      placeholder="Nhập nội dung tin nhắn gửi cho tất cả user đã chọn..."
                      maxlength="1000"></textarea>
            <div class="acm-bulk-charcount">
                <span id="acmBulkCharCount">0</span>/1000
            </div>

            <div class="acm-bulk-templates">
                <button class="acm-bulk-template" type="button" data-text="Chào bạn, chúc bạn ngày mới học vui!">Chào hỏi</button>
                <button class="acm-bulk-template" type="button" data-text="Tài khoản sắp hết hạn, gia hạn để học tiếp nhé bạn!">Nhắc hết hạn</button>
                <button class="acm-bulk-template" type="button" data-text="Đã gia hạn cho bạn rồi, học vui nha!">Đã gia hạn</button>
                <button class="acm-bulk-template" type="button" data-text="Nhớ luyện viết mỗi ngày nhé bạn!">Nhắc luyện viết</button>
                <button class="acm-bulk-template" type="button" data-text="Mỗi ngày 10 từ, bạn sẽ giỏi nhanh thôi!">Mẹo học</button>
                <button class="acm-bulk-template" type="button" data-text="Bạn học chăm quá, cố lên nhé!">Động viên</button>
                <button class="acm-bulk-template" type="button" data-text="Cảm ơn bạn đã đồng hành cùng mình!">Cảm ơn</button>
                <button class="acm-bulk-template" type="button" data-text="Cần gì cứ nhắn mình nhé bạn!">Hỗ trợ</button>
            </div>
        </div>
        <div class="acm-bulk-progress" id="acmBulkProgress">
            <div class="acm-bulk-progress-text">
                <span><i class="fas fa-spinner fa-pulse"></i> Đang gửi...</span>
                <span id="acmBulkProgressText">0/0</span>
            </div>
            <div class="acm-bulk-progress-bar">
                <div class="acm-bulk-progress-fill" id="acmBulkProgressFill"></div>
            </div>
        </div>
        <div class="acm-bulk-compose-footer">
            <button class="acm-bulk-btn ghost" type="button" id="acmBulkComposeCancel">
                <i class="fas fa-times"></i> Huỷ
            </button>
            <button class="acm-bulk-send-btn" type="button" id="acmBulkComposeSend" disabled>
                <i class="fas fa-paper-plane"></i> Gửi <span id="acmBulkSendCount">0</span> tin
            </button>
        </div>
    </div>
</div>

<span id="acmFabBadge" style="display:none;">0</span>
"""


def build_admin_chat_js():
    return r"""
(function() {
    'use strict';

    var ACM_PRESENCE_CUTOFF_MS = 20 * 60 * 1000;

    var ACM = {
        inited: false,
        isOpen: false,
        view: 'list',
        usersUnsub: null,
        threadsUnsub: null,
        presenceUnsub: null,
        historyUnsub: null,
        loginLogsUnsub: null,
        currentHistoryEmail: null,
        allUsers: [],
        usersMap: {},
        threadsMap: {},
        onlineMap: {},
        loginLogsMap: {},
        filter: 'all',
        searchTerm: '',
        renderTimer: null,
        pendingDelete: null,
        bulkMode: false,
        selectedUsers: []
    };

    function $id(id) { return document.getElementById(id); }
    function esc(s) {
        if (s == null) return '';
        return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
                        .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }
    function jsStr(s) {
        if (s == null) return '';
        return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/"/g,'\\"');
    }
    function cssEsc(s) {
        if (window.CSS && CSS.escape) return CSS.escape(s);
        return String(s).replace(/([^\w-])/g, '\\$1');
    }
    function getDb() { return window.db || null; }
    function getCu() { return window.currentUser || null; }
    function isAdmin() { var u = getCu(); return u && u.role === 'admin'; }

    function timeAgo(ms) {
        if (ms < 60000) return 'Vừa xong';
        if (ms < 3600000) return Math.floor(ms/60000) + 'p';
        if (ms < 86400000) return Math.floor(ms/3600000) + 'h';
        if (ms < 2592000000) return Math.floor(ms/86400000) + 'd';
        return Math.floor(ms/2592000000) + 'th';
    }
    function formatDateTime(ms) {
        if (!ms) return '';
        try {
            var d = new Date(ms);
            return d.toLocaleDateString('vi-VN') + ' ' +
                   d.toLocaleTimeString('vi-VN', {hour:'2-digit',minute:'2-digit'});
        } catch(e) { return ''; }
    }

    function getTierClass(tier) {
        tier = (tier || 'demo').toLowerCase();
        if (tier === 'active' || tier === 'premium') return 'active';
        if (tier === 'trial') return 'trial';
        if (tier === 'admin' || tier === 'super_admin') return 'admin';
        if (tier === 'expired') return 'expired';
        return 'demo';
    }
    function getTierLabel(tier) {
        tier = (tier || 'demo').toLowerCase();
        if (tier === 'super_admin') return 'ADMIN';
        if (tier === 'admin') return 'ADMIN';
        if (tier === 'active' || tier === 'premium') return 'ACTIVE';
        if (tier === 'trial') return 'TRIAL';
        if (tier === 'expired') return 'HẾT HẠN';
        return 'DEMO';
    }

    function rebuildList() {
        var map = {};

        Object.keys(ACM.usersMap).forEach(function(email) {
            var u = ACM.usersMap[email];
            var emailLower = (email || '').toLowerCase();
            map[email] = {
                email: email,
                name: u.name || u.displayName || email.split('@')[0],
                role: u.role || 'user',
                tier: u.tier || u.plan || 'demo',
                thread: null,
                unread: 0,
                lastMessage: '',
                lastMessageAt: 0,
                lastMessageFrom: '',
                lastLoginAt: ACM.loginLogsMap[emailLower] || 0
            };
        });

        Object.keys(ACM.threadsMap).forEach(function(email) {
            var t = ACM.threadsMap[email];
            var threadHasMessages = !!(t.lastMessage && t.lastMessage.trim());

            if (!map[email]) {
                map[email] = {
                    email: email,
                    name: t.userName || email.split('@')[0],
                    role: 'user',
                    tier: 'demo',
                    thread: threadHasMessages ? t : null,
                    unread: 0,
                    lastMessage: '',
                    lastMessageAt: 0,
                    lastMessageFrom: '',
                    lastLoginAt: 0
                };
            }

            if (threadHasMessages) {
                map[email].thread = t;
            }

            map[email].unread = t.unreadByAdmin || 0;
            map[email].lastMessage = t.lastMessage || '';
            map[email].lastMessageAt = t.lastMessageAt
                ? (t.lastMessageAt.toMillis ? t.lastMessageAt.toMillis() : 0)
                : 0;
            map[email].lastMessageFrom = t.lastMessageFrom || '';
            if (t.userName && !map[email].name) map[email].name = t.userName;

            if (!map[email].lastLoginAt && map[email].lastMessageAt) {
                map[email].lastLoginAt = map[email].lastMessageAt;
            }
        });

        ACM.allUsers = Object.keys(map).map(function(k) { return map[k]; });

        ACM.allUsers.sort(function(a, b) {
            if (a.unread > 0 && b.unread === 0) return -1;
            if (a.unread === 0 && b.unread > 0) return 1;

            var aOn = ACM.onlineMap[a.email] ? 1 : 0;
            var bOn = ACM.onlineMap[b.email] ? 1 : 0;
            if (aOn !== bOn) return bOn - aOn;

            if (a.lastLoginAt !== b.lastLoginAt) {
                return b.lastLoginAt - a.lastLoginAt;
            }

            if (a.lastMessageAt > 0 && b.lastMessageAt === 0) return -1;
            if (a.lastMessageAt === 0 && b.lastMessageAt > 0) return 1;
            if (a.lastMessageAt !== b.lastMessageAt) return b.lastMessageAt - a.lastMessageAt;

            return (a.name || '').localeCompare(b.name || '');
        });

        updateStats();
        scheduleRender();
    }

    function updateStats() {
        var all = ACM.allUsers.length;
        var unread = 0, hasThread = 0, noThread = 0, online = 0;

        ACM.allUsers.forEach(function(u) {
            var threadHasMessages = false;
            if (u.thread) {
                var t = u.thread;
                threadHasMessages = !!(t.lastMessage && t.lastMessage.trim());
            }

            if (u.unread > 0) unread++;
            if (threadHasMessages) hasThread++;
            else noThread++;
            if (ACM.onlineMap[u.email]) online++;
        });

        var el;
        if ((el = $id('acmCountAll'))) el.textContent = all;
        if ((el = $id('acmCountOnline'))) el.textContent = online;
        if ((el = $id('acmCountUnread'))) el.textContent = unread;
        if ((el = $id('acmCountHasThread'))) el.textContent = hasThread;
        if ((el = $id('acmCountNoThread'))) el.textContent = noThread;

        var fabBadge = $id('acmFabBadge');
        if (fabBadge) {
            fabBadge.textContent = unread > 99 ? '99+' : unread;
        }

        if (typeof window.__syncChatSubBadges === 'function') {
            window.__syncChatSubBadges();
        }
    }

    function scheduleRender() {
        if (ACM.renderTimer) clearTimeout(ACM.renderTimer);
        ACM.renderTimer = setTimeout(renderList, 100);
    }

    function renderList() {
        var el = $id('acmList');
        if (!el) return;

        var list = ACM.allUsers.filter(function(u) {
            if (ACM.filter === 'online' && !ACM.onlineMap[u.email]) return false;
            if (ACM.filter === 'unread' && u.unread === 0) return false;
            if (ACM.filter === 'has-thread' && !u.thread) return false;
            if (ACM.filter === 'no-thread' && u.thread) return false;

            if (ACM.searchTerm) {
                var s = ACM.searchTerm.toLowerCase();
                var name = (u.name || '').toLowerCase();
                var email = (u.email || '').toLowerCase();
                if (name.indexOf(s) < 0 && email.indexOf(s) < 0) return false;
            }
            return true;
        });

        if (list.length === 0) {
            var emptyMsg = 'Chưa có user nào';
            if (ACM.searchTerm) emptyMsg = 'Không tìm thấy user phù hợp';
            else if (ACM.filter === 'online') emptyMsg = 'Không có user nào online';
            else if (ACM.filter === 'unread') emptyMsg = 'Không có tin chưa đọc';
            else if (ACM.filter === 'has-thread') emptyMsg = 'Chưa có user nào nhắn tin';
            else if (ACM.filter === 'no-thread') emptyMsg = 'Tất cả user đều đã nhắn';

            el.innerHTML =
                '<div class="acm-empty">' +
                    '<i class="fas fa-inbox"></i>' +
                    '<div class="acm-empty-title">' + emptyMsg + '</div>' +
                    '<div class="acm-empty-desc">Thử đổi bộ lọc hoặc xóa từ khóa tìm kiếm</div>' +
                '</div>';
            return;
        }

        var html = '';

        var allSelected = list.length > 0 && list.every(function(u) {
            return ACM.selectedUsers.indexOf(u.email) !== -1;
        });
        html += '<label class="acm-select-all-row">' +
            '<input type="checkbox" ' + (allSelected ? 'checked' : '') +
                ' onchange="window.__acmToggleSelectAll(this.checked)" />' +
            '<span>Chọn tất cả (' + list.length + ' user đang hiển thị)</span>' +
        '</label>';

        list.forEach(function(u) {
            var hasUnread = u.unread > 0;
            var hasThread = !!u.thread;
            var isOnline = !!ACM.onlineMap[u.email];
            var isSelected = ACM.selectedUsers.indexOf(u.email) !== -1;
            var initial = (u.name || u.email || '?').charAt(0).toUpperCase();
            var tierClass = getTierClass(u.role === 'admin' ? 'admin' : u.tier);
            var tierLabel = getTierLabel(u.role === 'admin' ? 'admin' : u.tier);
            var isMe = (getCu() && getCu().email === u.email);

            var preview = '';
            if (hasThread && u.lastMessage) {
                var prefix = (u.lastMessageFrom === 'admin') ? '<b>Bạn:</b> ' : '';
                preview = prefix + esc(u.lastMessage);
            } else if (hasThread) {
                preview = '<i>(chưa có tin nhắn)</i>';
            } else {
                preview = '<i>Chưa nhắn tin</i>';
            }

            var timeText = '';
            var timeClass = '';
            if (isOnline) {
                timeText = 'Online';
                timeClass = 'online-now';
            } else if (u.lastLoginAt > 0) {
                timeText = timeAgo(Date.now() - u.lastLoginAt);
                timeClass = 'recent-login';
            } else if (u.lastMessageAt > 0) {
                timeText = timeAgo(Date.now() - u.lastMessageAt);
            }

            html += '<div class="acm-user' +
                        (hasUnread ? ' has-unread' : '') +
                        (hasThread ? '' : ' no-thread') +
                        (isSelected ? ' selected' : '') +
                    '" data-email="' + esc(u.email) + '">' +
                '<label class="acm-user-checkbox" onclick="event.stopPropagation()">' +
                    '<input type="checkbox" ' +
                        (isSelected ? 'checked' : '') +
                        ' onchange="window.__acmToggleSelect(\'' + jsStr(u.email) + '\', this.checked)" />' +
                '</label>' +
                '<div class="acm-user-avatar' +
                    (hasThread ? '' : ' no-thread') +
                    (isOnline ? ' online' : '') +
                '">' +
                    esc(initial) +
                '</div>' +
                '<div class="acm-user-info">' +
                    '<div class="acm-user-name">' +
                        esc(u.name) +
                        (isMe ? ' <span style="font-size:.6rem;color:#94a3b8;">(bạn)</span>' : '') +
                        ' <span class="acm-tier ' + tierClass + '">' + tierLabel + '</span>' +
                    '</div>' +
                    '<div class="acm-user-email">' + esc(u.email) + '</div>' +
                    '<div class="acm-user-preview">' + preview + '</div>' +
                '</div>' +
                '<div class="acm-user-meta">' +
                    (timeText ? '<span class="acm-user-time ' + timeClass + '">' + timeText + '</span>' : '') +
                    (hasUnread ? '<span class="acm-user-badge">' +
                        (u.unread > 99 ? '99+' : u.unread) + '</span>' : '') +
                '</div>' +
                '<div class="acm-user-actions">' +
                    (hasThread ?
                        '<button class="acm-user-btn delete-history" type="button" ' +
                            'onclick="window.__acmDeleteHistory(\'' + jsStr(u.email) + '\', \'' + jsStr(u.name || u.email) + '\', ' + (u.unread || 0) + ')" ' +
                            'title="Xoá lịch sử chat">' +
                            '<i class="fas fa-trash-alt"></i>' +
                        '</button>'
                        : ''
                    ) +
                    '<button class="acm-user-btn history" type="button" ' +
                        'onclick="window.__acmShowHistory(\'' + jsStr(u.email) + '\')" ' +
                        'title="Xem lịch sử hoạt động">' +
                        '<i class="fas fa-history"></i>' +
                    '</button>' +
                    '<button class="acm-user-btn chat" type="button" ' +
                        'onclick="window.__acmOpenThread(\'' + jsStr(u.email) + '\')" ' +
                        'title="Mở chat">' +
                        '<i class="fas fa-comments"></i>' +
                    '</button>' +
                '</div>' +
            '</div>';
        });

        el.innerHTML = html;
    }

    function toggleBulkMode() {
        ACM.bulkMode = !ACM.bulkMode;
        document.body.classList.toggle('acm-bulk-mode', ACM.bulkMode);

        var btn = $id('acmBulkToggle');
        if (btn) btn.classList.toggle('active', ACM.bulkMode);

        var toolbar = $id('acmBulkToolbar');
        if (toolbar) toolbar.classList.toggle('show', ACM.bulkMode);

        if (!ACM.bulkMode) {
            ACM.selectedUsers = [];
            updateBulkCount();
        }

        scheduleRender();
    }

    window.__acmToggleSelect = function(email, checked) {
        if (!email) return;
        var idx = ACM.selectedUsers.indexOf(email);
        if (checked && idx === -1) {
            ACM.selectedUsers.push(email);
        } else if (!checked && idx !== -1) {
            ACM.selectedUsers.splice(idx, 1);
        }
        updateBulkCount();
        var userEl = document.querySelector('.acm-user[data-email="' + cssEsc(email) + '"]');
        if (userEl) userEl.classList.toggle('selected', checked);
    };

    window.__acmToggleSelectAll = function(checked) {
        var visibleList = ACM.allUsers.filter(function(u) {
            if (ACM.filter === 'online' && !ACM.onlineMap[u.email]) return false;
            if (ACM.filter === 'unread' && u.unread === 0) return false;
            if (ACM.filter === 'has-thread' && !u.thread) return false;
            if (ACM.filter === 'no-thread' && u.thread) return false;
            if (ACM.searchTerm) {
                var s = ACM.searchTerm.toLowerCase();
                var name = (u.name || '').toLowerCase();
                var email = (u.email || '').toLowerCase();
                if (name.indexOf(s) < 0 && email.indexOf(s) < 0) return false;
            }
            return true;
        });

        if (checked) {
            visibleList.forEach(function(u) {
                if (ACM.selectedUsers.indexOf(u.email) === -1) {
                    ACM.selectedUsers.push(u.email);
                }
            });
        } else {
            visibleList.forEach(function(u) {
                var idx = ACM.selectedUsers.indexOf(u.email);
                if (idx !== -1) ACM.selectedUsers.splice(idx, 1);
            });
        }

        updateBulkCount();
        scheduleRender();
    };

    function updateBulkCount() {
        var count = ACM.selectedUsers.length;
        var countEl = $id('acmBulkCount');
        if (countEl) countEl.textContent = count;

        var sendBtn = $id('acmBulkSend');
        if (sendBtn) sendBtn.disabled = count === 0;
    }

    function openBulkCompose() {
        var count = ACM.selectedUsers.length;
        if (count === 0) {
            alert('Vui lòng chọn ít nhất 1 user!');
            return;
        }

        var listEl = $id('acmBulkRecipientsList');
        if (listEl) {
            var html = '';
            ACM.selectedUsers.forEach(function(email) {
                var user = ACM.usersMap[email] || {};
                var name = user.name || email.split('@')[0];
                html += '<span class="acm-bulk-recipient-tag">' + esc(name) + '</span>';
            });
            listEl.innerHTML = html;
        }

        var countEl = $id('acmBulkRecipientCount');
        if (countEl) countEl.textContent = count;

        var sendCountEl = $id('acmBulkSendCount');
        if (sendCountEl) sendCountEl.textContent = count;

        var ta = $id('acmBulkTextarea');
        if (ta) {
            ta.value = '';
            var cc = $id('acmBulkCharCount');
            if (cc) cc.textContent = '0';
        }

        var prog = $id('acmBulkProgress');
        if (prog) prog.classList.remove('show');
        var fill = $id('acmBulkProgressFill');
        if (fill) fill.style.width = '0%';

        var sendBtn = $id('acmBulkComposeSend');
        if (sendBtn) sendBtn.disabled = true;

        $id('acmBulkCompose').classList.add('show');
        setTimeout(function() { if (ta) ta.focus(); }, 200);
    }

    function closeBulkCompose() {
        $id('acmBulkCompose').classList.remove('show');
    }

    async function sendBulkMessage() {
        if (!isAdmin()) {
            alert('Chỉ admin mới có quyền gửi!');
            return;
        }

        var ta = $id('acmBulkTextarea');
        var text = (ta && ta.value.trim()) || '';

        if (!text) {
            alert('Vui lòng nhập nội dung tin nhắn!');
            if (ta) ta.focus();
            return;
        }

        var recipients = ACM.selectedUsers.slice();
        if (recipients.length === 0) {
            alert('Không có user nào để gửi!');
            return;
        }

        if (!confirm('GỬI TIN NHẮN HÀNG LOẠT\n\n' +
                     'Số người nhận: ' + recipients.length + '\n' +
                     'Nội dung: ' + text.substring(0, 100) + (text.length > 100 ? '...' : '') +
                     '\n\nTiếp tục?')) return;

        var db = getDb();
        if (!db) return;

        var sendBtn = $id('acmBulkComposeSend');
        var cancelBtn = $id('acmBulkComposeCancel');
        var closeBtn = $id('acmBulkComposeClose');

        if (sendBtn) sendBtn.disabled = true;
        if (cancelBtn) cancelBtn.disabled = true;
        if (closeBtn) closeBtn.disabled = true;

        var prog = $id('acmBulkProgress');
        if (prog) prog.classList.add('show');

        var success = 0;
        var failed = 0;
        var adminEmail = (getCu() && getCu().email) || 'admin';
        var adminName = (getCu() && getCu().name) || 'Admin';

        for (var i = 0; i < recipients.length; i++) {
            var email = recipients[i];

            var progText = $id('acmBulkProgressText');
            if (progText) progText.textContent = (i + 1) + '/' + recipients.length;
            var progFill = $id('acmBulkProgressFill');
            if (progFill) progFill.style.width = Math.round(((i + 1) / recipients.length) * 100) + '%';

            try {
                var threadRef = db.collection('chat_threads').doc(email);
                var doc = await threadRef.get();
                var data = doc.exists ? doc.data() : {};
                var msgs = data.messages || [];

                var newMsg = {
                    from: 'admin',
                    fromEmail: adminEmail,
                    fromName: adminName,
                    text: text,
                    at: firebase.firestore.Timestamp.now()
                };
                msgs.push(newMsg);
                if (msgs.length > 100) msgs = msgs.slice(-100);

                await threadRef.set({
                    messages: msgs,
                    lastMessage: text.substring(0, 100),
                    lastMessageAt: firebase.firestore.FieldValue.serverTimestamp(),
                    lastMessageFrom: 'admin',
                    userEmail: email,
                    userName: data.userName || email.split('@')[0],
                    unreadByUser: (data.unreadByUser || 0) + 1,
                    unreadByAdmin: 0,
                    adminTypingAt: null
                }, { merge: true });

                success++;

            } catch (e) {
                failed++;
            }

            if (i < recipients.length - 1) {
                await new Promise(function(r) { setTimeout(r, 100); });
            }
        }

        try {
            db.collection('activity_logs').add({
                email: adminEmail,
                type: 'admin',
                title: 'Gửi tin nhắn hàng loạt',
                detail: 'Gửi cho ' + success + '/' + recipients.length + ' user: ' + text.substring(0, 80),
                at: firebase.firestore.FieldValue.serverTimestamp(),
                metadata: { recipients: recipients, success: success, failed: failed }
            });
        } catch(e) {}

        if (sendBtn) sendBtn.disabled = false;
        if (cancelBtn) cancelBtn.disabled = false;
        if (closeBtn) closeBtn.disabled = false;

        showSmallToast('Đã gửi ' + success + '/' + recipients.length + ' tin' +
                       (failed > 0 ? ' (' + failed + ' lỗi)' : ''));

        closeBulkCompose();
    }

    window.__acmDeleteHistory = function(email, userName, unread) {
        if (!isAdmin()) {
            alert('Chỉ admin mới có quyền xoá!');
            return;
        }
        if (!email) return;

        ACM.pendingDelete = { email: email, userName: userName || email };

        var descEl = $id('acmConfirmDesc');
        if (descEl) {
            descEl.innerHTML =
                'Xoá toàn bộ tin nhắn của <b>' + esc(userName || email) + '</b>' +
                '<br><span style="font-size:.78rem;color:#94a3b8">' + esc(email) + '</span>' +
                (unread > 0 ? '<br><br>Có <b>' + unread + '</b> tin chưa đọc cũng sẽ bị xoá.' : '') +
                '<br><br>Hành động này <b>không thể khôi phục</b>.';
        }

        $id('acmConfirmDelete').classList.add('show');
    };

    function hideDeleteConfirm() {
        $id('acmConfirmDelete').classList.remove('show');
        ACM.pendingDelete = null;
    }

    async function doDeleteHistory() {
        if (!ACM.pendingDelete) return;
        var db = getDb();
        if (!db) return;

        var btn = $id('acmConfirmOk');
        var originalHTML = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Đang xoá...';

        try {
            var email = ACM.pendingDelete.email;
            var userName = ACM.pendingDelete.userName;

            /* ⭐ 1. XOÁ TIN NHẮN TRONG chat_threads */
            var threadRef = db.collection('chat_threads').doc(email);
            await threadRef.set({
                messages: [],
                lastMessage: '',
                lastMessageAt: firebase.firestore.FieldValue.serverTimestamp(),
                lastMessageFrom: '',
                unreadByAdmin: 0,
                unreadByUser: 0,
                userTypingAt: null,
                adminTypingAt: null,
                historyClearedAt: firebase.firestore.FieldValue.serverTimestamp(),
                historyClearedBy: (getCu() && getCu().email) || 'admin'
            }, { merge: true });

            /* ⭐ 2. XOÁ activity_logs loại 'chat' của user (batch, tối đa 500) */
            try {
                var chatLogsSnap = await db.collection('activity_logs')
                    .where('email', '==', email)
                    .where('type', '==', 'chat')
                    .limit(500)
                    .get();

                if (!chatLogsSnap.empty) {
                    var batch = db.batch();
                    var deletedCount = 0;
                    chatLogsSnap.forEach(function(doc) {
                        batch.delete(doc.ref);
                        deletedCount++;
                    });
                    await batch.commit();
                    console.log('[ACM] Đã xoá ' + deletedCount + ' chat activity log');
                }
            } catch(e) {
                console.warn('[ACM] Không xoá được activity_logs:', e);
            }

            /* ⭐ 3. Update local state */
            if (ACM.threadsMap && ACM.threadsMap[email]) {
                ACM.threadsMap[email].lastMessage = '';
                ACM.threadsMap[email].lastMessageAt = null;
                ACM.threadsMap[email].lastMessageFrom = '';
                ACM.threadsMap[email].unreadByAdmin = 0;
            }

            var selIdx = ACM.selectedUsers.indexOf(email);
            if (selIdx !== -1) ACM.selectedUsers.splice(selIdx, 1);
            updateBulkCount();

            try { localStorage.removeItem('admin_users_cache'); } catch(e) {}

            rebuildList();
            updateStats();
            hideDeleteConfirm();

            /* ⭐ 4. Xoá luôn khung chat user nếu đang mở */
            try {
                var chatBody = $id('chatBody');
                if (chatBody && chatBody.offsetParent !== null) {
                    var headerInfo = $id('chatHeaderInfo');
                    if (headerInfo && headerInfo.textContent && headerInfo.textContent.indexOf(email) !== -1) {
                        chatBody.innerHTML = '<div class="chat-empty">' +
                            '<i class="fas fa-comments"></i>' +
                            '<div class="title">Đã xoá lịch sử chat</div>' +
                            '<div class="desc">Bắt đầu cuộc trò chuyện mới.</div>' +
                        '</div>';
                    }
                }
            } catch(e) {}

            /* ⭐ 5. Ghi activity log việc xoá */
            try {
                db.collection('activity_logs').add({
                    email: email,
                    type: 'admin',
                    title: 'Admin đã xoá lịch sử chat',
                    detail: 'Bởi: ' + ((getCu() && getCu().email) || 'admin'),
                    at: firebase.firestore.FieldValue.serverTimestamp()
                });
            } catch(e) {}

            /* ⭐ 6. Refresh lại UI sau 800ms + 2s để chắc chắn */
            setTimeout(function() {
                rebuildList();
                updateStats();
            }, 800);

            setTimeout(function() {
                rebuildList();
                updateStats();
            }, 2000);

            showSmallToast('Đã xoá lịch sử chat của ' + userName);

        } catch (err) {
            alert('Lỗi: ' + err.message);
        } finally {
            btn.disabled = false;
            btn.innerHTML = originalHTML;
        }
    }

    function showSmallToast(msg) {
        var toast = document.getElementById('acmSmallToast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'acmSmallToast';
            toast.style.cssText =
                'position:fixed;top:20px;left:50%;transform:translateX(-50%) translateY(-100px);' +
                'background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;' +
                'padding:.8rem 1.4rem;border-radius:50px;font-weight:800;font-size:.88rem;' +
                'box-shadow:0 12px 40px rgba(22,163,74,.5);z-index:99999;' +
                'transition:transform .4s cubic-bezier(.34,1.56,.64,1),opacity .3s;' +
                'opacity:0;pointer-events:none;max-width:90vw;text-align:center;';
            document.body.appendChild(toast);
        }
        toast.textContent = msg;
        requestAnimationFrame(function() {
            toast.style.transform = 'translateX(-50%) translateY(0)';
            toast.style.opacity = '1';
        });
        clearTimeout(toast._timer);
        toast._timer = setTimeout(function() {
            toast.style.transform = 'translateX(-50%) translateY(-100px)';
            toast.style.opacity = '0';
        }, 3000);
    }

    function showHistory(email) {
        if (!email) return;
        var db = getDb();
        if (!db) return;

        ACM.view = 'history';
        ACM.currentHistoryEmail = email;

        $id('acmHeaderList').style.display = 'none';
        $id('acmStats').style.display = 'none';
        $id('acmSearchBar').style.display = 'none';
        $id('acmBulkToolbar').style.display = 'none';
        $id('acmList').style.display = 'none';

        $id('acmHeaderHistory').style.display = 'flex';
        $id('acmHistory').classList.add('show');

        $id('acmHistory').innerHTML =
            '<div class="acm-loading">' +
                '<i class="fas fa-spinner fa-pulse"></i>' +
                '<span>Đang tải lịch sử...</span>' +
            '</div>';

        if (ACM.historyUnsub) {
            try { ACM.historyUnsub(); } catch(e) {}
            ACM.historyUnsub = null;
        }

        var logsRef = db.collection('activity_logs')
            .where('email', '==', email)
            .orderBy('at', 'desc')
            .limit(100);

        ACM.historyUnsub = logsRef.onSnapshot(function(snap) {
            var activities = [];
            snap.forEach(function(doc) {
                var d = doc.data() || {};
                activities.push({
                    id: doc.id,
                    type: d.type || 'other',
                    title: d.title || '',
                    detail: d.detail || '',
                    at: d.at ? (d.at.toMillis ? d.at.toMillis() : 0) : 0,
                    metadata: d.metadata || {}
                });
            });
            renderHistory(email, activities);
        }, function(err) {
            renderHistory(email, []);
        });
    }

    function renderHistory(email, activities) {
        var el = $id('acmHistory');
        if (!el) return;

        var userInfo = ACM.usersMap[email] || {};
        var threadInfo = ACM.threadsMap[email] || {};
        var name = userInfo.name || threadInfo.userName || email.split('@')[0];
        var initial = (name || '?').charAt(0).toUpperCase();
        var tier = userInfo.tier || 'demo';
        var role = userInfo.role || 'user';
        var tierClass = getTierClass(role === 'admin' ? 'admin' : tier);
        var tierLabel = getTierLabel(role === 'admin' ? 'admin' : tier);
        var isOnline = !!ACM.onlineMap[email];

        var lastLoginMs = ACM.loginLogsMap[(email || '').toLowerCase()] || 0;
        var lastLoginText = lastLoginMs > 0 ? formatDateTime(lastLoginMs) : '';

        var counts = { login: 0, chat: 0, renewal: 0, favorite: 0, practice: 0, other: 0 };
        activities.forEach(function(a) {
            var t = a.type || 'other';
            if (counts[t] !== undefined) counts[t]++;
            else counts.other++;
        });

        var html =
            '<div class="acm-hist-header">' +
                '<div class="acm-hist-avatar">' +
                    (isOnline ? '<span style="position:absolute;bottom:0;right:0;width:14px;height:14px;border-radius:50%;background:#16a34a;border:2px solid #fff;"></span>' : '') +
                    esc(initial) +
                '</div>' +
                '<div class="acm-hist-info">' +
                    '<div class="acm-hist-name">' +
                        esc(name) +
                        ' <span class="acm-tier ' + tierClass + '">' + tierLabel + '</span>' +
                        (isOnline ? ' <span style="color:#16a34a;font-size:.7rem;font-weight:700;">Online</span>' : '') +
                    '</div>' +
                    '<div class="acm-hist-email">' + esc(email) + '</div>' +
                    '<div class="acm-hist-meta">' +
                        '<span><i class="fas fa-list"></i> ' + activities.length + ' hoạt động</span>' +
                        (threadInfo.userEmail ? '<span><i class="fas fa-comments"></i> Có tin nhắn</span>' : '') +
                        (lastLoginText ? '<span><i class="fas fa-sign-in-alt"></i> Login cuối: ' + esc(lastLoginText) + '</span>' : '') +
                    '</div>' +
                '</div>' +
                '<button class="acm-user-btn chat" type="button" ' +
                    'onclick="window.__acmOpenThread(\'' + jsStr(email) + '\')" ' +
                    'title="Mở chat">' +
                    '<i class="fas fa-comments"></i>' +
                '</button>' +
            '</div>';

        html +=
            '<div class="acm-hist-filters">' +
                '<button class="acm-hist-filter active" data-type="all">' +
                    '<i class="fas fa-list"></i> Tất cả (' + activities.length + ')' +
                '</button>' +
                '<button class="acm-hist-filter" data-type="login">' +
                    '<i class="fas fa-sign-in-alt"></i> Đăng nhập (' + counts.login + ')' +
                '</button>' +
                '<button class="acm-hist-filter" data-type="chat">' +
                    '<i class="fas fa-comments"></i> Chat (' + counts.chat + ')' +
                '</button>' +
                '<button class="acm-hist-filter" data-type="renewal">' +
                    '<i class="fas fa-money-bill"></i> Gia hạn (' + counts.renewal + ')' +
                '</button>' +
                '<button class="acm-hist-filter" data-type="practice">' +
                    '<i class="fas fa-pen"></i> Luyện tập (' + counts.practice + ')' +
                '</button>' +
                '<button class="acm-hist-filter" data-type="favorite">' +
                    '<i class="fas fa-heart"></i> Yêu thích (' + counts.favorite + ')' +
                '</button>' +
            '</div>';

        if (activities.length === 0) {
            html +=
                '<div class="acm-empty">' +
                    '<i class="fas fa-history"></i>' +
                    '<div class="acm-empty-title">Chưa có hoạt động nào</div>' +
                    '<div class="acm-empty-desc">' +
                        'Khi user đăng nhập, chat, gia hạn... sẽ được ghi lại ở đây' +
                    '</div>' +
                '</div>';
        } else {
            html += '<div class="acm-timeline" id="acmTimeline">';
            activities.forEach(function(a) {
                html += buildActivityItem(a);
            });
            html += '</div>';
        }

        el.innerHTML = html;

        el.querySelectorAll('.acm-hist-filter').forEach(function(btn) {
            btn.addEventListener('click', function() {
                el.querySelectorAll('.acm-hist-filter').forEach(function(b) {
                    b.classList.remove('active');
                });
                this.classList.add('active');
                var type = this.getAttribute('data-type');
                filterTimeline(type);
            });
        });
    }

    function buildActivityItem(a) {
        var icon = 'fa-circle';
        var title = a.title || 'Hoạt động';
        var detail = a.detail || '';

        switch (a.type) {
            case 'login':   icon = 'fa-sign-in-alt'; break;
            case 'logout':  icon = 'fa-sign-out-alt'; break;
            case 'chat':    icon = 'fa-comments'; break;
            case 'renewal': icon = 'fa-money-bill'; break;
            case 'favorite':icon = 'fa-heart'; break;
            case 'practice':icon = 'fa-pen'; break;
            case 'admin':   icon = 'fa-shield-alt'; break;
            default:        icon = 'fa-circle';
        }

        return '<div class="acm-tl-item" data-type="' + esc(a.type) + '">' +
            '<div class="acm-tl-head">' +
                '<div class="acm-tl-title">' +
                    '<span class="acm-tl-icon"><i class="fas ' + icon + '"></i></span>' +
                    esc(title) +
                '</div>' +
                '<span class="acm-tl-time">' + formatDateTime(a.at) + '</span>' +
            '</div>' +
            (detail ? '<div class="acm-tl-body">' + detail + '</div>' : '') +
        '</div>';
    }

    function filterTimeline(type) {
        var tl = $id('acmTimeline');
        if (!tl) return;
        tl.querySelectorAll('.acm-tl-item').forEach(function(item) {
            if (type === 'all' || item.getAttribute('data-type') === type) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    }

    function hideHistory() {
        ACM.view = 'list';
        ACM.currentHistoryEmail = null;

        $id('acmHeaderHistory').style.display = 'none';
        $id('acmHistory').classList.remove('show');
        $id('acmHistory').innerHTML = '';

        $id('acmHeaderList').style.display = 'flex';
        $id('acmStats').style.display = 'grid';
        $id('acmSearchBar').style.display = 'flex';
        if (ACM.bulkMode) $id('acmBulkToolbar').style.display = 'flex';
        $id('acmList').style.display = 'block';

        if (ACM.historyUnsub) {
            try { ACM.historyUnsub(); } catch(e) {}
            ACM.historyUnsub = null;
        }
    }

    function startWatchers() {
        stopWatchers();
        var db = getDb();
        if (!db || !isAdmin()) return;

        ACM.usersUnsub = db.collection('allowed_users')
            .onSnapshot(function(snap) {
                ACM.usersMap = {};
                snap.forEach(function(doc) {
                    var d = doc.data() || {};
                    var email = doc.id;
                    if (email) {
                        var tier = 'demo';
                        if (d.role === 'admin') tier = 'admin';
                        else if (d.isPermanent) tier = 'active';
                        else if (d.expiresAt) {
                            var expTime = d.expiresAt.toMillis ? d.expiresAt.toMillis() : 0;
                            tier = expTime > Date.now() ? 'active' : 'expired';
                        } else if (d.tier) tier = d.tier;

                        ACM.usersMap[email] = {
                            email: email,
                            name: d.name || d.displayName || email.split('@')[0],
                            role: d.role || 'user',
                            tier: tier
                        };
                    }
                });
                rebuildList();
            }, function(err) {
                console.error('ACM users watch error:', err);
            });

        ACM.threadsUnsub = db.collection('chat_threads')
            .onSnapshot(function(snap) {
                ACM.threadsMap = {};
                snap.forEach(function(doc) {
                    var d = doc.data() || {};
                    var email = d.userEmail || doc.id;
                    if (email) {
                        ACM.threadsMap[email] = {
                            userEmail: email,
                            userName: d.userName || email.split('@')[0],
                            lastMessage: d.lastMessage || '',
                            lastMessageAt: d.lastMessageAt,
                            lastMessageFrom: d.lastMessageFrom || '',
                            unreadByAdmin: d.unreadByAdmin || 0
                        };
                    }
                });
                rebuildList();
            }, function(err) {
                console.error('ACM threads watch error:', err);
            });

        if (typeof firebase !== 'undefined' && firebase.database) {
            try {
                var presenceRef = firebase.database().ref('presence');
                var PRESENCE_CUTOFF = ACM_PRESENCE_CUTOFF_MS;

                var handler = presenceRef.on('value', function(snap) {
                    var val = snap.val() || {};
                    var now = Date.now();
                    ACM.onlineMap = {};

                    Object.keys(val).forEach(function(key) {
                        var u = val[key];
                        if (u && u.at && (now - u.at) < PRESENCE_CUTOFF) {
                            var email = u.email || decodeURIComponent(key);
                            ACM.onlineMap[email] = true;
                        }
                    });

                    rebuildList();
                }, function(err) {
                    console.error('ACM presence watch error:', err);
                });

                ACM.presenceUnsub = function() {
                    try { presenceRef.off('value', handler); } catch(e) {}
                };
            } catch(e) {}
        }

        ACM.loginLogsUnsub = db.collection('login_logs')
            .orderBy('time', 'desc')
            .limit(500)
            .onSnapshot(function(snap) {
                ACM.loginLogsMap = {};
                snap.forEach(function(doc) {
                    var d = doc.data() || {};
                    var email = (d.email || '').toLowerCase();
                    if (!email) return;
                    if (!ACM.loginLogsMap[email] && d.time) {
                        var ts = d.time.toMillis ? d.time.toMillis() :
                                 (d.time.seconds ? d.time.seconds * 1000 : 0);
                        ACM.loginLogsMap[email] = ts;
                    }
                });
                rebuildList();
            }, function(err) {
                console.error('ACM login_logs watch error:', err);
            });
    }

    function stopWatchers() {
        if (ACM.usersUnsub) { try { ACM.usersUnsub(); } catch(e){} ACM.usersUnsub = null; }
        if (ACM.threadsUnsub) { try { ACM.threadsUnsub(); } catch(e){} ACM.threadsUnsub = null; }
        if (ACM.presenceUnsub) { try { ACM.presenceUnsub(); } catch(e){} ACM.presenceUnsub = null; }
        if (ACM.historyUnsub) { try { ACM.historyUnsub(); } catch(e){} ACM.historyUnsub = null; }
        if (ACM.loginLogsUnsub) { try { ACM.loginLogsUnsub(); } catch(e){} ACM.loginLogsUnsub = null; }
    }

    function openModal() {
        if (!isAdmin()) return;
        ACM.isOpen = true;
        $id('acmModal').classList.add('show');
        document.body.style.overflow = 'hidden';
        if (!ACM.usersUnsub && !ACM.threadsUnsub) {
            startWatchers();
        }
    }

    function closeModal() {
        ACM.isOpen = false;
        $id('acmModal').classList.remove('show');
        document.body.style.overflow = '';
        if (ACM.view === 'history') hideHistory();
        if (ACM.bulkMode) {
            ACM.bulkMode = false;
            document.body.classList.remove('acm-bulk-mode');
            var toolbar = $id('acmBulkToolbar');
            if (toolbar) toolbar.classList.remove('show');
            var btn = $id('acmBulkToggle');
            if (btn) btn.classList.remove('active');
            ACM.selectedUsers = [];
        }
    }

    function toggleModal() {
        if (ACM.isOpen) closeModal();
        else openModal();
    }

    window.__acmToggleModal = toggleModal;
    window.__acmOpenModal = openModal;
    window.__acmCloseModal = closeModal;

    window.__acmOpenThread = function(email) {
        closeModal();
        setTimeout(function() {
            if (typeof window.__chatOpen === 'function') {
                if (!document.getElementById('chatModal').classList.contains('show')) {
                    window.__chatOpen();
                }
            }
            setTimeout(function() {
                if (typeof window.__chatOpenThread === 'function') {
                    window.__chatOpenThread(email);
                }
            }, 400);
        }, 200);
    };

    window.__acmShowHistory = function(email) {
        showHistory(email);
    };

    function init() {
        if (ACM.inited) return;
        ACM.inited = true;

        var closeBtn = $id('acmClose');
        if (closeBtn) closeBtn.addEventListener('click', closeModal);

        var closeHistBtn = $id('acmCloseHistory');
        if (closeHistBtn) closeHistBtn.addEventListener('click', closeModal);

        var backBtn = $id('acmHistoryBack');
        if (backBtn) backBtn.addEventListener('click', hideHistory);

        var modal = $id('acmModal');
        if (modal) modal.addEventListener('click', function(e) {
            if (e.target === this) closeModal();
        });

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && ACM.isOpen) {
                if ($id('acmBulkCompose').classList.contains('show')) {
                    closeBulkCompose();
                } else if ($id('acmConfirmDelete').classList.contains('show')) {
                    hideDeleteConfirm();
                } else if (ACM.view === 'history') {
                    hideHistory();
                } else {
                    closeModal();
                }
            }
        });

        var searchInput = $id('acmSearchInput');
        if (searchInput) {
            var debounce;
            searchInput.addEventListener('input', function() {
                clearTimeout(debounce);
                var val = this.value;
                debounce = setTimeout(function() {
                    ACM.searchTerm = val.trim();
                    scheduleRender();
                }, 200);
            });
        }

        var refreshBtn = $id('acmRefreshBtn');
        if (refreshBtn) refreshBtn.addEventListener('click', function() {
            this.classList.add('spinning');
            var self = this;
            startWatchers();
            setTimeout(function() { self.classList.remove('spinning'); }, 800);
        });

        document.querySelectorAll('.acm-stat').forEach(function(tab) {
            tab.addEventListener('click', function() {
                document.querySelectorAll('.acm-stat').forEach(function(t) {
                    t.classList.remove('active');
                });
                this.classList.add('active');
                ACM.filter = this.getAttribute('data-filter');
                scheduleRender();
            });
        });

        var confirmCancel = $id('acmConfirmCancel');
        if (confirmCancel) confirmCancel.addEventListener('click', hideDeleteConfirm);

        var confirmOk = $id('acmConfirmOk');
        if (confirmOk) confirmOk.addEventListener('click', doDeleteHistory);

        var confirmOverlay = $id('acmConfirmDelete');
        if (confirmOverlay) confirmOverlay.addEventListener('click', function(e) {
            if (e.target === this) hideDeleteConfirm();
        });

        var bulkToggle = $id('acmBulkToggle');
        if (bulkToggle) bulkToggle.addEventListener('click', toggleBulkMode);

        var bulkSelectAll = $id('acmBulkSelectAll');
        if (bulkSelectAll) bulkSelectAll.addEventListener('click', function() {
            window.__acmToggleSelectAll(true);
        });

        var bulkClear = $id('acmBulkClear');
        if (bulkClear) bulkClear.addEventListener('click', function() {
            ACM.selectedUsers = [];
            updateBulkCount();
            scheduleRender();
        });

        var bulkSend = $id('acmBulkSend');
        if (bulkSend) bulkSend.addEventListener('click', openBulkCompose);

        var bulkComposeClose = $id('acmBulkComposeClose');
        if (bulkComposeClose) bulkComposeClose.addEventListener('click', closeBulkCompose);

        var bulkComposeCancel = $id('acmBulkComposeCancel');
        if (bulkComposeCancel) bulkComposeCancel.addEventListener('click', closeBulkCompose);

        var bulkComposeOverlay = $id('acmBulkCompose');
        if (bulkComposeOverlay) bulkComposeOverlay.addEventListener('click', function(e) {
            if (e.target === this) closeBulkCompose();
        });

        var bulkComposeSend = $id('acmBulkComposeSend');
        if (bulkComposeSend) bulkComposeSend.addEventListener('click', sendBulkMessage);

        var bulkTextarea = $id('acmBulkTextarea');
        if (bulkTextarea) {
            bulkTextarea.addEventListener('input', function() {
                var len = this.value.length;
                var cc = $id('acmBulkCharCount');
                if (cc) cc.textContent = len;
                var sendBtn = $id('acmBulkComposeSend');
                if (sendBtn) sendBtn.disabled = len === 0;
            });
        }

        document.querySelectorAll('.acm-bulk-template').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var text = this.getAttribute('data-text') || this.textContent.trim();
                var ta = $id('acmBulkTextarea');
                if (ta) {
                    ta.value = text;
                    ta.dispatchEvent(new Event('input'));
                    ta.focus();
                }
            });
        });

        handleAutoOpenFromUrl();
    }

    function handleAutoOpenFromUrl() {
        try {
            var urlParams = new URLSearchParams(window.location.search);
            var targetEmail = urlParams.get('admin_chat');

            if (!targetEmail) return;

            try { localStorage.setItem('acm_pending_email', targetEmail); } catch(e) {}

            setTimeout(function() {
                if (isAdmin()) {
                    openAutoChat(targetEmail);
                }
            }, 2000);
        } catch(e) {}
    }

    function openAutoChat(targetEmail) {
        openModal();

        setTimeout(function() {
            if (typeof window.__acmOpenThread === 'function') {
                window.__acmOpenThread(targetEmail);
            }

            try {
                var url = new URL(window.location.href);
                url.searchParams.delete('admin_chat');
                window.history.replaceState({}, '', url.pathname + url.hash);
            } catch(e) {}

            try { localStorage.removeItem('acm_pending_email'); } catch(e) {}
        }, 1500);
    }

    function checkPendingEmail() {
        try {
            var pending = localStorage.getItem('acm_pending_email');
            if (pending && isAdmin()) {
                setTimeout(function() {
                    openAutoChat(pending);
                }, 1000);
            }
        } catch(e) {}
    }

    var _lastRole = null;
    setInterval(function() {
        var u = getCu();
        var role = u ? (u.role || 'user') : null;
        if (role === _lastRole) return;
        _lastRole = role;

        if (role === 'admin') {
            if (!ACM.usersUnsub && !ACM.threadsUnsub) {
                startWatchers();
            }
            checkPendingEmail();
        } else {
            stopWatchers();
            if (ACM.isOpen) closeModal();
        }
    }, 2000);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
"""
