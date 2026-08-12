# WebLens 🔎

## Web Data Extraction & Analysis Tool

WebLens is a simple web scraping and data extraction web application
developed using Python and Flask.

The application allows users to enter a webpage URL and extract basic
information such as the page title, headings, paragraphs, links, and
image URLs. It also provides basic statistics about the extracted
content and allows users to download the collected data as a CSV file.

WebLens also maintains a lightweight scraping history using JSON,
allowing users to keep track of recently analyzed webpages.

The project was developed to gain practical experience with Python
web development, HTTP requests, HTML parsing, data extraction, and
integrating a Python backend with a web-based interface.


---

## 🚀 Features

- Extract webpage title
- Extract H1-H6 headings
- Extract paragraphs
- Extract webpage links
- Extract image URLs
- Calculate basic webpage statistics
- Count words extracted from paragraphs
- Maintain recent scraping history
- Clear scraping history
- Export scraped data as CSV
- Handle invalid or inaccessible URLs
- Responsive and professional web interface


---

## 🛠️ Tech Stack

### Backend

- Python
- Flask
- Requests
- BeautifulSoup4

### Frontend

- HTML
- CSS
- Jinja2 Templates

### Data Handling

- JSON
- CSV


---

## 📂 Project Structure

```text
WebLens/
│
├── app.py
├── scraper.py
├── history.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css
    └── script.js
