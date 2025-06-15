import json
import os

def log_unprocessed(messages, output_path=None):
    if not output_path:
        logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        output_path = os.path.join(logs_dir, 'unprocessed_messages.json')

    with open(output_path, 'w') as f:
        json.dump(messages, f, indent=4)
    print(f"🔍 Unprocessed messages logged to: {output_path}")

