const API_BASE_URL = "http://127.0.0.1:5000";

// Fetch and display all or filtered transactions
async function loadTransactions(type = "") {
  let url = type ? `${API_BASE_URL}/transactions/${type}` : `${API_BASE_URL}/transactions`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    displayTransactions(data);
  } catch (err) {
    console.error("Error loading transactions:", err);
  }
}

// Display transactions in the container
function displayTransactions(transactions) {
  const container = document.getElementById("transactions-container");
  if (transactions.length === 0) {
    container.innerHTML = "<p>No transactions found.</p>";
    return;
  }

  let html = `<table>
    <thead>
      <tr>
        <th>ID</th><th>Type</th><th>Amount</th><th>Sender</th><th>Recipient</th><th>Date</th>
      </tr>
    </thead>
    <tbody>`;

  transactions.forEach(tx => {
    html += `<tr>
      <td>${tx.id}</td>
      <td>${tx.tx_type}</td>
      <td>${tx.amount}</td>
      <td>${tx.sender}</td>
      <td>${tx.recipient}</td>
      <td>${tx.date}</td>
    </tr>`;
  });

  html += "</tbody></table>";
  container.innerHTML = html;
}

// Fetch and display transaction summary
async function loadSummary() {
  try {
    const res = await fetch(`${API_BASE_URL}/summary`);
    const summary = await res.json();
    displaySummary(summary);
  } catch (err) {
    console.error("Error loading summary:", err);
  }
}

function displaySummary(summary) {
  const container = document.getElementById("summary-container");
  if (summary.length === 0) {
    container.innerHTML = "<p>No summary data available.</p>";
    return;
  }

  let html = "<ul>";
  summary.forEach(item => {
    html += `<li>${item.tx_type}: ${item.total_transactions} transactions, Total amount: ${item.total_amount}</li>`;
  });
  html += "</ul>";

  container.innerHTML = html;
}

// Search transactions by sender or recipient
async function searchTransactions() {
  const query = document.getElementById("search-input").value.trim();
  if (!query) {
    alert("Please enter a search query.");
    return;
  }

  try {
    const res = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
    const results = await res.json();
    displayTransactions(results);
  } catch (err) {
    console.error("Error searching transactions:", err);
  }
}

// Load default data on page load
window.onload = () => {
  loadTransactions();
  loadSummary();
};
