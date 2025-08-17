import random
user=int(input("enter a number to guess the exact number:"))
for i in range(1,50):
    computer=random.randint()
    while True:
        if user==computer:
         print("you are right!")
        break
    else:
        print("you guessed the wrong number!")