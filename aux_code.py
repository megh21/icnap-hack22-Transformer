"""
Hackathon - INCAP - IconPro GmbH
Timeseries Classification with Transformers
"""

from dataclasses import dataclass
import os
from time import time
import typing
import numpy as np
from sklearn.model_selection import train_test_split
from lstm import lstm 
import pandas as pd
# Import packages as you need

def load_data(data_path : str) -> pd.DataFrame:
    """
    Loading of the dataset provided
    Edit the code below
    """
    data=pd.read_pickle(data_path)
    columns = data.columns
    data[columns[0]] = data[columns[0]].apply(lambda x: x.reshape((500,1)))
    return data


def preprocess_data(data):
    """
    A standard nan removal to be added.
    Add more preprocessing steps if needed.
    """
    data = data.dropna()
    columns = data.columns
    data[columns[1]] = data[columns[1]].apply(lambda x: int(x))
    data[columns[1]] = [0 for x in data[columns[1]].values() if x==-1]
    return data

def split_train_test(data):
    """
    Splitting the data into train, test, validation 
    """
    train, test = train_test_split(data,test_size=0.4, random_state=42,stratify=data['labels'])
    test, val = train_test_split(test,test_size=0.5, random_state=42, stratify=test['labels'])

    return train, test, val

def timeseries_transform(data):
    """
    Implement the timeseries transformer here
    """
    return

def model_training():
    """
    Train the data with the compatible model
    """
    model=None
    return model

def metric(validation_data, model):
    """
    Standard metrics and plotting should be same
    Metrics should be computed on validation data(unseen data)
    1. Balanced accuracy score
    2. Confusion matrix
    3. Per-class accuracy
    """
    metrics=None
    return metrics

def validation(metrics, metrics_validation):
    """
    Comparing the results with provided Series Embedder
    Plot confusion matrices of self analysis and LSTM with balanced_accuracy
    
    """
    return

if __name__=="__main__":
    path=r"/Users/tejaschaudhari/Desktop/hackathon/data.pkl"
    data=load_data(path)
    print(data)
    # preprocessed_data=preprocess_data(data)

    # transformed_data = timeseries_transform(preprocessed_data)
    # train,test,val=split_train_test(transformed_data)
    # model_self=model_training(train,test)
    # metrics=metric(val,model_self)
    
    # lstm_cm,lstm_balanced_accuracy=lstm(preprocessed_data,target='labels')
    # metrics_validation = [lstm_cm, lstm_balanced_accuracy]
    # validation(metrics,metrics_validation)