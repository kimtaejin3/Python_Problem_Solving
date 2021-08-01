'''
n과 m
https://www.acmicpc.net/problem/15649
'''

n,m = map(int,input().split())
visited = [False] * (n+1)

def dfs(s,depth):
  if depth == m:
    print(s)
    return
  else:
    for i in range(1,n+1):
      if not visited[i]:
        visited[i] = True
        dfs(s+str(i)+' ',depth+1)
        visited[i] = False

dfs('',0)  


