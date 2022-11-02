# third-party modules

import time
import os
import pandas

while True:
    if os.path.exists("python_course/python_basics/modules/temps_today.csv"):
        data = pandas.read_csv("python_course/python_basics/modules/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10) 

# Pandas Documentation 
# https://pandas.pydata.org/docs/
