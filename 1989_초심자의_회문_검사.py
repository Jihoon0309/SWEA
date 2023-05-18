T = int(input())
for test_case in range(1, T + 1):
    word=list(input())

    if list(reversed(word))==word:
        result=1
    else:
        result=0

    print('#{} {}'.format(test_case, result))