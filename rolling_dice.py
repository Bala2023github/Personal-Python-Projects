import random as rd
import os


def get_input():
    
    try:
        valid_dice_count=['1','2']
        no_of_dice=input("Enter the number of dice: 1 or 2 \n")

        if no_of_dice not in valid_dice_count:
            print("Invalid entry for number of dice prompt \n")
        else:
            return no_of_dice
    except ValueError as err:
        print(err)

def roll_dice():

    try_again='y'

    while try_again=='y':
        os.system('cls' if os.name=='nt' else 'clear')
        dice_count=get_input()

        if dice_count=='1':

            print("Rolled dice produced:",rd.randint(1,6))
            try_again=input("Want to try again? y or n:")
                

        elif dice_count=='2':
            print("Rolled dice 1 produced:",rd.randint(1,6))
            print("Rolled dice 2 produced:",rd.randint(1,6))
            try_again=input("Want to try again? y or n:")
   

if __name__ == '__main__':
    roll_dice()