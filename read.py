import json

# open the JSON file
with open("data.json", "r") as f:
    data = json.load(f)


print("Image URL:", data["image_url"])