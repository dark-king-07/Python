low = int(input())
high = int(input())
for i in range(low,high+1):
    for j in range(2,int(i/2)+1):
      if(i%j==0):
        print(i,sep='')
        break
      else:
        continue
