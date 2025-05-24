#!/usr/bin/env python3

from services.fetcher import fetch_html

def test_fetch_html():
    """Test fetching HTML from example.com"""
    try:
        print("Fetching HTML from example.com...")
        html = fetch_html("https://example.com")
        
        print(f"Success! Fetched {len(html)} characters")
        print("First 200 characters of HTML:")
        print(html[:200])
        print("...")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_fetch_html()