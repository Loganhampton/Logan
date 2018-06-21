ans = raw_input("Would you like to know your fortune? Y or No")

ans1 = "A giant dragon will become your friend"
ans2 = "Shrimp"
ans3 = "You become a famous soccer player"

if ans == "Y":
    choice = raw_input("Pick a number from 1-3")
    if choice == 1:
        print(ans1)
    elif choice == 2:
        print(ans2)
    elif choice == 3:
        print(ans3)
        
else:
    print("Nothing happens")
    