#                    HOMEWOR 3
# 1-task

mevalar = ["olma", "banan", "anor", "uzum", "shaftoli"]

print("Uchinchi meva:", mevalar[2])




# 2-task

sonlar1 = [1, 2, 3]

sonlar2 = [4, 5, 6]

birlashtirilgan = sonlar1 + sonlar2

print("Birlashtirilgan ro'yxat:", birlashtirilgan)




# 3-task

sonlar = [10, 20, 30, 40, 50, 60, 70]

birinchi = sonlar[0]

orta = sonlar[len(sonlar) // 2]

oxirgi = sonlar[-1]

yangi_royxat = [birinchi, orta, oxirgi]

print("Yangi ro'yxat:", yangi_royxat)




# 4-task

kinolar = ["Inception", "Titanic", "Interstellar", "The Matrix", "Avatar"]

kino_tuple = tuple(kinolar)

print("Tuple ko'rinishida:", kino_tuple)




# 5-task

shaharlar = ["Toshkent", "London", "New York", "Paris", "Tokyo"]

if "Paris" in shaharlar:
    print("Paris ro'yxatda mavjud.")
else:
    print("Paris ro'yxatda yo'q.")




# 6-task

sonlar = [1, 2, 3, 4, 5]

ikki_marta = sonlar * 2

print("Ikki marta ko'paytirilgan ro'yxat:", ikki_marta)




# 7-task

sonlar = [10, 20, 30, 40, 50]

sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]

print("Yangi ro'yxat:", sonlar)





# 8-task

# 1 dan 10 gacha bo'lgan sonlardan tuple yaratish
sonlar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 3-indeksdan 7-indeksgacha bo'lgan bo'lakni ajratib olish (7 indeks kirmaydi)
bolak = sonlar[3:7]

# Natijani chiqarish
print("Bolak:", bolak)




# 9-task

# Ranglar ro'yxati
ranglar = ["red", "blue", "green", "blue", "yellow", "blue", "black"]

# "blue" necha marta uchraganini hisoblash
sana = ranglar.count("blue")

# Natijani chiqarish
print('"blue" so‘zi ro‘yxatda', sana, 'marta uchradi.')





# 10-task

hayvonlar = ("cat", "dog", "lion", "tiger", "elephant")

indeks = hayvonlar.index("lion")

print('"lion" so‘zining indeksi:', indeks)




# 11-task

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

umumiy_tuple = tuple1 + tuple2

print("Umumiy tuple:", umumiy_tuple)




# 12-task

my_list = [10, 20, 30, 40, 50]

my_tuple = (1, 2, 3)

list_uzunligi = len(my_list)
tuple_uzunligi = len(my_tuple)

print("Ro'yxat uzunligi:", list_uzunligi)
print("To'plam uzunligi:", tuple_uzunligi)





# 13-task

sonlar_tuple = (10, 20, 30, 40, 50)

sonlar_list = list(sonlar_tuple)

print("Tuple:", sonlar_tuple)
print("List:", sonlar_list)




# 14-task

sonlar = (12, 45, 3, 89, 22)

eng_katta = max(sonlar)
eng_kichik = min(sonlar)

print("Eng katta qiymat:", eng_katta)
print("Eng kichik qiymat:", eng_kichik)





# 15-task

sozlar = ("olma", "anor", "banan", "gilos", "shaftoli")

teskari = sozlar[::-1]

print("Teskari tartibda:", teskari)

