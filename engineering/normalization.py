from sklearn.cross_validation import train_test_split
import pandas as pd
import xgboost as xgb
random_seed = 1225
#read the data file
train_x_csv = "../del_data/train_final.csv"
test_x_csv = "../del_data/test_final.csv"
features_type_csv = "../features_type.csv"

train = pd.read_csv(train_x_csv)
test = pd.read_csv(test_x_csv)
columns = train.drop(['uid'],axis=1).columns

my_range = [-1,0,1,2,3,4,5,6,7,8,9,10]

def func(col, col_test):
    max_ = col.max()
    min_ = col.min()
    dis = max_ - min_
    if (dis > 500):
        d = max_ / 10
        dis = [-10, -1, 0]
        for i in range(1, 10):
            dis.append(d * i)
        dis.append(99999999)
        cats = pd.cut(col,dis,labels=my_range,retbins = False).astype(int)
        res = list(cats)
        cats_test = pd.cut(col_test,dis,labels=my_range,retbins = False).astype(int)
        res_test = list(cats_test)
        return pd.Series(res), pd.Series(res_test)
    else:
        return pd.Series(col), pd.Series(col_test)

for c in columns:
    print c
    col = train[c]
    col_test = test[c]
    train[c], test[c] = func(col, col_test)

train.to_csv("../del_data/test1.csv",index=None,encoding='utf-8')
test.to_csv("../del_data/test2.csv",index=None,encoding='utf-8')