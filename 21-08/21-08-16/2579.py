n = int(input())

d = [0] * (301)
array = [0] * (301)

for i in range(1,n+1):
  array[i] = int(input())

d[1] = array[1]
d[2] = array[1] + array[2]

for i in range(3,n+1):
  d[i] = max(d[i-3]+array[i-1],d[i-2]) + array[i]

print(d[n])

