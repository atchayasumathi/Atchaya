n=int(input())
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+pow(rem,3)
    n=n//10
if(temp==sum):
    print(temp,"is armstrong")
else:
    print("not armstrong")
