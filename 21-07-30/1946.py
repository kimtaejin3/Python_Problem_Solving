'''
1946번: 신입사원
정답비율: 31.794%
https://www.acmicpc.net/problem/1946
'''
import sys

t = int(input())

for _ in range(t):
  n = int(input())
  list = []

  for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    list.append((a,b))
  
  list = sorted(list)
  result = 1
  v = list[0][1]
  for i in range(1,n):
    if list[i][1] < v:
      result += 1
      v = list[i][1]
  print(result)

# 시간초과 


