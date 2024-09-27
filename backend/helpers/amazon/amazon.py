import requests
from bs4 import BeautifulSoup

def get_amazon_info(url):
    """Output: HTML content of the Amazon product reviews page."""
    custom_header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        "origin": "https://www.amazon.in",
        "referer": "https://www.amazon.in/"
    }
    
    response = requests.get(url, headers=custom_header)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
    # Print the entire HTML content
    html_content = response.text
    soup = BeautifulSoup(response.text, 'lxml')
    print(html_content)
    
    return html_content

if __name__ == '__main__':
    amazon_url = "https://www.amazon.com/product-reviews/B0BP3ZK9K9"
    html = get_amazon_info(amazon_url)


"""
https://www.amazon.in/IFB-DIVA-AQUA-GBS-6010/dp/B0CB1FS1WR/?_encoding=UTF8&ref_=pd_hp_d_atf_dealz_m2
"""