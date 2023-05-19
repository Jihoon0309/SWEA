N=int(input())

num=list(map(int, input().split()))
num.sort()
result=num[(N)//2]
print(result)