#         HOMEWORK 8

#     Python Exception Handling: Exercises, Solutions, and Practice

#     Exception Handling Exercises

# 1-task

try:
    # Bo‘linuvchi va bo‘luvchini kiritish
    a = int(input("Sonni kiriting: "))
    b = int(input("Bo‘luvchini kiriting (nol bo‘lmasin): "))
    
    # Bo‘lish amali
    result = a / b
    print("Natija:", result)

except ZeroDivisionError:
    print("Xatolik: Sonni nolga bo‘lish mumkin emas.")




# 2-task

try:
    user_input = input("Butun son kiriting: ")
    number = int(user_input)
    print("Siz kiritgan son:", number)

except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")




# 3-task

try:
    filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi. Iltimos, fayl nomini tekshiring.")




# 4-task

try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")

    # Har ikkisini float (yoki int) ga aylantirish
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        raise TypeError("Faqat son kiritish kerak!")

    num1 = float(a)
    num2 = float(b)

    print("Kiritilgan sonlar:", num1, "va", num2)

except TypeError as e:
    print("Xatolik:", e)




# 5-task

try:
    filename = input("Fayl nomini kiriting: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except PermissionError:
    print("Xatolik: Faylni o‘qish uchun ruxsat yo‘q.")




# 6-task

try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz (0–4): "))
    print("Tanlangan element:", my_list[index])

except IndexError:
    print("Xatolik: Indeks ro‘yxat doirasidan tashqarida.")





# 7-task

try:
    number = int(input("Iltimos, biror son kiriting: "))
    print("Siz kiritgan son:", number)

except KeyboardInterrupt:
    print("\nXatolik: Kiritish jarayoni foydalanuvchi tomonidan bekor qilindi (Ctrl+C bosildi).")




# 8-task

try:
    a = float(input("Birinchi sonni kiriting (bo‘linuvchi): "))
    b = float(input("Ikkinchi sonni kiriting (bo‘luvchi): "))
    
    result = a / b
    print("Natija:", result)

except ArithmeticError as e:
    print("Arifmetik xatolik yuz berdi:", e)





# 9-task

try:
    filename = input("Fayl nomini kiriting: ")
    
    # Faylni UTF-8 kodlash bilan ochishga harakat qilinadi
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except UnicodeDecodeError:
    print("Xatolik: Faylni o'qishda kodlash (encoding) muammosi yuz berdi.")





# 10-task

try:
    my_list = [1, 2, 3, 4, 5]

    # Noto‘g‘ri atributga murojaat (masalan, 'split' — bu string atributi)
    result = my_list.split()
    print(result)

except AttributeError:
    print("Xatolik: Ro'yxatda bu atribut mavjud emas.")





#        Python File Input Output: Exercises, Practice, Solution
#      File Input/Output Exercises
# 1-task

# Foydalanuvchidan fayl nomini so‘rash
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 2-task

filename = input("Fayl nomini kiriting: ")
n = int(input("Nechta qatordan iborat bo‘limni o‘qishni xohlaysiz (n): "))

try:
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break  # Fayl tugadi
            print(line.strip())  # Qatorni chiqarish (oxiridagi \n ni olib tashlaydi)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 3-task

filename = input("Fayl nomini kiriting: ")
text_to_append = input("Qo‘shmoqchi bo‘lgan matnni kiriting: ")

try:
    # 1. Faylga matnni qo‘shish (append rejimida)
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')

    # 2. Faylni o‘qib, butun mazmunini ko‘rsatish
    print("\nFaylga yozilganidan keyingi mazmuni:")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")





# 4-task

filename = input("Fayl nomini kiriting: ")
n = int(input("Oxirgi nechta qatorni o‘qishni xohlaysiz (n): "))

try:
    with open(filename, 'r') as file:
        lines = file.readlines()  # Faylni barcha qatorlari ro‘yxatga o‘qiladi
        last_n_lines = lines[-n:]  # Oxirgi n ta qator olinadi

        print(f"\nFaylning oxirgi {n} qatori:")
        for line in last_n_lines:
            print(line.strip())  # Qatorlarni toza ko‘rinishda chiqarish

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting.")





# 5-task

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        lines_list = [line.strip() for line in file]  # Har bir qatorni ro‘yxatga qo‘shish

    print("\nFayldan o‘qilgan qatorlar ro‘yxati:")
    print(lines_list)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")



# 6-task

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = ""
        for line in file:
            content += line  # Har bir qatorni umumiy o‘zgaruvchiga qo‘shish

    print("\nFayl mazmuni:")
    print(content)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 7-task

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        array = [line.strip() for line in file]  # Har bir qatorni massivga qo‘shish

    print("\nFayldan o‘qilgan qatorlar:")
    print(array)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 8-task

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()  # Barcha so‘zlarni olish
        max_length = max(len(word) for word in words)  # Eng uzun so‘z uzunligini topish
        longest_words = [word for word in words if len(word) == max_length]  # Eng uzun so‘z(lar)ni topish

    print(f"\nEng uzun so‘z uzunligi: {max_length} belgi")
    print("Eng uzun so‘z(lar):")
    for word in longest_words:
        print(word)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 9-task

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)  # Har bir qator uchun 1 qo‘shiladi

    print(f"\nFayldagi qatorlar soni: {line_count}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 10-task

from collections import Counter

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        text = file.read().lower()  # Faylni o‘qish va kichik harflarga o‘tkazish
        words = text.split()        # So‘zlarga ajratish
        word_counts = Counter(words)  # Har bir so‘z necha marta uchraganini sanash

    print("\nSo‘zlar chastotasi:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 11-task

import os

filename = input("Fayl nomini kiriting: ")

try:
    file_size = os.path.getsize(filename)  # Fayl hajmi baytlarda
    print(f"\nFayl hajmi: {file_size} bayt")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")




# 12-task

# Yoziladigan ro‘yxat
my_list = ["Apple", "Banana", "Cherry", "Date"]

filename = input("Fayl nomini kiriting (masalan: fruits.txt): ")

try:
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(item + '\n')  # Har bir element yangi qatordan yoziladi

    print(f"\nRo‘yxatdagi elementlar '{filename}' fayliga muvaffaqiyatli yozildi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")




# 13-task

source_file = input("Nusxa olinadigan fayl nomini kiriting: ")
destination_file = input("Yangi fayl nomini kiriting: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()  # Asosiy fayldan barcha ma’lumotni o‘qish

    with open(destination_file, 'w') as dest:
        dest.write(content)   # Yangi faylga yozish

    print(f"\nFayl '{source_file}' dan '{destination_file}' ga muvaffaqiyatli nusxa ko‘chirildi.")

except FileNotFoundError:
    print("Xatolik: Asosiy fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")




# 14-task

file1 = input("1-fayl nomini kiriting: ")
file2 = input("2-fayl nomini kiriting: ")
output_file = input("Natija yoziladigan yangi fayl nomini kiriting: ")

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Qisqaroq faylga qarab uzunlikni moslashtirish
    combined_lines = [line1.strip() + " " + line2.strip() for line1, line2 in zip(lines1, lines2)]

    with open(output_file, 'w') as out:
        for line in combined_lines:
            out.write(line + "\n")

    print(f"\nQatorlar birlashtirilib '{output_file}' fayliga yozildi.")

except FileNotFoundError:
    print("Xatolik: Berilgan fayllardan biri topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")




# 15-task

import random

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()  # Barcha qatorlarni o‘qib ro‘yxatga joylaydi

    if lines:
        random_line = random.choice(lines).strip()  # Tasodifiy qator tanlash
        print(f"\nTasodifiy qator: {random_line}")
    else:
        print("Fayl bo‘sh.")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")





# 16-task

filename = input("Fayl nomini kiriting: ")

try:
    file = open(filename, 'r')  # Faylni ochish
    print(f"Fayl ochildimi? {'Yo‘q, hali ochiq' if not file.closed else 'Ha, yopilgan'}")

    file.close()  # Faylni yopish
    print(f"Fayl hozir yopildimi? {'Ha, yopilgan' if file.closed else 'Yo‘q, hali ochiq'}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")





# 17-task

filename = input("Fayl nomini kiriting: ")
output_file = input("Tozalangan natija yoziladigan fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Har bir qatorni `\n` belgisiz yozish
    cleaned_lines = [line.strip() for line in lines]

    with open(output_file, 'w') as file:
        file.write(' '.join(cleaned_lines))  # Qatorlarni bitta satrga yozish, bo‘sh joy bilan ajratilgan

    print(f"\nYangi qator belgilarisiz matn '{output_file}' fayliga yozildi.")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")




# 18-task

import re

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        text = file.read()

    # So'zlarni ajratish: harflar va raqamlar ketma-ketligi
    words = re.findall(r'\b\w+\b', text)

    print(f"\nSo‘zlar soni: {len(words)}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")




# 19-task

import os

# Foydalanuvchidan fayllar nomini olish (vergul bilan ajratilgan)
filenames = input("Matn fayllar nomlarini vergul bilan kiriting (masalan: a.txt, b.txt): ").split(',')

char_list = []

for fname in filenames:
    fname = fname.strip()  # Ortiqcha bo'sh joylarni olib tashlash

    try:
        with open(fname, 'r') as file:
            content = file.read()
            char_list.extend(list(content))  # Har bir belgini ro‘yxatga qo‘shish

    except FileNotFoundError:
        print(f"Xatolik: {fname} fayli topilmadi.")
    except Exception as e:
        print(f"{fname} faylida xatolik yuz berdi: {e}")

# Natijani chiqarish
print(f"\nTopilgan barcha belgilar ro‘yxati ({len(char_list)} ta):")
print(char_list)





# 20-task

import string

# Alfavitdagi barcha katta harflar: A dan Z gacha
for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")  # Faylga oddiy matn yoziladi

print("26 ta fayl muvaffaqiyatli yaratildi: A.txt dan Z.txt gacha.")





# 21-task

import string

# Foydalanuvchidan har bir qatorda nechta harf bo'lishini so'raymiz
num_letters_per_line = int(input("Har bir qatorda nechta harf bo‘lishi kerakligini kiriting: "))

filename = "alphabet_lines.txt"

try:
    with open(filename, 'w') as file:
        alphabet = string.ascii_uppercase  # A dan Z gacha
        for i in range(0, len(alphabet), num_letters_per_line):
            line = alphabet[i:i+num_letters_per_line]
            file.write(line + '\n')

    print(f"\nFayl '{filename}' yaratildi va harflar yozildi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")






