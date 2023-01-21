import random


# This function takes an array (the tic tac toe board) and a value
# It then returns any indexes that are adjacent to the value and contain the value 0
def adjacentZeroes(arr, val):
    out = []
    adjToZero = []

    # We are given an array of length 9, and need to find adjacent 0s to val
    for index, arrVal in enumerate(arr):
        if arrVal == 0:

            # We will check the 8 surrounding values to see if they are vals or if they even exist
            # The 8 values can be represented: [index - 1 - 3, index - 3, index + 1 - 3, index - 1, index + 1,
            #                                   index - 1 + 3, index + 3, index -3 + 1]
            # We want to make sure this code could potentially used for higher dimension boards, so we will use the
            # "-3 + 1" type of format instead of just checking all of the values between index - 4 and index + 4

            # Set the dimension to 3
            dimension = 3

            # Adjacent indexes
            adjIndexes = [index - 1 - dimension, index - dimension, index + 1 - dimension, index - 1, index + 1,
                          index - 1 + dimension, index + dimension, index - dimension + 1]

            for adjIndex in adjIndexes:
                try:
                    if arr[adjIndex] == val and not out.__contains__(index):
                        out.append(index)
                except IndexError:
                    continue

    return out


# This function takes the current board and returns the "bot's" move
def calculateMove(arr, unlocked):
    # Options for the bot to play
    options = []
    exampleMatrix = arr
    output = -1

    # Go through all board spaces and if the value is 0 (has not been played on), add the index to the options list
    for valIndex, val in enumerate(arr):
        if val == 0:
            options.append(valIndex)

    # Check if any moves can result in a win
    for option in options:

        exampleMatrix[option] = 2

        if checkBoard(exampleMatrix, 2):
            output = option
            exampleMatrix[option] = 0
            break

        exampleMatrix[option] = 0

    # Check if any moves that the player makes will result in a win for the player
    for option in options:

        exampleMatrix[option] = 1

        if checkBoard(exampleMatrix, 1):
            output = option
            exampleMatrix[option] = 0
            break

        exampleMatrix[option] = 0

    if output >= 0:
        if unlocked or not output == 13:
            return output

    # If there are no moves that either block the player from a win or win the game for the computer,
    # Play something adjacent to the previous move (if there has been a move)
    if arr.__contains__(2):
        adjacentVals = adjacentZeroes(arr, 2)
        output = adjacentVals[random.randint(0, len(adjacentVals) - 1)]
        while output == 13:
            output = adjacentVals[random.randint(0, len(adjacentVals) - 1)]
        return output

    # Return a random move from options
    output = options[random.randint(0, len(options) - 1)]
    while output == 13:
        output = options[random.randint(0, len(options) - 1)]
    return output


# This function checks the board for any "3 in a row" wins and returns true if it finds any
def checkBoard(arr, val):
    # Possible wins:
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8
    # 0, 3, 6
    # 1, 4, 7
    # 2, 5, 8
    # 0, 4, 8
    # 2, 4, 6

    # Possible 3D Board wins:
    # The normal wins, the normal wins + 9, the normal wins + 18
    # The through-board wins

    # Indexes that contain value (or in other words, spots that have been played)
    containsVals = []

    # Initialize output as false
    out = False

    for index, i in enumerate(arr):
        if i == val:
            containsVals.append(index)

    # Check horizontal wins
    for initialSpot in [0, 3, 6, 9, 12, 15, 18, 21, 24]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 1) and containsVals.__contains__(initialSpot + 2):
                out = True

    # Check vertical wins
    for initialSpot in [0, 1, 2, 9, 10, 11, 18, 19, 20]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 3) and containsVals.__contains__(initialSpot + 6):
                out = True

    # Check Diagonal wins
    for initialSpot in [0, 9, 18]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 4) and containsVals.__contains__(initialSpot + 8):
                out = True
    for initialSpot in [2, 11, 20]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 2) and containsVals.__contains__(initialSpot + 4):
                out = True

    # Check "through-board" wins

    # "Through-board" possible combinations are :
    """""
    Vertical
    0, 9, 18 
    Corner Adjs 
    0, 10, 20 (right) +10
    0, 12, 24 (down) + 12
    Corner Diags
    0, 13, 16 (diag right down) +13
    
    Vertical
    2, 11, 20
    Corner Adjs 
    2, 10, 18 (left) +8
    2, 14, 26 (down) +12
    Corner Diags
    2, 13, 24 (diag left down) +11
    
    
    Vertical
    6, 15, 24 
    Corner Adjs 
    6, 12, 18 (up) +6
    6, 16, 26 (right) +10
    Corner Diags
    6, 13, 20 (diag right up) +7
    
    
    Vertical
    8, 17, 26
    Corner Adjs 
    8, 14, 20 (up) +6
    8, 16, 24 (left) +8
    Corner Diags
    8, 13, 18 (diag left up) + 5
    
    
    Edges:
    1, 13, 25 (down) + 12
    3, 13, 23 (right) + 10
    5, 13, 21 (left) + 8
    7, 13, 19 (up) +6
    """
    # Check up and down combinations
    for initialSpot in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 9) and containsVals.__contains__(initialSpot + 18):
                out = True

    # Check right-facing "through-board" combinations (+10)
    for initialSpot in [0, 3, 6]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 10) and containsVals.__contains__(initialSpot + 20):
                out = True

    # Check left-facing "through-board" combinations (+8)
    for initialSpot in [2, 5, 8]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 8) and containsVals.__contains__(initialSpot + 16):
                out = True

    # Check down-facing "through-board" combinations (+12)
    for initialSpot in [0, 1, 2]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 12) and containsVals.__contains__(initialSpot + 24):
                out = True

    # Check up-facing "through-board" combinations (+6)
    for initialSpot in [6, 7, 8]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 6) and containsVals.__contains__(initialSpot + 12):
                out = True

    # Check diagonal "through-board" combinations (various)

    initialSpot = 0
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 13) and containsVals.__contains__(initialSpot + 26):
            out = True

    initialSpot = 2
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 11) and containsVals.__contains__(initialSpot + 22):
            out = True

    initialSpot = 6
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 7) and containsVals.__contains__(initialSpot + 14):
            out = True

    initialSpot = 8
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 5) and containsVals.__contains__(initialSpot + 10):
            out = True

    return out


# This function offers to play again, then restarts or exits the program
def exitProgram():
    global run
    global matrix
    answer = input("Would you like to play again? (Y/N): ").upper()
    if answer == "Y":
        run = True
        matrix = [0, 0, 0,
                  0, 0, 0,
                  0, 0, 0]
    else:
        exit()


matrix = [0, 0, 0,
          0, 0, 0,
          0, 0, 0,

          0, 0, 0,
          0, 0, 0,
          0, 0, 0,

          0, 0, 0,
          0, 0, 0,
          0, 0, 0]

stringMatrix = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-",

                "-", "-", "-",
                "-", "-", "-",
                "-", "-", "-",

                "-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

run = True
userVal = 0

gotInput = False

middleUnlocked = False

# Intro message
print("")
print("Welcome to my 3D tic tac toe game!")
print("To play, you will be asked to enter a value that corresponds to the spot on the board you would like to play.")
print("14 represents the very middle of the board, and is therefore the most powerful spot. Because of this, 14 may\n"
      "not be played until it is 'unlocked.' To unlock the center spot, play any spot other than 14 on the middle board"
      ".")
print("")
print("Here is an example layout of the board with the values at the corresponding spots:")
print("")
print("  Bottom   Middle      Top ")
print("| 1 2 3 | 10 11 12 | 19 20 21 |")
print("| 4 5 6 | 13 14 15 | 22 23 24 |")
print("| 7 8 9 | 16 17 18 | 25 26 27 |")
print("")

while run:

    userVal = input("Enter a value to play: ")

    # Check if the middle is unlocked
    for i in range(8):
        if matrix[i + 10] != 0:
            middleUnlocked = True

    gotInput = False

    # While we have not gotten a correctly formatted input
    while not gotInput:
        # Try to convert to an integer
        try:
            userVal = int(userVal) - 1

            # Check if the input is a valid integer between 1 and 27
            if 0 <= userVal <= 26:
                if not middleUnlocked and userVal == 13:
                    gotInput = False
                    userVal = input("The middle has not been unlocked, please play a different spot: ")
                else:
                    gotInput = True
            else:
                userVal = input("Error, please enter an integer between 1 and 27: ")

        # If input cannot be converted to integer, output an error
        except ValueError or TypeError:
            userVal = input("Error, please enter a valid integer: ")

        # Check if the spot has been played on
        if gotInput and matrix[userVal] != 0:
            userVal = input("Error, please select a spot that has not been played on: ")
            gotInput = False

    # If there is no more open spots
    if not matrix.__contains__(0):
        # Check if the player won
        if checkBoard(matrix, 1):
            print("Congratulations! You have won!")
            exitProgram()

        # Check if the computer won
        if checkBoard(matrix, 2):
            print("You have lost. Better luck next time!")
            exitProgram()

        # If neither won, the game ends in a tie
        print("This game ended in a draw. Better luck next time!")
        exitProgram()

    # Play the users move
    matrix[userVal] = 1

    # If there is no more open spots
    if not matrix.__contains__(0):
        # Check if the player won
        if checkBoard(matrix, 1):
            print("Congratulations! You have won!")
            exitProgram()

        # Check if the computer won
        elif checkBoard(matrix, 2):
            print("You have lost. Better luck next time!")
            exitProgram()

        # If neither won, the game ends in a tie
        else:
            print("This game ended in a draw. Better luck next time!")
            exitProgram()

    # The computer plays a move
    pcMove = calculateMove(matrix, middleUnlocked)
    matrix[pcMove] = 2
    print("The computer played move: " + str(pcMove))

    # Update string matrix
    for index, i in enumerate(matrix):
        if i == 0:
            stringMatrix[index] = "-"
        if i == 1:
            stringMatrix[index] = "X"
        if i == 2:
            stringMatrix[index] = "O"

    print("Current board: ")

    for row in range(3):
        print(str(stringMatrix[row * 3]) + " " + str(stringMatrix[row * 3 + 1]) + " " + str(stringMatrix[row * 3 + 2]) +
              "  " + str(stringMatrix[row * 3 + 9]) + " " + str(stringMatrix[row * 3 + 1 + 9]) +
              " " + str(stringMatrix[row * 3 + 2 + 9]) +
              "  " + str(stringMatrix[row * 3 + 18]) + " " + str(stringMatrix[row * 3 + 1 + 18]) +
              " " + str(stringMatrix[row * 3 + 2 + 18]))

    # Check if the player won
    if checkBoard(matrix, 1):
        print("Congratulations! You have won!")
        exitProgram()

    # Check if the computer won
    if checkBoard(matrix, 2):
        print("You have lost. Better luck next time!")
        exitProgram()
