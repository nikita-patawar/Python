import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

DatasetPath= "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)
print("Dataset gets loaded succesfully...")
print("First five records:")
print(df.head())
print("Last five records:")
print(df.tail())
print("Total numbers of rows and columns")
print(df.shape)
print("list of column")
print(list(df.columns))
print("Data Types of each column")
print(list(df.dtypes))