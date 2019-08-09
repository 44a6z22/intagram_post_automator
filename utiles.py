def time_checker(string):
    time = [0,0]
    time[0] = int(string.split(":")[0])
    time[1] = int(string.split(":")[1])
    # print(time[1])
    for t in  time: 
        if time[1] >= 60:
            time[1] = time[1] % 60
            time[0] = time[0] + 1
        elif time[0] >= 24:
            time[0] = time[0] % 24
    
    return str(time[0]) + ":" + str(time[1])

