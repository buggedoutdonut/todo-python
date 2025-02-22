import random
from random import randint
while True:
    try:
        num1 = int(input("Enter the starting number: "))
        num2 = int(input("Enter the end number: "))

        random_number = randint(num1,num2)
        print(random_number)
    except ValueError:
        print("Enter only digits.")
        continue