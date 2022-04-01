#Making calculator logic
#2+2=4

num1=int(input("Enter a 1st number: "))
optr=input("Enter operators(+,-,*,/,%): ")
num2=float(input("Enter a 2nd number: "))

if(optr=='+'):
    add=num1+num2
    print(f"{num1} {optr} {num2} = {add}")
elif(optr=='-'):
    sub=num1-num2
    print(f"{num1} {optr} {num2} = {sub}")
elif(optr=='*'):
    mul=num1*num2
    print(f"{num1} {optr} {num2} = {mul}")
elif(optr=='/'):
    div=num1/num2
    print(f"{num1} {optr} {num2} = {div}")
elif(optr=='%'):
    mod=num1%num2
    print(f"{num1} {optr} {num2} = {mod}")
else:
    print(f"{optr} is invalid")