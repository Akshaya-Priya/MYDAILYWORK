# TIC-TAC-TOE AI

# Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like

# Minimax with or without Alpha-Beta Pruning to make the AI
# player unbeatable. This project will help you understand
# game theory and basic search algorithm 

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 10)

def is_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

board = [[' ' for _ in range(3)] for _ in range(3)]

print("\n\t\t\t\tTic-Tac-Toe")
print("You are 'X' player and AI is 'O' player \n")
while True:
    print_board(board)
    x, y = map(int, input("Enter your move (row and column): ").split())
    x=x-1
    y=y-1
    if board[x][y] == ' ':
        board[x][y] = 'X'
        if is_winner(board, 'X'):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
    else:
        print("Invalid move, try again.")
