# HAND CRICKET GAME
import random

# Taking number of overs as input from user
overs = int(input("Enter number of overs : "))

# Generating the Score of Computer
com_score = random.randint(0,overs*36)
print(f'Computer has scored {com_score} runs. Your Target is {com_score+1} runs')

# Function to Check if the Player won the Game
def iswin(com_score,tot_score):
    if (tot_score>com_score):
        return True
    else:
        return False

# For looping through overs and ball until the game ends
def startbowling(overs,com_score):
    tot_score = 0
    end = False
    win = False
    for over in range(1,overs+1):
        if end:
            break
        for ball in range(1,7):        
            print(f'\nOver {over} Ball {ball}')
                
            user_input = 0
            while(True):
                user_input= int(input("Enter number to bat : "))
                if(user_input in range(1,7)):
                    break
                print("Invalid Input. Try again!")

            com_num = random.randint(0,6)
            print(f'Computer\'s Number : {com_num}' )
                
            if(com_num != user_input ):
                tot_score+= user_input
            else:
                print('You are Out')
                print(f'Total Runs : {tot_score}')
                end = True
                break
            print(f'Total Runs : {tot_score}')
            if iswin(com_score,tot_score):
                print("\nCongratulations, You Win!!")
                end = True
                win = True
                break
        if(com_score==tot_score):
                print('\nIt\'s a Tie')
        else:
            print('\nComputer wins the Game')

startbowling(overs,com_score)