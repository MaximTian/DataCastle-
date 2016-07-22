# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:06:01 2016

@author: MaximTian
"""
import pandas as pd
import numpy

f_csv = ".\category_feature.csv"

t = pd.read_csv(f_csv)
y = t
features = list(t.columns)
for feature in features:
    max_ = t[feature].max()
    y[feature] = (t[feature] - max_) * (-1)

numpy.savetxt('category_feature_OH.csv', y, delimiter=',', fmt='%d')