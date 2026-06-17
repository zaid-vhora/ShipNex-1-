/* ===================================================
   LogiTrack Transporter Portal - Main JavaScript
   =================================================== */

document.addEventListener('DOMContentLoaded', function () {

  // ---- Sidebar Toggle ----
  const sidebar = document.getElementById('sidebar');
  const collapseBtn = document.getElementById('collapseBtn');
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileOverlay = document.getElementById('mobileOverlay');

  if (collapseBtn) {
    collapseBtn.addEventListener('click', function () {
      sidebar.classList.toggle('collapsed');
    });
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', function () {
      sidebar.classList.toggle('mobile-open');
      mobileOverlay.classList.toggle('show');
    });
  }

  if (mobileOverlay) {
    mobileOverlay.addEventListener('click', function () {
      sidebar.classList.remove('mobile-open');
      mobileOverlay.classList.remove('show');
    });
  }

  // ---- Dark Mode Toggle ----
  const darkToggle = document.getElementById('darkToggle');
  const html = document.documentElement;

  // Load saved preference
  const savedTheme = localStorage.getItem('logitrack-theme');
  if (savedTheme === 'dark') {
    html.setAttribute('data-theme', 'dark');
    if (darkToggle) darkToggle.innerHTML = '<i class="bi bi-sun text-lg"></i>';
  }

  if (darkToggle) {
    darkToggle.addEventListener('click', function () {
      const isDark = html.getAttribute('data-theme') === 'dark';
      if (isDark) {
        html.removeAttribute('data-theme');
        localStorage.setItem('logitrack-theme', 'light');
        darkToggle.innerHTML = '<i class="bi bi-moon-stars text-lg"></i>';
      } else {
        html.setAttribute('data-theme', 'dark');
        localStorage.setItem('logitrack-theme', 'dark');
        darkToggle.innerHTML = '<i class="bi bi-sun text-lg"></i>';
      }
    });
  }

  // ---- Notification Dropdown ----
  const notifBtn = document.getElementById('notifBtn');
  const notifDropdown = document.getElementById('notifDropdown');
  const profileBtn = document.getElementById('profileBtn');
  const profileDropdown = document.getElementById('profileDropdown');

  if (notifBtn && notifDropdown) {
    notifBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      notifDropdown.classList.toggle('show');
      if (profileDropdown) profileDropdown.classList.remove('show');
    });
  }

  if (profileBtn && profileDropdown) {
    profileBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      profileDropdown.classList.toggle('show');
      if (notifDropdown) notifDropdown.classList.remove('show');
    });
  }

  document.addEventListener('click', function () {
    if (notifDropdown) notifDropdown.classList.remove('show');
    if (profileDropdown) profileDropdown.classList.remove('show');
  });

  if (notifDropdown) notifDropdown.addEventListener('click', function (e) { e.stopPropagation(); });
  if (profileDropdown) profileDropdown.addEventListener('click', function (e) { e.stopPropagation(); });

  // ---- Active Sidebar Link ----
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  const pageMap = {
    'index.html': '/',
    'assigned_shipments.html': '/assigned',
    'shipment_details.html': '/shipment',
    'vehicles.html': '/vehicles',
    'drivers.html': '/drivers',
    'routes.html': '/routes',
    'pod.html': '/pod',
    'earnings.html': '/earnings',
    'settings.html': '/settings',
  };

  sidebarLinks.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // ---- Animated Counters ----
  const counters = document.querySelectorAll('[data-counter]');
  const observerOptions = { threshold: 0.5 };

  const counterObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-counter'), 10);
        const prefix = el.getAttribute('data-prefix') || '';
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1500;
        const start = performance.now();

        function animate(now) {
          const progress = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          const current = Math.floor(eased * target);
          el.textContent = prefix + current.toLocaleString() + suffix;
          if (progress < 1) requestAnimationFrame(animate);
        }

        requestAnimationFrame(animate);
        counterObserver.unobserve(el);
      }
    });
  }, observerOptions);

  counters.forEach(function (counter) { counterObserver.observe(counter); });

  // ---- Filter Buttons ----
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const group = btn.closest('.filter-group');
      if (group) {
        group.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
      }
      btn.classList.add('active');

      // Filter table rows if applicable
      const filterValue = btn.getAttribute('data-filter');
      const tableRows = document.querySelectorAll('.data-table tbody tr');
      if (tableRows.length > 0 && filterValue) {
        tableRows.forEach(function (row) {
          if (filterValue === 'all') {
            row.style.display = '';
          } else {
            const status = row.getAttribute('data-status') || '';
            row.style.display = status === filterValue ? '' : 'none';
          }
        });
      }
    });
  });

  // ---- Search Table ----
  const searchInput = document.getElementById('tableSearch');
  if (searchInput) {
    searchInput.addEventListener('input', function () {
      const query = this.value.toLowerCase();
      const rows = document.querySelectorAll('.data-table tbody tr');
      rows.forEach(function (row) {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? '' : 'none';
      });
    });
  }

  // ---- Signature Pad ----
  const sigCanvas = document.getElementById('signaturePad');
  if (sigCanvas) {
    const ctx = sigCanvas.getContext('2d');
    let isDrawing = false;
    ctx.strokeStyle = '#4f46e5';
    ctx.lineWidth = 2.5;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    function getPos(e) {
      const rect = sigCanvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return { x: clientX - rect.left, y: clientY - rect.top };
    }

    sigCanvas.addEventListener('mousedown', function (e) { isDrawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); });
    sigCanvas.addEventListener('mousemove', function (e) { if (!isDrawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); });
    sigCanvas.addEventListener('mouseup', function () { isDrawing = false; });
    sigCanvas.addEventListener('mouseleave', function () { isDrawing = false; });

    sigCanvas.addEventListener('touchstart', function (e) { e.preventDefault(); isDrawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); });
    sigCanvas.addEventListener('touchmove', function (e) { e.preventDefault(); if (!isDrawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); });
    sigCanvas.addEventListener('touchend', function () { isDrawing = false; });

    const clearSig = document.getElementById('clearSignature');
    if (clearSig) {
      clearSig.addEventListener('click', function () {
        ctx.clearRect(0, 0, sigCanvas.width, sigCanvas.height);
      });
    }
  }

  // ---- Modal Functions ----
  window.openModal = function (id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.add('show');
  };

  window.closeModal = function (id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.remove('show');
  };

  // Close modal on backdrop click
  document.querySelectorAll('.modal-backdrop').forEach(function (modal) {
    modal.addEventListener('click', function (e) {
      if (e.target === modal) modal.classList.remove('show');
    });
  });

  // ---- Settings Tabs ----
  const settingsTabs = document.querySelectorAll('.settings-tab');
  const settingsPanels = document.querySelectorAll('.settings-panel');

  settingsTabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      settingsTabs.forEach(function (t) { t.classList.remove('active'); });
      settingsPanels.forEach(function (p) { p.style.display = 'none'; });
      tab.classList.add('active');
      const target = document.getElementById(tab.getAttribute('data-tab'));
      if (target) {
        target.style.display = 'block';
        target.classList.add('animate-fade-in');
      }
    });
  });

  // ---- POD Progress ----
  window.updatePodProgress = function () {
    const checks = document.querySelectorAll('.pod-check');
    const total = checks.length;
    let done = 0;
    checks.forEach(function (c) {
      if (c.checked || c.getAttribute('data-done') === 'true') done++;
    });
    const pct = Math.round((done / total) * 100);
    const fill = document.querySelector('.progress-bar-custom .fill');
    const label = document.querySelector('.pod-progress-label');
    if (fill) fill.style.width = pct + '%';
    if (label) label.textContent = done + ' of ' + total + ' steps completed';
  };

  // ---- POD Success ----
  window.showPodSuccess = function () {
    const modal = document.getElementById('podSuccessModal');
    if (modal) {
      modal.classList.add('show');
      setTimeout(function () { modal.classList.remove('show'); }, 4000);
    }
  };

});
