'''
Workflow of the game:
 
Case A - Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

Case B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

Case C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
'''

import random

items = ["Rock", "Paper", "Scissor"]
while True:
   user_choice = input("Enter your choice = Rock, Paper, Scissor = ")
   computer_choice = random.choice(items)
   print(f"You choose = {user_choice}, Computer choose = {computer_choice}")

   if user_choice == computer_choice:
    print("Both chooses the same, Match tied")

   elif user_choice == "Rock":
    print("Paper coves Rock, Paper win")

   elif user_choice == "Rock":
    print("Rock beats Scissor, Rock win")

   elif user_choice == "Paper":
    print("Paper covers Rock, Paper win")

   elif user_choice == "Paper":
    print("Scissor cuts Paper, Scissor win")

   elif user_choice == "Scissor":
    print("Rock beats Scissor, Rock win")

   elif user_choice == "Scissor":
    print("Scissor cuts Paper, Scissor win")
    break

user_end = input("To quit the game enter - end : ")
if user_end == "end":
  print("The game ended..")
    



        
    


        

    















