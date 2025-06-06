#!/usr/bin/env python3

import logging
from models.article import Article
from services.airtable import upload_article

def test_airtable_upload():
    """Test uploading a dummy article to Airtable"""
    
    # Set up logging to see success/error messages
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Create a dummy article
    dummy_url = "https://example.com/test-article"
    dummy_markdown = """# Test Article Upload

This is a **test article** created for testing Airtable integration.

## Content
- This article was generated by the test script
- It contains sample markdown formatting
- The timestamp shows when it was created

> This is a test quote to verify markdown formatting works correctly.

```python
# Sample code block
print("Hello from the test article!")
```

*End of test article.*
"""
    
    try:
        print("Creating dummy article...")
        article = Article.from_url_and_markdown(dummy_url, dummy_markdown)
        
        print(f"Article created with timestamp: {article.retrieved_at}")
        print(f"Markdown length: {len(article.markdown)} characters")
        
        print("\nUploading to Airtable...")
        record_id = upload_article(article)
        
        print(f"✅ Success! Article uploaded to Airtable.")
        print(f"📋 Record ID: {record_id}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_airtable_upload()