// Wait until DOM is ready
document.addEventListener("DOMContentLoaded", function() {
  console.log("Employee Management System Loaded ✅");
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function(event) {
      const email = document.querySelector('input[name="email"]').value;
      const phone = document.querySelector('input[name="phone"]').value;
      const salary = document.querySelector('input[name="salary"]').value;
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        showToast("❌ Invalid email format!");
        event.preventDefault();
        return;
      }
      if (!/^\d{10}$/.test(phone)) {
        showToast("❌ Phone number must be 10 digits!");
        event.preventDefault();
        return;
      }
      if (salary <= 0) {
        showToast("❌ Salary must be greater than 0!");
        event.preventDefault();
        return;
      }

      showToast("✅ Employee added successfully!");
    });
  }
  const searchInput = document.createElement("input");
  searchInput.placeholder = "🔍 Search by name, email, or department...";
  searchInput.style.margin = "10px";
  searchInput.style.padding = "8px";
  searchInput.style.width = "300px";
  searchInput.style.borderRadius = "6px";
  searchInput.style.border = "1px solid #ccc";

  const table = document.querySelector("table");
  if (table) {
    table.parentNode.insertBefore(searchInput, table);

    searchInput.addEventListener("keyup", function() {
      const filter = this.value.toLowerCase();
      const rows = table.querySelectorAll("tbody tr");

      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
      });
    });
  }
  if (table) {
    const headers = table.querySelectorAll("th");
    headers.forEach((header, index) => {
      header.style.cursor = "pointer";
      header.addEventListener("click", function() {
        sortTableByColumn(table, index);
      });
    });
  }

  function sortTableByColumn(table, columnIndex) {
    const rows = Array.from(table.rows).slice(1);
    const isAscending = table.getAttribute("data-sort") !== "asc";

    rows.sort((a, b) => {
      const aText = a.cells[columnIndex].textContent.trim();
      const bText = b.cells[columnIndex].textContent.trim();
      return isAscending ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });

    rows.forEach(row => table.appendChild(row));
    table.setAttribute("data-sort", isAscending ? "asc" : "desc");
  }
  const deleteLinks = document.querySelectorAll('a[href*="delete"]');
  deleteLinks.forEach(link => {
    link.addEventListener("click", function(event) {
      if (!confirm("⚠️ Are you sure you want to delete this employee?")) {
        event.preventDefault();
      }
    });
  });
  const toast = document.createElement("div");
  toast.id = "toast";
  document.body.appendChild(toast);

  function showToast(message) {
    toast.textContent = message;
    toast.className = "show";
    setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 3000);
  }
});
function sortTableByColumn(table, columnIndex) {
  const rows = Array.from(table.rows).slice(1);
  const isAscending = table.getAttribute("data-sort") !== "asc";
  rows.sort((a, b) => {
    const aText = a.cells[columnIndex].textContent.trim();
    const bText = b.cells[columnIndex].textContent.trim();
    return isAscending ? aText.localeCompare(bText) : bText.localeCompare(aText);
