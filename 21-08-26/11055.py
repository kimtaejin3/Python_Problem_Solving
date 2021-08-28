'''
11055번: 가장 큰 증가 부분 수열
https://www.acmicpc.net/problem/11055
'''
import copy

n = int(input())
a = list(map(int,input().split()))

# d[0]=0x
d = copy.deepcopy(a)
# d = a 안됨

for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+a[i])

print(max(d))
