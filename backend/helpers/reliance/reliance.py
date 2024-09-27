import requests
from bs4 import BeautifulSoup

def get_reliance_info(url):
    """
    output: object{id:string, title:string, body:string, verified:bool} 
    id->[initial name of website][review no.] eg r1, r2, r3
    """
    custom_header = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language' : 'en-US,en;q=0.9'
    }
    response = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(response.text, 'lxml')
    reviews = soup.select_one("div#reviews")
    print("status: ", response.status_code)
    all_reviews = reviews.contents[1].contents
    final_output = []
    for i in range(len(all_reviews)):
        review = all_reviews[i]
        review_body = review.contents[0].contents
        verified = None
        if "Certified" in review_body[0].text:
            verified = True
        else:
            verified = False
        output = {"id":f"r{i+1}", "title":review_body[1].text, "body":review_body[3].text, "verified":verified}
        final_output.append(output)
    return final_output
    


if __name__ == '__main__':
    print(get_reliance_info("https://www.reliancedigital.in/oppo-k12x-5g-128-gb-6-gb-ram-midnight-violet-mobile-phone/p/494422234"))
    