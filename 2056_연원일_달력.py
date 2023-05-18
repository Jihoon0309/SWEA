T=int(input())

for i in range(1,1+T):
    num=list(map(str, input()))

    year=''.join(num[:4])
    month=''.join(num[4:6])
    days=''.join(num[6:])
    if (month=='01' or month=='03' or month=='05' or month=='07' or month=='08' or month=='10' or month=='12') and ('01'<=days<='31'):
        print('#{} {}/{}/{}'.format(i,year,month,days))
    elif (month=='04' or month=='06' or month=='09' or month=='11') and ('01'<=days<='30'):
        print('#{} {}/{}/{}'.format(i,year,month,days))
    elif (month=='02') and ('01'<=days<='28'):
        print('#{} {}/{}/{}'.format(i,year,month,days))
    else:
        print('#{} {}'.format(i,-1))