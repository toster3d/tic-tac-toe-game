from art import logo

fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_sheet(fl):
    print(f"""
           |       |
       {fl[0]}   |   {fl[1]}   |   {fl[2]}
    _______|_______|_______
           |       |
       {fl[3]}   |   {fl[4]}   |   {fl[5]}
    _______|_______|_______
           |       |
       {fl[6]}   |   {fl[7]}   |   {fl[8]}
           |       |
    """)


# sprawdza, czy pole nie jest zajęte
def is_square_free(moves, current_move):
    for element in moves:
        if element in current_move:
            return False
    return True


# sprawdza, czy któryś z graczy ułożył trzy znaki w jednym rzędzie lub po skosie
def winner_check(sign, field):
    pass


# sprawdza, czy tablica została zapełniona
def table_full():
    pass


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
        player1_sign = input('Player 1: Choose your sign (O or X) --> ').upper()
        player2_sign = "X" if player1_sign == "O" or player1_sign == "0" else "O"
        print(f"Fantastic!\nPlayer 1: {player1_sign}\nPayer 2: {player2_sign}")
        print_sheet(fields)
        move_counter = 9
        player1_moves = []
        player2_moves = []
        all_moves = []
        while move_counter > 0:
            player1 = int(input("Player 1 (type field number from 1 - 9): ")) - 1
            while not is_square_free(all_moves, [player1]):
                print("Sorry, this field is already taken. Choose again.")
                player1 = int(input("Player 1 (type field number from 1 - 9): ")) - 1
            if is_square_free(all_moves, [player1]):
                fields[player1] = player1_sign
                all_moves.append(player1)
                print_sheet(fields)
                move_counter -= 1
                print(all_moves)

            if move_counter == 0:
                break

            player2 = int(input("Player 2 (type field number from 1 - 9): ")) - 1
            while not is_square_free(all_moves, [player2]):
                print("Sorry, this field is already taken. Choose again.")
                player2 = int(input("Player 2 (type field number from 1 - 9): ")) - 1

            fields[player2] = player2_sign
            all_moves.append(player2)
            print_sheet(fields)
            move_counter -= 1
            print(all_moves)

    elif number_of_players == "1":
        print("Perfect! Let's try yourself with AI!")
        player_square = input('Choose your square (O or X) --> ').upper()


else:
    print("Please, type yes or no.\n")
