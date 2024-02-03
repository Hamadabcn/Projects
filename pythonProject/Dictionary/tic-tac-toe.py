def print_board(board):
    # Print the Tic-Tac-Toe board
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')


def check_winner(board):
    # Check for a winner by examining rows, columns, and diagonals
    winning_conditions = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],
        ['7', '5', '3'], ['1', '5', '9'],
        ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3']
    ]

    # Iterate through winning conditions
    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True  # Found a winner

    return False  # No winner


def is_board_full(board):
    # Check if the board is full (no empty spaces)
    return all(value != ' ' for value in board.values())


def get_player_move(turn, board):
    # Get the player's move
    while True:
        print(f"It's your turn {turn}, choose an empty space? ")
        move = input()

        # Validate the move input
        if move.isdigit() and 1 <= int(move) <= 9 and board.get(move, None) == ' ':
            return move  # Valid move
        else:
            print('Invalid move. Please enter a number between 1 and 9 or choose an empty space.')


def play_again():
    # Ask the user if they want to play again
    print("Do you want to play again? (yes/no)")
    return input().lower().startswith('y')


def game():
    while True:
        # Initialize the game board
        the_board = {'7': ' ', '8': ' ', '9': ' ',
                     '4': ' ', '5': ' ', '6': ' ',
                     '1': ' ', '2': ' ', '3': ' '}
        turn = 'X'

        for _ in range(9):
            # Display the current state of the board
            print_board(the_board)
            # Get the player's move
            move = get_player_move(turn, the_board)
            # Update the board with the player's move
            the_board[move] = turn

            # Check for a winner or a tie
            if check_winner(the_board):
                print_board(the_board)
                print(f'\nGame Over\n**** {turn} Won 👍 ****')
                break

            if is_board_full(the_board):
                print('\nGame Over\nGame is a Tie 👊🏼\n')
                break

            # Switch turns between 'X' and 'O'
            turn = 'O' if turn == 'X' else 'X'

        if not play_again():
            break


if __name__ == "__main__":
    game()
