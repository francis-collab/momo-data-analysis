# MoMo Transaction Data Analysis Project

## Introduction

Welcome to **MoMo Transaction Data Analysis**, a full-stack web application built to parse, clean, store, and visualize mobile money transaction data extracted from SMS messages in XML format.

This app provides a **Flask-based REST API**, a **SQLite database**, and a **responsive JavaScript frontend** to help users filter, search, and analyze their mobile money transactions in a meaningful way.

---

## Features

- **Data Extraction & Cleaning**: Parses XML files containing SMS messages, extracting transaction fields such as amount, sender, recipient, type, and timestamp.
- **SQLite Database Storage**: Stores all cleaned transactions using a relational schema and indexes for fast lookup.
- **RESTful API**: A backend powered by Flask offering endpoints to get transactions, filter by type, search by name, and fetch stats.
- **Responsive Dashboard**: A clean HTML/CSS/JS-based frontend allowing users to interact with their data in real time.
- **Search & Filter Tools**: Includes type filters (e.g., send, receive), a live search bar, and transaction summaries.

---

## Project Directory Structure

```
momo-data-analysis/
├── backend/
│   ├── api.py              # Flask API server
│   ├── parse_and_clean.py # Extracts and cleans XML transaction data
│   ├── populate_db.py      # Parses cleaned data and populates SQLite DB
│   ├── logging_config.py   # Logging setup and configuration
│   ├── database_setup.sql  # SQL schema for creating the database
│   ├── requirements.txt    # Python dependencies
│   └── logs/               # Folder for storing raw or failed messages
├── frontend/
│   ├── index.html          # Main dashboard UI
│   ├── style.css           # Responsive styling
│   ├── app.js              # Frontend JS logic and API interaction
│   └── filters.js          # (Optional) Filtering utility functions
├── assets/
│   └── modified_sms_v2.xml # XML data source of SMS transactions
├── docs/
│   └── report.pdf          # Project report document
└── README.md               # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Flask
- SQLite3
- A modern web browser (Chrome, Firefox, Edge, etc.)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/momo-data-analysis.git
cd momo-data-analysis/backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Populate the database from XML

```bash
python3 populate_db.py
```

### 4. Run the Flask API server

```bash
python3 api.py
```

---

## Serving the Frontend

You can open the frontend directly in your browser:

```bash
cd ../frontend
open index.html
```

Or start a local development server:

```bash
python3 -m http.server 8000
```

Then access the app at: [http://localhost:8000](http://localhost:8000)

---

## How It Works

- **Upload & Parse**: The backend reads the SMS XML and extracts MoMo transactions.
- **Store in SQLite**: Structured data is inserted into the `momo_data.db` file.
- **Serve API**: Flask exposes transaction endpoints at `/transactions`, `/search`, `/summary`, etc.
- **Load Frontend**: The dashboard sends AJAX requests to the backend and renders the data interactively.

---

## API Endpoints

- `GET /transactions` — Get all transactions
- `GET /transactions?type=sent` — Filter by transaction type
- `GET /search?query=john` — Search by sender or recipient
- `GET /summary` — Get transaction summary statistics

---

## Contributing

Pull requests are welcome!

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Push to your fork
5. Submit a pull request

---

## Demo Video

**Awalkthrough of the application can be found here**: [Watch on YouTube](https://youtu.be/pdkA6sqBUoQ?si=Dcl5BKzHtk0eaCeM)

---

## License

This project is licensed under the MIT License.
See the `LICENSE` file for more details.

---

## Author

This application was designed and developed by **Francis Mutabazi**.
You can find more of my work on [GitHub](https://github.com/francis-collab).

                  
