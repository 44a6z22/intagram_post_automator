# this file is created to clean the json data file from the deleted images info 
import json 

def clean(jsonFile):
    with open(jsonFile, "r") as f:
            data = json.load(f)

    for posts in data["POSTS"]:
        if posts["deleted"] == True:
            data["POSTS"].remove(posts)

    with open(jsonFile, 'w') as f:
        json.dump(data, f, indent=4)
        print("Done")

def reset(jsonFile):
    return False 

