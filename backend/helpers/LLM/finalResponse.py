from helpers.LLM.classify import classify
from helpers.LLM.makeRequest import makeRequest
import json


def finalResponse(product: object):
    """
    input: product object
    output: list of review objects with category as key and reviews as value
    """
    category = classify(product)
    # category = "washing machine"
    print(category)
    parametersAll = {
        "smartphone": [
            "Performance",
            "Camera Quality",
            "Battery Life",
            "Display",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "laptop": [
            "Performance",
            "Battery Life",
            "Display Quality",
            "Build Quality",
            "Keyboard and Touchpad",
            "Value for Money",
            "Durability",
        ],
        "tablet": [
            "Display Quality",
            "Performance",
            "Battery Life",
            "Portability",
            "Stylus Support",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "smartwatche": [
            "Fitness Tracking",
            "Battery Life",
            "Display",
            "Compatibility",
            "Build Quality",
            "Health Monitoring Features",
            "Customization Options",
            "Value for Money",
            "Durability",
        ],
        "television": [
            "Picture Quality",
            "Screen Size",
            "Smart Features",
            "Sound Quality",
            "Refresh Rate",
            "Connectivity Options",
            "Energy Efficiency",
            "Value for Money",
            "Durability",
        ],
        "gaming console": [
            "Performance",
            "Game Library",
            "Online Services",
            "Backwards Compatibility",
            "Storage",
            "Controller Quality",
            "Multimedia Features",
            "Exclusive Titles",
            "Value for Money",
            "Durability",
        ],
        "digital camera": [
            "Image Quality",
            "Sensor Size",
            "Lens Options",
            "Autofocus Performance",
            "Low-light Capability",
            "Video Features",
            "Ergonomics",
            "Battery Life",
            "Value for Money",
            "Durability",
        ],
        "bluetooth speaker": [
            "Sound Quality",
            "Battery Life",
            "Portability",
            "Water Resistance",
            "Connectivity Range",
            "Build Quality",
            "Multi-speaker Pairing",
            "Voice Assistant Integration",
            "Value for Money",
            "Durability",
        ],
        "e-reader": [
            "Display Quality",
            "Battery Life",
            "Storage Capacity",
            "Lighting",
            "Ergonomics",
            "File Format Support",
            "Waterproofing",
            "Ecosystem Integration",
            "Value for Money",
            "Durability",
        ],
        "smart home device": [
            "Compatibility",
            "Ease of Setup",
            "Voice Assistant Integration",
            "Security Features",
            "Energy Efficiency",
            "Reliability",
            "App Quality",
            "Privacy Protections",
            "Value for Money",
            "Durability",
        ],
        "refrigerator": [
            "Capacity",
            "Energy Efficiency",
            "Temperature Control",
            "Storage Organization",
            "Noise Level",
            "Smart Features",
            "Build Quality",
            "Water/Ice Dispenser",
            "Value for Money",
            "Durability",
        ],
        "washing machine": [
            "Capacity",
            "Energy Efficiency",
            "Washing Performance",
            "Spin Speed",
            "Noise Level",
            "Cycle Options",
            "Water Consumption",
            "Smart Features",
            "Value for Money",
            "Durability",
        ],
        "dishwasher": [
            "Cleaning Performance",
            "Capacity",
            "Energy Efficiency",
            "Noise Level",
            "Cycle Options",
            "Drying Performance",
            "Water Consumption",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "microwave oven": [
            "Cooking Power",
            "Capacity",
            "Cooking Functions",
            "Size and Footprint",
            "Ease of Use",
            "Noise Level",
            "Build Quality",
            "Safety Features",
            "Value for Money",
            "Durability",
        ],
        "air conditioner": [
            "Cooling Capacity",
            "Energy Efficiency",
            "Noise Level",
            "Air Purification",
            "Smart Features",
            "Installation Requirements",
            "Humidity Control",
            "Maintenance Ease",
            "Value for Money",
            "Durability",
        ],
    }
    parameters = parametersAll[category]
    sysPrompt = (
        "Using the provided reviews, analyze the product based on the following parameters: "
        + str(parameters)
        + ". For each parameter, provide a comprehensive assessment based on majority sentiment. Do not give a short analysis, make it descriptive. If the majority of reviews are positive, lean the analysis towards a positive consensus. Similarly, if the majority are negative, lean towards a negative consensus. Only indicate a mixed opinion if there is a close balance between positive and negative reviews.\n In addition to this, return a list of general pros and cons. \n Here's a sample analysis: 'Customers have mixed opinions about the XM4 over-ear headphones in terms of value for money. Many reviewers feel that the premium features, such as excellent sound quality, effective noise cancellation, and comfort, justify the higher price point. However, some users note that there are alternative options available at a lower cost that offer comparable performance. Overall, while many consider the XM4 a worthwhile investment, others suggest weighing personal needs and budget before purchasing.' \n Return the analysis as a strict JSON object in this format: {'parameter1': 'analysis_value','parameter2': 'analysis_value','pros': ['list_of_pros'],'cons': ['list_of_cons']} \n If any parameter lacks relevant data, return 'None' for that parameter. \n The reply must be a JSON object only and nothing else."
    )
    reviewText = {"reviews": []}
    for review in product["reviews"]:
        reviewText["reviews"].append(review["body"])
    userPrompt = str(reviewText)
    print(sysPrompt)
    print(userPrompt)
    models = [
        "llama3-70b-8192",
        "llama-3.1-70b-versatile",
        "mixtral-8x7b-32768",
        "gemma-9b-it",
        "llama-3.1-8b-instant",
        "llama3-8b-8192",
        "llama-3.2-90b-text-preview",
    ]
    # print(sysPrompt)
    # print(userPrompt)
    # return None
    return makeRequest(sysPrompt, userPrompt, models)


if __name__ == "__main__":
    product = {
        "smartphone": [
            "Performance",
            "Camera Quality",
            "Battery Life",
            "Display",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "laptop": [
            "Performance",
            "Battery Life",
            "Display Quality",
            "Build Quality",
            "Keyboard and Touchpad",
            "Value for Money",
            "Durability",
        ],
        "tablet": [
            "Display Quality",
            "Performance",
            "Battery Life",
            "Portability",
            "Stylus Support",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "smartwatche": [
            "Fitness Tracking",
            "Battery Life",
            "Display",
            "Compatibility",
            "Build Quality",
            "Health Monitoring Features",
            "Customization Options",
            "Value for Money",
            "Durability",
        ],
        "television": [
            "Picture Quality",
            "Screen Size",
            "Smart Features",
            "Sound Quality",
            "Refresh Rate",
            "Connectivity Options",
            "Energy Efficiency",
            "Value for Money",
            "Durability",
        ],
        "gaming console": [
            "Performance",
            "Game Library",
            "Online Services",
            "Backwards Compatibility",
            "Storage",
            "Controller Quality",
            "Multimedia Features",
            "Exclusive Titles",
            "Value for Money",
            "Durability",
        ],
        "digital camera": [
            "Image Quality",
            "Sensor Size",
            "Lens Options",
            "Autofocus Performance",
            "Low-light Capability",
            "Video Features",
            "Ergonomics",
            "Battery Life",
            "Value for Money",
            "Durability",
        ],
        "bluetooth speaker": [
            "Sound Quality",
            "Battery Life",
            "Portability",
            "Water Resistance",
            "Connectivity Range",
            "Build Quality",
            "Multi-speaker Pairing",
            "Voice Assistant Integration",
            "Value for Money",
            "Durability",
        ],
        "e-reader": [
            "Display Quality",
            "Battery Life",
            "Storage Capacity",
            "Lighting",
            "Ergonomics",
            "File Format Support",
            "Waterproofing",
            "Ecosystem Integration",
            "Value for Money",
            "Durability",
        ],
        "smart home device": [
            "Compatibility",
            "Ease of Setup",
            "Voice Assistant Integration",
            "Security Features",
            "Energy Efficiency",
            "Reliability",
            "App Quality",
            "Privacy Protections",
            "Value for Money",
            "Durability",
        ],
        "refrigerator": [
            "Capacity",
            "Energy Efficiency",
            "Temperature Control",
            "Storage Organization",
            "Noise Level",
            "Smart Features",
            "Build Quality",
            "Water/Ice Dispenser",
            "Value for Money",
            "Durability",
        ],
        "washing machine": [
            "Capacity",
            "Energy Efficiency",
            "Washing Performance",
            "Spin Speed",
            "Noise Level",
            "Cycle Options",
            "Water Consumption",
            "Smart Features",
            "Value for Money",
            "Durability",
        ],
        "dishwasher": [
            "Cleaning Performance",
            "Capacity",
            "Energy Efficiency",
            "Noise Level",
            "Cycle Options",
            "Drying Performance",
            "Water Consumption",
            "Build Quality",
            "Value for Money",
            "Durability",
        ],
        "microwave oven": [
            "Cooking Power",
            "Capacity",
            "Cooking Functions",
            "Size and Footprint",
            "Ease of Use",
            "Noise Level",
            "Build Quality",
            "Safety Features",
            "Value for Money",
            "Durability",
        ],
        "air conditioner": [
            "Cooling Capacity",
            "Energy Efficiency",
            "Noise Level",
            "Air Purification",
            "Smart Features",
            "Installation Requirements",
            "Humidity Control",
            "Maintenance Ease",
            "Value for Money",
            "Durability",
        ],
    }
    print(finalResponse(product))