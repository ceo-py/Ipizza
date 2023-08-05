name = input()
grades = 1.0
sum_grades = 0.0
excluded = 0
grade_counter = 0
bad_grade_condition = False
while grades <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded += 1
        if excluded > 1:
            bad_grade_condition = True
            grade_counter += 1
            break
    else:
        sum_grades += grade
        grade_counter += 1

if bad_grade_condition:
    print(f'{name} has been excluded at {grade_counter} grade')
else:
    sum_grades /= grade_counter
    print(f'{name} graduated. Average grade:{sum_grades}')