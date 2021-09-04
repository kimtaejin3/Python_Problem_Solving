'''
9/3
2161번: 카드1
https://www.acmicpc.net/problem/2161

n = int(input())

list = [i for i in range(1,n+1)]

while True:
  a = list.pop(0)
  print(a,end=' ')
  if not list:
    break
  b = list.pop(0)
  list.append(b)

'''

'''
17608번: 막대기
https://www.acmicpc.net/problem/17608

내 코드
import sys
input = sys.stdin.readline

n = int(input())
bars = []

for i in range(n):
  bars.append(int(input()))

count = 1

for i in range(len(bars)-2,-1,-1):
  if bars[n-1] < bars[i]:
    count += 1
    bars[n-1] = bars[i]

print(count)

3등 코드
import sys
input()
a=[int(i)for i in sys.stdin][::-1]
top=a[0]
c=1
for i in a[1:]:
    if i>top:c+=1;top=i
print(c)
'''

'''
12605번: 단어순서 뒤집기
'''
n = int(input())

s = []
for i in range(n):
  ss = input()
  ss = ss.split(' ')
  s.append(ss)

for i in s:
  result = ''
  for j in range(len(i)-1,-1,-1):
    result += i[j] + ' '
  print('Case #1: %s' % result)


