import random
import plotly.express as px
import plotly.figure_factory as ff 
import csv
import pandas as pd 
count = []

diceresult = []

for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1 + dice2)
    count.append(i)
df = pd.read_csv("data.csv")
fig = ff.create_distplot ([df["Marks_In_Percentage"].tolist()],["Days_Present"],show_hist = False)
fig.show()
