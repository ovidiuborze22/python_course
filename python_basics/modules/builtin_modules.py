# builtin modules
# >>>import sys
# >>>sys.builtin_module_names
# import time
# dir(time)
# help(time.sleep)

import time

while True:
    with open("python_course/python_basics/file_processing/files/vegetables.txt") as file:
        print(file.read())
        time.sleep(10)

# "Time Documentation"
# https://docs.python.org/3/library/time.html