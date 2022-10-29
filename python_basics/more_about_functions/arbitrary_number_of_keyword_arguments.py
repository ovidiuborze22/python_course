# functions with arbitrary number of keyword arguments

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))