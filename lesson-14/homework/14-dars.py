
#1
[
    {
        "id": 1,
        "name": "Ali Karimov",
        "age": 20,
        "major": "Computer Science"
    },
    {
        "id": 2,
        "name": "Dilnoza Akramova",
        "age": 21,
        "major": "Data Analytics"
    },
    {
        "id": 3,
        "name": "Jasur Qodirov",
        "age": 19,
        "major": "Economics"
    }
]

import json

# JSON faylni ochish va o'qish
with open("students.json", "r", encoding='utf-8') as file:
    students = json.load(file)

# Har bir talabaning ma'lumotlarini chiqarish
for student in students:
    print("🧑‍🎓 Talaba ID:", student["id"])
    print("   Ismi:", student["name"])
    print("   Yoshi:", student["age"])
    print("   Yo'nalishi:", student["major"])
    print("-" * 30)

##2

import requests

# 🔑 API kalit
api_key = "cc4b2f049d301e555a04c17d64653f17"  # ← bu yerga o'z kalitingizni yozing

# 🏙 Shahar nomi
city = "Tashkent"

# 🌐 API so‘rov URL’ini tuzamiz
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# 🌍 API’ga murojaat yuboramiz
response = requests.get(url)

# 📦 JSON formatda javobni olamiz
data = response.json()

# 🔍 Zarur ma’lumotlarni ajratib olamiz
temperature = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

# 📤 Natijani chiqaramiz
print(f"🌍 Shahar: {city}")
print(f"🌡 Harorat: {temperature}°C")
print(f"💧 Namlik

import json

# 📥 Fayldan kitoblarni yuklash
def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# 💾 Faylga yozish
def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

# ➕ Yangi kitob qo‘shish
def add_book(books):
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = int(input("Yili: "))

    if books:
        new_id = max(book['id'] for book in books) + 1
    else:
        new_id = 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }

    books.append(new_book)
    print("✅ Yangi kitob qo‘shildi.")

# ✏️ Kitobni tahrirlash
def update_book(books):
    book_id = int(input("Tahrirlanadigan kitob ID’sini kiriting: "))
    for book in books:
        if book['id'] == book_id:
            book['title'] = input(f"Yangi nom ({book['title']}): ") or book['title']
            book['author'] = input(f"Yangi muallif ({book['author']}): ") or book['author']
            year_input = input(f"Yangi yil ({book['year']}): ")
            book['year'] = int(year_input) if year_input else book['year']
            print("✏️ Kitob yangilandi.")
            return
    print("⚠️ Kitob topilmadi.")

# ❌ Kitobni o‘chirish
def delete_book(books):
    book_id = int(input("O‘chiriladigan kitob ID’sini kiriting: "))
    initial_count = len(books)
    books[:] = [book for book in books if book['id'] != book_id]
    if len(books) < initial_count:
        print("🗑 Kitob o‘chirildi.")
    else:
        print("⚠️ Kitob topilmadi.")

# 📋 Menyu
def main():
    books = load_books()

    while True:
        print("\n=== 📚 KITOBLAR BOSHQARUVI ===")
        print("1. Yangi kitob qo‘shish")
        print("2. Kitobni tahrirlash")
        print("3. Kitobni o‘chirish")
        print("4. Barcha kitoblarni ko‘rish")
        print("5. Chiqish")

        choice = input("Tanlov (1-5): ")

        if choice == '1':
            add_book(books)
            save_books(books)
        elif choice == '2':
            update_book(books)
            save_books(books)
        elif choice == '3':
            delete_book(books)
            save_books(books)
        elif choice == '4':
            print("\n📚 Kitoblar ro'yxati:")
            for book in books:
                print(f"ID: {book['id']} | {book['title']} - {book['author']} ({book['year']})")
        elif choice == '5':
            print("👋 Dastur tugatildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")


# ▶️ Dastur ishga tushadi
if name == "main":
    main()
: {humidity}%")
print(f"📋 Ob-havo: {description}")


#4
import requests
import random

API_KEY = 'bb87b1f'  # bu yerga sizning haqiqiy API kalitingiz bo‘lishi kerak
OMDB_URL = "http://www.omdbapi.com/"

def get_random_movie_by_genre(genre):
    # Faqat test uchun oddiy kalit so'zlar ro'yxati
    keywords = ["love", "war", "future", "hero", "dark", "fire", "game", "life"]
    chosen_word = random.choice(keywords)

    params = {
        'apikey': API_KEY,
        's': chosen_word,
        'type': 'movie'
    }

    response = requests.get(OMDB_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'Search' in data:
            # Tavsiya qilish uchun 10 tagacha natijadan tasodifiy tanlab olish
            filtered = [
                movie for movie in data['Search']
                if check_genre(movie['imdbID'], genre)
            ]
            if filtered:
                movie = random.choice(filtered)
                print(f"🎬 Tavsiya: {movie['Title']} ({movie['Year']})")
            else:
                print("Afsuski, mos film topilmadi.")
        else:
            print("Filmlar topilmadi.")
    else:
        print("API bilan bog‘lanishda xatolik.")

def check_genre(imdb_id, genre):
    params = {
        'apikey': API_KEY,
        'i': imdb_id
    }
    response = requests.get(OMDB_URL, params=params)
    if response.status_code == 200:
        details = response.json()
        return genre.lower() in details.get("Genre", "").lower()
    return False

# Foydalanuvchidan janr so‘rash
user_genre = input("Qaysi janrdagi film tavsiya etilsin? (masalan: Action, Drama): ")
get_random_movie_by_genre(user_genre)
