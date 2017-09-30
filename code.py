correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(puzzle):
    grid = len(puzzle)   #Extract size of grid
    digit = 1       #Set digit to 1
    while digit <= grid:  #Go through each digit
        i = 0      
        while i < grid:     #Go through each column and row
            row_count = 0
            col_count = 0
            j = 0
            while j < grid:   # For each digit in row/column
                if puzzle[i][j] == digit: #Check row count
                    row_count += 1
                if puzzle[j][i] == digit: #Check column count
                    col_count += 1
                j += 1
            if row_count != 1 or col_count != 1:
                    return False
            i += 1   #Next row/col in grid
        digit += 1   #Next digit in puzzle
    return True
                
    




    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
