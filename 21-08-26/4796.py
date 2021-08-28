'''
4769번: 캠핑 my space 
https://www.acmicpc.net/problem/4796

세부사항 고려 못함 18line
'''

index = 1

while True:

  l,p,v = map(int,input().split())

  if l == 0 and p == 0 and v == 0:
    break
  
  result_v = 0
  result_v = (l*(v//p)) + min(l,v%p)

  
  result = 'Case %d: %d'%(index,result_v)
  index += 1
  print(result)

