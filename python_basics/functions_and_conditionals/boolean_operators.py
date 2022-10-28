# Warm or Cold (E)
# Define a function that:

# (1) takes a temperature as a parameter

# (2) returns "Warm" if the temperature is greater than 7

# (3) returns "Cold" if the temperature is equal to or less than 7

# If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.

from operator import gt


def foo(temperature):
    if temperature > 7: # &gt; 7
        return "Warm"    
    else:
        return "Cold"

print(foo(7))
print(foo(5))
print(foo(8))