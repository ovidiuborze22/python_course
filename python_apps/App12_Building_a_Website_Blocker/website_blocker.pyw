# App12 Building a Website Blocker
import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list =["www.facebook.com", "facebook.com", "www.yahoo.com", "yahoo.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp,'r+') as file: # change host_temp with host_path
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file: # change host_temp with hosts_path
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()        
        print("Fun hours...")
    time.sleep(5)