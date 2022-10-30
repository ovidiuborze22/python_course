# appending text to an existing file

with open('python_course/python_basics/file_processing/files/vegetables.txt', 'a+') as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()

print(content)
