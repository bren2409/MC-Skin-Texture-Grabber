import requests
import base64
import json
import urllib.request
import os


# Get Username
name = input("user: ")

# Get User ID
r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}')

# Specifying ID & Name

ID = r.json()["id"]
name1 = r.json()["name"]

# Getting Base64 Value

r2 = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{ID}')
value = r2.json()["properties"][0]["value"]

# Decoding It

decoded_string = base64.b64decode(value)
json_object = json.loads(decoded_string)

#---------------------------------------------
# Downloading Skin And Data                  
#---------------------------------------------

# Creating Folder

folder_name = name1

dir = f'Downloaded/{name1}'
if not os.path.exists(dir):
    os.makedirs(f"Downloaded/{name1}")

# Sample Json Data

dictionary = {
    "name": name1,
    "id": ID,
    "skin": json_object["textures"]["SKIN"]["url"]
}
json_data = json.dumps(dictionary, indent=4)

# Creating The Json File 
print("Downloading JSON")
with open(f"Downloaded/{name1}/{name1}'s Data.json", "w") as outfile:
    outfile.write(json_data)



# Downloading Skin File To Folder
print("Downloading Skin Texture")
urllib.request.urlretrieve(json_object["textures"]["SKIN"]["url"], f"./Downloaded/{name1}/{name1}.jpg")

print(f"Downloaded {name1}'s MC Skin Texture\n\n{name1}.jpg")
