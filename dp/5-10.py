n,m = map(int,input().split())

graph = []
count = 0

# 그래프 구성하기
for i in range(n):
  graph.append(list(map(int,input())))

# dfs 함수 만들기
def dfs(x,y):
  if x<0 or x>n-1 or y<0 or y>m-1:
    return
  if graph[x][y] == 1:
    return
  else:
    graph[x][y] = 1
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x+1,y)


# for문 구성
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      count+=1
      dfs(i,j)


# 결과 출력
print(count)

