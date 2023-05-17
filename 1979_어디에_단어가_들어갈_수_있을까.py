T = int(input())
for test_case in range(1, T + 1):
    N,K=map(int, input().split())

    # puzzle
    puzzle=[]
    for _ in range(N):
        num=list(map(int, input().split()))
        puzzle.append(num)

    count=0
    space=[]
    # row
    for i in range(N):
        space_count=0
        for j in range(N):
            if puzzle[i][j]==1:
                space_count+=1
            else:
                if space_count>0:
                    space.append(space_count)
                    space_count=0
                else:
                    continue
            if j==N-1 and space_count>0:
                space.append(space_count)

    # column
    for i in range(N):
        space_count=0
        for j in range(N):
            if puzzle[j][i]==1:
                space_count+=1
            else:
                if space_count>0:
                    space.append(space_count)
                    space_count=0
                else:
                    continue
            if j==N-1 and space_count>0:
                space.append(space_count)
    
    print('#{} {}'.format(test_case,space.count(K)))