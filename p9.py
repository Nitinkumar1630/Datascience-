import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("newdata.xlsx")
x=0
y=0
w=0
m=0
sp=0
o=0
dt=df.loc[:,"Q2"]
for i in dt:
    if i=="yes":
        x=x+1
    elif i=="no":
        y=y+1
    
dt=df.loc[:,"Q3"]  
for n in dt:
    b=str(n).split(" ") 
    for t in b: 
        if  t=="winters":
            w=w+1
        elif t=="monsoon":
            m=m+1
        elif t=="springs":
            sp=sp+1
        elif t=="occasional":
            o=o+1
spe=["winters","monsoon","springs","ocassional"]
spec=[w,m,sp,o]
explode=[0,0.1,0.4,0]
plt.pie(spec,labels=spe,
        explode = explode,
        autopct = "%0.2f%%") 
plt.show()