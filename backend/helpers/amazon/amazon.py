from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC




def getAmazonDetails(url):


    chrome_option = Options()
    chrome_option.add_argument("--headless")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

    driver.get(url)
    print(driver.title)
    wait = WebDriverWait(driver, 10)
    technical_details = wait.until(EC.presence_of_element_located((By.ID,"productDetails_feature_div"))).text
    customer_reviews = wait.until(EC.presence_of_element_located((By.ID,"customerReviews"))).text
    product_title = wait.until(EC.presence_of_element_located((By.ID,"productTitle"))).text
    final = {
        "product_title":product_title,
        "customer_reviews":customer_reviews,
        "technical_details":technical_details
    }
    driver.quit()
    return final
    