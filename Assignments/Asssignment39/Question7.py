import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,
                              classification_report,ConfusionMatrixDisplay)

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
feature_cols = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted','SleepHours']
 
X = df[feature_cols]
Y = df["FinalResult"]
 
print("X shape:", X.shape)
print("Y shape:", Y.shape)  
 
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
 
print("Independent:",X.shape)
print("Dependent:",Y.shape)
print("Data Splitting Activity:")
print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)
print("X_test shape:", X_test.shape)
print("Y_test shape:", Y_test.shape)

print(border)
 
print("We are going to use Decission Tree Classifier with max depth 1")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=42
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")

sampledata =[6,85,66,7,7]
sample_2D_list = [sampledata]

single_pred = model.predict(sample_2D_list)
single_prod = model.predict_proba(sample_2D_list)


print("Single sample prediction",single_pred)
print("Single sample probablity",single_prod)

print("Student is passed")