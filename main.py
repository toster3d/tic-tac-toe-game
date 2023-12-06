from art import logo

FIELDS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
WINNING_COMBINATIONS = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                        {0, 3, 6}, {1, 4, 7}, {2, 6, 8},
                        {0, 4, 8}, {2, 4, 6}]


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


def winner_check(sign, field):
    for combination in WINNING_COMBINATIONS:
        are_equal = True
        for i in combination:
            if field[i] != sign:
                are_equal = False
                break
        if are_equal:
            return True
    return False


# sprawdza, czy tablica została zapełniona
def table_full(table):
    return " " not in table


def check_input(player):
    possible_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if player in possible_input:
        return int(player) - 1
    else:
        print("Please, type a number from 1 to 9")
        new_player = input("Player 1 (type field number from 1 - 9): ")
        return check_input(new_player)


def two_players_game(table):
    print("Great! Let's get started!")
    player1_name = (input("Player 1: Type your nickname: "))
    player2_name = (input("Player 2: Type your nickname: "))
    player1_sign = input(f'{player1_name}: Choose your sign (O or X) --> ').upper()
    player2_sign = "X" if player1_sign == "O" or player1_sign == "0" else "O"
    print(f"Fantastic!\n{player1_name}: {player1_sign}\n{player2_name}: {player2_sign}\nThis is a board schema:\n")
    print_sheet(FIELDS)
    move_counter = 9
    all_moves = []
    while move_counter >= 0:
        player1_input = input(f"{player1_name} (type field number from 1 - 9): ")
        player1 = check_input(player1_input)
        while not is_square_free(all_moves, [player1]):
            print("Sorry, this field is already taken. Choose again.")
            player1_input = input(f"{player1_name} (type field number from 1 - 9): ")
            player1 = check_input(player1_input)
        if is_square_free(all_moves, [player1]):
            table[player1] = player1_sign
            all_moves.append(player1)
            print_sheet(table)
            player1_is_winner = winner_check(player1_sign, table)
            if player1_is_winner:
                print(f"{player1_name} is the WINNER!")
                break
            move_counter -= 1
        if move_counter == 0:
            break
        player2_input = input(f"{player2_name} (type field number from 1 - 9): ")
        player2 = check_input(player2_input)
        while not is_square_free(all_moves, [player2]):
            print("Sorry, this field is already taken. Choose again.")
            player2_input = input(f"{player2_name} (type field number from 1 - 9): ")
            player2 = check_input(player2_input)
        table[player2] = player2_sign
        all_moves.append(player2)
        print_sheet(table)
        player2_is_winner = winner_check(player2_sign, table)
        if player2_is_winner:
            print(f"{player2_name} is the WINNER!")
            break
        move_counter -= 1
    if move_counter == 0 and not winner_check(player1_sign, table) and not winner_check(player2_sign, table):
        print("It's a TIE!")


print(logo)
print("This is a TIC TAC TOE Game!")
game_on = True
board = [' '] * 9
while game_on:
    wanna_play = input("Do you want to play? Type 'yes' or 'no'.\n").upper()
    board = [' '] * 9
    if wanna_play == "NO":
        print("Goodbye.")
        game_on = False
    elif wanna_play == "YES":
        number_of_players = input("Do you want to play with AI or with your friend?\nType number of players (1 or 2)\n")
        if number_of_players == "2":
            two_players_game(board)
        elif number_of_players == "1":
            print("Perfect! Let's try yourself with AI!")
            player_square = input('Choose your square (O or X) --> ').upper()
            # TODO: Zrobić program dla AI
        else:
            print("Please, type a number 1 or 2. ")
    else:
        print("Please, type yes or no.\n")
