'''
1912번: 연속합 ms
https://www.acmicpc.net/problem/1912
'''
n = int(input())

arr = list(map(int,input().split()))
d = [0] * n


for i in range(n):
  d[i] = arr[i]

for i in range(1,n):
  d[i] = max(d[i], d[i-1] + arr[i])

print(max(d))


