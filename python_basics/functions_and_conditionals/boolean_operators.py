# Warm or Cold (E)
# Define a function that:

# (1) takes a temperature as a parameter

# (2) returns "Warm" if the temperature is greater than 7

# (3) returns "Cold" if the temperature is equal to or less than 7

# If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.


from operator import gt

def foo(temperature):
    if temperature and temperature > 7:
        return "Warm"    
    else:
        return "Cold"

print(foo(7))
print(foo(5))
print(foo(9))


# Define a function that:

# (1) takes a string as a parameter

# (2) returns False if the string contains less than 8 characters

# (3) returns True if the string contains 8 or more characters

# In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.

def foo(password):
    if len(password) and len(password) > 8:
        return True
    else:
        return False

print(foo("mylongpassword"))