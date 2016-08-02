import pandas as pd

feature_type = pd.read_csv('../features_type.csv')
numeric_feature = list(feature_type[feature_type.type=='category'].feature)

test = pd.read_csv('../test_x.csv')[['uid']+numeric_feature]
test.to_csv('test_x_category.csv',index=None)

train = pd.read_csv('../train_x.csv')[['uid']+numeric_feature]
train.to_csv('train_x_category.csv',index=None)
