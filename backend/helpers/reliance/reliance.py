from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC




def getRelianceDetails(url):


    chrome_option = Options()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    

    driver.get(url)
    print(driver.title)
    wait = WebDriverWait(driver, 10)
    driver.quit()
    

getAmazonDetails(url)