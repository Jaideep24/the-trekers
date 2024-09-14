from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def truncate_without_html(content, num_chars):
    if not content:
        return ""

    # Parse HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Extract text without HTML tags
    text = soup.get_text()

    # Truncate text to the desired number of characters
    truncated_text = text[:num_chars]

    return truncated_text
