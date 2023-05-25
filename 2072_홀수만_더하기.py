T=int(input())

for test_case in range(1, T + 1):
    num=map(int, input().split())
    result=0
    for i in num:
        if i%2!=0:
            result+=i
    print("#{} {}".format(test_case, result))