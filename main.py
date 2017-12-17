import requests
import json




result = requests.get('https://api.github.com/repos/sibbay-ai/public')

res = result.json()

with open("./res.json", "a") as f:
    f.write(json.dumps(res))
