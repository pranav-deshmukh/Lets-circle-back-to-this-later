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
from helpers.LLM.makeRequest import makeRequest
import time
from flask import request, jsonify,json
import logging

app = Flask(__name__)
CORS(app)

# def scrape2():
#     system = " Using the provided reviews, analyze the product based on the following parameters: ['Performance', 'Camera Quality', 'Battery Life', 'Display', 'Build Quality', 'Value for Money', 'Durability']. For each parameter, provide a comprehensive assessment based on majority sentiment. Do not give a short analysis, make it descriptive. If the majority of reviews are positive, lean the analysis towards a positive consensus. Similarly, if the majority are negative, lean towards a negative consensus. Only indicate a mixed opinion if there is a close balance between positive and negative reviews.  In addition to this, return a list of general pros and cons.  Here's a sample analysis: 'Customers have mixed opinions about the XM4 over-ear headphones in terms of value for money. Many reviewers feel that the premium features, such as excellent sound quality, effective noise cancellation, and comfort, justify the higher price point. However, some users note that there are alternative options available at a lower cost that offer comparable performance. Overall, while many consider the XM4 a worthwhile investment, others suggest weighing personal needs and budget before purchasing.'  Return the analysis as a strict JSON object in this format: {'parameter1': 'analysis_value' 'parameter2': 'analysis_value','pros': ['list_of_pros'],'cons': ['list_of_cons']}  If any parameter lacks relevant data, return 'None' for that parameter.  The reply must be a JSON object only and nothing else."
#     user = "{'reviews': ['It is something you can take a chance... Don't expect something special it's just a mid ranger phone with all good specs.', 'It's a one day delivery and it's just more than 6 hours now. I'll give uh a small review about....1 - camera - 4/5 bcz each and everything is good but it's processing for sometime ( at this range camera quality is awesome better than Motorola edge 40 I can say) 2- battery - No doubt it's amazing because I just used it for 3 hrs continuously like all the settings and camera and also BGMI and COD. No hitting it's just reduced to 15% to 20% within 3 hrs of continuous usage.3- Display - dam...', 'Not bad', 'Nothing phone 2a look very good, camera good, battery backup excellent, nothing software very useful and very fast.', 'Nice phone.. You can purchase easily to touCamera is perfect and model also good', 'Allrounder', 'Excellent product. The phone is very smooth. Camera quality is good but the ultra wide could have been better. Battery life is good. Overall the nothing OS is very smooth.', 'Pros-Display(4.5/5) good brightness.Speaker (4/5) very good quality.Software(4.5/5) very light and easy usage.Camera (4/5)--above average.video stability amazing.can take very good selfie.Battery(4.2/5)-- very good battery..I don't know about the actual charging time..maybe around 1:30mintPerformance(3.5/5)--- taking time to open and loading app...120hz implementation is not good.haptic is very good.Cons-Very bad build quality (2.5/5)Charger not included.Not great usage of glyphF...', 'Camera - 4.1/5⭐Video - 4.8/5 ⭐ Display -5/5 ⭐ Battery - 4.5/5 ⭐ Price - Value for money 4.8/5 ⭐ Performance - 4/5 ⭐ OS - 5/5 ⭐', 'Design 💯Camara 💯Display 💯Battery 💯', 'Camera - 4.1/5⭐Video - 4.8/5 ⭐ Display -5/5 ⭐ Battery - 4.5/5 ⭐ Price - Value for money 4.8/5 ⭐ Performance - 4/5 ⭐ OS - 5/5 ⭐', 'Wonderful product', 'Design 💯Camara 💯Display 💯Battery 💯', 'It's just amazing in this price. It's Blue with 8 and 256 GB. Only disappointed thing is that there is no charger with phone. Only C2C cable.', 'Have been using this product for the past two weeks. Looks stylish and comfortable with day long usage. Given below the pros and cons;1. Battery - Really good. Moderate usage typically lasts for two days. Battery does drain too much. Except gaming, I have been doing everything else.2. Display - Very responsive. Finger print sensor works well. 3. Camera - not that great. NOTHING should work on improving the camera performance through its UI. Definitely needed. There are issues in low light ...', 'I am an iPhone user .. and I keep one Android phone with me always . If you are looking for a all rounder phone .. just grab it ..you will the phone .Camera is not a flagship one but produce quite good image .Processor is good enough to handle heavy task.I will recommend if have little more budget just buy 256gb varient.Ignore those negative comments.Definitely you will have a premium experience. I will update few more things after a month with some more photography of this phone.My e...', 'Nothing's best budget phone 5/5⭐⭐⭐⭐⭐', 'I love the design and it looks premium.I have been using this since 15 days now and I'm quite happy with the purchase.You can go for it!', 'Pros : 1. Smooth and Fluid Software Experience.2. Unique design.3. Ultra wide camera is very good for this range.Cons : 1. Charger not in the box,2. Main camera should be better.', 'Camera super phone nice', 'If you're in the market for a phone that excels in both performance and photography, this model is a compelling choice. As an ACE Dominator-Masters player, I can confidently say that this phone offers a stable gaming experience with minimal lag. It handles heavy gaming well, with only occasional lag when the server conditions are poor. The touch response is impressive, making it a solid option for competitive play.The camera quality is surprisingly good, capturing clear and vibrant photos, which is perfect for heavy camera usage. Social media enthusiasts will also appreciate its performance in this area.However, there are a few drawbacks. The phone tends to get quite warm, especially when using the 120Hz refresh rate and full brightness. While this is manageable and doesn't affect the overall experience too much, it’s something to be aware of. Additionally, the UI stability seems to have taken a hit after the recent update, making the phone feel less enjoyable to use compared to before.Overall, this phone is a strong contender for those who need a device that performs well in gaming, photography, and social media, despite a few minor drawbacks.', 'I have been using this phone since last 1 month and everything this is working fine on an average use of 4-5 hours a day.Battery backup is also good and I usually charge the phone once in 2 days.Camera quality is also good as compared to the price and phone is also fast.Phone Design is fabulous 🤩 and it gives you an altogether different feel.Phone weight is equally distributed so doesn't feel heavy while using.', 'This phone is for you if you are looking for a sturdy, smart and practical phone with a neat user experience. The phone surely feels premium in hand and looks distinct from other devices.UI is amazing. No bloatware, clean design and lot of emphasis on practicality and user friendliness.Another department where phone scores very high is it's battery. It easily last for 2 days if you are an average user.The only area where phone underperforms is the camera. Despite good specs , the image quality is snot consistent. Colours are often saturated (even after the latest update) and the edge detection in potrait mode is still a struggle. Hopefully Nothing team will roll out more updates to improve and stablize the camera of the phone.Overall, a great product at this price point.', 'this is a good phone, decent processor, extremely good os, decent cameras and if you want to game it doesn't run that hot. However I would appreciated a charger and a bit better specs for this phone. Also would have wished it came with ufs 3.0 but not really a deal breaker for me. Dont use the preapplied screen protector , it is fragile so just get a new one. Tldr: good phone for everyday casual use, get it if you want a good os system, clean phone and fast charging with the nothing gimmicky glyph lighting, go for it Can say it's worth, unless if you only want gaming phone then go for poco x6 pro, sacrificing basically everything expect the processor.', 'Dear Amazon Customer Service,I am writing to express my extreme disappointment with the service I have received regarding my recent purchase of the Nothing 2A phone. Despite assurances from your mobile inspection team that my concerns would be addressed promptly, I have encountered nothing but frustration and unfulfilled promises.I purchased the Nothing 2A phone expecting a certain standard of quality, particularly in its camera capabilities. Upon realizing the camera did not meet my expectations, I promptly initiated a return request. Despite the initial confirmation from your team, there has been an alarming lack of follow-through on Amazon's part.For over 6-7 days, I patiently waited for a call to arrange the return pick-up, only to receive none. Your application, which I attempted to use for customer service, failed to connect me, highlighting serious deficiencies in its functionality. It took a staggering 10 days of persistent effort via your website before I was finally able to speak with someone.To my disbelief, the response I received was that Amazon could no longer assist with a return or replacement. This level of incompetence and indifference is simply unacceptable from a company of Amazon's stature.My experience with Amazon's handling of this matter has been nothing short of a nightmare. I have been left with a defective product and no recourse for resolution. As a loyal customer who has relied on Amazon for years, this experience has shattered my trust and left me questioning whether I can continue to support your platform.I urge Amazon to seriously reconsider its policies and procedures for handling customer complaints and returns. There needs to be accountability for the promises made to customers and a genuine effort to rectify situations when they fail to meet expectations.In conclusion, I demand a full refund for the Nothing 2A phone and a formal apology for the way this matter has been mishandled. If Amazon hopes to retain my trust and loyalty as a customer, swift action is needed to address these concerns.Sincerely,Sowmya', 'Nothing phone 2a- \u2060- Design: Sleek, transparent; showcases internal components.- **Build Quality: Sturdy and premium feel.- **Display: Bright, vibrant; excellent for media consumption.- **Performance: Smooth and responsive; handles multitasking well.- **Battery Life: Long-lasting; supports fast charging.- **Software: Clean, minimalistic UI; close to stock Android.- **Camera: Decent performance; good in well-lit conditions.- **Unique Features: LED glyph interface; customizable notifications.- **Overall: Distinctive design, solid performance; stands out in a crowded market.', 'Battery life is not good at all . Looks are good. Camera is average . Ease of use is good', 'Will recommend,  nice camera, handling and overall value for money.', 'Initially I was skeptical about buying this phone since it's not a main stream brand. I have had the phone for almost a week and I am very impressed as how fast it is, the style is unique, and a good size all around phone. My gf is now switching from her Samsung S24Plus phone to a Nothing 2a phone.Great product, great purchase 👍👍👍😁', 'Quality vs price balance', 'WHEN ANDROID MEETS IOS ... THIS IS THE PHONE', '', 'Tengo casi 1 mes de usarlo, y, tengo que decir que es absolutamente brillante, es muy rápido, tiene un sistema y UI muy bueno, muchas funciones extras buenas y es perfecto para jugar algunos videojuegos, el único problema es que no viene con el cargador (cuadro) para cargarlo, solamente viene el cable, por lo que vas a tener que comprarlo por separado.Fuera de eso, muy buen celular, vale la pena completamente']}"
#     models = [
#         "llama-3.1-70b-versatile",
#         "llama3-70b-8192",
#         "mixtral-8x7b-32768",
#         "gemma-9b-it",
#         "llama-3.1-8b-instant",
#         "llama3-8b-8192",
#         "llama-3.2-90b-text-preview",
#     ]
#     response = makeRequest(system, user, models)
#     return response

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
        # print(link)
        # print(" ")
        if link and "amazon" in link:
            amazon_links.append(link)
        if link and "flipkart" in link:
            flipkart_links.append(link)
    amazonurl = None
    flipkarturl = None
    if(len(amazon_links)>0):
        amazonurl = amazon_links[0]
    if(len(flipkart_links)>0):
        flipkarturl = flipkart_links[0]
    driver.quit()
    print("here1")
    try:
        amazon = userInput if amazonFlag else getAmazonDetails(amazonurl)
    except:
        amazon = {"reviews": []}
    try:
        flipkart = userInput if flipkartFlag else getFlipkartDetails(flipkarturl)
    except:
        flipkart = {"reviews": []}
    print("here2")
    temp_reviews = []
    print(amazon)
    print(flipkart)
    if(flipkart.get("reviews") is not None):
        temp_reviews += flipkart["reviews"]
    if(amazon.get("reviews") is not None):
        temp_reviews += amazon["reviews"]
    new_final = {
        "product-name": name,
        "about":amazon["about"] if amazon.get("about") is not None else [],
        "reviews":flipkart["reviews"]+amazon["reviews"]
    }
    print("here3")
    response = finalResponse(new_final)
    return response

@app.route("/testing", methods = ['POST'])
def jsonme():
    thing = [{1:"hello"},{2:"hello"}]
    return json.dumps(thing)

@app.route('/review',methods = ['POST'])
def review():
    data = request.json
    if not data or 'url1' not in data:
        return json.dumps({"error": "URL is required in the JSON payload"}), 400
    url1 = data['url1']
    response1 = scrape(url1)
    return json.dumps(response1)
    
@app.route('/compare',methods = ['POST'])
def compare():
    data = request.json
    if not data or 'url1' not in data or 'url2' not in data:
        return json.dumps({"error": "Both URLs are required in the JSON payload"}), 400
    url1 = data['url1']
    url2 = data['url2']
    response1 = scrape(url1)
    print(response1)
    print("here101")
    response2 = scrape(url2)
    print(response2)
    print("here202")
    return json.dumps([response1, response2])

          
if __name__ == '__main__':
    # logging.info("Starting the application...")
    # print(scrape2())
    # print(scrape("https://www.amazon.in/Nothing-Phone-Black-256GB-Storage/dp/B0CX74JKLL/ref=sr_1_3?sr=8-3"))
    # print(compare("https://www.amazon.in/Apple-iPhone-11-128GB-Black/dp/B07XVMJF2D", "https://www.amazon.in/Samsung-Galaxy-Smartphone-Silver-Storage/dp/B0D83YD1TF/ref=sr_1_1?nsdOptOutParam=true&sr=8-1"))

    app.run(host='0.0.0.0', port=8000)