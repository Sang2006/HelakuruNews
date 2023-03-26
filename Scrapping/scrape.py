import time as t
import requests
import json
from bs4 import BeautifulSoup

# initialize the post_id variable
post_id = 97079

while True:
    url = f"https://www.helakuru.lk/esana/news/{post_id}"
    response = requests.get(url)
    
    # if the response is 404, it means the post_id is not available yet
    if response.status_code == 404:
        print("No new post available yet")
        
    # if the response is 200, it means there is a new post available
    elif response.status_code == 200:
        print("New post available!")
        
        # do your scraping here
        soup = BeautifulSoup(response.content, "html.parser")
        
        # extract the image URL
        image_url = soup.find("meta", property="og:image")["content"]
        
        # extract the title
        title = soup.find("meta", property="og:title")["content"]
        
        # extract the description
        description = soup.find("meta", property="og:description")["content"]
        
        # extract the time
        time = soup.find("meta", itemprop="datePublished")["content"]
        
        # create a dictionary to store the values
        data = {
            "title": title,
            "description": description,
            "image_url": image_url,
            "time": time
        }
        
        # write the dictionary to a JSON file
        with open("data.json", "w") as f:
            json.dump(data, f)
            
        print("Data written to data.json")
        
        # increment the post_id for the next iteration
        post_id += 1
    
    # sleep for some time before checking again
    t.sleep(60)
    print("Looking for new posts...")
