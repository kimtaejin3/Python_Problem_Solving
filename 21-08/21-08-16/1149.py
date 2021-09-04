'''
RGB 거리
https://www.acmicpc.net/problem/1149
'''
import copy

n = int(input())

array = []
for i in range(n):
  array.append(list(map(int,input().split())))

d = [[2000]*3 for _ in range(n)]
d[0] = copy.deepcopy(array[0])

for i in range(1,n):
  for j in range(3):
    for k in range(3):
      if j!=k:
        d[i][j] = min(d[i][j],array[i][j] + d[i-1][k])

print(min(d[n-1]))

  