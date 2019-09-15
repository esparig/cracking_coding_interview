"""Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
- DFS is chosen, easy to implement. 
BFS finds the shortest path, but in this case the length of the path is fixed.
- Args:
    n: num of rows
    m: num of cols
    i: current row of the robot
    j: current col of the robot
- Return:
    moves: stores the moves of the robot ("R" for right moves, "D" for down moves)
"""
GRID = [[1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1], 
        [1, 0, 1, 1, 1, 1]]

def robot_path(n: int, m: int, i: int, j: int):
    if i == n-1 and j == m-1:
        return ""
    if i+1<n and GRID[i+1][j] > 0:
        moves = robot_path(n, m, i+1, j)
        if moves is not None:
            return "D" + moves
    if j+1<m and GRID[i][j+1] > 0:
        moves = robot_path(n, m, i, j+1)
        if moves is not None:
            return "R" + moves


print(robot_path(4, 6, 0, 0))