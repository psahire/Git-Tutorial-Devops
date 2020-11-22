import requests
import random
from random import getrandbits
import time

session = requests.session()

url = 'http://khadadkhau.com/register/'
headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}


name = 'John' #enter your name
#surname = 'Doe' #enter your surname
email = 'test+{}@gmail.com'.format(getrandbits(40)) #enter your email, dont     change anything after '+'
#password = 'Testing1234' #enter your password, minimum 8 characters

times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of account(s) you would like to create: ")))
text_file = open("chmielna accounts.txt", "w")

def create_account():
    print("[" + (time.strftime("%H:%M:%S")) + "]" + " - SUBMITTING INFO.....")
    global session
    global email
    payload = {
        "Name": name,
       # "surname": surname,
        "email": email,
        #"password": password,
        #"zapoznalem": "on"
    }

def write():
    text_file.write(email + ":" + password + "\n")
    if "Success" in response.text:
        print("[" + (time.strftime("%H:%M:%S")) + "]" +" - SUCCESSFULLY CREATED     ACCOUNT "+email+":"+password)
        write()
    else:
        print("[" + (time.strftime("%H:%M:%S")) + "]" +" - ERROR COULD NOT CREATE "+email+":"+password)

for i in range (times):
    create_account()