import os
import logging
from dotenv import load_dotenv
from airtable import Airtable
from models.article import Article

load_dotenv()

def upload_article(article: Article) -> str:
    """
    Upload an Article to Airtable.
    
    Args:
        article (Article): The article to upload
        
    Returns:
        str: Airtable record ID
        
    Raises:
        Exception: If upload fails
    """
    api_key = os.getenv('AIRTABLE_API_KEY')
    base_id = os.getenv('BASE_ID')
    table_name = os.getenv('TABLE_NAME')
    
    if not all([api_key, base_id, table_name]):
        raise Exception("Missing Airtable configuration. Check .env file.")
    
    try:
        airtable = Airtable(base_id, table_name, api_key)
        
        record = {
            'url': article.url,
            'retrieved_at': article.retrieved_at.isoformat(),
            'markdown': article.markdown
        }
        
        result = airtable.insert(record)
        
        if 'id' not in result:
            raise Exception(f"Airtable upload failed: No record ID returned. Response: {result}")
            
        logging.info(f"Successfully uploaded article to Airtable. Record ID: {result['id']}")
        return result['id']
        
    except Exception as e:
        error_msg = f"Failed to upload article to Airtable: {str(e)}"
        logging.error(error_msg)
        raise Exception(error_msg)