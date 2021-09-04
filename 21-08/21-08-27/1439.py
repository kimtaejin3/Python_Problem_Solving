'''
1439번: 뒤집기 ms
https://www.acmicpc.net/problem/1439
'''
def count_x(list,x):
  continuous = False
  cnt = 0
  for i in range(len(list)):
    if list[i] == x:
      if continuous == False:
        cnt += 1
        continuous = True
    else:
      continuous =  False
  return cnt


s = list(map(int,input()))
print(min(count_x(s,0),count_x(s,1)))
