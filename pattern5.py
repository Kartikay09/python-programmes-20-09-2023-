'''
WAPP to print the pattern
* * * * *
  * * * *
    * * * 
      * *  
        *
'''

n=int(input("enter limit: "))
for i in range(n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end="")
    print()


#output:
'''
enter limit: 5
*****
 ****
  ***
   **
    *


enter limit: 10
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
'''
