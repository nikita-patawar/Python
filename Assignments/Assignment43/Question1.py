import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def main():
    Border = "-"*40
    ####################################################################

    # Step 1: Load the dataset

    ####################################################################

    print(Border)
    print("Step 1: Load the Dataset")
    print(Border)
    df = pd.read_csv("PlayPredictor.csv")
    print(df.head())

    ####################################################################

    # Step 2: Clean prepare and manupalate

    ####################################################################

    print(Border)
    print("Step 1: Clean prepare and manupalate")
    print(Border)
    print("Removed unnamed column")
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Shape of dataset after removel",df.shape) 
    print(df.head())

    le = LabelEncoder()

    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])

    #----------------------------------------------------
    #step3: Summary of dataset
    #----------------------------------------------------
    print(Border)
    print("Step3: Summary of dataset")
    print(Border)
    print("Summary of dataset:")
    print(df.head())
    #----------------------------------------------------
    #step4: Split the data into features and target variable
    #----------------------------------------------------
    print(Border)
    print("Step 4 : Split the data into features and target variable")
    print(Border)

    X = df[["Whether","Temperature"]]
    Y = df["Play"]

    print("Features:", X.shape)
    print("Labels:",Y.shape)
    #----------------------------------------------------
    #step5 : Split the data in train and test
    #----------------------------------------------------
    print(Border)
    print("Step6 :  Split the data in train and test")
    print(Border)
   
    X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X train:", X_train.shape)
    print("X test:", X_test.shape)
    print("Y train:", Y_train.shape)
    print("Y test:", Y_test.shape)
    
    #----------------------------------------------------
    #step6 : Train the model
    #----------------------------------------------------
    print(Border)
    print("Step7 : Train the model")
    print(Border)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)

    #----------------------------------------------------
    #step7 : Test the Model
    #----------------------------------------------------
    print(Border)
    print("Step8 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)
    print("Predicted output:")
    print(Y_pred.shape)
    print(Y_pred)

    #----------------------------------------------------
    #step8 : Calculate Accuracy
    #----------------------------------------------------
    print(Border)
    print("Step9 : Calculate Accuracy")
    print(Border)
    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model is :", accuracy % 100)


if __name__ == "__main__":
    main()
