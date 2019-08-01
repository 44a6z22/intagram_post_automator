from instapy_cli import client


def  login(userName, password): 
    with client(userName, password) as cli : 
        return cli 
