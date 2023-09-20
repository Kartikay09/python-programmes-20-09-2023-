#guess the no.
import random
computer_no=random.randrange(1,101)
score =10

while True:
    user_num=int(input("guess the number between 1 and 100"))
    if user_num==computer_no:
        print("You won",score)
        break
    elif user_num<computer_no:
        print("too small")
    else:
        print("too large")
    score-=1
    
    
