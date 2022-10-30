# File Processing Inside Function (E)
# Define a function that gets a single string character and a filepath as parameters and returns the number of occurrences of that character in the file.

def foo(character, filepath="python_course/python_basics/file_processing/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
   
print(foo(character=''))

