import requests
from bs4 import BeautifulSoup

def get_amazon_info(url):
    """Output: HTML content of the Amazon product reviews page."""
    custom_header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    response = requests.get(url, headers=custom_header)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
    # Print the entire HTML content
    html_content = response.text
    print(html_content)
    
    return html_content

if __name__ == '__main__':
    amazon_url = "https://www.amazon.com/product-reviews/B0BP3ZK9K9"
    html = get_amazon_info(amazon_url)
