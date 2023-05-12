T=int(input())

for test_case in range(1, T + 1):
    count=0
    max_count=0
    order=int(input())
    num=list(map(int, input().split()))
    num.sort()
    
    for i in range(0,len(num)-1):
        if num[i]==num[i+1]:
            count+=1
        else:
            if max_count<=count:
                max_count=count
                result=num[i]
            count=1

    print('#{} {}'.format(test_case,result))