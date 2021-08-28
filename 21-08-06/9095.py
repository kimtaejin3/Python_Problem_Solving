'''
9095번: 1,2,3 더하기 / 62%
https://www.acmicpc.net/problem/9095
분류: 다이나믹 프로그래밍

기타: 백트래킹으로 풀음.
'''

def backTracking(_sum,n):
  global case
  if _sum == n:
    case+=1
    return
  elif _sum > n:
    return
  else:
    for i in range(1,4):
      backTracking(_sum+i,n)

t = int(input())
for _ in range(t):
  case=0
  n = int(input())
  backTracking(0,n)
  print(case)

