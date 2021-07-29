n = int(input())

list = []

for i in range(n):
  name,score = input().split()
  print(name,score)
  score = int(score)
  list.append((name,score))

sorted(list, key=lambda x:x[1])
print(list)
