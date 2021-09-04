'''
전자레인지
https://www.acmicpc.net/problem/10162
'''
times = [300,60,10]
times_count = [0] * 4
n = int(input())


for time in times:
  times_count[times.index(time)] += n//time
  n = n%time

if n == 0:
  print('%d %d %d'%(times_count[0],times_count[1],times_count[2]))
else:
  print(-1)


