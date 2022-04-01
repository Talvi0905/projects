
pi_value1=22/7
pi_value=(pi_value1)

#Area of Surface

#4*pi_value*redius*redius

print("Area of Sphere")
redius_1=int(input("Enter the Redius:"))
sph_area=4*pi_value*redius_1*redius_1

print(f"Surface Area of Sphere : {sph_area}m2") 

#Area of Cuboid
#2*(lenth*width+lenth*height+height*width)

print("Area of Cuboid")
lenth_1=int(input("Enter the Lenth: "))
width_1=int(input("Enter the width: "))
height_1=int(input("Enter the height: "))
cub_area=2*(lenth_1*width_1+lenth_1*height_1+height_1*width_1)

print(f"Area of cuboid :{cub_area}m2 ")

#Area of Cylinder
#2*pi_value*redius*(redius+height)

print("Area of Cylinder")
redius_2=int(input("Enter the Redius: "))
height_2=int(input("Enter the height: "))
cyl_area=2*pi_value*redius_2*(redius_2+height_2)

print(f"Area of Cylinder: {cyl_area}m2")


#Area of Cone (includind bottam)
#pi_value*redius*lenth+pi_value*redius*redius
#lenth_1=redius_3*redius_3+height_3*height_3
#lenth_2=lenth_1**(1/2)

print("Area of Cone (includind bottam)")
redius_3=int(input("Enter the Reduis: "))
height_3=int(input("Enter the height: "))

lenth_1=redius_3*redius_3+height_3*height_3
lenth_2=lenth_1**(1/2)

#a=pi_value*redius_3*lenth_2+pi_value*redius_3*redius_3
cone_area=pi_value*redius_3*(2+lenth_2)

print(f"Area of cone {cone_area}.m2")



input("Enter to exit")

#squrroot=value**(1/2)







#print(pressEnter to exit)
