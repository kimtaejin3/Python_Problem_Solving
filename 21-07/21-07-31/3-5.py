'''
이코테 99page: 1이 될 때까지 ver1
'''

n,k = map(int,input().split())
cnt = 0

cnt += n%k
n = n//k
  
  

print(cnt)


