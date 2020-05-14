#! /usr/bin/env python3

# Tic Tac Toe

import random, pyinputplus as pyip

CORNERS = [1, 3, 7, 9]
SIDES = [2, 4, 6, 8]
CENTER = 5

def drawBoard(board: list):
    # Prints out the board that it was passed

    # "Board" is a list of 10 strings representing the board (ignore index 0)

   print('   |   |')
   print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   print('   |   |')


def inputPlayerLetter():
    # Lets the player type which letter they want to be
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.

    letter = ''

    playerPrompt = 'Would like you be to X or O?\n'
    letter = pyip.inputChoice(['X', 'O'], prompt=playerPrompt)

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.

    playAgainPrompt = 'Do you want to play again? (yes/no)\n'
    response = pyip.inputYesNo(prompt=playAgainPrompt)

    return response.startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board

    return board[move] == ' '


def getPlayerMove(board):
    # Let the player type in their move

    movePrompt = 'What is your next move? (1-9)\n'
    
    while True:
        move = pyip.inputNum(prompt=movePrompt, min=1, max=9)
        if isSpaceFree(board, move):
            return move


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move

    possibleMoves = list()
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves):
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine whether to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if we can win the game
    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if player could win on their next move, and block them
    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free
    corner_move = chooseRandomMoveFromList(board, CORNERS)
    if corner_move:
        return corner_move

    # Try to take the center, if it is free
    if isSpaceFree(board, CENTER):
        return CENTER
    
    # Move on one ofthe sides
    return chooseRandomMoveFromList(board, SIDES)


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise, return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10

        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        
        round = 1
        gameIsPlaying = True

        while gameIsPlaying:
            print('Round %s' % (round))
            if turn == 'player':
                # Player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
            round += 1
        if not playAgain():
            break