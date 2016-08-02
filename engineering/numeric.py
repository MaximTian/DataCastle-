import pandas as pd

feature_type = pd.read_csv('../raw_data/features_type.csv')
numeric_feature = list(feature_type[feature_type.type=='numeric'].feature)

test = pd.read_csv('../raw_data/test_x.csv')[['uid']+numeric_feature]
test.to_csv('test_x_numeric.csv',index=None)

train = pd.read_csv('../raw_data/train_x.csv')[['uid']+numeric_feature]
train.to_csv('train_x_numeric.csv',index=None)