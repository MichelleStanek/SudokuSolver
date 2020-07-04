board = [
    [9, 0, 8, 0, 4, 2, 0, 7, 0],
    [4, 7, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 9, 0, 4, 0],
    [3, 0, 7, 0, 0, 0, 2, 0, 9],
    [0, 2, 0, 4, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 5, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 1, 6],
    [0, 6, 0, 1, 9, 0, 5, 0, 7],
]

# Backtracking Algorithm

def solve(sudoku):
    found = find_blank(sudoku)
    if not found:
        return True
    else:
        row, col = found

    posVals = possible_values(sudoku, found)
    for val in posVals:
        if valid(sudoku, val, (row, col)):
            sudoku[row][col] = val

            if solve(sudoku):
                return True

            sudoku[row][col] = 0

    return False


def possible_values(sudoku, pos):
    already_used_row = []
    already_used_col = []
    already_used_quad = []

    for r in range(len(sudoku)):
        if sudoku[pos[0]][r] != 0:
            already_used_row.append(sudoku[pos[0]][r])

    for c in range(len(sudoku[0])):
        if sudoku[c][pos[1]] != 0:
            already_used_col.append(sudoku[c][pos[1]])

    quad_x = pos[1] // 3
    quad_y = pos[0] // 3

    for r in range(quad_y * 3, quad_y * 3 + 3):
        for c in range(quad_x * 3, quad_x * 3 + 3):
            if sudoku[r][c] != 0:
                already_used_quad.append(sudoku[r][c])

    usedValues = mergeList(already_used_col, already_used_row, already_used_quad)
    posValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for val in usedValues:
        posValues.remove(val)

    return(posValues)


def mergeList(list1, list2, list3):
    for val in list2:
        list1.append(val)
    for val in list3:
        list1.append(val)
    return (list(dict.fromkeys(list1)))


def valid(sudoku, num, pos):
    # Check column
    for r in range(len(sudoku)):
        if sudoku[r][pos[1]] == num and pos[0] != r:
            return False

    # Check row
    for c in range(len(sudoku[0])):
        if sudoku[pos[0]][c] == num and pos[1] != c:
            return False

    # Check box
    quad_x = pos[1] // 3
    quad_y = pos[0] // 3

    for r in range(quad_y * 3, quad_y * 3 + 3):
        for c in range(quad_x * 3, quad_x * 3 + 3):
            if sudoku[r][c] == num and (r, c) != pos:
                return False

    return True


def print_board(sudoku):
    for r in range(len(sudoku)):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - - ")

        for c in range(len(sudoku[0])):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")

            if c == 8:
                print(sudoku[r][c])
            else:
                print(str(sudoku[r][c]) + " ", end="")


def find_blank(sudoku):
    for r in range(len(sudoku)):
        for c in range(len(sudoku[0])):
            if sudoku[r][c] == 0:
                return (r, c)  # row, col

    return False


solve(board)
print_board(board)
