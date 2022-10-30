# closing a file
myfile = open("python_course/python_basics/file_processing/fruits.txt")
content = myfile.read()
myfile.close()
print(content)