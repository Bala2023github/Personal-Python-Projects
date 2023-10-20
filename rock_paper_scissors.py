import random as rd
import time
import os


def get_input():
    
    try:
        valid_play=['R','P','S']
        your_choice=input("Enter your choice: R for Rock or P for Paper or S for Scissors \n")
        time.sleep(1)

        if your_choice not in valid_play:
            print("Invalid entry for rock, paper or scissors \n")
            time.sleep(1)
        else:
            return your_choice
    except ValueError as err:
        print(err)

def play_game():

    try_again='y'

    while try_again=='y':
       # os.system('cls' if os.name=='nt' else 'clear')
        player_choice=get_input()
        valid_plays=['R','P','S']
        computers_play=rd.choice(valid_plays)
        
        if player_choice==computers_play:

            print("Your choice was",player_choice,"and computer's choice was",computers_play,".Hence, No Winner!")
            time.sleep(1)
            try_again=input("Want to try again? y or n:")
            time.sleep(1)
        
        elif player_choice=='R' and computers_play=='S':
            print("Your choice was",player_choice,"and computer's choice was",computers_play,".Hence, You Win!")
            time.sleep(1)
            try_again=input("Want to try again? y or n:")
            time.sleep(1)
        
        elif player_choice=='P' and computers_play=='R':
            print("Your choice was",player_choice,"and computer's choice was",computers_play,".Hence, You Win!")
            time.sleep(1)
            try_again=input("Want to try again? y or n:")
            time.sleep(1)

        elif player_choice=='S' and computers_play=='P':
            print("Your choice was",player_choice,"and computer's choice was",computers_play,".Hence, You Win!")
            time.sleep(1)
            try_again=input("Want to try again? y or n:")
            time.sleep(1)
        
        else:
            print("Your choice was",player_choice,"and computer's choice was",computers_play,".Hence, Computer Win!")
            time.sleep(1)
            try_again=input("Want to try again? y or n:")
            time.sleep(1)
         

if __name__ == '__main__':
    play_game()