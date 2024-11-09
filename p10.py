import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("newdata.xlsx")
x=0
y=0
wb=0
sd=0
bd=0
bb=0
bs=0
dt=df.loc[:,"Q1"]
for i in dt:
    if i=="yes":
        x=x+1
    elif i=="no":
        y=y+1
    elif len(str(i))>3:
        x=x+1
        a=i.split(",")
        b=a[1].split(" ")
        for t in b:
            if t=="wildboar":
                wb=wb+1 
            elif t=="swampdeer":
                sd=sd+1
            elif t=="barkingdeer":
                bd=bd+1
            elif t=="blackbear":
                bb=bb+1
            elif t=="bluesheep":
                bs=bs+1
spe=["wildboar","swampdeer","barkingdeer","blackbear","bluesheep"] 
spec=[wb,sd,bd,bb,bs]
plt.bar(spe,spec, width = 0.4, align = "edge", 
        color = "g",
        linewidth = 5, alpha = 0.9,
       label ="spec", visible=True)
plt.show()