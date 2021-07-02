d0 = [0]*41
d1 = [0]*41

d0[0] = 1
d1[1] = 1


for i in range(2,41):
  d0[i],d1[i] = d0[i-1]+d0[i-2],d1[i-1]+d1[i-2]

t = int(input())
s = ''

for i in range(t):
  n = int(input())
  s += str(d0[n])+' '+str(d1[n])+'\n'

print(s)
