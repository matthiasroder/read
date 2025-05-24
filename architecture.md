# Python CLI Tool: URL to Markdown to Airtable

## File + Folder Structure

```bash
url2airtable/
│
├── main.py                 # CLI entry point
├── config.py               # Global configuration (API keys, Airtable settings)
├── utils/
│   ├── __init__.py
│   └── markdown.py         # Article to Markdown conversion
│
├── services/
│   ├── __init__.py
│   ├── fetcher.py          # Download article HTML from URL
│   └── airtable.py         # Handle Airtable interaction
│
├── models/
│   ├── __init__.py
│   └── article.py          # Article dataclass to store state
│
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and usage
```

---

## Component Responsibilities

### `main.py`

* CLI entry script
* Orchestrates the flow: fetch → convert → upload
* Accepts arguments like URL (optionally: config override, dry-run)

### `config.py`

* Stores:

  * Airtable base ID
  * Table name
  * Airtable API key (via env vars or dotenv)
* Centralized place for config management

### `utils/markdown.py`

* Uses a library like `readability-lxml`, `BeautifulSoup`, or `html2text`
* Extracts the main content from HTML and converts to Markdown

### `services/fetcher.py`

* Fetches the HTML of a given URL
* Handles common HTTP exceptions and retries

### `services/airtable.py`

* Interacts with Airtable using the **official Airtable API**
* Handles authentication, insertion, and response handling
* Posts the following fields:

  * `url` (string)
  * `retrieved_at` (datetime)
  * `markdown` (long text)

### `models/article.py`

* A `@dataclass` representing an `Article` with:

  * `url`
  * `retrieved_at`
  * `markdown`

---

## State Management

### In-Memory State

* The `Article` object holds transient state for each run:

  * Populated after fetching + conversion
  * Passed to Airtable service

### Persistent State

* No local persistence unless you add a cache or SQLite layer
* All saved data is uploaded to **Airtable** (acts as your DB)

---

## Service Connections

```text
          +-------------+      +-------------+      +---------------+
CLI Input |   main.py   |----->| fetcher.py  |----->| markdown.py   |
          +-------------+      +-------------+      +---------------+
                  |                                        |
                  v                                        v
          +-------------+                         +-----------------+
          |  article.py |<------------------------|  HTML to MD     |
          +-------------+                         +-----------------+
                  |
                  v
          +---------------+
          | airtable.py   |
          +---------------+
                  |
                  v
           Airtable (API)
```

---

## Example `requirements.txt`

```txt
requests
html2text
python-dotenv
airtable-python-wrapper
```

---

## Example CLI Usage

```bash
python main.py "https://example.com/article-to-save"
```

---

## Airtable Schema Example

| url          | retrieved\_at    | markdown         |
| ------------ | ---------------- | ---------------- |
| https\://... | 2025-05-24 12:30 | # Title\nContent |
