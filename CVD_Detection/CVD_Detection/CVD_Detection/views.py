from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn. metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report




def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    df = pd.read_csv(r"C:\Users\kamya\PycharmProjects\CVD_Detection\CVD_Detection\heart.csv")

    X = df.drop(['target'], axis=1)
    y = df['target']

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=40)

    lr = LogisticRegression()
    lr.fit(X_train, y_train)


    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])




    pred = lr.predict([[val1, val2, val3, val4, val5, val6, val7,val8,val9,val10,val11,val12,val13]])

    result1 = ''
    if pred == [0]:
        result1 = "The Person does not have a Heart Disease"

    else:
        result1 = "The Person has Heart Disease"





    return render(request,'predict.html',{"result2":result1})

