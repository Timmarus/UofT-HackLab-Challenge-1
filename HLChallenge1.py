l=[]
n=l[::-1]
while n!=l:
 n = [n[x+2*(not x%2)-1] for x in range(len(n))]
 print(n)
 if n!=l:
  n=n[::-1]
