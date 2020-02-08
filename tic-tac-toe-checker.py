def isSolved(board):
    for row in board:
        if row == [1, 1, 1]:
            return 1
        if row == [2, 2, 2]:
            return 2
    
    for j in range(3):
        column = []
        for row in board:
            column.append(row[j])
        if column == [1, 1, 1]:
            return 1
        if column == [2, 2, 2]:
            return 2
    
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    
    if diagonal1 == [1, 1, 1] or diagonal2 == [1, 1, 1]:
        return 1
    if diagonal1 == [2, 2, 2] or diagonal2 == [2, 2, 2]:
        return 2
    
    for row in board:
        if 0 in row:
            return -1
    
    return 0
