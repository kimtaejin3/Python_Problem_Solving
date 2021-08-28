'''
미로탐색
https://www.acmicpc.net/problem/2178
'''
from collections import deque

n,m = map(int,input().split())

maze = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  maze.append(list(map(int,input())))

def solve():
  q = deque()
  q.append((0,0))

  while q:
    x,y = q.popleft()
    for i in range(4):
      nx,ny = x + dx[i], y + dy[i]
      if nx<0 or nx>n-1 or ny<0 or ny>m-1:
        continue
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        q.append((nx,ny))

solve()
print(maze[n-1][m-1])

