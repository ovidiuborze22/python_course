
# using getitem method to access an item in the list
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures.__getitem__(1))


# Complete the script so that it prints out the 3rd item of list serials
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])


# Complete the script so that it prints out the 1st, 3rd, and the 6th items of the list serials
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

# Append the first item of weekend to workdays.
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]

workdays.append(weekend[0])
print(workdays)
