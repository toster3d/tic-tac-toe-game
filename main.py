import random
from art import logo

FIELDS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
WINNING_COMBINATIONS = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
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


def opponent_sign(sign):
    """Automatically chooses the opposite sign for your opponent"""
    return "X" if sign == "O" or sign == "0" else "O"


# sprawdza, czy pole nie jest zajęte
def is_square_free(moves, current_move):
    """Checks if the current field is free, returns true or false"""
    for element in moves:
        if element in current_move:
            return False
    return True


def winner_check(sign, field):
    """Checks whether it is possible to determine a winner after making a move, returns true or false"""
    for combination in WINNING_COMBINATIONS:
        are_equal = True
        for i in combination:
            if field[i] != sign:
                are_equal = False
                break
        if are_equal:
            return True
    return False


def table_full(table):
    """Checks whether there are any empty squares left on the board"""
    return " " not in table


def check_input(player, nickname):
    """Checks the correctness of the field number entered by the user"""
    possible_input = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if player in possible_input:
        return int(player) - 1
    else:
        print("Please, type a number from 1 to 9")
        new_player = input(f"{nickname} (type field number from 1 - 9): ")
        return check_input(new_player, nickname)


def get_empty_squares(board):
    """Checks which fields on the board are empty."""
    empty_fields = [i for i in range(9) if board[i] == " "]
    return empty_fields


def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm for Tic Tac Toe."""

    scores = {"X": 1, "O": -1, "Tie": 0}

    if winner_check("X", board):
        return scores["X"]
    if winner_check("O", board):
        return scores["O"]
    if table_full(board):
        return scores["Tie"]

    empty_squares = get_empty_squares(board)

    if is_maximizing:
        max_eval = float("-inf")
        for square in empty_squares:
            board[square] = "X"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[square] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for square in empty_squares:
            board[square] = "O"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[square] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def best_move(board):
    """Checks the best AI move"""
    max_eval = float("-inf")
    best_square = None
    for square in get_empty_squares(board):
        board[square] = "X"
        eval = minimax(board, 0, False, float("-inf"), float("inf"))
        board[square] = " "
        if eval > max_eval:
            max_eval = eval
            best_square = square
    return best_square


def sign_check(player_sign, nickname):
    """Checks the correctness of the character entered by the user"""
    possible_inputs = ['X', 'x', 'o', 'O', '0']
    if player_sign in possible_inputs:
        return player_sign.upper()
    else:
        print("Please, type X, x, o, O, or 0")
        new_player_sign = input(f'{nickname}: Choose your sign (O or X) --> ')
        return sign_check(new_player_sign, nickname)


def one_player_game():
    print("Perfect! Let's try yourself with AI!")
    player_name = input("Player: Type your nickname: ")
    player_sign = "O"
    ai_name = "AI"
    ai_sign = "X"
    print(f"Fantastic!\n{player_name}: {player_sign}\n{ai_name}: {ai_sign}\nThis is a board schema:\n")
    print_sheet(FIELDS)
    move_counter = 9
    all_moves = []
    chart = [" "] * 9

    current_player = random.choice([player_sign, ai_sign])

    while move_counter > 0:
        if current_player == player_sign:
            player_input = input(f"{player_name} (type field number from 1 - 9): ")
            player = check_input(player_input, player_name)
            while not is_square_free(all_moves, [player]):
                print("Sorry, this field is already taken. Choose again.")
                player_input = input(f"{player_name} (type field number from 1 - 9): ")
                player = check_input(player_input, player_name)
            chart[player] = player_sign
            all_moves.append(player)
            print_sheet(chart)
            player_is_winner = winner_check(current_player, chart)
            if player_is_winner:
                print(f"{player_name} is the WINNER!")
                break
            move_counter -= 1
        else:
            print("AI's turn:")
            ai_move = best_move(chart)
            chart[ai_move] = ai_sign
            all_moves.append(ai_move)
            print_sheet(chart)
            ai_is_winner = winner_check(ai_sign, chart)
            if ai_is_winner:
                print(f"{ai_name} is the WINNER!")
                break
            move_counter -= 1

        if move_counter == 0:
            print("It's a TIE!")
            break

        current_player = player_sign if current_player == ai_sign else ai_sign


def two_players_game(chart):
    print("Great! Let's get started!")
    player1_name = input("Player 1: Type your nickname: ")
    player2_name = input("Player 2: Type your nickname: ")
    player1_sign_input = input(f'{player1_name}: Choose your sign (O or X) --> ').upper()
    player1_sign = sign_check(player1_sign_input, player1_name)
    player2_sign = opponent_sign(player1_sign)
    print(f"Fantastic!\n{player1_name}: {player1_sign}\n{player2_name}: {player2_sign}\nThis is a board schema:\n")
    print_sheet(FIELDS)
    move_counter = 9
    all_moves = []

    current_player = random.choice([player1_sign, player2_sign])

    while move_counter >= 0:
        if current_player == player1_sign:
            player_input = input(f"{player1_name} (type field number from 1 - 9): ")
            player = check_input(player_input, player1_name)
        else:
            player_input = input(f"{player2_name} (type field number from 1 - 9): ")
            player = check_input(player_input, player2_name)

        while not is_square_free(all_moves, [player]):
            print("Sorry, this field is already taken. Choose again.")
            if current_player == player1_sign:
                player_input = input(f"{player1_name} (type field number from 1 - 9): ")
            else:
                player_input = input(f"{player2_name} (type field number from 1 - 9): ")
            player = check_input(player_input, player2_name)

        if is_square_free(all_moves, [player]):
            chart[player] = current_player
            all_moves.append(player)
            print_sheet(chart)
            player_is_winner = winner_check(current_player, chart)
            if player_is_winner:
                print(f"{current_player} is the WINNER!")
                break
            move_counter -= 1

        if move_counter == 0:
            print("It's a TIE!")
            break

        current_player = player1_sign if current_player == player2_sign else player2_sign


print(logo)
print("This is a TIC TAC TOE Game!")
game_on = True
table = [' '] * 9
while game_on:
    wanna_play = input("Do you want to play? Type 'yes' or 'no'.\n").upper()
    table = [' '] * 9
    if wanna_play == "NO":
        print("Goodbye.")
        game_on = False
    elif wanna_play == "YES":
        number_of_players = input("Do you want to play with AI or with your friend?\nType number of players (1 or 2)\n")
        if number_of_players == "2":
            two_players_game(table)
        elif number_of_players == "1":
            one_player_game()
        else:
            print("Please, type a number 1 or 2. ")
    else:
        print("Please, type yes or no.\n")
