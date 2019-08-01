import os
from os.path import join
import time
import shutil 
import json
# custom libs 
import login as log 
import upload as up
import cleaner

if __name__ == "__main__":  
	with open("json_data/cashe.json", "r") as c:
		cache = json.load(c)

	isFirstTime = cache["isFirstTime"]
	images_path = cache["images_path"]
	json_file_path = cache["json_file_path"]
	cleaner_file = cache["cleaner_file"]

	# paths variables
	before = dict([(f, None) for f in os.listdir(images_path)])

	# set up the pics file 
	if isFirstTime == True:
		userName = input("what's your username: ")
		password = input("what's your password: ")
		images_path = input("please provide us with a path of a folder that we can monitore while looking for pics to post: \n ")

		with open("json_data/cashe.json", 'r') as c : 
			cache = json.load(c)

		cache["images_path"] = images_path
		cache["username"] = userName
		cache["password"] = password
		cache["isFirstTime"] = False


		with open("json_data/cashe.json", 'w') as c:
			json.dump(cache, c, indent=4)

	cli = log.login(cache["username"], cache["password"])
	while True:
		
		with open(cleaner_file, "r") as cleaner:
			cleaner_data = json.load(cleaner)

		for cleaner_time in cleaner_data["Cleaner-times"]:
			hours = int(cleaner_time['time'].split(':')[0])
			minutes = int(cleaner_time['time'].split(':')[1])
			seconds = int(cleaner_time['time'].split(':')[2])

			localTime = time.localtime()
			current_hour = localTime.tm_hour
			current_minutes = localTime.tm_min
			current_seconds = localTime.tm_sec

			if current_hour == hours and \
				current_minutes == minutes and \
				current_seconds == seconds:
				
				cleaner.clean(json_file_path)
				
		up.uploadPic(json_file_path, cli, images_path)
		# counter

		after = dict([(f, None) for f in os.listdir(images_path)])
		added = [f for f in after if not f in before]
		removed = [f for f in before if not f in after]
		
		if added:
			print ("images\\", ",".join(added))
			image = ",".join(added)
			caption = input("your caption for this photo :")
			time = input("time (hh:mm) :")
			tags = input("your tags for this picture : ")
		
			post  =  {
				"image": image, 
				"caption" : caption,
				"tags" : tags,
				"time" : time,
				"posted": False,
				"deleted": False
			}

			with open(json_file_path, "r") as f:
				data = json.load(f)
				
			data["POSTS"].append(post)

			with open(json_file_path, 'w') as f:
				json.dump(data, f, indent=4)
				print("Done")
		
		if removed:
			print ("Removed: ", ",".join(removed))
			with open(json_file_path, "r") as f:
				data = json.load(f)

			for posts in data["POSTS"]:
				if posts["image"] == ",".join(removed):
					posts['deleted'] = True 

			with open(json_file_path, 'w') as f:
				json.dump(data, f, indent=4)
				print("Done")

		before = after