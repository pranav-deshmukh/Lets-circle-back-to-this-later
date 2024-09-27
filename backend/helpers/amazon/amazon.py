import requests
from bs4 import BeautifulSoup
import random

url = "https://www.amazon.in/Samsung-Storage-Display-Charging-Security/dp/B0DFY3XCB6/ref=sr_1_3?dib=eyJ2IjoiMSJ9.WVleBvkHymbDiu3OEHJYg2ulH2bv9G9OInAosnUxFSQo23LpiFYru8kHxa4GiB5CnJytOwQOjxz8iBA27yYwwYIDan86aQOoKDj1-zX_dJFjKCVm2i4cjmxq8NVc3V3PeIoZFs6BqvwN9IVMLZAKI95siTRcZf8gEMbNqDo8mfzCQrQnRivJLlks-OJnd8o6lR_KoF_oXcWZrWOdLsebcGAQkdx2Kvuxt8h50C5y0gU.-vCJ92ckX-SLfCCcqr6suqgNskUHlB1udyCAF2f56og&dib_tag=se&keywords=phone&qid=1727428755&sr=8-3"
user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1'
]

# Randomly select a user-agent
user_agent = random.choice(user_agents)
def getAmazonReviews(url):
    HEADERS = ({
        'User-Agent': user_agent,
        'Accept-Language': 'en-US, en;q=0.5'
    })
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)


getAmazonReviews(url)