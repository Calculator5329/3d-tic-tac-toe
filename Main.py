import random


# This function takes the current board and returns the "bot's" move
def calculateMove(arr):
    # Options for the bot to play
    options = []

    # Go through all board spaces and if the value is 0 (has not been played on), add the index to the options list
    for valIndex, val in enumerate(arr):
        if val == 0:
            options.append(valIndex)

    # Return a random move from options
    return options[random.randint(0, len(options) - 1)]


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

    # Indexes that contain value (or in other words, spots that have been played)
    containsVals = []

    # Initialize output as false
    out = False

    for index, i in enumerate(arr):
        if i == val:
            containsVals.append(index)

    # Check horizontal wins
    for initialSpot in [0, 3, 6]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 1) and containsVals.__contains__(initialSpot + 2):
                out = True

    # Check horizontal wins
    for initialSpot in [0, 1, 2]:
        if containsVals.__contains__(initialSpot):
            if containsVals.__contains__(initialSpot + 3) and containsVals.__contains__(initialSpot + 6):
                out = True

    # Check Diagonal wins
    initialSpot = 0
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 4) and containsVals.__contains__(initialSpot + 8):
            out = True
    initialSpot = 2
    if containsVals.__contains__(initialSpot):
        if containsVals.__contains__(initialSpot + 2) and containsVals.__contains__(initialSpot + 4):
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
          0, 0, 0]

stringMatrix = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-", ]

run = True
userVal = 0

gotInput = False

# Intro message
print("")
print("Welcome to my tic tac toe game!")
print("To play, you will be asked to enter a value that corresponds to the spot on the board you would like to play.")
print("Here is an example layout of the board with the values at the corresponding spots:")
print("")
print(" 1 2 3")
print(" 4 5 6")
print(" 7 8 9")
print("")

while run:

    userVal = input("Enter a value to play: ")

    gotInput = False

    # While we have not gotten a correctly formatted input
    while not gotInput:
        # Try to convert to an integer
        try:
            userVal = int(userVal) - 1

            # Check if the input is a valid integer between 1 and 9
            if 0 <= userVal <= 8:
                gotInput = True
            else:
                userVal = input("Error, please enter an integer between 1 and 9: ")

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
        if checkBoard(matrix, 2):
            print("You have lost. Better luck next time!")
            exitProgram()

        # If neither won, the game ends in a tie
        print("This game ended in a draw. Better luck next time!")
        exitProgram()

    # The computer plays a move
    matrix[calculateMove(matrix)] = 2

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
        print(str(stringMatrix[row * 3]) + " " + str(stringMatrix[row * 3 + 1]) + " " + str(stringMatrix[row * 3 + 2]))

    # Check if the player won
    if checkBoard(matrix, 1):
        print("Congratulations! You have won!")
        exitProgram()

    # Check if the computer won
    if checkBoard(matrix, 2):
        print("You have lost. Better luck next time!")
        exitProgram()
