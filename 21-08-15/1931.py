'''
1931번: 회의실 배정
https://www.acmicpc.net/problem/1931

참고자료
https://source-sc.tistory.com/59

https://it-eldorado.tistory.com/53
'''

n = int(input())
list = []

for _ in range(n):
  list.append(tuple(map(int,input().split())))

list.sort(key = lambda x: (x[1],x[0]))
maxVal = -1

cnt = 1
c = list[0][1]
for i in range(1,n):
  if c <= list[i][0]:
    cnt += 1
    c = list[i][1]

print(cnt)

