import random

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

game_images=[rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice= int(input("What's your choice:"))
if user_choice >= 3 and user_choice<0:
  print("Invalid Input")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("Computer choice is \n")
  print(game_images[computer_choice])
  
  
  
  if computer_choice==2 and user_choice==0:
    print("You Win!")
  elif computer_choice==0 and user_choice==2:
    print("Computer Wins!")
  elif computer_choice > user_choice:
    print("Computer Wins!")
  elif computer_choice < user_choice:
    print("You Win!")
  elif computer_choice == user_choice:
    print("It's a Draw")
  
    