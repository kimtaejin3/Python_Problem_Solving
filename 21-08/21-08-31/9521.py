'''
LCS  's not my space 장기기억 전환 연습필요
**중요**
https://www.acmicpc.net/problem/9251
'''
a = input()
b = input()


d = [[0]*(len(a)+1) for _ in range(len(b)+1)]

'''
set up
'''
for i in range(1,len(b)+1):
  for j in range(1,len(a)+1):
    if a[j-1] == b[i-1]:
      d[i][j] = d[i-1][j-1] + 1
    else:
      d[i][j] = max(d[i-1][j],d[i][j-1])


for i in d:
  print(i)
