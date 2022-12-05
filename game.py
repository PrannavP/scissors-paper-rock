import random
from playsound import playsound

# take user's choice
userchoice = input("Enter your choice: ")
lowercased_userchoice = userchoice.lower()
# print(lowercased_userchoice)

def check_user_input():
    if userchoice == 'rock':
        print("User chose rock!")
    elif userchoice == 'paper':
        print("User chose paper!")
    elif userchoice == 'scissor':
        print("User chose scissor!")
    else:
        print("Invalid choice!!")

check_user_input()

# computer logic
computer_choice = int(random.random() * 3) # Prints number between 0 and 2

def check_computer_choice():
    if computer_choice == 0:
        print("Computer chose rock!")
    elif computer_choice == 1:
        print("Computer chose paper!")
    elif computer_choice == 2:
        print("Computer chose scissor!")
    else:
        print("Computer crashed!!")

check_computer_choice()

# Compare choices of computer and player

def compare_choices():
    # Draw case
    if computer_choice == 0 and userchoice == "rock":
        print("DRAW!")
    elif computer_choice == 1 and userchoice == "paper":
        print("DRAW!")
    elif computer_choice == 2 and userchoice == "scissor":
        print("DRAW!")
    
    # User win case
    elif computer_choice == 0 and userchoice == "paper":
        print("User won!")
        playsound('sounds/victory.mp3')
    elif computer_choice == 1 and userchoice == "scissor":
        print("User won!")
        playsound('sounds/victory.mp3')
    elif computer_choice == 2 and userchoice == "rock":
        print("User won!")
        playsound('sounds/victory.mp3')
    
    # Computer win case
    elif computer_choice == 0 and userchoice == "scissor":
        print("Computer won!")
        playsound('sounds/lost.mp3')
    elif computer_choice == 1 and userchoice == "rock":
        print("Computer won!")
        playsound('sounds/lost.mp3')
    elif compare_choices == 2 and userchoice == "paper":
        print("Computer won!")
        playsound('sounds/lost.mp3')
    else:
        print("Error occured!")

compare_choices()