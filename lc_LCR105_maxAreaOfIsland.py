from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #深搜
        def dfs(x_coor, y_coor):
            area = 1
            for i in range(4):
                x = x_coor + dir[i][0]
                y = y_coor + dir[i][1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if not visited[x][y] and grid[x][y] == 1:
                        visited[x][y] = True
                        area += dfs(x, y)
            return area
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    res = max(res, dfs(i, j))
        return res
        #广搜
        def bfs(x_coor, y_coor):
            queue = deque()
            queue.append([x_coor, y_coor])
            visited[x_coor][y_coor] = True
            nonlocal count
            while queue:
                coor_x, coor_y = queue.popleft()
                for i in range(4):
                    x, y = coor_x + dir[i][0], coor_y + dir[i][1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if not visited[x][y] and grid[x][y] == 1:
                            count += 1
                            queue.append([x,y])
                            visited[x][y] = True
            return count
        dir = [[1,0], [-1,0], [0, 1], [0, -1]]
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    count = 1
                    visited[i][j] = True
                    res = max(res, bfs(i, j))
        return res
