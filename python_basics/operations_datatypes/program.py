# better error messages in Python 3.10

print("todai".replace("i", "y"))

# print("todai".replace("i", "y")
#      ^
# SyntaxError: '(' was never closed


x = [1, 2, 3]
# x = [1, 2 3]
#         ^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?