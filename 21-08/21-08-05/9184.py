'''
9184 신나는 함수실행
42%
https://www.acmicpc.net/problem/9184
'''
n = 51
d = [[[0]*n for _ in range(n)] for i in range(n)]
def w(a,b,c):
  if a<=0 or b<=0 or c<=0:
    return 1
  if a>20 or b>20 or c>20:
    return w(20,20,20)
  # 여기에다 이 문장을 두는 이유: a,b,c에 음수가 들어오면 파이썬은 맨 끝부터 인덱싱함..
  if d[a][b][c] > 0:
    return d[a][b][c]
  if a<b<c:
    d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    return d[a][b][c]
  
  d[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
  return d[a][b][c]

while True:
  a,b,c = map(int,input().split())
  if a == -1 and b == -1 and c==-1:
    break
  result_val = w(a,b,c)
  print('w(%d, %d, %d) = %d' % (a,b,c,result_val))

