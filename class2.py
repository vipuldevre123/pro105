from asyncore import readwrite
import csv
import stat
import pandas as pd
import plotly.express as px
import statistics

with open("class2.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
totalmarks=0
for i in filedata:
    totalmarks=totalmarks+float(i[1])

l=len(filedata)
mean=totalmarks/l

print("mean="+str(mean))

#lets plot the graph
df=pd.read_csv("class1.csv")
fig=px.line(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(
    type="line",
    x0=0,
    x1=l,
    y0=mean,
    y1=mean
)])
fig.show()