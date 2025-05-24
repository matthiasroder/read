import html2text


def convert_html_to_markdown(html):
    """
    Convert HTML content to Markdown format.
    
    Args:
        html (str): Raw HTML content
        
    Returns:
        str: Markdown formatted content
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    
    markdown = h.handle(html)
    return markdown.strip()