# 2 - Homework 
# 1 - task

import datetime  # hozirgi yilni olish uchun

# Foydalanuvchidan ma’lumot so‘raymiz
name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))

# Hozirgi yilni aniqlaymiz
current_year = datetime.datetime.now().year

# Yoshni hisoblaymiz
age = current_year - birth_year

# Natijani chiqaramiz
print(f"Salom, {name}! Sizning yoshingiz: {age} yosh.")


# 2- task

txt = 'LMaasleitbtui'
car_name = txt[::2]
print(car_name) 
print(txt[1::2]) 


# 3-task

txt = 'MsaatmiazD'
car_name = txt[::2]
print("Topilgan mashina nomi:", car_name)
print("Topilgan mashina nomi:", txt[::-2])


# 4- task

txt = "I'am John. I am from London"
words = txt.split()  
area = words[-1]    
print("Yashash joyi:", area)



# 5- task

matn = input("Matn kiriting: ")

teskari = matn[::-1]

print("Teskari matn:", teskari)



# 6 - task

matn = input("Matn kiriting: ")

unlilar = "aeiouAEIOU"

soni = 0

for harf in matn:
    if harf in unlilar:
        soni += 1

print("Unli harflar soni:", soni)



# 7- task

raqamlar = input("Sonlarni vergul bilan kiriting (masalan: 3,5,1,8): ")

sonlar = [int(x) for x in raqamlar.split(",")]

maksimum = max(sonlar)

print("Eng katta son:", maksimum)



# 8- task

soz = input("So‘z kiriting: ")

teskari = soz[::-1]

if soz == teskari:
    print("Bu so‘z palindrom.")
else:
    print("Bu so‘z palindrom emas.")




# 9- task

email = input("Email manzilini kiriting: ")

if "@" in email:
    domen = email.split("@")[1]
    print("Domen:", domen)
else:
    print("Noto‘g‘ri email manzil.")




# 10 - task

import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))

belgilar = string.ascii_letters + string.digits + string.punctuation

parol = ''.join(random.choice(belgilar) for i in range(uzunlik))

print("Yaratilgan parol:", parol)












