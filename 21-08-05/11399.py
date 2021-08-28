'''
ATM/66
https://www.acmicpc.net/problem/11399
'''
n = int(input())

# 아래와 같이 쓰는 것은 상관없음 다만, print(list()) 와 같은 형식으로는 출력x is not callable error
list = list(map(int,input().split()))
list = sorted(list)


# for i in range(n):
#   sum_list = 0
#   for j in range(i+1):
#     sum_list += list[j]
#   result.append(sum_list)

for i in range(1,n):
  list[i] += list[i-1]
print(sum(list))
