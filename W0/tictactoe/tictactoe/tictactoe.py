"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.

    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    X always goes first
    Count how many X's and O's are on the board.
    If equal, it's X's turn.
    """

    XnbTurn = sum(row.count(X) for row in board)
    YnbTurn = sum(row.count(O) for row in board)
    
    return X if XnbTurn == YnbTurn else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    scan each cell, If the cell is EMPTY, it's a legal move
    the return value should be a set of tuples
    """
    movePossible = set()

    for i in range(3):  
        for j in range(3):
            if board[i][j] == EMPTY:
                movePossible.add((i, j))

    return movePossible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    It should not modify the original board, it must return a new copy.
    if the action is invalid raise an exception.
    
    """

    i, j = action

    if board[i][j] is not EMPTY:
        raise Exception("Impossible move.")
    
    boardCopy = [row.copy() for row in board]
    boardCopy[i][j] = player(board)

    return boardCopy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    return X or O in fucntion of who won or None if nobody won
    """
    #iterate through line to check if all elems are identical
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
        
    #iterate collumns to check if all elems are identical
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]
            and board[0][col] is not EMPTY):

            return board[0][col]

    #iterate through the 2 diagonals to check if elems are identical
    if (board[0][0] == board[1][1] == board[2][2]
            and board[0][0] is not EMPTY):

            return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0]
            and board[0][2] is not EMPTY):

            return board[0][2]
    
    return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    Game is done if someone won or board is full
    """ 
    
  
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    Should only be called if the game is over.
    """

    XOwinner = winner(board)

    if XOwinner == X:
        return 1
    elif XOwinner == O:
        return -1
    else:
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current = player(board)

    if current == X:
        value = -math.inf
        best_move = None
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > value:
                value = move_val
                best_move = action
        return best_move

    else:  # current == O
        value = math.inf
        best_move = None
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < value:
                value = move_val
                best_move = action
        return best_move
    

    raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v