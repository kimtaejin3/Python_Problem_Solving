n = int(input())
direction = {'R':(0,1),'U':(-1,0),'L':(0,-1),'D':(1,0)}

current_positon = (1,1)

input_direction = input().split()

for i in range(len(input_direction)):
  x,y = current_positon
  if x + direction[input_direction[i]][0] > 0 and x + direction[input_direction[i]][0] < n:
    x = x + direction[input_direction[i]][0]
  if y + direction[input_direction[i]][0] > 0 and y + direction[input_direction[i]][0] < n:
    y = y + direction[input_direction[i]][1]
  current_positon = (x,y)


print(current_positon)

