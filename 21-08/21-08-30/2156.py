'''
2156번: 포도주 시식 ms **공부많이 됨
https://www.acmicpc.net/problem/2156

기타사항
2579 계단오르기 

참고자료
https://www.acmicpc.net/board/view/60664
'''
n = int(input())
d = [0] * (10001)
array = [0] *(10001)

for i in range(1,n+1):
  array[i] = int(input())

d[1] = array[1]
d[2] = array[1]+array[2]

for i in range(3,n+1):
  d[i] = max(array[i-1]+d[i-3] + array[i],d[i-2] + array[i],d[i-1])

print(max(d))
