from flask import Flask
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
app = Flask(__name__)
CORS(app)


# app.route('/info',method = ['get'])
def scrape():
    chrome_option = Options()
    # chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.get('https://www.google.com')
    searchbox = driver.find_element(By.NAME,"q")
    searchbox.send_keys("iphone 15")
    searchbox.submit()
    time.sleep(5)
    search_results = driver.find_elements(By.XPATH, "//a")


    amazon_links = []
    flipkart_links = []

   
    for result in search_results:
        link = result.get_attribute("href")
        if link and "amazon" in link:
            amazon_links.append(link)
        if link and "flipkart" in link:
            flipkart_links.append(link)

    
    amazonurl = amazon_links[0]
    flipkarturl = flipkart_links[0]
    
    driver.quit()
        

    
scrape()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)