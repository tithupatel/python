#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n1=int(input("Enter a value of n1:"))
n2=int(input("Enter a value of n2:"))
n3=int(input("Enter a value of n3:"))

if(n1==n2):
    print("The sum will be zero")
elif(n2==n3):
    print("The sum will be zero")
elif(n3==n1):
    print("The sum will be zero")
else:
    print("sum of three integer: ",n1+n2+n3)    
