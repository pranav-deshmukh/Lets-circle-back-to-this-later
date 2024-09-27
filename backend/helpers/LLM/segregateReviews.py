from classify import classify
from makeRequest import makeRequest
import json

def segregateReviews(product: object):
    """
    input: product object
    output: list of review objects with category as key and reviews as value
    """
    category = classify(product)
    print(category)
    parameters = None
    with open("parameters.json") as f:
        try:
            parameters = json.load(f)[category]
        except:
            print("Category not found in parameters.json")
    
    sysPrompt = "Using the provided reviews, analyze the product based on the following parameters: " + str(parameters) + ". For each parameter, provide a comprehensive assessment based on majority sentiment. Do not give a short analysis, make it descriptive. If the majority of reviews are positive, lean the analysis towards a positive consensus. Similarly, if the majority are negative, lean towards a negative consensus. Only indicate a mixed opinion if there is a close balance between positive and negative reviews.\n In addition to this, return a list of general pros and cons. \n Here's a sample analysis: 'Customers have mixed opinions about the XM4 over-ear headphones in terms of value for money. Many reviewers feel that the premium features, such as excellent sound quality, effective noise cancellation, and comfort, justify the higher price point. However, some users note that there are alternative options available at a lower cost that offer comparable performance. Overall, while many consider the XM4 a worthwhile investment, others suggest weighing personal needs and budget before purchasing.' \n Return the analysis as a strict JSON object in this format: {'parameter1': 'analysis_value','parameter2': 'analysis_value','pros': ['list_of_pros'],'cons': ['list_of_cons']} \n If any parameter lacks relevant data, return 'None' for that parameter. \n The reply must be a JSON object only and nothing else."
    reviewText = {"reviews": []}
    for review in product["reviews"]:
        reviewText["reviews"].append(review["body"])
    userPrompt = str(reviewText)
    print(sysPrompt)
    print(userPrompt)
    models = ["llama3-70b-8192", "llama-3.1-70b-versatile","mixtral-8x7b-32768", "gemma-9b-it","llama-3.1-8b-instant", "llama3-8b-8192", "llama-3.2-90b-text-preview"]
    return makeRequest(sysPrompt, userPrompt, models)

if __name__ == "__main__":
    product = None
    with open("products.json") as f:
        product = json.load(f)[0]
    print(segregateReviews(product))