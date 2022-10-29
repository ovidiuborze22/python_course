# Loop Over Dictionary and Replace
# Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'. In other words, your code should output:

# 0037682929928

# 00423998200919

# Hint: You can access dictionary values with phone_numbers.values() and you can replace characters using str.replace() 

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))