'''
2839번: 설탕배달
https://www.acmicpc.net/problem/2839
'''

n = int(input())
cnt = 0
INF = int(1e9)

d = [INF] * (n+1)
d[0] = 0
array = [3,5]

for i in range(2):
  for j in range(array[i],n+1):
    d[j] = min(d[j],d[j-array[i]]+1)

if d[n] == INF:
  print('-1')
else:
  print(d[n])
'''
좋은 풀이법
하지만 직관적으로 푸는 것은 어떨까?

n = int(input())

cnt = 0

while n > 0:
  if n % 5 == 0:
    cnt += (n//5)
    break
  n -= 3
  cnt += 1

if n < 0:
  print(-1)
else:
  print(cnt)

'''

'''
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
'''




