# conditionals examples

def mean(value):
    if isinstance(value, dict): # type(value) == dict
        the_mean = sum(value.values()) / len(value)
    else:    
        the_mean = sum(value) / len(value)
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(students_grades))
print(mean(monday_temperatures))
