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
print(hand_gesture[user_choice])

# Generate the computer's choice
computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(hand_gesture[computer_choice])

if user_choice == computer_choice:
    print("It is a tie.") 

if (user_choice == 0) and (computer_choice == 2):
    print("You win.")
elif (user_choice == 2) and (computer_choice == 1):
    print("You win.")
elif (user_choice == 1) and (computer_choice == 0):
    print("You win.")
else:
    print("You lose.")