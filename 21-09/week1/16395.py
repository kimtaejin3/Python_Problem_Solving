'''
9/2
16395번 파스칼의 삼각형
https://www.acmicpc.net/problem/16395
'''

n,k = map(int,input().split())

paskal = [[0]*30 for i in range(30)]

for i in range(30):
  for j in range(30):
    if j==0 or j==i:
      paskal[i][j] = 1
    else:
      paskal[i][j] = paskal[i-1][j-1] + paskal[i-1][j]

print(paskal[n-1][k-1])
