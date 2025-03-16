
import random 


a=int(input("enter your no: "))
guess=random.randint(1,10)

count=0

if a>=0 and a<=10:
    if guess == a:
        print("youre right")

    else:
        print("wrong")
else:
    print("please submit 1 to 10")

print("computer guess",guess)

