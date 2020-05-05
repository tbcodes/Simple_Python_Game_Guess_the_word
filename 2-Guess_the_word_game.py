# Guess the Word - Python Game - Truzz Blogg
# Youtube link: https://youtu.be/2kVb0_EJgn4

import random
import sys

players = 'Cristiano, Hazard, Messi, VanDijk, Neymar, Salah, Dybala, Mbappe, Kane, Mane, Benzema, Kroos, Aguero, Ozil, Oblak, Coutinho, Modric, DeBruyne'
players = players.split(',')
final_players = []
for x in players:
    players = x.strip()
    final_players.append(players)

score = 0

def guessThePlayer():
    global score
    print('### Python Football/Soccer Game - Guess the name of the player ###')
    print("List of players...You have to guess the name of a random player!")
    print(final_players)

    random_final_players = random.choice(final_players).casefold()
    # print("El valor de random player es: ", random_final_players)
    print(random_final_players[0].capitalize() + '-' * (len(random_final_players) - 2) + random_final_players[-1])
    if random_final_players in ['messi', 'cristiano']:
        print("Hint: D10s or Almost D10s")
    user_input = str(input('Guess the name of the player: ')).casefold()
    if user_input == random_final_players:
        score += 1
        print("Score:", score)
        guessThePlayer()
    else:
        print('Upppss! Wrong answer! The correct answer is: {}'.format(random_final_players))
        print('Your final score is: {}'.format(str(score)))
        play_again = str(input("Would you like to try again?")).lower()
        if play_again in ['yes', 'y']:
            score = 0
            guessThePlayer()
        else:
            sys.exit("Bye Bye!!!")


guessThePlayer()