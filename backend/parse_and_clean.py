#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import re
import json

# Load and parse XML file
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

# Function to extract and process SMS messages
def extract_sms_data(root):
    sms_list = []
    unprocessed_messages = []

    for sms in root.findall('sms'):
        body = sms.find('body').text if sms.find('body') is not None else ""

        processed_sms = categorize_sms(body)
        if processed_sms:
            sms_list.append(processed_sms)
        else:
            unprocessed_messages.append(body)

    return sms_list, unprocessed_messages

# Function to categorize SMS transactions
def categorize_sms(body):
    categories = {
        "Incoming Money": r"received (\d+) RWF",
        "Payments to Code Holders": r"payment of (\d+) RWF to",
        "Transfers to Mobile Numbers": r"transferred (\d+) RWF",
        "Bank Deposits": r"deposited (\d+) RWF",
        "Airtime Bill Payments": r"purchased an internet bundle",
        "Cash Power Bill Payments": r"Cash Power Bill Payments",
        "Withdrawals from Agents": r"withdrawn (\d+) RWF",
        "Bank Transfers": r"Bank Transfer",
        "Internet and Voice Bundle Purchases": r"purchased.*bundle",
        "Transactions Initiated by Third Parties": r"initiated by|processed by|via agent"
    }

    for category, pattern in categories.items():
        match = re.search(pattern, body, re.IGNORECASE)
        if match:
            return {
                "category": category,
                "amount": match.group(1) if match.groups() else None,
                "raw_text": body
            }

    return None

# Function to log unprocessed messages
def log_unprocessed(messages, file_path="unprocessed_messages.json"):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)

# Main execution
if __name__ == "__main__":
    xml_file = "assets/momo_sample.xml"
    
    root = parse_xml(xml_file)
    cleaned_sms, unprocessed = extract_sms_data(root)
    
    log_unprocessed(unprocessed)
    
    print("Processed SMS:", cleaned_sms)
    print(f"Unprocessed messages saved to 'unprocessed_messages.json'")

