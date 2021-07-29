
# n, m = map(int, input().split())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, input())))


# def dfs(x, y, result):
#     # 길을 벗어났다면
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False

#     # 출구에 도달했다면
#     if x == n - 1 and y == m - 1:
#         result_list.append(result)
#         # return True

#     # 뚫린 길이고 방문하지 않은 길이라면
#     if graph[x][y] == 1:
#         graph[x][y] = result
#         dfs(x + 1, y, result + 1)  # 상
#         dfs(x - 1, y, result + 1)  # 하
#         dfs(x, y - 1, result + 1)  # 좌
#         dfs(x, y + 1, result + 1)  # 우

#     # # 막힌 길이라면
#     # return False

# result = 1
# result_list = []
# dfs(0, 0, result)
# # 출구까지 가는 경로가 여러 개라면 그중 최단 거리 반환
# print(min(result_list))
# for i in range(n):
#   print(graph[i])

from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny <0 or nx >= n or ny >=m:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx,ny))

  return graph[n-1][m-1]

print(bfs(0,0))       

print('-그래프-')

for i in range(n):
  for j in range(len(graph[i])):
    print(graph[i][j],end=' ')
  print()


