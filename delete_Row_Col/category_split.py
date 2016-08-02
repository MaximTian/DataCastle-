import pandas as pd

train_x_csv = "./train_x_del.csv"
test_x_csv = "./test_del.csv"
train = pd.read_csv(train_x_csv)
test = pd.read_csv(test_x_csv)

select_cols = ['x411', 'x415', 'x416', 'x417']
for i in range(1107, 1139):
    col = 'x' + str(i)
    select_cols.append(col)

category_train = train.loc[:, select_cols]
category_test = test.loc[:, select_cols]

#collect the info about max, min, dis between max and min each colume
train_info = {}
test_info = {}
for col in select_cols:
    max_ = category_train.loc[:, col].max()
    min_ = category_train.loc[:, col].min()
    train_info[col] = [min_, max_, max_ - min_]
    
    max_ = category_test.loc[:, col].max()
    min_ = category_test.loc[:, col].min()
    test_info[col] = [min_, max_, max_ - min_]
#minimize the dis between ench colume
train_r = category_train
test_r = category_test
for key in train_info:
    if (train_info[key][2] > 10):
        train_r.loc[:, str(key)] = train_r.loc[:, str(key)] / train_info[key][1] * 10
        test_r.loc[:, str(key)] = test_r.loc[:, str(key)] / test_info[key][1] * 10
train_r = train_r.astype(int)
test_r = test_r.astype(int)
# replace the category datas of train,test with the ones in train_r,test_r
train.loc[:, select_cols] = train_r.loc[:, select_cols]
test.loc[:, select_cols] = test_r.loc[:, select_cols]

train.to_csv("./train_Category.csv",index=None,encoding='utf-8')
test.to_csv("./test_Category.csv",index=None,encoding='utf-8')