n,m = list(map(int,input().split()))
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start+end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
  
print(result)

answer = 0
def height_of_cutter(start,end,array):
  global answer
  if start>end:
    return
  mid = (start+end)//2
  total = 0
  for x in array:
    if x>mid:
      total += x-mid
  if total < m:
    height_of_cutter(start,mid-1,array)
  else:
    answer = mid
    height_of_cutter(mid+1,end,array)
   
height_of_cutter(0,max(array),array)
print(answer)
