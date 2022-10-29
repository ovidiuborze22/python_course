# Indefinite Number of Strings Processed (E)
# Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. 
# For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(foo("snow", "glacier", "iceberg"))