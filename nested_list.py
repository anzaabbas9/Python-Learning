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

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}")
position = input("enter position (e.g. 32 = row 3, col 2): ")
row = int(position[0])
column = int(position[1])
grid[row-1][column-1] = 'x'
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}")
