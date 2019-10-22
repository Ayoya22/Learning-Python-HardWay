students = 856
num_of_classes = 20
teachers = 36
num_sport_grounds = 6

#Average number of students per class
avg_num_sdt_per_class = students / num_of_classes

#Average number of students per each teacher.
avg_num_sdt_per_teacher = students / teachers

#Average number of individual per class
avg_person_per_class = (students + teachers) / num_of_classes

print("Total number of students is : ", students)

print('We averagely have ', avg_num_sdt_per_class,' students per class')

print('We averagely have ', avg_num_sdt_per_teacher,' students per teacher to lecture them.')

print('We averagely have ', avg_person_per_class,' persons per class')

print('This is is an important test!')

print(f'The number of students is {students} in the whole school.')