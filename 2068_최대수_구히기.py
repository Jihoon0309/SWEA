T = int(input())

for i in range(1,T+1):
    num=list(map(int, input().split()))
    print('#{} {}'.format(i, max(num)))