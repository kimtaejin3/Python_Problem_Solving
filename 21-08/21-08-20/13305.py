'''
주유소
https://www.acmicpc.net/problem/13305
'''

n = int(input())
road = list(map(int,input().split()))
cities = list(map(int,input().split()))

sum = 0

sum += cities[0] * road[0]
minV = cities[0]

for i in range(1,n-1):
  minV = min(minV,cities[i])
  sum += minV * road[i]

print(sum)

