n = int(input())

d = [0] * 1001 # 1~ 1000까지이고 index로 접근을 해야 하기에

d[1] = 1
d[2] = 3

for i in range(3,n+1):
  d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])





