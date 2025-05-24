# read
A CLI tool for fetching online articles, converting them to Markdown, and saving them to Airtable.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Airtable
Create a `.env` file in the project root:
```bash
# Airtable Configuration
AIRTABLE_API_KEY=your_airtable_api_key_here
BASE_ID=your_base_id_here
TABLE_NAME=your_table_name_or_id_here
```

**Getting your Airtable credentials:**
- **API Key**: Go to [Airtable Account](https://airtable.com/account) → Generate API key
- **Base ID**: From your base URL: `https://airtable.com/appXXXXXX/tblYYYYYY` → Base ID is `appXXXXXX`
- **Table Name**: Either the table name (e.g., "WebArticles") or table ID (e.g., "tblYYYYYY")

### 3. Create Airtable Table
Your Airtable table should have these fields:
- `url` (Single line text)
- `retrieved_at` (Date & time)
- `markdown` (Long text)

## Usage

### Basic Usage
```bash
python main.py <URL>
```

### Examples
```bash
# Fetch and upload an article
python main.py https://example.com/article

# Test without uploading (dry run)
python main.py https://example.com/article --dry-run

# URLs without http/https are automatically prefixed
python main.py example.com/article
```

### Options
- `--dry-run`: Preview the conversion without uploading to Airtable

## How It Works

1. **Fetch**: Downloads HTML content from the provided URL
2. **Convert**: Transforms HTML to clean Markdown format
3. **Save**: Uploads article with URL, timestamp, and markdown to Airtable

## Testing

Run individual component tests:
```bash
python test_fetcher.py     # Test URL fetching
python test_markdown.py    # Test HTML to Markdown conversion
python test_article.py     # Test Article data model
python test_airtable.py    # Test Airtable upload
```
