# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:16:17 2016

@author: MaximTian
"""

import pandas as pd

feature_type = pd.read_csv('../features_type.csv')
numeric_feature = list(feature_type[feature_type.type=='numeric'].feature)

#rank特征的命名：在原始特征前加'r',如'x1'的rank特征为'rx1'

#三份数据集分别排序，使用的时候需要归一化。
#更合理的做法是merge到一起排序，这个我们也试过，效果差不多，因为数据分布相对比较一致。

test = pd.read_csv('../test_x.csv')[['uid']+numeric_feature]
test_rank = pd.DataFrame(test.uid,columns=['uid'])
for feature in numeric_feature:
    test_rank['r'+feature] = test[feature].rank(method='max')
test_rank.to_csv('test_x_rank.csv',index=None)


train = pd.read_csv('../train_x.csv')[['uid']+numeric_feature]
train_rank = pd.DataFrame(train.uid,columns=['uid'])
for feature in numeric_feature:
    train_rank['r'+feature] = train[feature].rank(method='max')
train_rank.to_csv('train_x_rank.csv',index=None)