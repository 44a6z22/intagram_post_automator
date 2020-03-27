
# this file is created to clean the json data file from the deleted images info 
import json 
import sys
import Classes.Cleaner as Cleaner


if __name__ == "__main__":
   
    jsonFile = "json_data/cashe.json"
    obj = Cleaner.Cleaner(jsonFile, "init")  

    if len(sys.argv) > 1:

        if   sys.argv[1] == "--set-username":
            obj.setUserName(sys.argv[2])

        elif sys.argv[1] == "--set-password":
            obj.setPassword(sys.argv[2])
        
        elif sys.argv[1] == "--set-all": # to set the username, password and the path. 
            obj.defineIgInfo(
                sys.argv[2].split(":")[0], # username 
                sys.argv[2].split(":")[1],  # password
                # sys.argv[2].split(":")[2]
                )
        
        elif sys.argv[1] == "--set-path":
            obj.setPath(sys.argv[2])
        
        elif sys.argv[1] == "--help": 
            obj.document()
            
        obj.verify()

    else:
        obj.document()
