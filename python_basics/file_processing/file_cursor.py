# file cursor
myfile = open("python_course/python_basics/file_processing/fruits.txt")
#print(myfile.read())
#print(myfile.read())# cursor stops at the end

# to fix this we will apply this method
# store the content in a variable
content = myfile.read()# read method to read only once

# now we can print as many times we want
print(content)
print(content)



