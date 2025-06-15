import os
import sqlite3
from parse_and_clean import extract_sms_data
from datetime import datetime

DB_FILE = 'momo_data.db'
SMS_XML_FILE = '../assets/modified_sms_v2.xml'
UNPROCESSED_LOG_FILE = './logs/unprocessed_messages.json'

def create_table_if_not_exists(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tx_id TEXT,
            tx_type TEXT,
            amount INTEGER,
            sender TEXT,
            recipient TEXT,
            date TEXT,
            balance INTEGER,
            fee INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()

def insert_transaction(conn, txn):
    sql = """
    INSERT INTO transactions
    (tx_id, tx_type, amount, sender, recipient, date, balance, fee)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """
    conn.execute(sql, (
        txn.get('tx_id'),        # unique transaction id or None
        txn.get('type'),         # tx_type: e.g. 'Sent', 'Received'
        txn.get('amount'),       # integer amount
        txn.get('sender'),       # sender string
        txn.get('recipient'),    # recipient string
        txn.get('date'),         # date string (e.g. '2025-06-15')
        txn.get('balance'),      # int or None
        txn.get('fee')           # int or None
    ))
    conn.commit()

def main():
    if not os.path.exists(SMS_XML_FILE):
        print(f"❌ File not found: {SMS_XML_FILE}")
        return

    transactions, unprocessed = extract_sms_data(SMS_XML_FILE)

    if unprocessed:
        os.makedirs(os.path.dirname(UNPROCESSED_LOG_FILE), exist_ok=True)
        import json
        with open(UNPROCESSED_LOG_FILE, 'w') as f:
            json.dump(unprocessed, f, indent=2)
        print(f"🔍 Unprocessed messages logged to: {os.path.abspath(UNPROCESSED_LOG_FILE)}")

    conn = sqlite3.connect(DB_FILE)
    create_table_if_not_exists(conn)

    count = 0
    for txn in transactions:
        insert_transaction(conn, txn)
        count += 1

    conn.commit()
    conn.close()

    print(f"✅ {count} transactions inserted into {DB_FILE}")

if __name__ == "__main__":
    main()

