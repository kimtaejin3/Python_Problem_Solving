'''
수들의 합
https://www.acmicpc.net/problem/1789
최적해: 제일 작은 수 부터 차례대로
더해나가면 된다.
'''

s = int(input())

x = 1
cnt = 0
while True:
  if x > s:
    break
  s-=x
  x+=1
  cnt += 1

print(cnt)

