'''
WAPP to print the pattern
* * * * *
* * * *
* * * 
* *  
*  
'''

n=int(input("enter limit: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

#output:
'''
enter limit: 10
* * * * * * * * * * 
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


enter limit: 6
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
