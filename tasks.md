# MVP Build Plan: URL to Markdown to Airtable

## Phase 1: Project Setup

### 1.1 Initialize the project folder

**Start**: Empty directory
**End**: `url2airtable/` created with a `.gitignore`, `README.md`, and Python package structure

### 1.2 Create and activate virtual environment

**Start**: Inside `url2airtable/`
**End**: Virtual environment created and activated, e.g., `.venv`

### 1.3 Create `requirements.txt`

**Start**: Empty file
**End**: File includes:

```
requests
html2text
airtable-python-wrapper
python-dotenv
```

### 1.4 Create base file structure

**Start**: Inside project root
**End**: Files and folders created as described in the architecture

---

## Phase 2: Article Fetching

### 2.1 Implement `fetcher.py` with `fetch_html(url)`

**Start**: Empty file
**End**: Function accepts a URL, returns raw HTML string using `requests.get`

### 2.2 Add error handling for bad URLs and timeouts

**Start**: Working `fetch_html(url)`
**End**: Handles non-200 responses and `requests.exceptions`

### 2.3 Write a test script to verify HTML is fetched from a known URL

**Start**: Basic fetcher implemented
**End**: `test_fetcher.py` script prints HTML from e.g. `example.com`

---

## Phase 3: Markdown Conversion

### 3.1 Implement `convert_html_to_markdown(html)` in `markdown.py`

**Start**: HTML string input
**End**: Function returns Markdown using `html2text`

### 3.2 Write a test script for Markdown conversion

**Start**: Conversion function complete
**End**: Script loads a sample HTML string and prints Markdown output

---

## Phase 4: Data Model

### 4.1 Define `Article` dataclass in `article.py`

**Start**: Empty module
**End**: Class with `url`, `retrieved_at`, and `markdown` fields

### 4.2 Add factory function `Article.from_url_and_markdown(url, markdown)`

**Start**: Article class defined
**End**: Creates instance with current UTC datetime

### 4.3 Write a test script that instantiates and prints an `Article` object

**Start**: Factory method created
**End**: Test script shows expected field values

---

## Phase 5: Airtable Integration

### 5.1 Create `.env` file with `AIRTABLE_API_KEY`, `BASE_ID`, `TABLE_NAME`

**Start**: None exist
**End**: Environment file is created and loaded via `dotenv`

### 5.2 Implement `airtable.py` with function `upload_article(article)`

**Start**: Article object available
**End**: Function uses Airtable client to create a new row

### 5.3 Add error handling for API errors

**Start**: Airtable upload working
**End**: Logs descriptive error on failure

### 5.4 Write a test script that uploads a dummy article

**Start**: Upload function ready
**End**: Script uploads article and prints Airtable response ID

---

## Phase 6: CLI Orchestration

### 6.1 Implement `main.py` to parse URL from command line

**Start**: Empty file
**End**: Script reads `sys.argv[1]` and prints it

### 6.2 Wire main flow: fetch → convert → wrap in Article

**Start**: URL printing script
**End**: Prints an `Article` object with all fields populated

### 6.3 Add call to `upload_article(article)` in main flow

**Start**: Article object created
**End**: Article is uploaded to Airtable on run

### 6.4 Add logging output for each major step

**Start**: Full flow wired
**End**: Logs: "Fetching URL...", "Converting to Markdown...", etc.

---

## Phase 7: Final Touches

### 7.1 Add input validation for empty or invalid URLs

**Start**: Script assumes valid input
**End**: Gracefully rejects empty or malformed URLs

### 7.2 Add `--dry-run` CLI flag (prints instead of uploads)

**Start**: All code uploads automatically
**End**: If `--dry-run` is passed, article is printed not uploaded

### 7.3 Add README instructions for setup and usage

**Start**: Incomplete README
**End**: Includes setup steps, example `.env`, and CLI usage
