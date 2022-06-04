import random

mylist = ["R", "P", "S"]

print("Rules for the Rock paper scissor game are as follow: \n"
                                +"Rock vs paper: paper wins \n"
                                +"Rock vs scissor: Rock wins \n"
                                +"paper vs scissor: scissor wins \n")

while True:
    print("Enter a choice \n R for Rock, \n P for Paper, and \n S for Scissors")
    choice = input("User turn: ")

    while choice not in mylist:
        choice = input("Your choice is invalid, please enter a valid input: ")

    if choice == "R":
        choice_name = "Rock"
    elif choice == "P":
        choice_name = "Paper"
    elif choice == "S":
        choice_name = "Scissor"

    print("user choice is: " + choice_name)
    print("\nNow its the computer's turn ...")

    CPU_choice = random.choice(mylist)

    while CPU_choice == choice:
        CPU_choice = random.choice(mylist)

    if CPU_choice == "R":
        CPU_choice_name = "Rock"
    elif CPU_choice == "P":
        CPU_choice_name = "Paper"
    elif CPU_choice == "S":
        CPU_choice_name = "Scissor"

    print("Computer choice is: " + CPU_choice_name)
    print(choice_name + " v/s " + CPU_choice_name)

    if ((choice == CPU_choice)):
        print("It is a tie")
        result = "Tie"

    elif ((choice == "R" and CPU_choice == "P") or
            (choice == "P" and CPU_choice == "R")):
        print("Paper wins : ", end="")
        result = "Paper"

    elif ((choice == "R" and CPU_choice == "S") or
          (choice == "S" and CPU_choice == "R")):
        print("Rock wins :", end="")
        result = "Rock"

    else:
        print("Scissors wins :", end="")
        result = "Scissor"

    print("Do you want to play again, if not type exit?")
    answer = input()

    if answer == "exit" or answer == "EXIT":
        break

print("Thanks for playing, hope to see you soon!")
