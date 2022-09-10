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

#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0,2)
print(computer_input)
if user_input == 0 and computer_input ==0:
  print("Its a tie")
elif user_input == 0 and computer_input ==1:
  print("you lose, the computer wins")
elif user_input == 0 and computer_input ==2:
  print("computer lost, you won")
elif user_input == 1 and computer_input ==1:
  print("Its a tie")
elif user_input == 1 and computer_input == 2:
  print("you lose, the computer wins")
elif user_input == 1 and computer_input ==0:
  print("computer lost, you won")
elif user_input == 2 and computer_input ==0:
  print("you lose, the computer wins")
elif user_input == 2 and computer_input ==1:
  print("computer lost, you won")
elif user_input == 2 and computer_input ==2:
  print("Its a tie")
else:
  print("its an invalid input")

  
