#!/usr/bin/env python3

import json
import os

LOG_DIR = "backend/logs"
LOG_FILE = f"{LOG_DIR}/unprocessed_messages.json"

# Ensure logs directory exists
def ensure_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

# Function to log unprocessed messages
def log_unprocessed(messages):
    ensure_log_directory()
    
    # Write unprocessed messages to JSON file
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)

    print(f"Unprocessed messages logged in '{LOG_FILE}'")

# Example usage (Testing logging)
if __name__ == "__main__":
    sample_unprocessed = [
        "Transaction details unclear: Received XYZ amount from unknown sender",
        "Incomplete SMS format - missing amount"
    ]
    log_unprocessed(sample_unprocessed)

