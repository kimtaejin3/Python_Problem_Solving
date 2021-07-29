'''
백준 1157번: 단어공부
https://www.acmicpc.net/problem/1157
'''

words = input().lower()
word = list(set(words))
cnt = []

for w in word:
  cnt.append(words.count(w))

max_value = max(cnt)

if cnt.count(max_value) > 1:
  print('?')
else:
  index = cnt.index(max_value)
  print(word[index].upper())


'''
1t: 시간초과 -> 위의 경우는 set을 통해 중복을 없앰.
2t: 특정 중복 문자열 삭제 시도 
3t: 이전 문자열 저장 시도 
4t: 접근 방법이 잘못되었음을 알았음. + 문제를 제대로 보지도 않았음.
'''
