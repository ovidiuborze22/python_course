# runtime errors 
# Exceptions
a = 1
b = "2"
print(int(2.5))
# print(a + int(b))
print(str(a) + b)

# 1. Python first checks for SyntaxErrors
# File "runtime_errors.py", line 5
#   print(int(2.5)
#        ^
# SyntaxError: '(' was never closed

# 2. Python second checks for Exception errors
# Traceback (most recent call last):
# File "runtime_errors.py", line 6, in <module>
#    print(a + b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# name error
c = 3
print(c)
# Traceback (most recent call last):
#  File "runtime_errors.py", line 22, in <module>
#    print(c)
# NameError: name 'c' is not defined