import re
import xml.etree.ElementTree as ET
from datetime import datetime

def extract_transaction_data(body):
    body = body.strip()

    if "received" in body.lower() and "from" in body.lower():
        match = re.search(r"received\s+([\d,]+)\s+RWF from (.+?)\s+\(", body)
        if match:
            amount = int(match.group(1).replace(",", ""))
            return {"sender": match.group(2).strip(), "recipient": "Me", "amount": amount, "type": "Received"}

    elif "payment of" in body.lower():
        match = re.search(r"payment of\s+([\d,]+)\s+RWF to (.+?)\s", body)
        if match:
            amount = int(match.group(1).replace(",", ""))
            return {"sender": "Me", "recipient": match.group(2).strip(), "amount": amount, "type": "Sent"}

    elif "transferred to" in body.lower():
        match = re.search(r"\*165\*S\*(\d{3,})\s+RWF transferred to (.+?)\s+\(", body)
        if match:
            amount = int(match.group(1).replace(",", ""))
            return {"sender": "Me", "recipient": match.group(2).strip(), "amount": amount, "type": "Sent"}

    elif "deposit of" in body.lower():
        match = re.search(r"deposit of\s+([\d,]+)\s+RWF", body)
        if match:
            amount = int(match.group(1).replace(",", ""))
            return {"sender": "Bank", "recipient": "Me", "amount": amount, "type": "Deposit"}

    elif "to airtime" in body.lower():
        match = re.search(r"payment of\s+([\d,]+)\s+RWF to Airtime", body)
        if match:
            amount = int(match.group(1).replace(",", ""))
            return {"sender": "Me", "recipient": "Airtime", "amount": amount, "type": "Sent"}

    return None

def extract_sms_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    messages = []
    unprocessed = []

    for sms in root.findall(".//sms"):
        body = sms.attrib.get("body", "")
        date_ms = int(sms.attrib.get("date", "0"))

        tx = extract_transaction_data(body)
        if tx:
            tx["timestamp"] = datetime.fromtimestamp(date_ms / 1000).isoformat()
            messages.append(tx)
        else:
            unprocessed.append(body)

    return messages, unprocessed

