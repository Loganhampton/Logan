import random
print("Welcome to surviers")
print("You wake up in a attic and there is a zombie about to break the door you jump out the window")
print("You see a hoard behind you and you run to a car and get in and find the keys just in time you drive away")

#variables
milesTraveled = 20
thirst = 0
gas  = 50
zombiesTraveled = -20
water = 3

done = False


#start main loop
while not done: 
    zombiesBehind = milesTraveled - zombiesTraveled
    fullSpeed = random.randrange(13, 21)
    moderateSpeed = random.randrange(5, 12)
    print("""
    A. Drink the water.
    B. Ahead at the moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check
    Q. Quit.""")
    print()
    userInput = raw_input("Your choice?")  
    if userInput.lower() == "q":
        done = True
    elif userInput.lower() == "e":
        print("Miles traveled: ",milesTraveled)
        print("Drink water: ",water)
        print("Your car has ",gas,"amount of gas.")
        print("The zombies are",zombiesBehind,"miles behind you")
    elif userInput.lower() == "d":
        zombiesTraveled += random.randrange(7,15)
        gas = gas + random.randrange(5,10)
        water = water + random.randrange(1,3)
        print("You feel rested and ready to start the next day")
        
#move full speed
    elif userInput.lower() == "c":
        print("You traveled ",fullSpeed,"miles!")
        milesTraveled += fullSpeed
        thirst += 1
        gas = gas - 10
        supplies_cache = random.randrange(8,21)
        zombiesTraveled += random.randrange(6,15)
        
#move moderate speed
    elif userInput.lower() == "b":
        print("You went ",moderateSpeed,"miles!")
        milesTraveled += moderateSpeed
        thirst += 1
        gas = gas - 5
        
#supplies cache
        supplies_cache = random.randrange(1,3)
        zombiesTraveled += random.randrange(7,15)
        if supplies_cache == 2:
            water += 6
            print("your water is filled")
            thirst *= 0
            print("thirst is " ,thirst)
            gas += 60
            print ("gas is", gas)
        
#drink water
    elif userInput.lower() == "a":
       if water == 0:
           print("Your out of water")
       else:
            thirst -= 1
            water -= 1
            
        
    if zombiesTraveled <= 15:
        print("zombies are closing in")
    if milesTraveled >= 200 and not done:
        print("You have escaped the horrors or have you?")
        done = True
    if zombiesTraveled >= milesTraveled and not done:
        print("The zombies have eaten your brains")
        print("You have died")
        done = True
        
    if thirst > 3 and thirst <= 6 and not done:
        print("you are thirst")
    if thirst > 6 and not done:
        print("You died of thirst")
        done = True
        
    if gas <= 25 and not done:
        print("You are running low on gas")
    if gas <= 0 and not done:
        print("Your car died and the zombies caught up with ou and ate you")
        done = True 
        
            
         
        
    
    
    