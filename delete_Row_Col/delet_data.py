import pandas as pd
#read the data file
train_x_csv = "../raw_data/train_x.csv"
test_x_csv = "../raw_data/test_x.csv"
train = pd.read_csv(train_x_csv)
test = pd.read_csv(test_x_csv)

train_y_csv = "../raw_data/train_y.csv"
train_y = pd.read_csv(train_y_csv)

train_feature = "../raw_data/features_type.csv"
feature = pd.read_csv(train_feature)
############delete the rows whose acount of '-1' is over 190
uids = train.uid
train.index = uids
train_y.index = uids
feature.index = feature.feature
del_row_list = []
for uid in uids:
    count = 0
    for value in train.loc[uid]:
        if (value < 0):
            count += 1
    if count >= 190:
        del_row_list.append(uid)
train = train.drop(del_row_list, axis=0)
train_y = train_y.drop(del_row_list, axis=0)
############delete the columns whose acount of '-1' is over 6000
columns = train.columns
del_col_list = []
for col in columns:
    if (len(train[train[col] < 0]) > 7000):
        del_col_list.append(col)

print del_col_list
train = train.drop(del_col_list, axis=1)
test = test.drop(del_col_list, axis=1)
feature = feature.drop(del_col_list, axis=0)

train.to_csv("./train_x_del.csv",index=None,encoding='utf-8')
train_y.to_csv("./train_y_del.csv",index=None,encoding='utf-8')
test.to_csv("./test_del.csv",index=None,encoding='utf-8')
feature.to_csv("./features_del.csv",index=None,encoding='utf-8')