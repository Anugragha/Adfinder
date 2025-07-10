# Contectual Adfinder
A Python Django web application that analyzes the content of any webpage and displays relevant ads based on extracted keywords. It uses Beautiful Soup for HTML parsing, RAKE (Rapid Automatic Keyword Extraction) for keyword extraction, and Tailwind CSS for a responsive, modern UI.

Features
  Fetches and parses webpage HTML using Beautiful Soup
  Extracts key terms using RAKE algorithm
  Matches keywords to a local ad database
  Displays contextually relevant ads
  Styled with Tailwind CSS for clean, responsive design

Tech Stack
  Backend: Python, Django
  Frontend: Tailwind CSS
  Web Scraping: Beautiful Soup
  Keyword Extraction: RAKE (via rake-nltk or custom RAKE implementation)
  Database: SQLite (default with Django, can be configured)

Installation

Clone the repository
```
git clone https://github.com/yourusername/contextual-adfinder.git
cd contextual-adfinder
```

Create a virtual environment
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

Install dependencies
```
pip install -r requirements.txt
```
Apply migrations
```
python manage.py migrate
```
Run the server
```
python manage.py runserver
```

How It Works

  User inputs a URL into the app.
  The backend uses Beautiful Soup to fetch and parse the HTML content.
  The raw text is sent through the RAKE algorithm to extract important keywords.
  Keywords are matched against a predefined ad database.
  Relevant ads are displayed back to the user on the frontend.
