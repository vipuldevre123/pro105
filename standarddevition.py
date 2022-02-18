import csv
import math
with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

data=filedata[0]
totalmarks=0
for i in data:
    totalmarks=totalmarks+int(i)

l=len(data)
mean=totalmarks/l
print(l)
print("mean="+str(mean))

squarelist=[]
for i in data:
    a=int(i)-mean
    a=a**2
    squarelist.append(a)

sum=0
for i in squarelist:
    sum=sum+i    

N=len(data)-1
r=sum/N
standarddevition=math.sqrt(r)

print(standarddevition)