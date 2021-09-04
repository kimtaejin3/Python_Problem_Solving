'''
18352번: 특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352
28%
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append((b,1))

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q,(0,start))

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(x)

count = 0
index = 0
for d in distance:
  if d == k:
    count += 1
    print(index)
  index += 1

if count == 0:
  print('-1')




