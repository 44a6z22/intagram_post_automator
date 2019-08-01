# this file is created to clean the json data file from the deleted images info 
import json 
import sys
def clean(jsonFile):
    with open(jsonFile, "r") as f:
            data = json.load(f)

    for posts in data["POSTS"]:
        if posts["deleted"] == True:
            data["POSTS"].remove(posts)

    with open(jsonFile, 'w') as f:
        json.dump(data, f, indent=4)
        print("Done")



if __name__ == "__main__":
    
    jsonFile = "json_data/cashe.json"

    with open(jsonFile, 'r') as f:
        cache = json.load(f)

    if sys.argv[1] == "--reset-cache":
        cache["images_path"] = None
        cache['username'] = None
        cache['password'] = None
        cache['isFirstTime'] = True

    elif sys.argv[1] == "--set-username":
        cache["username"] = sys.argv[2] 
    elif sys.argv[1] == "--set-password":
        cache["password"] = sys.argv[2]
    elif sys.argv[1] == "--set-path":
        cache["images_path"] = sys.argv[2] 
    elif sys.argv[1] == "--help": 
        print("--")

    if cache["username"] != None and cache["password"] != None and cache["images_path"] != None : 
        cache["isFistTime"] = False 
   
    with open(jsonFile, "w") as target:
        json.dump(cache, target, indent=4)
        print('Done')
        
