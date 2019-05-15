n=int(input())
k=int(input())
a=[]
for i in range(0,n):
  s=int(input("enter a number"))
  a.append(s)
print(a)
sum=0
for i in range(0,k):
  sum=sum+a[i]
print(sum)
