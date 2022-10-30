# opening files using "with"

with open("python_course/python_basics/file_processing/fruits.txt") as myfile:
    content = myfile.read()

print(content)