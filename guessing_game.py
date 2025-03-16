
import random 


a=int(input("enter your no: "))
guess=random.randint(1,100)

count=0

while a!=guess:
    # print("computer guess",guess)
    delta= guess-a
    if delta==0:
        print("your guess is right")
        break
    elif delta > 0:
        print("guess is greater than input")
        a=int(input("enter your no: "))
    elif delta < 0:
        print("guess is lower than input")
        a=int(input("enter your no: "))
    count+=1
count+=1
print(f'your guess  is right in {count} attempt ')    

