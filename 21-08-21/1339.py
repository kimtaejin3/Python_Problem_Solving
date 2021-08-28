'''
단어수학* 공부 많이 됨
https://www.acmicpc.net/problem/1339
'''

n = int(input())
s = []
alphabet = [0 for _ in range(26)]

for i in range(n):
  s.append(input())

for s_element in s:
  for i in range(len(s_element)-1,-1,-1):
    alphabet[ord(s_element[i])-ord('A')] += pow(10,len(s_element)-i-1)

alphabet.sort(reverse=True)

result = 0

for i in range(9):
  result += alphabet[i] * (9-i)

print(result)


