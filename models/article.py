from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    """
    Data model for an article with URL, retrieval timestamp, and markdown content.
    """
    url: str
    retrieved_at: datetime
    markdown: str
    
    @classmethod
    def from_url_and_markdown(cls, url: str, markdown: str) -> 'Article':
        """
        Factory method to create an Article with current UTC datetime.
        
        Args:
            url (str): The source URL
            markdown (str): The markdown content
            
        Returns:
            Article: New Article instance with current timestamp
        """
        return cls(
            url=url,
            retrieved_at=datetime.utcnow(),
            markdown=markdown
        )