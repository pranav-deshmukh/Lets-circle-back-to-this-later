from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import requests


url = r"https://www.flipkart.com/fastrack-optimus-pro-1-43-amoled-display-aod-466x466-functional-crown-bt-calling-smartwatch/p/itma4744c9053b72?pid=SMWGV3ZY9YJYEYEC&lid=LSTSMWGV3ZY9YJYEYECZN6QCW&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_3&otracker=browse&fm=organic&iid=948e4ca2-56f1-4bb0-a6f1-43a0bf35715e.SMWGV3ZY9YJYEYEC.SEARCH&ppt=browse&ppn=browse&ssid=6mf64b2fk00000001727471398381"


def getFlipkartReviews(url):
    chrome_option = Options()
    chrome_option.add_argument("--headless")
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
    reviews_element = soup.find_all(string=re.compile(r"Certified Buyer"))
    all_reviews_list = []
    count = 0
    for review in reviews_element:
        review_object = {}
        count+=1
        review_object["id"] = f"f{count}"
        review_object["title"] = None
        description = None
        first_sibling = review.parent.parent.parent.parent.previous_sibling.text.rstrip("READ MORE")
        if(first_sibling == ""):
            description = review.parent.parent.parent.parent.previous_sibling.previous_sibling.text.rstrip("READ MORE")
        else:
            description = first_sibling
        review_object["body"] = description
        review_object["verified"] = None
        all_reviews_list.append(review_object)
    driver.quit()
    return all_reviews_list

def getFlipkartDetails(url, pages=2):

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
    reviews = soup.select_one("div#container")
    product_object = {}
    reviews = soup.select_one("div#container")
    title = (
        reviews.contents[0]
        .contents[2]
        .contents[0]
        .contents[1]
        .contents[1]
        .contents[0]
        .contents[0]
        .contents[0]
        .contents[0]
        .text
    )
    product_object["product-name"] = title
    about = (
        soup.find(lambda tag: tag.string == "Description")
        .find_next_sibling()
        .contents[0]
        .contents[0]
        .text
    )
    product_object["about"] = about
    # all_reviews = (
    #     reviews.contents[0]
    #     .contents[2]
    #     .contents[0]
    #     .contents[1]
    #     .contents[8]
    #     .contents[6]
    #     .contents[0]
    #     .contents[3]
    #     .contents
    # )
    # print("here")
    reviews_element = soup.find(string=re.compile(r"All \d+ reviews"))
    href = None
    if reviews_element:
            grandparent = reviews_element.parent.parent.parent
            # print(grandparent)
            href = grandparent.get('href')
    reviews_url = f"https://www.flipkart.com{href}"
    driver.quit()
    page1 = getFlipkartReviews(reviews_url)
    for i in range(2, pages+1):
        page_url = f"{reviews_url}&page={i}"
        page_cur = getFlipkartReviews(page_url)
        page1 += page_cur
    product_object["reviews"] = page1
    # product_object["reviews"] = getFlipkartReviews(reviews_url)
    
    return product_object



