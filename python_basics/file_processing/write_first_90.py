# Write First 90 (E)
# Create a first.txt file that contains the first 90 characters of bear.txt.

# Note that you should read the content of bear.txt with Python, 
# extract its first 90 characters with Python, and write those characters in first.txt with Python.

with open("python_course/python_basics/file_processing/bear.txt") as file:
    content = file.read()

with open("python_course/python_basics/file_processing/files/first.txt", "w") as file:
    file.write(content[:90])