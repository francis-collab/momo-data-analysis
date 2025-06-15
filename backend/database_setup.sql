-- Create or update the transactions table with the revised schema
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
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
