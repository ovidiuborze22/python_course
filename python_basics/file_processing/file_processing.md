# **Cheatsheet: File Processing**
In this section, you learned that:

* You can **read** an existing file with Python:
```py
with open("file.txt") as file:
    content = file.read()
```
* You can **create** a new file with Python and **write** some text on it:
```py
with open("file.txt", "w") as file:
    content = file.write("Sample text")
```
* You can **append** text to an existing file without overwriting it:
```py
with open("file.txt", "a") as file:
    content = file.write("More sample text")
```    
* You can both append and read a file with:
```py
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
```