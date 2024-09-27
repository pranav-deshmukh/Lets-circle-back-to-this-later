import requests
from bs4 import BeautifulSoup

def get_reliance_info(url):
    custom_header = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language' : 'en-US,en;q=0.9'
    }
    response = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(response.text, 'lxml')
    reviews = soup.select_one("#reviews")
    print(reviews)


if __name__ == '__main__':
    get_reliance_info("https://www.reliancedigital.in/oppo-k12x-5g-128-gb-6-gb-ram-midnight-violet-mobile-phone/p/494422234")