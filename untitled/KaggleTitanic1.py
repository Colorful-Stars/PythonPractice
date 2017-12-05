#!/usr/bin/env python
# -*- coding = utf-8 -*-

import os
#数据处理
import pandas as pd
import numpy as np
import random
#sklearn数据预处理
import sklearn.preprocessing as preprocessing
#数据可视化
import matplotlib as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import (GradientBoostingClassifier, GradientBoostingRegressor,
                              RandomForestClassifier, RandomForestRegressor)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve


train = pd.read_csv('F:\Python\Kaggle\Titanic\\train.csv')
test = pd.read_csv('F:\Python\Kaggle\Titanic\\test.csv')

train.head(3)

