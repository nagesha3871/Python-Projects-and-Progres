#code for wampus problem sloving 
print("-------welcome to Gold Hunting Game-------")
print("You have the Options to Go Left or Right only")
choice=input("Enter your First Move:Left / Right ")
if choice=="Left":
    print("Your are out.....!!!!!")
    exit()
elif choice=="Right":
    print("You are Suceed in First Thread......***")
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
