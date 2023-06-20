from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    num_A=input()
    num_B=input()
    list_A=deque(list(map(int, num_A.split())))
    list_B=deque(list(map(int, num_B.split())))
    result=0

    if N<M:
        for _ in range(M-N):
            list_A.append(0)
        for i in range(M-N+1):
            sum=0
            for i,j in zip(list_A,list_B):
                sum+=i*j
            if sum>result:
                result=sum
            pop=list_A.pop()
            list_A.appendleft(pop)
        print('#{} {}'.format(test_case, result))

    elif N>M:
        for _ in range(N-M):
            list_B.append(0)
        for i in range(N-M+1):
            sum=0
            for i,j in zip(list_A,list_B):
                sum+=i*j
            if sum>result:
                result=sum
            pop=list_B.pop()
            list_B.appendleft(pop)
        print('#{} {}'.format(test_case, result))