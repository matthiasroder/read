#!/usr/bin/env python3

from utils.markdown import convert_html_to_markdown

def test_markdown_conversion():
    """Test HTML to Markdown conversion"""
    
    sample_html = """
    <html>
    <head><title>Test Article</title></head>
    <body>
        <h1>Sample Article</h1>
        <p>This is a <strong>test article</strong> with some <em>formatting</em>.</p>
        <h2>Features</h2>
        <ul>
            <li>Links: <a href="https://example.com">Example</a></li>
            <li>Images: <img src="test.jpg" alt="Test image"></li>
            <li>Code: <code>print("hello")</code></li>
        </ul>
        <blockquote>This is a quote</blockquote>
    </body>
    </html>
    """
    
    try:
        print("Converting sample HTML to Markdown...")
        markdown = convert_html_to_markdown(sample_html)
        
        print("Success! Conversion complete.")
        print("\nMarkdown output:")
        print("-" * 50)
        print(markdown)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_markdown_conversion()