import pandas as pd
#set data path
train_x_csv1 = "train_col.csv"
train_x_csv2 = "../engineering/train_x_category.csv"
test_x_csv1 = "test_col.csv"
test_x_csv2 = "../engineering/test_x_category.csv"
#load data
train_x1 = pd.read_csv(train_x_csv1)
train_x2 = pd.read_csv(train_x_csv2)
train = pd.merge(train_x1, train_x2, on='uid')

test_x1 = pd.read_csv(test_x_csv1)
test_x2 = pd.read_csv(test_x_csv2)
test = pd.merge(test_x1, test_x2, on='uid')

train.to_csv("./train_del_col.csv",index=None,encoding='utf-8')
test.to_csv("./test_del_col.csv",index=None,encoding='utf-8')