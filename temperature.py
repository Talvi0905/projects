
#tempreture calculator
t=0
while  True:
    t=int(input("""Tempreture calculator
                1 Convert °F to °C
                2 Convert °C to °F
                3 Exit
                ENTER YOUR CHOCIE:-  """ ))

    if t==1:
        #convert °F to °C
        print("convert °F to °C")
        fah1=int(input("Enter a tempreture in °F:"))
        cel1=(fah1 - 32) * 5/9
        print("Tempreture in celcius :- {}°C".format(cel1))
    
    elif t==2:
        #convert °C to °F
        print("convert °C to °F")

        cel2=int(input("Enter a tempreture in °C:"))
        fah2=(cel2 * 9/5) + 32
        print("Tempreture in Fahrenheit:- {}°F".format(fah2))

    elif t==3:
        break

    else : print("invalid")




