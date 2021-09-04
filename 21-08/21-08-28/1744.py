'''
1744번 수 묶기 ms -n
https://www.acmicpc.net/problem/1744
'''
import heapq

n = int(input())
q = []
for i in range(n):
  heapq.heappush(q,-int(input()))

sum = 0
while q:
  if len(q) == 1:
    sum += heapq.heappop(q)*(-1)
    break
  
  x = heapq.heappop(q)*(-1)
  y = heapq.heappop(q)*(-1)
  
  if (x==0 and y <0) or (x<0 and y==0):
    sum+=x*y
  elif (x==0 and y >0) or (x>0 and y==0):
    sum+=x+y
  elif (x==1) or (y==1):
    sum+=x+y
  elif x>0 and y>0:
    sum += x*y
  elif x<0 and y<0:
    sum += x*y
  elif (x<0 and y>0) or (x>0 and y<0):
    sum += x+y


print(sum)

