import os
from os.path import join
import time
import shutil 
import json
# custom libs 
import login as log 
import upload as up
import globals.variables as var


cli = log.login(var.userName, var.password)


# paths variables 
before = dict([(f, None) for f in os.listdir(var.path_to_watch)])




if __name__ == "__main__":  
	counter = 0 
	while True:
		
		# up.uploadPic(json_file_path, cli , counter)

		after = dict([(f, None) for f in os.listdir(var.path_to_watch)])
		added = [f for f in after if not f in before]
		removed = [f for f in before if not f in after]
		if added:
			print ("images\\", ",".join(added))
			image = ",".join(added)
			caption = input("your caption for this photo :")
			time = input("time :")
		
			post  =  {
			"image": image, 
			"caption" : caption,
			"time" : time,
			"posted": False
			}

			with open(var.json_file_path, "r") as f:
				data = json.load(f)
				
			data["POSTS"].append(post)

			with open(var.json_file_path, 'w') as f:
				json.dump(data, f, indent=4)
				print("Done")
		
		if removed:
			print ("Removed: ", ",".join(removed))
			with open(var.json_file_path, "r") as f:
				data = json.load(f)

			for posts in data["POSTS"]:
				if posts["image"] == ",".join(removed):
					del posts

			with open(var.json_file_path, 'w') as f:
				json.dump(data, f, indent=4)
				print("Done")

		before = after
