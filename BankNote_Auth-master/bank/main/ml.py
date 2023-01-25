import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def is_authentic(varience, skewness, curtosis, entropy):
    dataset = pd.read_csv("../bank/BankNote_Authentication.csv")

    X = dataset.drop('class', axis=1)
    y = dataset['class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    authenticity_flag =  classifier.predict([[varience, skewness, curtosis, entropy]])[0]

    return authenticity_flag