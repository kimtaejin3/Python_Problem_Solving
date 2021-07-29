'''
dfs와 bfs
https://www.acmicpc.net/problem/1260
'''
from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 만들기(인접리스트 방식)
for i in range(m):
  v1,v2 = map(int,input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

def dfs(v,visited,graph):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(i,visited,graph)

def bfs(node):
  visited[node] = True
  queue = deque()
  queue.append(node)
  while queue:
    popped = queue.popleft()
    print(popped,end=' ')
    for i in graph[popped]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

print('====dfs결과====')
dfs(v,visited,graph) #굳이 매개변수 안넘겨도 되긴함.
print()

visited = [False] * (n+1)

print('====bfs결과====')
bfs(v) #굳이 매개변수 안넘김.
print()

  



