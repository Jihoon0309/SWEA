for test_case in range(1,11):
    dump=int(input())
    box=list(map(int, input().split()))
    box.sort()

    for i in range(dump):
        box[-1]-=1
        box[0]+=1
        box.sort()
    print('#{} {}'.format(test_case,box[-1]-box[0]))