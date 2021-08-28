'''
별 찍기 - 10
https://www.acmicpc.net/problem/2447
n = int(input())
stars = [[' '] * n for _ in range(n)]


def solution(x, y, s):
  if s == 1:
    stars[x][y] = '*'
    return

  d = s//3

  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        continue
      solution(x+i*d,y+j*d,d)


solution(0, 0, n)

# for k in stars:
#   print(''.join(k))
for i in range(n):
  for j in range(n):
    print(stars[i][j],end='')
  print()
'''
a=int(input())
def s(n):
    if n==3:return['***','* *','***']
    x=s(n//3)
    print('x:',x)
    y=list(zip(x,x,x))
    print('before:',y)
    for i in range(len(y)):
        y[i]=''.join(y[i])
    print('after:',y)
    
    z=list(zip(x,[' '*(n//3)]*(n//3),x))
    print(z)
    for i in range(len(z)):
        z[i]=''.join(z[i])
    return y+z+y
print('\n'.join(s(a)))


