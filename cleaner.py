# this file is created to clean the json data file from the deleted images info 
import json 
import sys
import Classes.Cleaner as Cleaner

if __name__ == "__main__":
    
    jsonFile = "json_data/cashe.json"
    
    if len(sys.argv) > 1:
        obj = Cleaner.Cleaner(jsonFile)
        datastore = Cleaner.Cleaner("json_data/data.json")

        if sys.argv[1] == "--reset-datastore":
            obj.resetCache()
            datastore.resetData()

        if sys.argv[1] == "--reset-cache":
            obj.resetCache()
        elif sys.argv[1] == "--set-username":
            obj.setUserName(sys.argv[2])
        elif sys.argv[1] == "--set-password":
            obj.setPassword(sys.argv[2])
        elif sys.argv[1] == "--set-all": # to set the username, password and the path. 
            obj.defineIgInfo(
                sys.argv[2].split(":")[0], # username 
                sys.argv[2].split(":")[1],  # password
                sys.argv[2].split(":")[2]
                )
        elif sys.argv[1] == "--set-path":
            obj.setPath(sys.argv[2])
        elif sys.argv[1] == "--help": 
            obj.document()

        
            
        obj.verify()
    else:
        print("can't call this file like that, user --help for documentation")
