# 1- task

year = int(input("Yilni kiriting: "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Kabisa yili")
    else:
        print("Kabisa yili emas")
else:
    print("Kabisa yili emas")



# 2- task

n = int(input("Butun son kiriting: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n > 20
    print("Not Weird")




# 3- task

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

# a va b ni kichikdan kattaga qarab tartiblaymiz
a, b = min(a, b), max(a, b)

# to‘g‘ridan-to‘g‘ri boshlang‘ich nuqtani hisoblab olamiz
start = a + (a % 2)  # agar a toq bo‘lsa, keyingi juftdan boshlanadi

# juft sonlar ro‘yxatini quramiz
even_numbers = list(range(start, b + 1, 2))

print("Juft sonlar:", even_numbers)
