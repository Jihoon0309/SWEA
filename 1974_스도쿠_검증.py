T = int(input())

for test_case in range(1, T + 1):
    sudoku=[]
    
    # 스도쿠 만들기
    for _ in range(9):
        num=list(map(int, input().split()))
        sudoku.append(num)
    
    result=-1

    # row 검증
    for i in range(9):
        if len(set(sudoku[i]))!=9:
            result=0
            break
    if result==0:
        print('#{} {}'.format(test_case, result))
        continue
    else:
        for i in range(9):
            column=[]
            for j in range(9):
                column.append(sudoku[j][i])
            if len(set(column))!=9:
                result=0
                break
    if result==0:
        print('#{} {}'.format(test_case, result))
        continue
    else:
        num_1=-3
        num_2=-3
        for i in range(9):
            nine=[]
            if i==0 or i==3 or i==6:
                num_1+=3
            num_2+=3
            for j in range(num_1,num_1+3):
                for z in range(num_2,num_2+3):
                    nine.append(sudoku[j][z])
            if len(set(nine))!=9:
                result=0
                break
            if z==8:
                num_2=-3
        
    if result==0:
        print('#{} {}'.format(test_case, result))
        continue
    else:
        result=1

    print('#{} {}'.format(test_case, result))