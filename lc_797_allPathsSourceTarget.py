
def dfs(v, path):
    if v == vertex:
        res.append(path[:])
        return
    for ver in graph[v]:
        #邻接表
        path.append(ver)
        dfs(ver, path)
        path.pop()
        
if __name__ == "__main__":
    #邻接表
    vertex, edge = map(int, input().split())
    graph = {i : [] for i in range(1, vertex+1)}
    for _ in range(edge):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    # print(graph)
    #邻接矩阵
    # vertex, edge = map(int, input().split())
    # graph = [[0] * vertex+1 for _ in range(vertex+1)]
    # for _ in range(edge):
    #     v1, v2 = map(int, input().split())
    #     graph[v1][v2] = 1
    
    res = []
    dfs(1, [1])
    for path in res:
        print(" ".join(map(str, path)))
