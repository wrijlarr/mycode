#!/usr/bin/python3
""" wrijlarr | larry.wright@tlgcohort.com

Lab 48: Mini Project #1: IF-LOGIC SCRIPT

Rock Paper Scissors"""

import random
#RPS (Rock, Paper, Scissors)

def main():
    
    #define game options
    options = ["rock", "paper", "scissors"]
    
    #human chooses preference
    human_choice = input(" Enter your selection (rock, paper, scissors): ")

    #define computer chooses random options

    computer_choice = random.choice(options)
    
    #create if, elif, else logic for the game
    
    if human_choice == computer_choice:
        print("Choices are the same! It's a tie!")
    
    ## example 1
    elif human_choice == "rock" and computer_choice == "paper":
            print("Paper beats rock. You lose.")

    elif human_choice == "rock" and computer_choice == "scissors":
            print("Rock beats scissors. You Win!")

    ## example 2
    elif human_choice == "paper" and computer_choice == "rock":
            print("Paper beats rock. You Win!")

    elif human_choice == "paper" and computer_choice == "scissors":
            print("Scissors beat paper. You Lose.")

    # functionally this is the same as "example 1" and "example 2"
    elif human_choice == "scissors":
        if computer_choice == "rock":
            print("Rock beats scissors. You lose.")
        elif computer_choice == "paper":
            print("Scissors beat paper. You Win!")

if __name__ == "__main__":
    main()




