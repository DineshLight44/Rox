# 1 for snake
# -1 for water
# 0 for gun
import random

computer = random.choice([-1,0,1])
you = input("Enter your choice: ")
dict = {"s":1 ,"w":-1 ,"g":0}
revdec = {1:"s" ,-1:"w" ,0:"g"}
younum =  dict[you]
print(f" Your chose {revdec[younum]} \n Computer chose {revdec[computer]}")

if(computer==younum):
    print("drew")

else:

 if(computer ==-1 and younum ==1):
    print("You win")

 elif(computer ==-1 and younum ==0):
    print("You lose")

 elif(computer ==1 and younum ==-1):
    print("you lose")

 elif(computer ==1 and younum ==0):
    print("You win")

 elif(computer ==0 and younum ==-1):
    print("you lose")

 elif(computer ==0 and younum ==1):
    print("You win")

 else:
    print("Enter correct choice")