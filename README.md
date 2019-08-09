# INSTAGRAM_POSTS_AUTOMATOR
This is a Script made using the [instaPy_cli](https://github.com/instagrambot/instapy-cli) an unoficial instagram API for uploading posts/videos to feed/story.
it help  you schedule you next posts for the next 24 hours 

# Files
* app.py : the file that you would want to run to get going with the script
* upload.py : a file that contains the login of when to upload and what to upload 
* cleaner.py : responsible for executing commands sucha as 
	 * `python cleaner.py --reset-chase` 
	 * `python cleaner.py --set-username`  
* login.py : logs you in IG using the API 
* utiles.py : hold some functionalitins like verifiying if the time entered is valid ... 
 
## Set up your IG Account
* METHOD #1
	* `python app.py` it will ask for the details 

* METHOD #2
	* user the cleaner functionalities 
		* `python cleaner.py --set-username YOUR_USERNAME`
		* `python cleaner.py --set-password YOUR_PASSWORD`
		* `python cleaner.py --set-path YOUR_FOLDERS_PATH`
			*	**NOTE** : your folder should be empty as it will not consider the picture that are pre-existing in there 
				*	it monitors the folder for picture that are added to the folder after the script is runing   

## Cleaning cache and pictures data 
	

* `python cleaner.py --reset-cache`  this reset your cache.json file to it's default stat where your username and password and path to the pics folder aren't defined yet.  
* `python cleaner.py --reset-datastore` to reset the data.json file to is initial stat 

## Delete a picture 

You can delete a picure by deleting it from the folder manualy then run `python cleaner.py --delete-pics`  to remove it from the json file to avoid any confilict. 
(to be improved)