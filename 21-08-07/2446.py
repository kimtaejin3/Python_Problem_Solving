n = int(input())

for i in range(1,n+1):
  print(' '*(i-1),end='')
  print('*'* (2*n - (2*(i-1)+1)))

for i in range(2,n+1):
  print(' '*(n-i), end='')
  print('*' * (2*i-1))


