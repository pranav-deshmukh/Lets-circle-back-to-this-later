import json
import os 
from makeRequest import makeRequest

def classify(product: dict):
    """
    input: object containing the name and about
    output: category of the product
    """
    details = {"product-name": product["product-name"], "about": product["about"]}
    SysPrompt = "based on the given name and details of the electronic product classify it into one of the following categories: 'smartphone', 'laptop', 'tablet', 'smartwatch', 'television', 'gaming console', 'digital camera', 'bluetooth speaker', 'e-reader', 'smart home device', 'refrigerator', 'washing machine', 'dishwasher', 'microwave oven', 'air conditioner'\nreturn it form of a JSON like this: {'category': 'smartphones'}\nthe reply should be stricly json object and nothing else:\n"
    userMsg = str(details)
    models = ["gemma2-9b-it","gemma-7b-it"]
    category = json.loads(makeRequest(SysPrompt, userMsg, models))
    try:
        return category["category"]
    except:
        return None

if __name__ == '__main__':
    products = None
    keys = None
    with open("./products.json") as f:
        products = json.load(f)
    with open("./parameters.json") as f:
        keys = json.load(f).keys()
    # name_about = {products[0]["product-name"], products[0]["about"]}
    print(classify(products[0]))