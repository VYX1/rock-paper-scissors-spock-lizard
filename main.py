import random
import sys

print("Welcome to Rock Paper Scissors Spock Lizard!\n")

def diff_selector():
    diff = input("Please select your difficulty! 1 (Easy) or 2 (Hard): ")
    try:
        intdiff = int(diff)
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        diff_selector()
    if(intdiff == 1):
        print("Thank you! you have selected easy difficulty " + diff)
        easy_mode()
    elif(intdiff == 2):
        print("Thank you! you have selected hard difficulty " + diff)
        hard_mode()
    else:
        print("Not an available difficulty. Please try again.\n")
        diff_selector()


def easy_mode():
    print("The rules are simple. You may choose any of 5 possible moves, as can the computer.")
    print("1. Rock\n2. Paper\n3. Scissors\n4. Spock\n5. Lizard\nChoices must be inputted as integers.")
    ez_choice = input("Please make your choice: ")
    ez_choice_pc = random.randint(1, 5)
    try:
        ez_choice_int = int(ez_choice)
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        easy_mode()
    if(ez_choice_int in range(1,6)):
        if(ez_choice_int == ez_choice_pc):
            print(f"You and the computer both chose " + str(ez_choice_int) + " Its a tie!")
        elif(ez_choice_int == 1 and ez_choice_pc in (3,5)):
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You win!")
        elif (ez_choice_int == 2 and ez_choice_pc in (1, 4)):
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You win!")
        elif (ez_choice_int == 3 and ez_choice_pc in (2, 5)):
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You win!")
        elif (ez_choice_int == 4 and ez_choice_pc in (1, 3)):
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You win!")
        elif (ez_choice_int == 5 and ez_choice_pc in (2, 4)):
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You win!")
        else:
            print(f"You chose " + str(ez_choice_int) + " and the computer chose " + str(ez_choice_pc) + ". You lose :(")
    else:
        print("Not an available option. Please try again.\n")
        easy_mode()
    re_run()

def hard_mode():
    print("The rules are simple. You may choose any of 5 possible moves, as can the computer.\nIn hard mode, the computer chooses twice, and has its choices favored.")
    print("1. Rock\n2. Paper\n3. Scissors\n4. Spock\n5. Lizard\nChoices must be inputted as integers.")
    hard_choice = input("Please make your choice: ")
    hard_choice_pc = random.randint(1, 5)
    hard_choice_pc_2 = random.randint(1,5)
    try:
        hard_choice_int = int(hard_choice)
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        hard_mode()
    if(hard_choice_int in range(1,6)):
        if(hard_choice_int == 1 and (hard_choice_pc in (3,5) and hard_choice_pc_2 in (3,5))):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You win!")
        elif (hard_choice_int == 2 and (hard_choice_pc in (1,4) and hard_choice_pc_2 in (1,4))):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You win!")
        elif (hard_choice_int == 3 and (hard_choice_pc in (2,5) and hard_choice_pc_2 in (2,5))):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You win!")
        elif (hard_choice_int == 4 and (hard_choice_pc in (1,3) and hard_choice_pc_2 in (1,3))):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You win!")
        elif (hard_choice_int == 5 and (hard_choice_pc in (2,4) and hard_choice_pc_2 in (2,4))):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You win!")
        elif (hard_choice_int == hard_choice and hard_choice_int == hard_choice_pc_2):
            print(f"You chose " + str(hard_choice_int) + ", the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". Its a tie!")
        else:
            print(f"You chose " + str(hard_choice_int) + " , the computer chose " + str(hard_choice_pc) + " and " + str(hard_choice_pc_2) + ". You lose :(")
    else:
        print("Not an available option. Please try again.\n")
        hard_mode()
    re_run()

def re_run():
    run = input("Run again? Y/N")
    if (run == "Y"):
        diff_selector()
    elif (run == "y"):
        diff_selector()
    else:
        sys.exit()

diff_selector()
