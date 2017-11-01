l=[]
n=l[::-1]
while n!=l:
 for i in range(0,len(n)-1,2):
  n[i],n[i+1]=n[i+1],n[i]
 print(n)
 n=n[::-1]if n!=l else n
