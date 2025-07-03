print('''                    ___
              . -^   `--,
             /# =========`-_
            /# (--====___====\
           /#   .- --.  . --.|_
          /##   |  * ) (   * ),
           |##   \    /\ \   / |
           |###   ---   \ ---  |
           |####      ___)    #|
           |######           ##|
            \##### ---------- /
             \####           (
              `\###          |
                \###         |
                /\###        |
               /  \###\     _/\
              /     \##########
             |       \########|
             |________\#######|
               |       |#######|
               |_______|#######|
               |       |#######|
               |       |#######|
               |       |#######|
               |       |#######|
               |       |#######|
 ''')

# The below two lines will print the welcome message
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

# Takes input from the user and stores it in the choice1 variable, and this  .lower() will ensure that whatever like capital or small words typed by the user are taken input as lower case.
choice1 = input(
    '"You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hold. Game Over.")
