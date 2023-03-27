import time as t
import requests
import json
import subprocess
from bs4 import BeautifulSoup

# getting the latest post
with open("data.json", "r") as f:
    data = json.load(f)

post_id = data["latest_post"]

while True:
    url = f"https://www.helakuru.lk/esana/news/{post_id}"
    response = requests.get(url)
    
    data = {"latest_post" : post_id}
        
    with open("data.json", "w") as f:
            json.dump(data, f)
    
    if response.status_code == 404:
        print("No new post available yet")
        
    elif response.status_code == 200:
        print("New post available!")
        

        soup = BeautifulSoup(response.content, "html.parser")
        image_url = soup.find("meta", property="og:image")["content"]
        title = soup.find("meta", property="og:title")["content"]
        description = soup.find("meta", property="og:description")["content"]
        time = soup.find("meta", itemprop="datePublished")["content"]
        latest_id = post_id
        
        data = {
            "title": title,
            "description": description,
            "image_url": image_url,
            "time": time
        }
        
        
        with open("data.json", "w") as f:
            json.dump(data, f)
            
        print("Data written to data.json")
        
        subprocess.run(["python", "posting.py"])
        
        post_id += 1
    
    t.sleep(60)
    print("Looking for new posts...")
