from collections import deque

n,m = map(int,input().split())


graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  graph.append(list(map(int,input())))

def bfs(graph,start):
  
  queue = deque([start])
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx,ny = x + dx[i], y + dy[i]
      if nx<0 or nx>n-1 or ny<0 or ny>m-1:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] += graph[x][y]
        queue.append((nx,ny))


start = (0,0)
bfs(graph,start)
print(graph[n-1][m-1])

print()
print('==그래프==')
print()

for i in range(n):
  for j in range(m):
    print(graph[i][j],end=' ')
  print()
  
