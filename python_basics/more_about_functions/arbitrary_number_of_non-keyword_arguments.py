# function with an arbitrary number of non-keyword arguments
 
def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4, 5))
