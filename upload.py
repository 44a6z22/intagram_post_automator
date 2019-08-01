from instapy_cli import client
import time 
import json
import login


def uploadPic(jsonFile, cli , picsPath): 
    with open(jsonFile,  'r') as f:
        datastore = json.load(f)

    for post in datastore["POSTS"]:

        isUploaded = post["posted"]
        isDeleted = post["deleted"]
        # getting current time
        localTime = time.localtime()
        current_hour = localTime.tm_hour
        current_minutes = localTime.tm_min
        # getting data from the json file
        image = post["image"]
        caption = post["caption"] + "\n\n\n\n\n\n\n" + post["tags"]

        uploadTime_hour = int(post["time"].split(":")[0])
        uploadTime_min = int(post["time"].split(":")[1])
    
        if current_hour == uploadTime_hour and current_minutes == uploadTime_min and isUploaded == False and isDeleted == False:
            print("uploading .. ")
            cli.upload(picsPath + "/" + image, caption)
            post["posted"] = not isUploaded
            with open(jsonFile, "w") as jsonFile:
                json.dump(datastore, jsonFile, indent=4)
     
