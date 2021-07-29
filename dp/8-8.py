n,m = map(int,input().split())
visit=[0]*(n+1)


def f(s,depth):
  if depth == m:
    print(s)
    return
  else:
    for i in range(1,n+1):
      if visit[i] == 0:
        visit[i] = 1
        f(s+str(i)+' ',depth+1)
        visit[i] = 0

f('',0)
