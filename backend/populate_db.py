#!/usr/bin/env python3

import sqlite3
import json
from parse_and_clean import extract_sms_data, parse_xml

# Database file path
DB_FILE = "database/momo_data.db"

# Create database connection
def create_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

# Create table for transactions
def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL,
        raw_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn.execute(query)
    conn.commit()

# Insert cleaned data into the database
def insert_transactions(conn, transactions):
    query = """
    INSERT INTO transactions (category, amount, raw_text)
    VALUES (?, ?, ?);
    """
    cursor = conn.cursor()
    
    for sms in transactions:
        cursor.execute(query, (sms["category"], sms["amount"], sms["raw_text"]))
    
    conn.commit()

# Main execution
if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)

    # Load and process XML data
    xml_file = "assets/modified_sms_v2.xml"
    root = parse_xml(xml_file)
    cleaned_sms, _ = extract_sms_data(root)  # Ignore unprocessed for now

    # Insert data into the database
    insert_transactions(conn, cleaned_sms)
    
    print(f"Inserted {len(cleaned_sms)} transactions into the database.")
    conn.close()

