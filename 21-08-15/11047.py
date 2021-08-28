'''
11047번 동전0
https://www.acmicpc.net/problem/11047
'''

n,k = map(int,input().split())
coins = []

for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
for coin in coins:
  cnt += k//coin
  k%=coin

print(cnt)

