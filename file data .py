#Ques1: write a python program to stored 10 fav. movies name into file.

i=1
file_name=input("enter your file name (with extension):-  ")
while i<=10:
    data=input(f"enter the movie name :{i}.")
    with open(file_name,"a") as fe:
        fe.write(f"\n{i}. ")
        fe.write(data)
    i+=1
print("save file success")




#Ques2: write a python program taking a list and total all elements in the list and stroed in file.

file_name1=input(" enter your file name (with extension):-  ")
j=1
student=[]
while j<=3:
    data=input(f"enter the student name :{j}.")
    student.append(f"\n{j}. {data}")
    j+=1


with open(file_name1,"a") as fh:
    fh.writelines(student)

print("Data is save")



