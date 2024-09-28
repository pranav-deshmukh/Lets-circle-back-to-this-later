from flask import Flask
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from helpers.amazon.amazon import getAmazonDetails
from helpers.flipkart.flipkart import getFlipkartDetails
from helpers.LLM.getName import getName
from helpers.LLM.finalResponse import finalResponse
import time
from flask import request, jsonify

app = Flask(__name__)
CORS(app)


def scrape(url):
    amazonFlag = False
    flipkartFlag = False
    userInput = None
    if "amazon" in url:
        userInput = getAmazonDetails(url)
        amazonFlag = True
    elif "flipkart" in url:
        userInput = getFlipkartDetails(url)
        flipkartFlag = True
    name = getName(userInput["product-name"])["name"]
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.get('https://www.google.com')
    searchbox = driver.find_element(By.NAME,"q")
    searchbox.send_keys(name)
    searchbox.submit()
    time.sleep(5)
    search_results = driver.find_elements(By.XPATH, "//a")
    amazon_links = []
    flipkart_links = []
    for result in search_results:
        link = result.get_attribute("href")
        print(link)
        print(" ")
        if link and "amazon" in link:
            amazon_links.append(link)
        if link and "flipkart" in link:
            flipkart_links.append(link)
    amazonurl = amazon_links[0]
    flipkarturl = flipkart_links[0]
    driver.quit()
    amazon = userInput if amazonFlag else getAmazonDetails(amazonurl)
    flipkart = userInput if flipkartFlag else getFlipkartDetails(flipkarturl)
    new_final = {
        "product-name": name,
        "about":amazon["about"],
        "reviews":flipkart["reviews"]+amazon["reviews"]
    }
    response = finalResponse(new_final)
    return response

@app.route('/review',methods = ['POST'])
def compare(url1, url2):
    data = request.json
    if not data or 'url1' not in data or 'url2' not in data:
        return jsonify({"error": "Both URLs are required in the JSON payload"}), 400
    url1 = data['url1']
    url2 = data['url2']
    response1 = scrape(url1)
    response2 = scrape(url2)
    return jsonify([response1, response2])

          
if __name__ == '__main__':
    # print(scrape("https://www.amazon.in/Samsung-Galaxy-Smartphone-Silver-Storage/dp/B0D83YD1TF/ref=sr_1_1?nsdOptOutParam=true&sr=8-1"))
    # print(compare("https://www.amazon.in/Apple-iPhone-11-128GB-Black/dp/B07XVMJF2D", "https://www.amazon.in/Samsung-Galaxy-Smartphone-Silver-Storage/dp/B0D83YD1TF/ref=sr_1_1?nsdOptOutParam=true&sr=8-1"))

    app.run(host='0.0.0.0', port=8000)