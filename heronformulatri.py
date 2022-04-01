print("Area of triangle (Heron's formula)")
#s=1/2*(a+b+c)
#p=s*(s-a)*(s-b)*(s-c)
#p**=(1/2)

a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
c=int(input("Enter the c: "))

s=1/2*(a+b+c)

p=s*(s-a)*(s-b)*(s-c)

p**=(1/2)

print(f"Area of triangle Heron's formula:{p}.m2")

input ("Enter to Exit")
