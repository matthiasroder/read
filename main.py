#!/usr/bin/env python3

import sys
import logging
from urllib.parse import urlparse
from services.fetcher import fetch_html
from utils.markdown import convert_html_to_markdown
from models.article import Article
from services.airtable import upload_article

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def validate_url(url):
    """Validate that URL is not empty and has proper format"""
    if not url or not url.strip():
        raise ValueError("URL cannot be empty")
    
    url = url.strip()
    
    # Add http:// if no scheme provided
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Parse URL to validate format
    parsed = urlparse(url)
    if not parsed.netloc:
        raise ValueError("Invalid URL format")
    
    return url

def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL> [--dry-run]")
        sys.exit(1)
    
    url = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    try:
        # Validate URL
        url = validate_url(url)
        logger.info(f"URL validated: {url}")
        
        # Fetch HTML from URL
        logger.info(f"Fetching HTML from: {url}")
        html = fetch_html(url)
        logger.info(f"Successfully fetched {len(html)} characters of HTML")
        
        # Convert to Markdown
        logger.info("Converting HTML to Markdown...")
        markdown = convert_html_to_markdown(html)
        logger.info(f"Successfully converted to {len(markdown)} characters of Markdown")
        
        # Create Article object
        logger.info("Creating Article object...")
        article = Article.from_url_and_markdown(url, markdown)
        logger.info(f"Article created with timestamp: {article.retrieved_at}")
        
        # Print Article details
        print("\nArticle created successfully!")
        print(f"URL: {article.url}")
        print(f"Retrieved at: {article.retrieved_at}")
        print(f"Markdown length: {len(article.markdown)} characters")
        
        # Upload to Airtable or dry run
        if dry_run:
            logger.info("DRY RUN: Skipping Airtable upload")
            print("🔍 DRY RUN: Article would be uploaded to Airtable")
            print("   To actually upload, run without --dry-run flag")
        else:
            logger.info("Uploading to Airtable...")
            record_id = upload_article(article)
            logger.info(f"Successfully uploaded to Airtable! Record ID: {record_id}")
            print(f"✅ Article uploaded successfully! Record ID: {record_id}")
        
        print("\nFirst 300 characters of markdown:")
        print("-" * 50)
        print(article.markdown[:300])
        if len(article.markdown) > 300:
            print("...")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()