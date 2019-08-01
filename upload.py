from instapy_cli import client

import time 
import json
import login

username = '44a6z22'
password = 'Hamza-_-'



def uploadPic(jsonFile, cli, counter = 0 ): 


    with open(jsonFile,  'r') as f:
        datastore = json.load(f)
        isUploaded = datastore["POSTS"][counter]["posted"]

    if len(datastore["POSTS"]) > counter:
        print(counter)
        # getting current time
        localTime = time.localtime()
        hour = localTime.tm_hour
        minutes = localTime.tm_min

        # getting data from the json file
        image = datastore["POSTS"][counter]["image"]
        caption = datastore["POSTS"][counter]["caption"]
        uploadTime_hour = int(
            datastore["POSTS"][counter]["time"].split(":")[0])
        uploadTime_min = int(datastore["POSTS"][counter]["time"].split(":")[1])

        if hour == uploadTime_hour and minutes == uploadTime_min and isUploaded == False:

            datastore["POSTS"][counter]["posted"] = not isUploaded
            with open(json_file_path, "w") as jsonFile:
                json.dump(datastore, jsonFile, indent=4)

            cli.upload("images/"+image, caption)
            counter = counter + 1

        elif isUploaded == True:
            counter = counter + 1
        else:
            print("not time yet")

    else:
        counter = 0
