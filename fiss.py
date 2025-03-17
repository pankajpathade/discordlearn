import random

# num=random.randint(1,11)

num=int(input("enter your num: "))

try:
    if (num % 3==0) and (num % 5==0):
        print("fiss buss")

    elif num % 3==0:
        print('fiss')
    elif num % 5==0:
        print("buzz")
    else:
        print(num)
except ValueError:
    print("please insert correct no")