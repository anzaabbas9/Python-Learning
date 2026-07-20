#listname[index:length of list:step u wanna jump]  ->list slicing

"""list=[0,4,6,["ali","hadi","reham"],90,-60]
print(len(list))
print(list[3][0])
print(list[len(list)-3][0])"""

"""list=[[1,2,3],[4,5,6],[7,8,9]]
print(f"{list[0]}\n{list[1]}\n{list[2]}")
position=input("please enter a position (first digit represent row n second one represent column)").split(" ")
print(position)
print({list[int(position[0])-1][int(position[1])-1]} )
idx=list[int(position[0])-1][int(position[1])-1]='x'
print({list[int(position[0])-1][int(position[1])-1]} )"""

"""grid = [[1,2,3],[4,5,6],[7,8,9]]
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}")
position = input("enter position (e.g. 32 = row 3, col 2): ")
row = int(position[0])
column = int(position[1])
grid[row-1][column-1] = 'x'
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}")"""

"""
Question 7 (Nested List) — Sum of All Elements
Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], use nested loops to add up 
every number and print the total."""
"""matrix=[[1,2,3],[4,5,6],[7,8,9]]
total=0
for i in matrix:
    for j in i:
        total+=j
        print(j)
print(total)"""

"""
Question 8 (Nested List) — Print Row and Column Position
Loop through the same matrix above using nested loops and print each element along with its row 
and column index, like:Row 0, Col 0: 1 / Row 0, Col 1: 2"""
"""matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"row {i} , column{j} ->{matrix[i][j]}")"""
"""
Bonus — Search a Grid Using Nested Loops + break
Create a 3x3 nested list (like your tic-tac-toe grid). Using nested loops with range(), search for 
a specific value (e.g., 5) inside it. Use break to stop searching as soon as it's found, and
 print its row and column position."""
matrix=[[1,2,6],[4,5,6],[7,8,9]]
target=6
found=False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j]==target):
            print(f"its found\n row{i},column{j}->{matrix[i][j]}")
            found=True
            break
    if found:
        break
print("out of loop")
            


