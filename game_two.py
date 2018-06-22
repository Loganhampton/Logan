#import random module to create random number
import random

#my game in a function so I could replay game
def game():
    #generate random number
    computer = int(random.randint(1, 100))
    # variable that allows us to replay game
    done = False
    while not done:
        userNumber =int(raw_input("Guess number 1-100: "))
        if userNumber == computer:
            print("Congratulation! You win.")
            done = True
        elif userNumber > computer:
            print("To High, try again:")
        elif userNumber < computer:
            print("To Low, try again:")
        
    choice = raw_input("Would you like to play again? Y or N")
    if choice == "Y":
        game()
    else:
        print("Goodbye")
        done = True
#code to start game            
print("Welcome to quessing game")   
choice = raw_input("Would you like to play? Y or N")
if choice == "Y":
    #calling my function to play game
    game()
else:
    print("You're loss, Goodbye")
 