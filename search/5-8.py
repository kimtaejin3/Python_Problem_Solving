'''
dfs
'''
def dfs_r(graph,v,visited):
  visited[v] = True
  print(v,end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs_r(graph,i,visited)

def dfs(graph,v,visited):
  stack = []
  stack.append(v)

  while stack:
    v = stack.pop()
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        stack.append(i)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9
dfs(graph,1,visited)
