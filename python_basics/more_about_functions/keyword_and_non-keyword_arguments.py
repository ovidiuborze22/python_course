# default and non-default parameters and keyword and non-keyword arguments

def area(a, b=6):
    return a * b

print(area(5, 6))
print(area(a=5, b=6))
print(area(b=6, a=5))
print(area(5))
print(area(a=5))
print(area(b=5,a=6))

