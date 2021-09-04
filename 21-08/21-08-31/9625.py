'''
BABBA
https://www.acmicpc.net/problem/9625
k = int(input())
a = [0] * (k+1)
b = [0] * (k+1)

a[0] = 1
b[1] = 1

for i in range(2,k+1):
  a[i] = a[i-1] + a[i-2]
  b[i] = b[i-1] + b[i-2]

print(a[k],b[k])
'''

'''
13301번: 타일 장식물
https://www.acmicpc.net/problem/13301

규칙성 -> 보텀업
'''

n = int(input())
d = [0] * (81)
d[1] = 4
d[2] = 6

for i in range(3,81):
  d[i] = d[i-1] + d[i-2]

print(d[n])

