# Copy n-times (E)
# The existing content of data.txt looks like this:

# 1.3, 1.5

# 2.3, 2.7

# Use Python to modify the content of data.txt so that its content looks like below:

# 1.3, 1.5

# 2.3, 2.7

# 1.3, 1.5

# 2.3, 2.7

# 1.3, 1.5

# 2.3, 2.7

# So, you need to find a way to insert the existing content two more times.

with open("python_course/python_basics/file_processing/files/data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)