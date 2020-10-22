import random


print('Let\'s play Rock, Paper, Scissors')

options = ('rock', 'paper', 'scissors')
def ai_choice():
  rand_choice = random.choice(options)
  return rand_choice

my_score = 0
AI_score = 0

pick = ()
while pick != 'exit':
  print('Choose "r" for rock, "p" for paper, or "s" for scissors')
  pick = input('What is your choice? ')
  if pick == 'r':
    x = ai_choice()
    if x == 'rock':
      print('Tie, you both had rock, play again!')
    elif x == 'paper':
      print('AI had paper, you lose!')
      AI_score += 1
    else:
      print('Rock beats scissors, you win!')
      my_score += 1
  elif pick == 'p':
    x = ai_choice()
    if x == 'paper':
      print('Tie, you both had paper, play again!')
    elif x == 'scissors':
      print('AI had scissors, you lose!')
      AI_score += 1
    else:
      print('Paper beats rock, you win!')
      my_score += 1
  elif pick == 's':
    x = ai_choice()
    if x == 'scissors':
      print('Tie, you both had scissors, play again!')
    elif x == 'rock':
      print('AI had rock, you lose!')
      AI_score += 1
    else:
      print('Scissors beats paper, you win!')
      my_score += 1
  elif pick == 'exit':
    continue
  else:
    print('Please pick one of the available options.')

print(f'The final score was: Player One {my_score} Computer {AI_score}. Thanks for playing!')



