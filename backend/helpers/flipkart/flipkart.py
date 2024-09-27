import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/lenovo-ideapad-slim-1-amd-ryzen-5-hexa-core-5500u-8-gb-512-gb-ssd-windows-11-home-15acl6-15alc7-2-thin-light-laptop/p/itmfab29c14ba777?pid=COMG9VHHF6HVJPP9&lid=LSTCOMG9VHHF6HVJPP9U213LU&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=en_p6gHKKEhlv56DRLdnNqEw8m6Ocw5SNmd9DVRWu_podZFFpduMO8nkjcKnRjAxXVBpv1nN6GR9cGi5QgFjiBdw04IsYyWu-Pj9cxFjFAoaLk%3D&ppt=None&ppn=None&ssid=koqu9mhbkw0000001727422556327&qH=312f91285e048e09"





def getFlipkartReviews(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en;q=0.9',
    }


    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    main = soup.select('div#container')
    


getFlipkartReviews(url)