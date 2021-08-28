'''
1541번: 잃어버린 괄호
https://www.acmicpc.net/problem/1541
'''

s = input()
arr = s.split('-')

result = 0

b = arr[0].split('+')
b = list(map(int,b))
result += sum(b)

for i in range(1,len(arr)):
  b = arr[i].split('+')
  b = list(map(int,b))
  result -= sum(b)

print(result)

