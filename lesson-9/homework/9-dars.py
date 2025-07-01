#          HOMEWORK 9
# 1-task

# So‘zlardan iborat tuple (to‘plam) yaratish
sozlar = ("olma", "anor", "banan", "gilos", "shaftoli")

# Tuple ni teskari tartibda chiqarish
teskari = sozlar[::-1]

# Natijani chop etish
print("Teskari tartibda:", teskari)



# 2-task

from datetime import datetime

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")  # tug'ilgan sana formatda bo'lishi kerak

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        # Agar tug‘ilgan kun hali kelmagan bo‘lsa, 1 yil ayiramiz
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

# Foydalanuvchi obyektini yaratish
person1 = Person("Abbosbek", "O‘zbekiston", "2000-05-20")

# Ma'lumotlarni chiqarish
print("Ismi:", person1.name)
print("Mamlakati:", person1.country)
print("Yoshi:", person1.calculate_age())




# 3-task

class Calculator:
    def yigindisi(self, a, b):
        return a + b

    def ayirmasi(self, a, b):
        return a - b

    def kopaytmasi(self, a, b):
        return a * b

    def bolinmasi(self, a, b):
        if b == 0:
            return "0 ga bo‘lish mumkin emas"
        return a / b

# Kalkulyator obyektini yaratish
calc = Calculator()

# Foydalanuvchidan sonlar va amalni olish
a = float(input("a sonini kiriting: "))
b = float(input("b sonini kiriting: "))


tanlov = input("Amal raqamini kiriting: +, -, *, / ")

# Tanlovga qarab natijani chiqarish
if tanlov == "+":
    print("a + b = ", calc.yigindisi(a, b))
elif tanlov == "-":
    print("a - b = ", calc.ayirmasi(a, b))
elif tanlov == "*":
    print("a * b = ", calc.kopaytmasi(a, b))
elif tanlov == "/":
    print("a / b = ", calc.bolinmasi(a, b))
else:
    print("Noto‘g‘ri amal!")



# 4-task

import math

# Asosiy Shape klassi
class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

# Doira klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Kvadrat klassi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Uchburchak klassi
class Triangle(Shape):
    def __init__(self, a, b, c):  # a, b, c — tomonlar
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # yarim perimetr
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Geron formulasi

# 🔍 Sinovlar:
circle = Circle(5)
print("Doira → Maydon:", circle.area())
print("Doira → Perimetr:", circle.perimeter())

square = Square(4)
print("\nKvadrat → Maydon:", square.area())
print("Kvadrat → Perimetr:", square.perimeter())

triangle = Triangle(3, 4, 5)
print("\nUchburchak → Maydon:", triangle.area())
print("Uchburchak → Perimetr:", triangle.perimeter())






# 5-task

# Daraxt tuguni (Node) klassi
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Chap bola
        self.right = None  # O'ng bola

# Ikkilik qidiruv daraxti (BST) klassi
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Yangi element qo'shish
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    # Elementni qidirish
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

# 🔍 Sinovlar:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("60 mavjudmi?", bst.search(60))  # True
print("25 mavjudmi?", bst.search(25))  # False





# 6-task

# Stack klassi
class Stack:
    def __init__(self):
        self.items = []

    # Element qo'shish (push)
    def push(self, item):
        self.items.append(item)

    # Elementni olib tashlash (pop)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo'sh"

    # Stack bo'shligini tekshirish
    def is_empty(self):
        return len(self.items) == 0

    # Stackni ko'rish
    def display(self):
        print("Stack:", self.items)

# 🔍 Sinov
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.display()     # Stack: [10, 20, 30]

print("Olib tashlandi:", stack.pop())  # 30
stack.display()     # Stack: [10, 20]




# 7-task

# Tugun (node) klassi
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList klassi
class LinkedList:
    def __init__(self):
        self.head = None

    # Element qo'shish (oxiriga)
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Tugun o'chirish
    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print("Element topilmadi:", data)

    # Ro'yxatni ko'rsatish
    def display(self):
        current = self.head
        if not current:
            print("Ro'yxat bo'sh")
            return
        print("Linked List:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 🔍 Sinov
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()           # 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()           # 10 -> 30 -> None

ll.delete(100)         # Element topilmadi: 100





# 8-task

# Savatcha klassi
class ShoppingCart:
    def __init__(self):
        self.items = {}  # {'Olma': [narx, soni]}

    # Mahsulot qo'shish
    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name][1] += quantity
        else:
            self.items[name] = [price, quantity]
        print(f"{quantity} ta '{name}' savatchaga qo‘shildi.")

    # Mahsulot o'chirish
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"'{name}' savatchadan o‘chirildi.")
        else:
            print(f"'{name}' savatchada topilmadi.")

    # Umumiy narxni hisoblash
    def total_price(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    # Savatchadagi mahsulotlarni ko‘rsatish
    def show_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
            return
        print("Savatchadagi mahsulotlar:")
        for name, (price, quantity) in self.items.items():
            print(f"- {name}: {quantity} dona, narxi: {price} so‘m")

# 🔍 Sinov
cart = ShoppingCart()

cart.add_item("Olma", 5000, 3)
cart.add_item("Banan", 7000, 2)
cart.add_item("Olma", 5000, 1)

cart.show_cart()

print("Umumiy narx:", cart.total_price(), "so‘m")

cart.remove_item("Banan")
cart.show_cart()




# 9-task

# Stack (Stek) klassi
class Stack:
    def __init__(self):
        self.stack = []

    # Element qo'shish
    def push(self, element):
        self.stack.append(element)
        print(f"'{element}' stekka qo‘shildi.")

    # Element olib tashlash
    def pop(self):
        if not self.stack:
            print("Stek bo‘sh. Element olib bo‘lmaydi.")
        else:
            element = self.stack.pop()
            print(f"'{element}' stekdan olib tashlandi.")

    # Elementlarni ko'rsatish
    def display(self):
        if not self.stack:
            print("Stek bo‘sh.")
        else:
            print("Stekdagi elementlar (pastdan yuqoriga):")
            for el in self.stack:
                print(el)

# 🔍 Sinov
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()




# 10-task

# Queue (Navbat) klassi
class Queue:
    def __init__(self):
        self.queue = []

    # Element qo'shish (navbat oxiriga)
    def enqueue(self, element):
        self.queue.append(element)
        print(f"'{element}' navbatga qo‘shildi.")

    # Element olib tashlash (navbat boshidan)
    def dequeue(self):
        if not self.queue:
            print("Navbat bo‘sh. Element olib bo‘lmaydi.")
        else:
            element = self.queue.pop(0)
            print(f"'{element}' navbatdan olib tashlandi.")

    # Navbatdagi elementlarni ko‘rsatish
    def display(self):
        if not self.queue:
            print("Navbat bo‘sh.")
        else:
            print("Navbatdagi elementlar (boshidan oxirigacha):")
            for el in self.queue:
                print(el)

# 🔍 Sinov
q = Queue()
q.enqueue("Olma")
q.enqueue("Banan")
q.enqueue("Nok")

q.display()

q.dequeue()
q.display()




# 11-task

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💰 {amount} so‘m qo‘shildi. Yangi balans: {self.balance} so‘m")
        else:
            print("⚠️ Yaroqsiz miqdor")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"💸 {amount} so‘m yechildi. Yangi balans: {self.balance} so‘m")
        else:
            print("❌ Yetarli mablag‘ mavjud emas.")

    def check_balance(self):
        print(f"📊 {self.name} balansida: {self.balance} so‘m mavjud.")

        # Mijoz uchun yangi hisob ochamiz
client1 = BankAccount("Abbos", 100000)

client1.check_balance()        # Balansni tekshirish
client1.deposit(50000)         # Hisobni to‘ldirish
client1.withdraw(30000)        # Mablag‘ yechib olish
client1.withdraw(150000)       # Yetarli mablag‘ bo‘lmaganda
client1.check_balance()        # Yana balansni tekshirish




