# Indefinite Number of Keyword Arguments (E)
# Enter the correct parameters inside find_sum() so that the output of the code is 9.

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(x=1, y=2, z=6))