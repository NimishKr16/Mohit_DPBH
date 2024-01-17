import requests
from pprint import pprint

mytext = input("Enter text:")
response = requests.post(
    "https://api.sapling.ai/api/v1/aidetect",
    json={
        "key": "4KUJMMC886VPWQMQUOW2MRNEZLX0REFQ",
        "text": mytext
    }
)
response_Dict = response.json()
score = response_Dict['score']
print(f"This sentence is {round(score*100,2)}% likely to be AI generated")
print("Detailed Review:")
pprint(response.json())



