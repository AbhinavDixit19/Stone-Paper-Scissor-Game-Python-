import random

'''
1 for stone
-1 for paper
0 for scissor
'''

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (stone/paper/scissor): ").lower()

youDict = {"stone": 1, "paper": -1, "scissor": 0}
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

# check valid input
if youstr not in youDict:
    print("Invalid input!")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chooses {reverseDict[computer]}")

    if computer == you:
        print("It's a draw")

    else:
        if computer == -1 and you == 1: 
            print("You lose!")
        
        elif computer == -1 and you == 0:  
            print("You win!")
        
        elif computer == 1 and you == -1: 
            print("You win!")

        elif computer == 1 and you == 0:  
            print("You lose!")
        
        elif computer == 0 and you == -1: 
            print("You lose!")

        elif computer == 0 and you == 1:  
            print("You win!")

        else:
            print("Something went wrong!")

