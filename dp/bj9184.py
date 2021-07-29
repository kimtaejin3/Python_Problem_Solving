dp = {}

def w(a,b,c):
  if a > 20 or b > 20 or c >20:
    return w(20,20,20)
  if a<=0 or b<=0 or c<=0:
    return 1
  if (a,b,c) in dp:
    return dp[(a,b,c)]
  if a < b < c:
    dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)  
    return dp[(a,b,c)]
    
  dp[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return dp[(a,b,c)]

while True:
  a,b,c  = map(int,input().split())
  if a == -1 and b == -1 and c == -1:
    break
  print("w(%d, %d, %d) = %d"%(a, b, c, w(a, b, c)))


  
 
# r = w(50,50,50)
# print(r)


# 딕셔너리 & 리스트 연습
# a = {(1,2,3):3}

# a[(2,3,4)]=[1,2]
# a[(2,3,4)].append(7)

# print(a[(1,2,3)])
# print((1,2,3) in a)
# print(3 in a)
# print(a)
# b = {}
# b['t'] = []
# print(b)