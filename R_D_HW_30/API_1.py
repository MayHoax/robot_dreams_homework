import requests
import random
import json


urls = ["https://google.com", "https://www.facebook.com/", "https://twitter.com/",
        "https://www.amazon.com/", "https://www.apple.com/"]

url = random.choice(urls)

response = requests.get(url)

print(f" Response status: {response.status_code} \n Site's domain: {response.url}"
      f" \n Response's length: {len(response.text)}")

