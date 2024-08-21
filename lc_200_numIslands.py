from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #深搜
        def dfs(x_coor, y_coor):
            for i in range(4):
                x, y = x_coor + dir[i][0], y_coor + dir[i][1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if visited[x][y] == 0 and grid[x][y] == "1":
                        visited[x][y] = 1
                        dfs(x, y)
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        #方向：上，右，左，下
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    visited[i][j] = 1
                    island_count += 1
                    dfs(i, j)
        return island_count
        #广搜
        def bfs(x_coor, y_coor):
            queue = deque()
            queue.append([x_coor, y_coor])
            visited[x_coor][y_coor] = True
            while queue:
                [x1, y1] = queue.popleft()
                for i in range(4):
                    x = x1 + dir[i][0]
                    y = y1 + dir[i][1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if visited[x][y] == False and grid[x][y] == "1":
                            visited[x][y] = True
                            queue.append([x, y])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] == "1":
                    bfs(i, j)
                    island_count += 1
        return island_count
