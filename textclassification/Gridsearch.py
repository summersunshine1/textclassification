# -*- coding:utf-8 -*-
print(__doc__)

import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import Normalize

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
import codecs
import os

thetapath="F:/model-final.theta"
theta_file = codecs.open(thetapath,'r','utf-8')
theta=[]
wordlen=0
try:
    for line in theta_file:
        arr=line.split()
        theta.append(arr)
        wordlen=len(arr)       
finally:
    theta_file.close()
X = theta

Y=[]
rootdir = "F:\\datatrain"
dir = os.walk(rootdir)
classindex=1
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    cate=0
    for filename in filenames: #输出文件信息
        cate+=1
        Y.append(classindex)
    # print("Y: " +str(len(Y)))
    # print("cata: "+str(cate))
    if not cate==0:
        classindex+=1

# Dataset for decision function visualization: we only keep the first two
# features in X and sub-sample the dataset to keep only 2 classes and
# make it a binary classification problem.

# X_2d = X[:, :2]
# X_2d = X_2d[y > 0]
# y_2d = y[y > 0]
# y_2d -= 1

# It is usually a good idea to scale the data for SVM training.
# We are cheating a bit in this example in scaling all of the data,
# instead of fitting the transformation on the training set and
# just applying it on the test set.

scaler = StandardScaler()
X = scaler.fit_transform(X)
print(len(X))
# X_2d = scaler.fit_transform(X_2d)
print(len(Y))

# C_range = np.logspace(-4, 4, 3)
# gamma_range = np.logspace(-4, 4, 3)
# param_grid = dict(gamma=gamma_range, C=C_range)
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3,10,100,1000],
                     'C': [1e-2, 10, 100]}]
# cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
grid = GridSearchCV(SVC(), param_grid=tuned_parameters, cv=5)
grid.fit(X, Y)

print("The best parameters are %s with a score of %0.2f"
      % (grid.best_params_, grid.best_score_))