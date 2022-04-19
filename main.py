from pandas import read_csv
from matplotlib.pyplot import show, bar, xlabel, ylabel, title

teen = 0
adult = 0
old = 0

age = ["14-20", "20-40", "40-60"]

with open("Deaths_by_Police_US.csv", encoding="utf8", errors='ignore') as data:
    death_dataframe = read_csv(data)

death_dataframe_age = death_dataframe.groupby("age").size()

for i in range(14, 21):
    teen = teen + death_dataframe_age[i]
for j in range(21, 41):
    adult = adult + death_dataframe_age[j]
for k in range(41, 61):
    old = old + death_dataframe_age[k]

age_list = [teen, adult, old]

bar(age, age_list)
xlabel("Age")
ylabel("Number of suspect")
title("")
show()
