#countdown timer
import time
a=int(input("enter the no.:"))
i=1
print("start")
while a>=i:
    print(a)
    a-=1
    time.sleep(0.5)
print("stop")
