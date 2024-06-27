#----------------------------------------#
#Sudoku Puzzle
#----------------------------------------#
board = [
    [5,0,0,0,0,8,0,0,3],
    [8,3,0,9,4,6,0,0,7],
    [0,7,2,1,3,0,9,0,0],
    [1,0,7,6,9,0,0,3,2],
    [0,0,0,8,0,2,0,0,0],
    [0,8,0,3,5,0,0,9,6],
    [4,0,5,0,0,9,0,7,8],
    [0,0,0,0,0,1,0,2,0],
    [0,2,0,4,7,0,5,0,0]
]

def solve(bo):#part-4; we are going to call it recursively 
    #print(bo) #just to check how things are progressing
    #below 5 lines are our base case of recursion
    find = find_empty(bo)
    if not find: 
        return True # if no empty values are found then our sudoku is completed
    else: 
        row,col = find #else we get the pos tuple with row and col values
    
    #below is the code we actually try inserting a number into the sudoku, if its valid, we proceed with next empty value, if 
    #not we reset the value to 0 and try another 'i' value recursively.
    for i in range(1,10):
        if is_valid(board, i, (row,col)):
            bo[row][col]=i
            
            if solve(bo): #recursively calling solve function on new board after filling above i value in row,col position successfully.
                return True
            
            bo[row][col]= 0 #in case if previously tried i [from 1-9] is already existing, continue the loop with other value
    return False #in case if the sudoku is unable to be solved. this is pretty much else case for previous if, just we didnt 
                # write else case statement since the above if will terminate if success, else automatically come here


def is_valid(bo, num, pos):#part-3
    #check row
    for i in range(len(bo[0])): #we are looping through every single column in each row, we just took 1st row from the board, 
        #it could be any row
        if bo[pos[0]][i] == num and pos[1] != i: #here pos is a tuple (i,j); '0' stands for row in that tuple (i,j)
            #essentially we are passing through all the columns in the given row of tuple pos[0]  has any other position as the given num, 
            #apart from the actual position j, which pos[1] of the tuple.
            return False #this means the num we inserted is present in the same row apart from the pos[1]
    
    #check column
    for i in range(len(bo)): #we are looping through every row
        if bo[i][pos[1]] == num and pos[0] != i: #here we are checking in every row (referred by i) and the second value of tuple 
            #pos[1] and not in the given tuple; that means entire column is scanned for the number except the one we inserted
            return False
    
    box_x = pos[1] //3 # here pos[1] is representing column
    box_y = pos[0] //3 # here pos[0] is representing row 
    #so total sudoku 9 smaller boxes are denoted as below
    #[0,0] | [0,1] | [0,2]
    #---------------------
    #[1,0] | [1,1] | [1,2]
    #---------------------
    #[2,0] | [2,1] | [2,2]
    #now with the above info, we know which small box we are in; so we are going to search for that small box and ensure we 
    #dont have any other number with our num
    for i in range(box_y*3, box_y*3+3): # here we traversing column position as i; multiplying by 3 will give actual position
        #of the smaller box
        for j in range(box_x*3, box_x*3+3): #here we are traversing row position as j
            if bo[i][j] == num and (i,j) != pos: #here we are checking for same num anywhere else in small box apart from our pos
                return False 
    return True        
            
def find_empty(bo):#part-2
    for i in range(len(bo)):
        for j in range(len(bo[i])):
                       if bo[i][j] == 0:
                           return (i,j) #row, col
    return False

def print_board(bo):#part-1
    for i in range(len(bo)):
        if i%3 ==0 and i != 0:
            print('-----------------------')
        for j in range(len(bo[i])):
            if j%3 == 0 and j != 0:
                print( ' | ', end ="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]), end = " ")

print_board(board)
solve(board)
print("___________________")
print_board(board)
#----------------------------------------#
