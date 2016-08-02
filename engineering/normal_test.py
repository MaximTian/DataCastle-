from sklearn.cross_validation import train_test_split
import pandas as pd
import xgboost as xgb
random_seed = 1225
#read the data file
train_x_csv = "../del_data/test_final.csv"
features_type_csv = "../features_type.csv"

train = pd.read_csv(train_x_csv)
features_type = pd.read_csv(features_type_csv)

features_type.index = features_type.feature
features_type = features_type.drop('feature',axis=1)
features_type = features_type.to_dict()['type']

columns = train.drop(['uid'],axis=1).columns
drop_list = ['x380', 'x412', 'x414']

def func(col1, col, l):
    i = 0
    k = 0
    dis = [-10, -1, 0]
    
    rg = 1500
    if (l >= 1500):
        i = -l + 1
        rg = (14894 - l) / 10
    else:
        i = 0
        l = 0
    for val in col1:
        i = i + 1
        k = k + 1
        if (i > 0):
            if ((i % rg == 0 and i / rg < 10) or k == 14894):
                dis.append(val)
    cats = pd.cut(col,dis,labels=[-1,0,1,2,3,4,5,6,7,8,9,10],retbins = False).astype(int)
    res = list(cats)
    return res

for c in columns:
    if (features_type[c] == "numeric"):
        col = train[c]
        l = len(train[train[c] <= 0])
        l1 = len(train[train[c] == 1])
        if c in drop_list:
            continue
        if (l > 6000 or l1 > 1500):
            continue
        print c
        col_order = col.sort_values()
        train[c] = pd.Series(func(col_order, col, l))

train.to_csv("../del_data/test2.csv",index=None,encoding='utf-8')