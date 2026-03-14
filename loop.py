#LOOP EXERCISE
#WAP to check whether the no is prime or not
'''
x = int(input("Enter No:"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
'''
'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''
'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print(" "*(5-i),"*"*i)
'''
x = input("Enter String")
#print no of vowels
#in and not in - membership operator
v=0
for char in x:
    if char in "aeiouAEIOU":
        v+=1
print(v)
        
