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

def reset(jsonFile):
    with open(jsonFile, 'r') as f: 
        cache = json.load(f)

    cache["images_path"] = None
    cache['username'] = None
    cache['password'] = None
    cache['isFirstTime'] = True
    
    with open(jsonFile,"w") as target:
        json.dump(cache, target, indent=4 )
    
    return print("cache reset") 

if __name__ == "__main__":
    if sys.argv[2] == "--reset" and sys.argv[1] == "cache":
        reset("json_data/cashe.json")
