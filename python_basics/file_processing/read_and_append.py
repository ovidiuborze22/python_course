# Read and Append (E)
# Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.

with open("python_course/python_basics/file_processing/files/bear1.txt", "r") as file:
    content = file.read()
    
    
with open ("python_course/python_basics/file_processing/files/bear2.txt", "a") as file:
    file.write(content)