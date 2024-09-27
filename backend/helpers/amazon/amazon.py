from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

def getAmazonReviews(url):
    chrome_option = Options()
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_option
    )
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    html_content = driver.page_source
    # html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    reviews_element = soup.find_all(class_="a-row a-spacing-small review-data")
    all_reviews_list = []
    count = 0
    for review in reviews_element:
        review_object = {}
        count+=1
        review_object["id"] = f"f{count}"
        review_object["title"] = None
        description = review.text
        review_object["body"] = description
        review_object["verified"] = None
        all_reviews_list.append(review_object)
    driver.quit()
    return all_reviews_list

def getAmazonDetails(url, pages=0):
    chrome_option = Options()
    # chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.get(url)
   
    wait = WebDriverWait(driver, 10)
    technical_details = wait.until(EC.presence_of_element_located((By.ID,"feature-bullets"))).text
    product_title = wait.until(EC.presence_of_element_located((By.ID,"productTitle"))).text
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "lxml")
    reviews_element = soup.find(string=re.compile(r"See more reviews"))
    reviews_url = "https://www.amazon.in"+reviews_element.parent.get("href")
    print(reviews_url)
    product_object = {
        "product_name":product_title,
        "about":technical_details,
    }
    front_reviews = soup.find_all(class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content")
    count = 0
    page0 = []
    for review in front_reviews:
        review_object = {}
        count+=1
        review_object["id"] = f"f{count}"
        review_object["title"] = None
        description = review.contents[1].text
        review_object["body"] = description
        review_object["verified"] = None
        page0.append(review_object)

    driver.quit()
    for i in range(1, pages+1):
        page_url = f"{reviews_url}&pageNumber={i}"
        page_cur = getAmazonReviews(page_url)
        page0 += page_cur
    product_object["reviews"] = page0
    print(product_object)
    return product_object
    
if __name__ == "__main__":
    url = "https://www.amazon.in/Samsung-Moonlight-Storage-Corning-Gorilla/dp/B0D8134JH8?ref_=pd_hp_d_btf_unk_B0D8134JH8"

    """
    https://www.amazon.in/Samsung-Moonlight-Storage-Corning-Gorilla/product-reviews/B0D8134JH8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
    """
    """
    https://www.amazon.in/Samsung-Moonlight-Storage-Corning-Gorilla/product-reviews/B0D8134JH8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2
    """
    getAmazonDetails(url)