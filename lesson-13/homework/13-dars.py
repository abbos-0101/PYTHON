
#1
import datetime

birth_date = input('Plese birth date : "%m/%d/%Y "')

delta_birth_date=datetime.datetime.strptime(birth_date,"%m/%d/%Y")

today=datetime.datetime.today()

age=today-delta_birth_date

years = today.year - delta_birth_date.year
months = today.month - delta_birth_date.month
days = delta_birth_date.day-today.day 



print(f"Sizning yoshingiz : \n{years} yil,\n{months} oy,\n{days} kun")


#2
import datetime

next_birthday = input('Plese birth date : "%m/%d/%Y "')

delta_next_birthday=datetime.datetime.strptime(next_birthday,"%m/%d/%Y")

today=datetime.datetime.today()

months = today.month - delta_next_birthday.month
days=delta_next_birthday.day-today.day

print(f"Tug'ilgan kuningizgacha {months} oy,{days} kun qoldi")


#3
from datetime import datetime, timedelta

current_date_str = input('Please enter current date : "%m/%d/%Y %H:%M:%S" ')
hour = int(input('Please enter Hours of meeting: '))
minute = int(input('Please enter Minutes of meeting: '))

current_date = datetime.strptime(current_date_str, "%m/%d/%Y %H:%M:%S")
duration = timedelta(hours=hour, minutes=minute)
end_date = current_date + duration

print("Meeting ends at:", end_date.strftime("%m/%d/%Y %H:%M:%S"))


#4
from datetime import datetime,date,time,timedelta,timezone
import pytz

local = datetime.now()
print("Local: ", local.strftime("%m/%d/%Y %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datettime_NY = datetime.now(tz_NY)
print("New York: ", datettime_NY.strftime("%m/%d/%Y %H:%M:%S"))


#5
import datetime
import time


future_str = input('Kelajakdagi sanani kiriting : "%m/%d/%Y %H:%M:%S" ')

future_time = datetime.datetime.strptime(future_str, "%m/%d/%Y %H:%M:%S")

while True:
    now = datetime.datetime.now()
    delta = future_time - now

    if delta.total_seconds() <= 0:
        print("\n⏰ Countdown tugadi!")
        break


    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    print(f"Qolgan vaqt: {days} kun, {hours} soat, {minutes} daqiqa, {seconds} soniya", end='\r')

    time.sleep(1)

#6
email = input("Email manzilini kiriting: ")

if "@" in email and "." in email and email.count('@') == 1 and " " not in email:
    print("✅ Email manzili to‘g‘ri formatda.")
else:
    print("❌ Email manzili noto‘g‘ri.")


#7
phone = input("Telefon raqamingizni kiriting (10 raqam, masalan: 1234567890): ")

# Tekshirish
if len(phone) == 10 and phone.isdigit():
    area = phone[:3]
    prefix = phone[3:6]
    line = phone[6:]
    formatted = f"({area}) {prefix}-{line}"
    print("Formatlangan raqam:", formatted)
else:
    print("❌ Noto‘g‘ri kirish! Iltimos, faqat 10 ta raqam kiriting.")


#8

password = input("Parolingizni kiriting: ")


length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

has_special = any(char in "!@#$%^&*()_+-=" for char in password)


print("\n--- Parol tahlili ---")
print(f"1️⃣ Uzunlik (>=8): {'✅' if length_ok else '❌'}")
print(f"2️⃣ Katta harf:     {'✅' if has_upper else '❌'}")
print(f"3️⃣ Kichik harf:    {'✅' if has_lower else '❌'}")
print(f"4️⃣ Raqam:          {'✅' if has_digit else '❌'}")
print(f"5️⃣ Maxsus belgi:   {'✅' if has_special else '❌'}")


if all([length_ok, has_upper, has_lower, has_digit]):
    print("\n Sizning parolingiz kuchli!")
else:
    print("\n Parolingiz kuchsiz! Iltimos, uni yaxshilang.")


#9
text = "The sun is shining. The sky is blue. Sunlight makes us feel good."


word = input("Qanday so‘zni qidirmoqchisiz? ").lower()


words = text.lower().split()


count = words.count(word)

print(f"\n🔎 So‘z: '{word}'")
print(f"✅ Matnda {count} marta uchradi.")


import re

text = input("Matnni kiriting (sana mavjud bo‘lishi mumkin): ")


date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b'

# 3. Mos keluvchi sanalarni topish
dates = re.findall(date_pattern, text)

# 4. Natijani chiqarish
if dates:
    print("\n📅 Topilgan sanalar:")
    for date in dates:
        print(f"- {date}")
else:
    print("❌ Matnda sana topilmadi.")
