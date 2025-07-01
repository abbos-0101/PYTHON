# Lesson 4 Homework 

# Task 1 

my_dict={'apple':10,'banana':6,'cherry':9,'watermelon':5}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("O‘sish tartibida:", ascending)
print("Kamayish tartibida:", descending)
O‘sish tartibida: {'watermelon': 5, 'banana': 6, 'cherry': 9, 'apple': 10}
Kamayish tartibida: {'apple': 10, 'cherry': 9, 'banana': 6, 'watermelon': 5}

#Task 2

d={0: 10, 1: 20}
d['2']=30
d
{0: 10, 1: 20, '2': 30}

# Task 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict={**dic1,**dic2,**dic3}

print (new_dict)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#Task 4

n = int(input("n ni kiriting: "))
kvadrat_lugat = {}

for x in range(1, n+1):
    kvadrat_lugat[x] = x * x

print(kvadrat_lugat)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Task 5

kvadrat_lugat = {}

for x in range(1, 16):  
    kvadrat_lugat[x] = x * x

print(kvadrat_lugat)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Task 6

s={1,2,3,4,'salom','UZB','Aka'}

# Task 7

Students={"Islom","A'loxon","Azizbek","Abbos"}

for student in Students:
    print(student)
  Islom
A'loxon
Azizbek
Abbos

# Task 8

Students.add('Mirzobek')
Students
{"A'loxon", 'Abbos', 'Azizbek', 'Islom', 'Mirzobek'}

# Task 9 

Students.remove('Mirzobek')
Students
{"A'loxon", 'Abbos', 'Azizbek', 'Islom'}

# task 10 

Students = {"Islom","A'loxon","Azizbek","Abbos"}

element = "Abbos"

if element in Students:
    Students.remove(element)

print(Students)
{'Islom', "A'loxon", 'Azizbek'}
