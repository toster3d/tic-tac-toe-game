from art import sheet, logo


def player_sign(player_choice):
    if player_choice == "O" or player_choice == "0":
        player2_sign = "X"
        return player2_sign
    elif player_choice == "X":
        player2_sign = "O"
        return player2_sign
    else:
        print("Please, type only X or O")


print(logo)
print("This is a TIC TAC TOE Game!")
wanna_play = input("Do you want to play? Type 'yes' or 'no'.\n").upper()

game_on = True
if wanna_play == "NO":
    print("Goodbye.")
    game_on = False
elif wanna_play == "YES":
    number_of_players = input("Do you want to play with AI or with your friend?\nType number of players (1 or 2)\n")
    if number_of_players == "2":
        print("Great! Let's get started!")
        player1_square = input('Player 1: Choose your square (O or X) --> ').upper()
        player2_square = player_sign(player1_square)
        print(f"Fantastic!\nPlayer 1: {player1_square}\nPayer 2: {player2_square}")
    elif number_of_players == "1":
        print("Perfect! Let's try yourself with AI!")
        player_square = input('Choose your square (O or X) --> ').upper()


else:
    print("Please, type yes or no.\n")

