def dfs(graph,v,visited):
  stack = []
  stack.append(v)
  visited[v] = True

  while stack:
    p = stack.pop()
    print(p,end=' ')
    for i in graph[p]:
      if not visited[i]:
        stack.append(i)
        visited[p] = True # 중요

def dfs_r(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs_r(graph,i,visited)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*9

dfs(graph,1,visited)
visited = [False]*9
print()
dfs_r(graph,1,visited)
# dfs, bfs의 차이는 위에서 없음 (로직차이)
