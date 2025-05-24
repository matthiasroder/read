#!/usr/bin/env python3

from models.article import Article

def test_article():
    """Test Article dataclass and factory method"""
    
    sample_url = "https://example.com/test-article"
    sample_markdown = """# Test Article

This is a **test article** with some *formatting*.

## Features
- Lists
- Links
- Code blocks

> This is a quote
"""
    
    try:
        print("Creating Article using factory method...")
        article = Article.from_url_and_markdown(sample_url, sample_markdown)
        
        print("Success! Article created.")
        print("\nArticle details:")
        print(f"URL: {article.url}")
        print(f"Retrieved at: {article.retrieved_at}")
        print(f"Markdown length: {len(article.markdown)} characters")
        print("\nMarkdown content:")
        print("-" * 50)
        print(article.markdown)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_article()