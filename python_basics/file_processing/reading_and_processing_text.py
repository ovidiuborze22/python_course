# Reading and Processing Text (E)
# Read the bear.txt file, and print out the first 90 characters of its content.

file = open("python_course/python_basics/file_processing/bear.txt")
content = file.read()
file.close()

print(content[:90])