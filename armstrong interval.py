n=int(input())
k=int(input())
for i in range(n,k):
    temp=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+pow(rem,3)
        i=i//10
    if(sum==temp):
        print(temp)
