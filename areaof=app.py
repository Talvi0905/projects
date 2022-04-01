q=0
pi_value=22/7
while True:
        q=int(input('''Type of equation
                    '1 Area of Square'
                    '2 Area of Triangle'
                    '3 Area of Rectangle'
                    '4 Area of Circle'
                    '5 Area of Ellipes'
                    '6 Exit'
                    enter your choice :-     '''))
        if q==1:
            side1=int(input("Enter the side 1 :"))
            side2=int(input("Enter the side 2 :"))

            area=side1*side2
            print(f"Area of square : {area} sq m2")
        
        elif q==2:
            print("area of Triagle")

            base=int(input("Enter the base :"))
            height=int(input("Enter the height :"))

            tri_area=1/2*base*height

            print(f"Area of Triagle : {tri_area} sq m2")


        elif q==3:
            print("Area of Rectangle")

            rbase=int(input("Enter the base :"))
            rheight=int(input("Enter the height :"))

            rec_area=rbase*rheight

            print(f"Area of Rectangle : {rec_area} sq m2")


        elif q==4:
                print("Areaa of Circle")
                redius=int(input("Enter the Redius :"))
                cir_area=pi_value*redius*redius

                print(f"Area of Circle : {cir_area} sq m2")

        elif q==5:
            print("Area of Ellipes")

            a_axis=int(input("Enter the Axis a :"))
            basec=int(input("Enter the Axis b :"))

            elli_area=pi_value*a_axis*basec

            print(f"Area of Circle : {elli_area} sq m2")

        elif q==6 :
            break
        else:print("invalid")
    
