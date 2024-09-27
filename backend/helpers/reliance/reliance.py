import requests
from bs4 import BeautifulSoup

def get_reliance_info(url):
    """
    output: object{id:string, title:string, body:string, verified:bool, rating:int} 
    id->[initial name of website][review no.] eg r1, r2, r3
    """
    custom_header = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language' : 'en-US,en;q=0.9'
    }
    response = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(response.text, 'lxml')
    reviews = soup.select_one("div#reviews")
    all_reviews = reviews.contents[1].contents
    for review in all_reviews:
        review_body = review.contents[0].contents
        for thing in review_body:
            print(thing.text)
    


if __name__ == '__main__':
    get_reliance_info("https://www.reliancedigital.in/oppo-k12x-5g-128-gb-6-gb-ram-midnight-violet-mobile-phone/p/494422234")