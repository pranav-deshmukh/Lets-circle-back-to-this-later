import json

def classify(details : dict):
    """
    input: object containing the name and about
    output: category of the product
    """
    prompt = "based on the given name and details of the electronic product classify it into one of the following categories: 'smartphones', 'laptops', 'tablets', 'smartwatches', 'televisions', 'gaming consoles', 'digital cameras', 'bluetooth speakers', 'e-readers', 'smart home devices', 'refrigerators', 'washing machines', 'dishwashers', 'microwave ovens', 'air conditioners'\nreturn it form of a JSON like this: {'category': 'smartphones'}\nthe reply should be stricly json object and nothing else:\n"
    prompt += str(details)
    print(prompt)
    return name_about

if __name__ == '__main__':
    products = None
    keys = None
    with open("./products.json") as f:
        products = json.load(f)
    with open("./parameters.json") as f:
        keys = json.load(f).keys()
    name_about = {products[0]["product-name"], products[0]["about"]}
    classify(name_about)