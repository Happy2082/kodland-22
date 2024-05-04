import random

symbols= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Jak długie ma być hasło "))

for i in range(length):
    print(random.choice(symbols))
