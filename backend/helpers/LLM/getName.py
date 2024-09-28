from helpers.LLM.makeRequest import makeRequest
import json
def getName(rawName):
    sysPrompt = "From the given string extract the product name and return it in form of a JSON: {'name': 'value'}:"
    userPrompt = rawName
    models = ["gemma2-9b-it", "gemma-7b-it"]
    return json.loads(makeRequest(sysPrompt, userPrompt, models))

if __name__ == "__main__":
    print(getName("Samsung Galaxy M35 5G (Moonlight Blue,6GB RAM,128GB Storage)| Corning Gorilla Glass Victus+| AnTuTu Score 595K+ | Vapour Cooling Chamber | 6000mAh Battery | 120Hz Super AMOLED Display| Without Charger"))