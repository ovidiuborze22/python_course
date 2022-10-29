# looping through a dictionary

students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in students_grades.items(): # instead we can use .keys() or .values()
    print(grades)