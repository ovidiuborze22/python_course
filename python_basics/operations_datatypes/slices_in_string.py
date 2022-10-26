# accessing characters and slices in strings
monday_temperatures = ['hello', 1, 2, 3]
print(monday_temperatures[0])

# we can also access the index from a string
monday_temperatures = ['hello', 1, 2, 3]
print(monday_temperatures[0][2])

# Slicing a List, 2nd to 4th (E)
# Print out the slice ['b', 'c', 'd'] of the letters list using slicing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

# Slicing a List, First Three (E)
# Print out the slice ['a', 'b', 'c'] of the letters list using slicing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0:3])

# Slicing a List, Last Three (E)
# Print out the slice ['e', 'f', 'g'] of the letters list using slicing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])
