n=int(input("enter a no"))
k=int(input("enter a no"))
count=0
l=[]
for i in range(n+1,k+1):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      print(i)
         
