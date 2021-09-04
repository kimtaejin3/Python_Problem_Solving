'''
카트정렬하기 my space - little hard
https://www.acmicpc.net/problem/1715

핵심은 작은 카드부터 더해야 한다는 것 - 그리디
'''
import heapq

n = int(input())
q = []


for i in range(n):
  heapq.heappush(q,int(input()))

result = 0

#조건: 마지막 남은 원소(필요x) 처리
while len(q) > 1:
  
  first = heapq.heappop(q)
  second = heapq.heappop(q)
  
  result += first + second
  
  heapq.heappush(q,(first+second))

print(result)




