/* ===================================================
   LogiTrack Transporter Portal - Charts (Chart.js)
   =================================================== */

document.addEventListener('DOMContentLoaded', function () {

  // ---- Shipment Status Doughnut ----
  const statusCtx = document.getElementById('statusChart');
  if (statusCtx) {
    new Chart(statusCtx.getContext('2d'), {
      type: 'doughnut',
      data: {
        labels: ['Delivered', 'In Transit', 'Pending', 'Cancelled'],
        datasets: [{
          data: [186, 25, 37, 8],
          backgroundColor: ['#22c55e', '#4f46e5', '#f97316', '#ef4444'],
          borderWidth: 0,
          hoverOffset: 6,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '65%',
        plugins: {
          legend: {
            position: 'bottom',
            labels: { padding: 16, usePointStyle: true, pointStyle: 'circle', font: { size: 12, family: 'Inter' } }
          }
        }
      }
    });
  }

  // ---- Delivery Performance Line ----
  const perfCtx = document.getElementById('performanceChart');
  if (perfCtx) {
    new Chart(perfCtx.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            label: 'Shipments Delivered',
            data: [120, 145, 132, 158, 170, 186, 195, 210, 225, 240, 255, 270],
            borderColor: '#4f46e5',
            backgroundColor: 'rgba(79,70,229,0.1)',
            fill: true,
            tension: 0.4,
            pointRadius: 3,
            pointHoverRadius: 6,
          },
          {
            label: 'Shipments Assigned',
            data: [150, 165, 155, 180, 195, 210, 220, 235, 250, 265, 280, 295],
            borderColor: '#f97316',
            backgroundColor: 'rgba(249,115,22,0.08)',
            fill: true,
            tension: 0.4,
            pointRadius: 3,
            pointHoverRadius: 6,
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11, family: 'Inter' } } },
          y: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { size: 11, family: 'Inter' } } },
        },
        plugins: {
          legend: { position: 'bottom', labels: { padding: 16, usePointStyle: true, pointStyle: 'circle', font: { size: 12, family: 'Inter' } } }
        }
      }
    });
  }

  // ---- Monthly Earnings Bar (Dashboard) ----
  const earnCtx = document.getElementById('earningsBarChart');
  if (earnCtx) {
    new Chart(earnCtx.getContext('2d'), {
      type: 'bar',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Earnings (₹)',
          data: [65000, 72000, 68000, 85000, 92000, 105000],
          backgroundColor: 'rgba(79,70,229,0.7)',
          borderRadius: 8,
          barThickness: 28,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11, family: 'Inter' } } },
          y: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { size: 11, family: 'Inter' }, callback: function(v) { return '₹' + (v/1000) + 'k'; } } }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  // ---- Monthly Earnings Line (Earnings page) ----
  const earnLineCtx = document.getElementById('earningsLineChart');
  if (earnLineCtx) {
    new Chart(earnLineCtx.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Earnings (₹)',
          data: [65000, 72000, 68000, 85000, 92000, 105600],
          borderColor: '#4f46e5',
          backgroundColor: 'rgba(79,70,229,0.1)',
          fill: true,
          tension: 0.4,
          pointRadius: 4,
          pointHoverRadius: 7,
          pointBackgroundColor: '#4f46e5',
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false }, ticks: { font: { size: 11, family: 'Inter' } } },
          y: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { size: 11, family: 'Inter' }, callback: function(v) { return '₹' + (v/1000) + 'k'; } } }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

  // ---- Settlement Breakdown Doughnut ----
  const settleCtx = document.getElementById('settlementChart');
  if (settleCtx) {
    new Chart(settleCtx.getContext('2d'), {
      type: 'doughnut',
      data: {
        labels: ['Completed', 'Pending', 'In Review'],
        datasets: [{
          data: [78, 15, 7],
          backgroundColor: ['#22c55e', '#f97316', '#4f46e5'],
          borderWidth: 0,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '65%',
        plugins: {
          legend: { position: 'bottom', labels: { padding: 16, usePointStyle: true, pointStyle: 'circle', font: { size: 12, family: 'Inter' } } }
        }
      }
    });
  }

  // ---- Route Performance Bar ----
  const routeCtx = document.getElementById('routeChart');
  if (routeCtx) {
    new Chart(routeCtx.getContext('2d'), {
      type: 'bar',
      data: {
        labels: ['Mumbai-Delhi', 'Bangalore-Chennai', 'Delhi-Jaipur', 'Pune-Hyderabad', 'Kolkata-Bhubaneswar', 'Chennai-Coimbatore'],
        datasets: [{
          label: 'Trips Completed',
          data: [186, 142, 98, 112, 78, 89],
          backgroundColor: 'rgba(79,70,229,0.7)',
          borderRadius: 6,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        indexAxis: 'y',
        scales: {
          x: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { size: 11, family: 'Inter' } } },
          y: { grid: { display: false }, ticks: { font: { size: 11, family: 'Inter' } } }
        },
        plugins: { legend: { display: false } }
      }
    });
  }

});
