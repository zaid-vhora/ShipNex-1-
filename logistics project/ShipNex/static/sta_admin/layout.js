/* Shared layout: sidebar + topbar renderer */
(function () {
  const navItems = [
    { section: 'Main' },
    { href: '/adminapp/index_view/', icon: 'fa-gauge-high', label: 'Dashboard', id: 'dashboard' },
    // { section: 'Management' },
    // { href: '/adminapp/users_view/', icon: 'fa-users', label: 'User Management', id: 'users', badge: '5' },
    // { href: '/adminapp/shipments_view/', icon: 'fa-boxes-stacked', label: 'Shipment Management', id: 'shipments' },
    // { href: '/adminapp/deliveries_view/', icon: 'fa-truck-fast', label: 'Delivery Management', id: 'deliveries', badge: '3' },
    // { href: '/adminapp/payments_view/', icon: 'fa-credit-card', label: 'Payment Management', id: 'payments' },
    { section: 'Fleet & Logistics' },
    { href: '/adminapp/vehicles_view/', icon: 'fa-car-side', label: 'Vehicle Management', id: 'vehicles' },
    { href: '/adminapp/drivers_view/', icon: 'fa-id-card', label: 'Driver Management', id: 'drivers' },
    { href: '/adminapp/warehouses_view/', icon: 'fa-warehouse', label: 'Warehouse Management', id: 'warehouses' },
    { href: '/adminapp/transporters_view/', icon: 'fa-building-columns', label: 'Transporter Management', id: 'transporters' },
    { section: 'System' },
    { href: '/adminapp/reports_view/', icon: 'fa-chart-pie', label: 'Reports & Analytics', id: 'reports' },
    { href: '/adminapp/settings_view/', icon: 'fa-gear', label: 'System Settings', id: 'settings' },
  ];

  const notifications = [
    { icon: 'fa-box', color: '#eff6ff', iconColor: '#3b82f6', title: 'New Shipment Booked', msg: 'SHP-20240611 from John Doe', time: '2 min ago', unread: true },
    { icon: 'fa-user-plus', color: '#ecfdf5', iconColor: '#10b981', title: 'New User Registered', msg: 'Sarah Connor joined LogiTrack', time: '18 min ago', unread: true },
    { icon: 'fa-triangle-exclamation', color: '#fffbeb', iconColor: '#f59e0b', title: 'Delivery Delayed', msg: 'SHP-20240609 delayed at checkpoint', time: '1 hr ago', unread: true },
    { icon: 'fa-circle-check', color: '#ecfdf5', iconColor: '#10b981', title: 'Payment Received', msg: '₹4,500 received for INV-2024-088', time: '3 hrs ago', unread: false },
  ];

  function currentPage() {
    const parts = window.location.pathname.split('/').filter(Boolean);
    let last = parts.length ? parts[parts.length - 1] : 'index';
    // normalize trailing .html and view suffix
    if (last.endsWith('.html')) last = last.replace('.html', '');
    if (last.endsWith('_view')) last = last.replace(/_view$/, '');
    // map index-like names
    if (!last) last = 'dashboard';
    return last;
  }

  function renderSidebar() {
    const cur = currentPage();
    let navHtml = '';
    navItems.forEach(item => {
      if (item.section) {
        navHtml += `<div class="nav-section-title">${item.section}</div>`;
      } else {
        const active = (cur === item.id || (cur === '' && item.id === 'dashboard')) ? 'active' : '';
        const badge = item.badge ? `<span class="nav-badge">${item.badge}</span>` : '';
        navHtml += `
          <div class="nav-item">
            <a href="${item.href}" class="nav-link ${active}">
              <span class="nav-icon"><i class="fas ${item.icon}"></i></span>
              <span class="nav-text">${item.label}</span>
              ${badge}
            </a>
          </div>`;
      }
    });

    const sidebar = document.createElement('aside');
    sidebar.className = 'sidebar';
    sidebar.id = 'sidebar';
    sidebar.innerHTML = `
      <div class="sidebar-brand">
        <div class="brand-icon"><i class="fas fa-truck-fast"></i></div>
        <div class="brand-text">
          <div class="brand-name">LogiTrack</div>
          <div class="brand-sub">Admin Portal</div>
        </div>
      </div>
      <nav class="sidebar-nav">${navHtml}</nav>
      <div class="sidebar-footer">
        <div class="sidebar-user">
          <div class="avatar">AD</div>
          <div class="user-info">
            <div class="user-name">Super Admin</div>
            <div class="user-role">Administrator</div>
          </div>
        </div>
      </div>`;
    return sidebar;
  }

  function renderTopbar(title, breadcrumb) {
    let notifHtml = notifications.map(n => `
      <div class="notif-item ${n.unread ? 'unread' : ''}">
        <div class="notif-icon" style="background:${n.color}; color:${n.iconColor}">
          <i class="fas ${n.icon}"></i>
        </div>
        <div>
          <div class="notif-item-title">${n.title}</div>
          <div class="notif-item-msg">${n.msg}</div>
          <div class="notif-item-time"><i class="fas fa-clock fa-xs"></i> ${n.time}</div>
        </div>
      </div>`).join('');

    const topbar = document.createElement('header');
    topbar.className = 'topbar';
    topbar.innerHTML = `
      <button class="topbar-toggle" id="sidebarToggle" onclick="toggleSidebar()">
        <i class="fas fa-bars"></i>
      </button>
      <div class="topbar-breadcrumb">
        <div class="page-title">${title}</div>
        <div class="breadcrumb-trail">Admin &rsaquo; ${breadcrumb}</div>
      </div>
      <div class="topbar-actions">
        <div style="position:relative">
          <button class="topbar-btn" id="notifBtn" onclick="toggleNotif()">
            <i class="fas fa-bell"></i>
            <span class="badge-dot"></span>
          </button>
          <div class="notif-dropdown" id="notifDropdown">
            <div class="notif-header">
              <span class="notif-title">Notifications</span>
              <span style="font-size:12px;color:#3b82f6;cursor:pointer">Mark all read</span>
            </div>
            ${notifHtml}
            <div style="padding:12px 18px;text-align:center;border-top:1px solid #f1f5f9">
              <a href="#" style="font-size:13px;color:#3b82f6;font-weight:600">View all notifications</a>
            </div>
          </div>
        </div>
        <button class="topbar-btn" data-tooltip="Settings" onclick="window.location.href='/adminapp/settings_view/'">
          <i class="fas fa-gear"></i>
        </button>
        <div class="topbar-profile" onclick="window.location.href='/adminapp/settings_view/'">
          <div class="avatar">AD</div>
          <div class="profile-info">
            <div class="profile-name">Super Admin</div>
            <div class="profile-role">Administrator</div>
          </div>
          <i class="fas fa-chevron-down" style="font-size:10px;color:#94a3b8;margin-left:4px"></i>
        </div>
        <button class="topbar-btn" data-tooltip="Logout" onclick="window.location.href='/adminapp/login_view/'" style="color:#ef4444">
          <i class="fas fa-sign-out-alt"></i>
        </button>
      </div>`;
    return topbar;
  }

  window.initLayout = function (title, breadcrumb) {
    // Page loader
    const loader = document.createElement('div');
    loader.className = 'page-loader';
    loader.id = 'pageLoader';
    loader.innerHTML = '<div class="loader-ring"></div>';
    document.body.prepend(loader);

    const wrapper = document.querySelector('.admin-wrapper');
    if (!wrapper) return;

    wrapper.prepend(renderSidebar());

    const mainContent = wrapper.querySelector('.main-content');
    if (mainContent) {
      mainContent.prepend(renderTopbar(title, breadcrumb));
    }

    // Hide loader
    setTimeout(() => {
      loader.classList.add('hide');
      setTimeout(() => loader.remove(), 400);
    }, 400);
  };

  window.toggleSidebar = function () {
    const sidebar = document.getElementById('sidebar');
    const main = document.querySelector('.main-content');
    if (window.innerWidth <= 1024) {
      sidebar.classList.toggle('mobile-open');
    } else {
      sidebar.classList.toggle('collapsed');
      main && main.classList.toggle('expanded');
    }
  };

  window.toggleNotif = function () {
    document.getElementById('notifDropdown').classList.toggle('show');
  };

  document.addEventListener('click', function (e) {
    const btn = document.getElementById('notifBtn');
    const dd = document.getElementById('notifDropdown');
    if (dd && !dd.contains(e.target) && btn && !btn.contains(e.target)) {
      dd.classList.remove('show');
    }
  });
})();
