import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,
                              classification_report,ConfusionMatrixDisplay)

Border = "-"*50
print(Border)
print("Loding data set")
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print(df)
print("Analysing the Data")
print("shape of dataset",df.shape)
print("columns of dataset",df.columns)
print("Missing Values of dataset",df.isnull().sum())
print("Statitical summary report",df.describe())

print(Border)
print("Data visuallization")

F_cols = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted','SleepHours']
 
X = df[F_cols]
Y = df["FinalResult"]
plt.figure(figsize=(15,8))

for i,col in enumerate(F_cols):
    plt.subplot(2,3,i+1)
    sns.scatterplot(data=df,x=col,y="FinalResult")
    plt.title(f"{col} VS FinalResult")

plt.tight_layout()
plt.show() 

print(Border)
print("Data Splitting")
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Traning set shape", X_train.shape)
print("Result set shape", Y_train.shape)
print("Testing set shape", X_test.shape)
print("Result set shape", Y_test.shape)

print(Border)
 
print("We are going to use Decission Tree Classifier with max depth 1")

print("Model training")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=42
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")

print(Border)

print("Model evaluation")
Y_pred = model.predict(X_test)
print("Model Evaluation(testing) complete")
print(Border)

print("Accuracy calculator")
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model:", accuracy*100)

print("Confusion Matrix")
cm = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix: "),
print(cm)

