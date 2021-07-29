array = [7,5,9,0,3,1,6,2,4,8]

'''
while문 풀이

for i in range(1,len(array)-1):
  j = i
  while j>=0 and array[j-1] > array[j]:
    array[j],array[j-1] = array[j-1],array[j]
    j-=1
'''

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else:
      break



print(array)


