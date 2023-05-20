T=int(input())

for test_case in range(1, T + 1):
    num=list(map(int, input().split()))
    if num[0]<num[1]:
        print('#{} <'.format(test_case))
    elif num[0]==num[1]:
        print('#{} ='.format(test_case))
    else:
        print('#{} >'.format(test_case))