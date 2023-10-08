import pandas as pd
import numpy as np
import os
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import ElasticNet

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
import argparse

def get_data():
    URL="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

    #read the data as df
    try:
        df=pd.read_csv(URL,sep=",")
        return df
    except Exception as e:
        raise e
    
def evaluate(y_true,y_pred):
    mae=mean_absolute_error(y_true,y_pred)
    mse=mean_squared_error(y_true,y_pred)
    rmse=np.sqrt(mean_squared_error(y_true,y_pred))
    r2=r2_score(y_true,y_pred)

    return mae,mse,rmse,r2
    
def main():
    df=get_data()
    train,test=train_test_split(df)
    X_train=train.drop(['quality'],axis=1)
    X_test=test.drop(['quality'],axis=1)

    y_train=train[["quality"]]
    y_test=test[['quality']]

    lr=ElasticNet()
    lr.fit(X_train,y_train)
    pred=lr.predict(X_test)

    rf=RandomForestClassifier()


    mae,mse,rmse,r2=evaluate(y_test,pred)

    print(f"mean absolute error {mae},mse {mse},rmse {rmse}, r2_score {r2}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        raise e

