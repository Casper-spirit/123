grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s_student = sorted(list(students))     # сортировка учеников в алф.порядке
print(s_student)
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
f = sum(grades[4]) / len(grades[4])
sr_bal = list[a,b,c,d,f]
print(sr_bal)
cby = dict({s_student[0]:a, s_student[1]:b, s_student[2]:c, s_student[3]:d, s_student[4]:f})
print(cby)  #средний бал учеников в классе