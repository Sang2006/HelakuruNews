import json

# open the JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# print the data
print("Time:", data["time"])
print("Title:", data["title"])
print("Description:", data["description"])
print("Image URL:", data["image_url"])