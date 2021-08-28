import pandas as pd 
import plotly.figure_factory as pf 
import statistics as stats 
df  = pd.read_csv("StudentsPerformance.csv")
MathScore = df["math score"].tolist()
graph = pf.create_distplot([MathScore],["Math Score"],show_hist=False)
#graph.show()
Mathstd = stats.stdev(MathScore)
mean = stats.mean(MathScore)
fstartingpoint = mean  - Mathstd
fendingpoint = mean  + Mathstd
Sstartingpoint = mean -2*Mathstd
Sendingpoint = mean + 2*Mathstd
Tstartingpoint  = mean-3*Mathstd
Tendingpoint = mean+3*Mathstd
flist = []
Slist  = []
Tlist = []
for data in MathScore:
    if data>fstartingpoint and data<fendingpoint:
        flist.append(data)

for data in MathScore:
    if data>Sstartingpoint and data<Sendingpoint:
        Slist.append(data)

for data in MathScore:
    if data>Tstartingpoint and data<Tendingpoint:
        Tlist.append(data)
Fpercent = len(flist)/len(MathScore)*100
print(Fpercent)
Spercent = len(Slist)/len(MathScore)*100
print(Spercent)
Tpercent = len(Tlist)/len(MathScore)*100
print(Tlist)