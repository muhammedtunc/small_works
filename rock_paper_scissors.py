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
import random
rps = [rock, paper, scissors]
computer_chose = random.choice(rps)
player = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))

if rps.index(computer_chose) == 0 and player == 2:
  print(f"{scissors}\nComputer chose:\n{rock}\nYou lose")
elif rps.index(computer_chose) == 2 and player == 0:
  print(f"{rock}\nComputer chose:\n{scissors}\nYou win")
else:
  if rps.index(computer_chose) < player:
    print(f"{rps[player]}\nComputer chose:\n{rps[rps.index(computer_chose)]}\nYou win")
  elif rps.index(computer_chose) == player:
    print(f"{rps[player]}\nComputer chose:\n{rps[rps.index(computer_chose)]}\nDraw") 
