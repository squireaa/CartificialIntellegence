import pandas as pd

df = pd.read_csv('betterdata.csv')
df = df.dropna()

black = 0
blue = 0
brown = 0
burgundy = 0
gold = 0
gray = 0
green = 0
orange = 0
pearl = 0
purple = 0
red = 0
silver = 0
tan = 0
unknown = 0
white = 0
yellow = 0

for i in range(len(df)):
    black += df[df.columns[417 - 1]].iloc[i]
    blue += df[df.columns[418 - 1]].iloc[i]
    brown += df[df.columns[419 - 1]].iloc[i]
    burgundy += df[df.columns[420 - 1]].iloc[i]
    gold += df[df.columns[421 - 1]].iloc[i]
    gray += df[df.columns[422 - 1]].iloc[i]
    green += df[df.columns[423 - 1]].iloc[i]
    orange += df[df.columns[424 - 1]].iloc[i]
    pearl += df[df.columns[425 - 1]].iloc[i]
    purple += df[df.columns[426 - 1]].iloc[i]
    red += df[df.columns[427 - 1]].iloc[i]
    silver += df[df.columns[428 - 1]].iloc[i]
    tan += df[df.columns[429 - 1]].iloc[i]
    unknown += df[df.columns[430 - 1]].iloc[i]
    white += df[df.columns[431 - 1]].iloc[i]
    yellow += df[df.columns[432 - 1]].iloc[i]

list1 = [black, blue, brown, burgundy, gold, gray, green, orange, pearl, purple, red, silver,
 tan, unknown, white, yellow]
list1.sort()

total = 0
for i in list1:
    total += i/len(df)
    print(i/len(df))

print(total)
