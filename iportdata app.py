import os
import csv
while True:
    i=int(input("""ENTER YOUR CHOICE:-
                1. START NEW PROJECT
                2. READ DATA
                3. ADD NEW DATA
                4. DELETE FILE
                5. EXIT
                     ..- """))
    
    if i==1:
        file_name=input("enter your file name (with extension):-  ")    
        d=1
        while d<=10:
            data=input(f"enter the name :{d}.")
            d+=1
            with open(file_name,"w") as fe:
                fe.write(f"\n{data}")            
        print("save file success")
    elif i==2:
        file_name=input("enter your file name (with extension):-  ")
        with open(file_name,"r") as fh:
            print(fh.read())
    elif i==3:
        file_name=input("enter your file name (with extension):-  ")
        e=1
        while e<=10:
            data=input(f"enter the name :{e}.")
            e+=1
            with open(file_name,"a") as fg:
                fg.write(f"\n{data}")
        print("save file success")
    elif i==4:
        file_name=input("enter your file name (with extension):-  ")
        os.remove(file_name)
    elif i==5 :
        break
    else:
            print("try again")


    

