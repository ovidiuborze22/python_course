# standard python modules

# >>> import sys
# >>>sys.builtin_module_names
# >>>sys.prefix
# 'C:\\Users\\ovidi\\AppData\\Local\\Programs\\Python\\Python310'
# >>>import os
# >>>dir(os)
# >>> os.path.exists("python_course/python_basics/file_processing/files/vegetables.txt") 
# True
import time
import os

while True:
    if os.path.exists("python_course/python_basics/file_processing/files/vegetables.txt"):
        with open("python_course/python_basics/file_processing/files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)      

# "Time Documentation"
# https://docs.python.org/3/library/time.html

# Os Documentation
# https://docs.python.org/3/library/os.html