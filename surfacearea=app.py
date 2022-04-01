q=0
pi_value=22/7
while True:
    q=int(input('''type of equation
                1  Area of Sphere
                2  Area of Cuboid
                3  Area of Cylinder
                4  Area of Cone (includind bottam)
                5  Exit 
                ENTER YOUR CHOICE :-   '''))

    if q==1:
        print("Area of Sphere")
        redius_1=int(input("Enter the Redius:"))
        sph_area=4*pi_value*redius_1*redius_1

        print(f"Surface Area of Sphere : {sph_area}m2")

    elif q==2:
        print("Area of Cuboid")
        lenth_1=int(input("Enter the Lenth: "))
        width_1=int(input("Enter the width: "))
        height_1=int(input("Enter the height: "))
        cub_area=2*(lenth_1*width_1+lenth_1*height_1+height_1*width_1)

        print(f"Area of cuboid :{cub_area}m2 ")

    elif q==3:
        print("Area of Cylinder")
        redius_2=int(input("Enter the Redius: "))
        height_2=int(input("Enter the height: "))
        cyl_area=2*pi_value*redius_2*(redius_2+height_2)

        print(f"Area of Cylinder: {cyl_area}m2")

    elif q==4:
        print("Area of Cone (includind bottam)")
        redius_3=int(input("Enter the Reduis: "))
        height_3=int(input("Enter the height: "))

        lenth_1=redius_3*redius_3+height_3*height_3
        lenth_2=lenth_1**(1/2)


        cone_area=pi_value*redius_3*(2+lenth_2)

        print(f"Area of cone {cone_area}.m2")

    elif q==5:
        break

else:print("invalid")