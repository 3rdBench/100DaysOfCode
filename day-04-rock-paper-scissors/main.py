rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# 3 Simple Rules (https://www.wrpsa.com/the-official-rules-of-rock-paper-scissors/):
# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

# Save choices to a list
hand_gesture = [rock, paper, scissors]

# Display how to play the game & get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Generate the computer's choice
computer_choice = random.randint(0,2)

# Check for incorrect user input
if (user_choice >= 3) or (user_choice < 0):
    print("You typed an invalid number, you lose!")
# Rock wins against Scissors    
elif (user_choice == 0) and (computer_choice == 2):
    print(hand_gesture[user_choice])
    print("Computer chose:")
    print(hand_gesture[computer_choice])
    print("You win")
# Scissors wins against Paper   
elif (user_choice == 2) and (computer_choice == 1):
    print(hand_gesture[user_choice])
    print("Computer chose:")
    print(hand_gesture[computer_choice])
    print("You win")
# Paper wins against Rock    
elif (user_choice == 1) and (computer_choice == 0):
    print(hand_gesture[user_choice])
    print("Computer chose:")
    print(hand_gesture[computer_choice])
    print("You win")
# Draw    
elif user_choice == computer_choice:
    print(hand_gesture[user_choice])
    print("Computer chose:")
    print(hand_gesture[computer_choice])    
    print("It is a draw.")
# User loses    
else:
    print(hand_gesture[user_choice])
    print("Computer chose:")
    print(hand_gesture[computer_choice])    
    print("You lose")
