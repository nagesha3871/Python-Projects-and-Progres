# print("welcome to Your Love Score cheking")
# king=input("Enter King name:")
# queen=input("Enter your Queen name:")
# combine=king+queen
# new_str=combine.lower()
# #True
# t=new_str.count("t")
# r=new_str.count("r")
# u=new_str.count("u")
# e=new_str.count("e")
# true=t+r+u+e

# l=new_str.count("l")
# o=new_str.count("o")
# v=new_str.count("v")
# e=new_str.count("e")
# love=l+o+v+e

# result=int(str(true)+str(love))

# if (result<10) or (result>90):
#     print("coke")
# elif result>40 and result<50:
#     print("good")
# else:
#     print("z")




#code for wampus problem sloving 
print("-------welcome to Gold Hunting Game-------")
print("You have the Options to Go Left and right only")
choice=input("Enter your First Move:L/R")
if choice=="L":
    print("Your are out!!!!!")
    exit()
elif choice=="R":
    print("You are Suceed first Move ????")
    choice2=int(input("Enter Your Choice: 1.Smell 2.Cold 3.Nothing"))
    if choice2==1:
        print("you are out due to drinage......")
        exit()
    elif choice2==2:
        print("your under cold warmer you are out...")
        exit()
    elif choice2==3:
        print("good move////")
        last=int(input("enter your choice 1.red 2.blue 3.yello"))
        if last==1:
            print("You falied due to fair")
            exit()
        elif last==2:
            print("you falied due to watre")
            exit()
        elif last==3:
            print("congratulations you have win gold..")
            exit()
        else:
            print("invalid choice")

    else:
        print("invalid choice")

print("invalid choice")