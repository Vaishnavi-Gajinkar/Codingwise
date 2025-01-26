import random

#possible choices
choices = ['Rock','Paper','Scissor']

#player input
player_choice = input('Enter your Choice Rock/Paper/Scissor = ')

comp_choice = random.choice(choices)

if player_choice == comp_choice:
    print('Math tie')

elif player_choice == 'Rock':
    if comp_choice == 'Paper':
        print('Computer won! Paper covers Rock')
    else:
        print('You won! Rock smashes scissor!')

elif player_choice == 'Paper':
    if comp_choice == 'Rock':
        print('You won! Paper covers Rock')
    else:
        print('Computer won! Scissor cuts paper')

elif player_choice == 'Scissor':
    if comp_choice == 'Rock':
        print('Computer won! Rock smashes scissor')
    else:
        print('You won! Scissor cuts paper')

else:
    print('In-valid option')