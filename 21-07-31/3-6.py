'''
이코테 99page: 1이 될 때까지 ver2
1씩 빼는 while문을 없앰.
'''

n,k = map(int,input().split())
cnt = 0

while n>1:
  if n%k!=0:
    cnt += (n%k)    
  n //= k
  cnt+=1
  
  

print(cnt)