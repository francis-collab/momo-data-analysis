from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS
DATABASE = "/home/francis-collab/momo-data-analysis/backend/momo_data.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API Route: Fetch all transactions
@app.route("/transactions", methods=["GET"])
def get_all_transactions():
    conn = get_db_connection()
    transactions = conn.execute("SELECT * FROM transactions").fetchall()
    conn.close()
    return jsonify([dict(tx) for tx in transactions])

# API Route: Fetch transactions by type
@app.route("/transactions/<tx_type>", methods=["GET"])
def get_transactions_by_type(tx_type):
    conn = get_db_connection()
    query = "SELECT * FROM transactions WHERE tx_type = ?"
    transactions = conn.execute(query, (tx_type,)).fetchall()
    conn.close()
    return jsonify([dict(tx) for tx in transactions])

# API Route: Search transactions by sender or recipient or date
@app.route("/search", methods=["GET"])
def search_transactions():
    query_param = request.args.get("q", "")
    conn = get_db_connection()
    query = """
    SELECT * FROM transactions
    WHERE sender LIKE ? OR recipient LIKE ? OR date LIKE ?
    """
    transactions = conn.execute(query, (f"%{query_param}%", f"%{query_param}%", f"%{query_param}%")).fetchall()
    conn.close()
    return jsonify([dict(tx) for tx in transactions])

# API Route: Fetch transaction summary
@app.route("/summary", methods=["GET"])
def transaction_summary():
    conn = get_db_connection()
    query = """
    SELECT tx_type, COUNT(*) as total_transactions, SUM(amount) as total_amount
    FROM transactions GROUP BY tx_type
    """
    summary = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(s) for s in summary])

# Run server
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

