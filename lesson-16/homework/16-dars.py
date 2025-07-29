#1
import numpy as np

ls = [12.23, 13.32, 100, 36.32]


array_1d = np.array(ls)

# Display results
print("Original List:", ls)
print("One-dimensional NumPy array:", array_1d)


#2

# 2 dan 10 gacha sonlar
array = np.arange(2, 11)

# 3x3 matritsaga aylantirish
matrix = array.reshape(3, 3)

# Natijani chiqarish
print(matrix)



#3

import numpy as np

# 1. Null vektor yaratish (10 ta elementdan iborat)
null_vector = np.zeros(10)

# 2. Oltinchi elementni 11 ga o'zgartirish
null_vector[6] = 11

# 3. Natijani chiqarish
print(null_vector)

#4
arr=np.arange(12,38)

print(arr)


#5
arr = np.array([1, 2, 3, 4])

# Convert to float type
float_arr = arr.astype(float)

# Print results
print("Original array:", arr)
print("Array converted to float type:", float_arr)


#6
import numpy as np

# Ikkita alohida Celsius array
celsius1 = np.array([0, 12, 45.21, 34, 99.91])
celsius2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

# Fahrenheit ga o‘tkazish
fahrenheit1 = (celsius1 * 9/5) + 32
fahrenheit2 = (celsius2 * 9/5) + 32

# Natijalar
print("Values in Fahrenheit degrees:", np.round(fahrenheit1, 2))
print("Values in Centigrade degrees:", celsius2)
print("Values in Fahrenheit degrees:", np.round(fahrenheit2, 2))



#7
arr = np.array([10, 20, 30])

values_append=[40,50,60,70,80,90]

new_array=np.append(arr,values_append)

print(new_array)





#8
ar=np.random.randint(1,100,size=10)

mean_value=np.mean(ar)

median_value=np.median(ar)

std_value = np.std(ar)

print("Array:", ar)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)




#9

ar1=np.random.randint(1,100, size=(10, 10))


min_value=np.min(ar1)

max_value=np.max(ar1)

print("Minimum:", min_value)
print("Maximum:", max_value)



#10

ar1=np.random.rand(3,3,3)

print(ar1)
