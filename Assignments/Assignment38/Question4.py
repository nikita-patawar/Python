import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
count = (df["FinalResult"].value_counts())
precentage = df["FinalResult"].value_counts(normalize=100)*100
print("count :\n",count)
print("precentage :\n",precentage)
print("Data is Balanced")