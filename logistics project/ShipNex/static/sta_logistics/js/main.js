/* ==========================
   THEME SWITCHER
   ========================== */

function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  updateThemeIcon(newTheme);
  
  // Show visual toast notification
  showToast("Switched to " + (newTheme === 'dark' ? 'Dark' : 'Light') + " Mode");
}

function updateThemeIcon(theme) {
  const btn = document.getElementById('themeToggle');
  if (btn) {
    const icon = btn.querySelector('i');
    if (icon) {
      if (theme === 'dark') {
        icon.className = 'fa-solid fa-sun';
      } else {
        icon.className = 'fa-solid fa-moon';
      }
    }
  }
}

function highlightActiveSidebarLink() {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll('.sidebar ul li a');
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href && (currentPath === href || currentPath.endsWith(href))) {
      link.classList.add('active');
      const li = link.closest('li');
      if (li) li.classList.add('active');
    }
  });
}

// Initialise theme and active links on page load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  highlightActiveSidebarLink();
});


/* ==========================
   SEARCH TABLE
   ========================== */

function searchTable(inputId, tableId) {
  let input = document.getElementById(inputId);
  let filter = input.value.toUpperCase();
  let table = document.getElementById(tableId);
  let tr = table.getElementsByTagName("tr");

  for (let i = 1; i < tr.length; i++) {
    let found = false;
    let td = tr[i].getElementsByTagName("td");

    for(let j=0; j<td.length; j++){
      if(td[j]){
        let txtValue = td[j].textContent || td[j].innerText;
        if(txtValue.toUpperCase().indexOf(filter) > -1){
          found = true;
          break;
        }
      }
    }
    tr[i].style.display = found ? "" : "none";
  }
}

/* ==========================
   DELETE CONFIRMATION
   ========================== */

function deleteRecord(id){
  let confirmDelete = confirm("Are you sure you want to delete this record?");
  if(confirmDelete){
    showToast("Record " + id + " Deleted Successfully");
  }
}

/* ==========================
   STATUS UPDATE
   ========================== */

function updateStatus(id, status){
  showToast("Status of " + id + " Updated To: " + status);
}

/* ==========================
   VIEW DETAILS
   ========================== */

function viewDetails(id){
  showToast("Opening details for: " + id);
}

/* ==========================
   DOWNLOAD PDF
   ========================= */

function downloadPDF(id){
  showToast("Preparing PDF download for: " + id);
}

/* ==========================
   PRINT INVOICE
   ========================== */

function printInvoice(){
  window.print();
}

/* ==========================
   PAYMENT REMINDER
   ========================== */

function sendReminder(id){
  showToast("Payment Reminder Sent for: " + id);
}

/* ==========================
   REFUND PAYMENT
   ========================== */

function refundPayment(id){
  let refund = confirm("Refund this payment?");
  if(refund){
    showToast("Refund Processed for: " + id);
  }
}

/* ==========================
   ASSIGN DRIVER
   ========================== */

function assignDriver(driverId){
  showToast("Driver Assigned: " + driverId);
}

/* ==========================
   ASSIGN VEHICLE
   ========================== */

function assignVehicle(vehicleId){
  showToast("Vehicle Assigned: " + vehicleId);
}

/* ==========================
   TRACK SHIPMENT
   ========================== */

function trackShipment(){
  let trackingId = document.getElementById("trackingId").value;
  if(trackingId === ""){
    showToast("Please enter a Tracking ID");
    return;
  }
  showToast("Searching Shipment: " + trackingId);
}

/* ==========================
   POD SUBMIT
   ========================== */

function submitPOD(){
  showToast("Proof Of Delivery Submitted Successfully");
}

/* ==========================
   EXPORT TABLE CSV
   ========================== */

function exportTableToCSV(filename){
  let csv = [];
  let rows = document.querySelectorAll("table tr");

  for(let i=0; i<rows.length; i++){
    let row = [];
    let cols = rows[i].querySelectorAll("td, th");

    for(let j=0; j<cols.length; j++){
      row.push(cols[j].innerText);
    }
    csv.push(row.join(","));
  }
  downloadCSV(csv.join("\n"), filename);
}

function downloadCSV(csv, filename){
  let csvFile;
  let downloadLink;

  csvFile = new Blob([csv], { type: "text/csv" });
  downloadLink = document.createElement("a");
  downloadLink.download = filename;
  downloadLink.href = window.URL.createObjectURL(csvFile);
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);
  downloadLink.click();
}

/* ==========================
   LIVE DATE TIME
   ========================== */

function updateDateTime(){
  let now = new Date();
  let dateTime = now.toLocaleDateString() + " " + now.toLocaleTimeString();
  let el = document.getElementById("datetime");
  if(el){
    el.innerHTML = dateTime;
  }
}

setInterval(updateDateTime, 1000);

/* ==========================
   DASHBOARD COUNTER
   ========================== */

function animateCounter(id, target){
  let el = document.getElementById(id);
  if (!el) return;
  
  let count = 0;
  let speed = target / 100;

  let update = () => {
    count += speed;
    if(count < target){
      el.innerHTML = Math.floor(count);
      requestAnimationFrame(update);
    } else {
      el.innerHTML = target;
    }
  };

  update();
}

/* ==========================
   LOADER
   ========================== */

function showLoader(){
  let el = document.getElementById("loader");
  if (el) el.style.display = "flex";
}

function hideLoader(){
  let el = document.getElementById("loader");
  if (el) el.style.display = "none";
}

/* ==========================
   TOAST MESSAGE
   ========================== */

function showToast(message){
  let existingToast = document.querySelector(".custom-toast");
  if(existingToast) {
    existingToast.remove();
  }

  let toast = document.createElement("div");
  toast.className = "custom-toast";
  toast.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${message}</span>`;
  
  // Custom styled popup in javascript
  toast.style.position = "fixed";
  toast.style.bottom = "24px";
  toast.style.right = "24px";
  toast.style.background = "var(--primary-gradient, linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%))";
  toast.style.color = "#ffffff";
  toast.style.padding = "14px 22px";
  toast.style.borderRadius = "12px";
  toast.style.boxShadow = "0 10px 25px -5px rgba(79, 70, 229, 0.4)";
  toast.style.zIndex = "9999";
  toast.style.display = "flex";
  toast.style.alignItems = "center";
  toast.style.gap = "10px";
  toast.style.fontFamily = "'Plus Jakarta Sans', sans-serif";
  toast.style.fontSize = "14px";
  toast.style.fontWeight = "600";
  toast.style.animation = "toastSlideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1)";
  
  // Append animation style dynamically if not defined in CSS
  if (!document.getElementById("toast-animation-style")) {
    let style = document.createElement("style");
    style.id = "toast-animation-style";
    style.innerHTML = `
      @keyframes toastSlideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
  }

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.transition = "opacity 0.3s ease, transform 0.3s ease";
    toast.style.opacity = "0";
    toast.style.transform = "translateY(10px)";
    setTimeout(() => {
      toast.remove();
    }, 3000);
  }, 3000);
}