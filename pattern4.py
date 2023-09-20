'''
WAPP to print the pattern
        *
      * *
    * * * 
  * * * *  
* * * * *  
'''

n=int(input("enter limit: "))
for i in range(n):
    for j in range(0,n-1-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()
    
#output:
'''
enter limit: 5
    *
   **
  ***
 ****
*****


enter limit: 10
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
'''
