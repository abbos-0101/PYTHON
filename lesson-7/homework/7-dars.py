def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
is_prime(2)

def digit_sum(k):
    sum = 0
    while k > 0:
        sum = sum + k % 10
        k = k // 10
    print(sum)
        
digit_sum(123)

def power_2(n):
    k = 1
    while (2 ** k) <= n:
        print(2 ** k, end=' ')
        k += 1

power_2(10)
