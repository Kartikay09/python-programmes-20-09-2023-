'''
WAPP to print the pattern
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''

n=int(input("enter limit: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


#output:
'''
enter limit: 10
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 


enter limit: 6
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
'''
