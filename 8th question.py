#Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series.
import pandas as pd
data= pd.read_csv("D:\Study\Intern\diamonds.csv")
df=pd.DataFrame(data)
print (df.iloc[0:1])
