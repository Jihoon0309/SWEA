T = int(input())

score=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for test_case in range(1, T + 1):
    N,K= map(int, input().split())
    student=list()
    for i in range(N):
        mid_exam, final_exam, homework = map(int, input().split())
        sum=(mid_exam*0.35)+(final_exam*0.45)+(homework*0.2)
        student.append(sum)

    result_sum=student[K-1]
    student.sort(reverse=True)
    num=0
    final_sum=student.index(result_sum)//(N//10)
    print('#{} {}'.format(test_case, score[final_sum]))