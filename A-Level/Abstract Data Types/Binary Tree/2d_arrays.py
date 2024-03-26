#1D array of integers
ids = [14, 22, 56, 19 ,81]

#iterate using index
#for i in range (0,len(ids)):
#    print("id is :", ids[i])

#for id in ids:
#    print("id is :", id)











#2D array is an array where each element is itself an array
grid = [ 101, 201, 301]
print(grid[0])







grids = [ [101,102,103], 201, 301]
#print(grids[0][2])





cells = [ [101,102,103],
          [201,202,203],
          [301,302,303] ]

#print(cells[1][2])




for row in range(3):
    for col in range(3):
        print(cells[row][col])




board = [["x","o","o"],
         ["x","x","o"],
         ["x","x","x"]]



outstring = ""
for row in range (3):
    for col in range (3):
        outstring += board[row][col]
    print(outstring)
    outstring=""


