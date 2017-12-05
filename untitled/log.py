# import math

# print(math.log(4,2))

# print((4/9)*(-(3/4)*math.log(3/4,2)-(1/4)*math.log(1/4,2))+(3/9)*(-(2/3)*math.log(2/3,2)-(1/3)*math.log(1/3,2)))

# import os

# mingw_path = 'C:\\Program Files\\mingw-w64\\x86_64-5.3.0-posix-seh-rt_v4-rev0\\mingw64\\bin'

# os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']

import xgboost as xgb
import numpy as np
data = np.random.rand(5,10) # 5 entities, each contains 10 features
label = np.random.randint(2, size=5) # binary target
dtrain = xgb.DMatrix( data, label=label)
dtest = dtrain
param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( param, dtrain, num_round, evallist )
bst.dump_model('dump.raw.txt')