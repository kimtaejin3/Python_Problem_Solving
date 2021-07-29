import heapq

INF = int(1e9)

n,m = map(int,input().split())
distance_k = [INF] * (n+1)
distance_x = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))


x,k = map(int,input().split())

def dijkstra(start,distance):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(1,distance_k)
dijkstra(k,distance_x)

if distance_k[k] == INF or distance_x[x] == INF:
  print('-1')
else:
  print(distance_k[k]+distance_x[x])




