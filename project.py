from random import randint

val = randint(1,100)
done = False

while not done:
    choice = int(raw_input("Chose a number through 1-100"))
    if (choice == val):
        print("good job")
        done = True
    if (choice >= val):
        print("high")
    if (choice <= val):
        print("low")


