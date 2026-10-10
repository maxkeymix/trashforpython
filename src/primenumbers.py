import math

def pr(x):
    if x < 2: return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

number = int(input("Введите ваше число: "))
if pr(number):
    print("Ваше число простое")
else:
    print("Ваше число составное")