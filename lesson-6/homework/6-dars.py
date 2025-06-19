txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]



n = int(input("Butun son kiriting: "))

for i in range(n):
    print(i * i)

i = 1

while i <= 10:
    print(i)
    i += 1


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()  # har bir qatordan keyin yangi qator
    i += 1

n = int(input('Son kiriting:'))

sum = 0
for i in range(0, n + 1):
    sum = sum + i
print(sum)



n = int(input('Son kiriting:'))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  
    if num % 5 == 0 and num <= 150:
        print(num)



n = int(input('Son kiriting:'))
cnt = 0
while n != 0:
    n = n // 10
    cnt += 1
print(count)    



n = int(input('Son kiriting:'))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()   




list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):   # i = 4, 3, 2, 1, 0
    print(list1[i])



for i in range(-10, 0, 1):
    print(i)




for i in range(5):
    print(i)
print("Done!")



start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1: 
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  
        else:
            print(num)




n = int(input("Son kiriting: "))

faktorial = 1

if n < 0:
    print("Manfiy sonning faktoriali mavjud emas.")
else:
    for i in range(1, n + 1):
        faktorial *= i
    print(f"{n}! = {faktorial}")




list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

natija = []

copy2 = list2.copy()
for el in list1:
    if el in copy2:
        copy2.remove(el)
    else:
        natija.append(el)

copy1 = list1.copy()
for el in list2:
    if el in copy1:
        copy1.remove(el)
    else:
        natija.append(el)

print(natija)


