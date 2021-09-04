'''
15881번 Pen Pineapple Apple Pen ms -y
https://www.acmicpc.net/problem/15881
'''

n = int(input())
s = input()

target = 'pPAp'
cnt = 0

i = 0
while i<n:
  if i+4 <= n:
    sub_s = s[i:i+4]
    if sub_s == target:
      i = i+4
      cnt+=1
      continue
  i += 1

print(cnt)

