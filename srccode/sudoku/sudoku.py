import sys, getopt

try:

    input = sys.argv[1]

except IndexError:
    print("Oops!  You didn't enter the puzzle's values!")
    sys.exit()

def board_creation(values):
    length = len(values)
    if length != 81:
        print("Invalid number of values entered!! I need 81 values not %d :(" % length)
        sys.exit()
    board = []
    row = []
    for i in values:
        row.append(int(i))
        if len(row) == 9:
            #print(row)
            board.append(row)
            row = []
    return board

board = board_creation(input)
#print(board)

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True



print("\n_________Puzzle__________\n")
print_board(board)
solve(board)
print("\n________Solution_________\n")
print_board(board)