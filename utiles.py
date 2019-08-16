def time_checker(string):
    time = [0,0]
    time[0] = int(string.split(":")[0])
    time[1] = int(string.split(":")[1])
    
    for t in  time: 
        if time[1] >= 60:
            time[1] = time[1] % 60
            time[0] = time[0] + 1
        
        elif time[0] >= 24:
            time[0] = time[0] % 24
    
    return str(time[0]) + ":" + str(time[1])




def post_type_picker():

    typeString = ""
    
    print("pick what type of post this file will be : \n 1) feed picture ? \n 2) feed video ? \n 3) Story ?  ")
    number = int(input())
    
    if number == 1: 
        typeString = "picture"
    elif number == 2 :
        typeString  = "video"
    elif number == 3 : 
        typeString = "story"

    return typeString 
