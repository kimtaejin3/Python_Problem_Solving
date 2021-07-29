'''
이진탐색의 경우 데이터의 크기가 커서 입력 받는 것만으로 시간초과 될 수 있다.
해결법은 sys의 readline()를 사용하는 것이다.
'''

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
