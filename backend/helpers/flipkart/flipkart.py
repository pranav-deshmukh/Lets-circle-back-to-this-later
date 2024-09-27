from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



url = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&q=phone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=55e9453a-621c-4e38-bde9-7fdf161f4433.MOBGTAGPAQNVFZZY.SEARCH&ppt=None&ppn=None&ssid=kpmwhv948w0000001727446085278&qH=f7a42fe7211f98ac"


def getFlipkartDetails(url):
    
    chrome_option = Options()
    # chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    

    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    # container = wait.until(EC.presence_of_element_located((By.ID,"container"))).text
    # print(container)
    

    html_content = driver.page_source
    soup = BeautifulSoup(html_content,'lxml')
    reviews = soup.select_one("div#container")
    # all_reviews_button = reviews.contents[0].contents[2].contents[0].contents[1].contents[8].contents[6].contents[0].contents[5]
    # all_reviews_url = all_reviews_button['href']
    
   

   
    
    

    
    reviews = soup.select_one("div#container")
    
    all_reviews = reviews.contents[0].contents[2].contents[0].contents[1].contents[8].contents[6].contents[0].contents[3].contents
    product_title = driver.title
    product_description =  reviews.contents[0].contents[2].contents[0].contents[1].contents[8].contents[3].contents[1:]

    
    # for review in all_reviews:
    #     review_body = review.contents[0].contents
    #     for thing in review_body:
    #         print(thing.text)
            

   
            
    
    
    
    

    
   
    driver.quit()
   
    
getFlipkartDetails(url)


