N=int(input())

for i in range(1,N+1):
    count=0
    if i//100==3 or i//100==6 or i//100==9:
        count+=1
    if i//10==3 or i//10==6 or i//10==9:
        count+=1
    if i%10==3 or i%10==6 or i%10==9:
        count+=1
    
    if count==0:
        print(i, end=' ')
    else:
        print('-'*count,end=' ')