import json
class Cleaner():

    def __init__(self, jsonFile):
        self.jsonFile = jsonFile

    def clean(self):
        with open(self.jsonFile, "r") as f:
                data = json.load(f)

        for posts in data["POSTS"]:
            if posts["deleted"] == True:
                data["POSTS"].remove(posts)

        with open(self.jsonFile, 'w') as f:
            json.dump(data, f, indent=4)
            print("Done")

    def resetData(self):
 
        with open(self.jsonFile, "r") as f:
                data = json.load(f)

        # reset data.json file
        for posts in data["POSTS"]:
            data["POSTS"].remove(posts)      

        with open(self.jsonFile, 'w') as f:
            json.dump(data, f, indent=4)

        print("Reset datastore done")

    def resetCache(self):
        with open(self.jsonFile, 'r') as f:
            cache = json.load(f)

        cache["images_path"] = None
        cache['username'] = None
        cache['password'] = None
        cache['isFirstTime'] = True

        with open(self.jsonFile, "w") as target:
            json.dump(cache, target, indent=4)
            print('Reset cache done')

    def setUserName(self, var):
        with open(self.jsonFile, 'r') as f:
            cache = json.load(f)

        cache["username"] = var

        with open(self.jsonFile, "w") as target:
            json.dump(cache, target, indent=4)

    def setPassword(self, var):
        with open(self.jsonFile, 'r') as f:
            cache = json.load(f)

        cache["password"] = var

        with open(self.jsonFile, "w") as target:
            json.dump(cache, target, indent=4)

    def setPath(self, var):
        with open(self.jsonFile, 'r') as f:
            cache = json.load(f)

        cache["images_path"] = var

        with open(self.jsonFile, "w") as target:
            json.dump(cache, target, indent=4)

    def verify(self):
        with open(self.jsonFile, 'r') as f:
            cache = json.load(f)

        if cache["username"] != None and cache["password"] != None and cache["images_path"] != None:
                cache["isFirstTime"] = False

        with open(self.jsonFile, "w") as target:
            json.dump(cache, target, indent=4)

    def document(self):
        print('''
            --reset-chache :
                to reset your cache file (your login and password will be lost after this step)
            --reset-datastore :
                to delete all picture stored in the data.json file (need to empty the pictures folder manualy atm )
            --set-username :
                to set your ig username up
            --set-password :
                to set your ig password up
            --set-path :
                to set the path to where you gonna put the pic you wanna upload (link to your pics folder)
            --help :
                for help with the inline commands
        ''')
    
    def defineIgInfo(self, userName, password, path):
        self.setPassword(password)
        self.setUserName(userName)
        self.setPath(path)