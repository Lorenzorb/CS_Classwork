grade = input("Enter your letter grade for math: ").upper()
math_points = 0
if grade == 'A':
    math_points += 4.0
elif grade == 'B':
    math_points += 3.5
elif grade == 'C':
    math_points += 3.0
elif grade == 'D':
    math_points += 2.5
elif grade == 'F':
    math_points += 2.0
print(math_points)

grade = input("Enter your letter grade for history: ").upper()
history_points = 0
if grade == 'A':
    history_points += 4.0
elif grade == 'B':
    history_points += 3.5
elif grade == 'C':
    history_points += 3.0
elif grade == 'D':
    history_points += 2.5
elif grade == 'F':
    history_points += 2.0
print(history_points)

grade = input("Enter your letter grade for science: ").upper()
science_points = 0
if grade == 'A':
    science_points += 4.0
elif grade == 'B':
    science_points += 3.5
elif grade == 'C':
    science_points += 3.0
elif grade == 'D':
    science_points += 2.5
elif grade == 'F':
    science_points += 2.0
print(science_points)

print('you\'re overall gpa is...')
gpa = ((science_points + history_points + math_points)/3)
total_gpa = round(gpa, 2)
print(total_gpa)