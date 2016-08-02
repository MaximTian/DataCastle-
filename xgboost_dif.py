from sklearn.cross_validation import train_test_split
import pandas as pd
import xgboost as xgb
random_seed = 1225
#read the data file
train_x_csv = "./train_Category.csv"
train_y_csv = "./raw_data/train_y.csv"
test_x_csv = "./test_Category.csv"

train_x = pd.read_csv(train_x_csv)
train_y = pd.read_csv(train_y_csv)
train_xy = pd.merge(train_x,train_y,on='uid')
test = pd.read_csv(test_x_csv)
test_uid = test.uid
test_x = test.drop(['uid'],axis=1)

#split train set,generate train,val,test set
train_xy = train_xy.drop(['uid'],axis=1)
train,train_test = train_test_split(train_xy, test_size = 0.2,random_state=random_seed)
y = train.y
x = train.drop(['y'],axis=1)
train_test_y = train_test.y
train_test_x = train_test.drop(['y'],axis=1)

#xgboost
dtest = xgb.DMatrix(test_x)
dtrain_test = xgb.DMatrix(train_test_x, label = train_test_y)
dtrain = xgb.DMatrix(x, label = y)
params = {
    'n_estimators':8000,
    'objective': 'binary:logistic',
    'scale_pos_weight': 8.0,
    'gamma':0.48,
    'max_depth':5.0,
    'min_child_weight':4,
    'subsample':0.655,
    'colsample_bytree':0.4,
    'reg_lambda':2300,
    'learning_rate':0.02,
    'eval_metric': 'auc',
    }
watchlist  = [(dtrain_test,'test'), (dtrain,'train')] # watchdog
model = xgb.train(params, dtrain, num_boost_round=10000, evals = watchlist)
test_y = model.predict(dtest, ntree_limit=model.best_ntree_limit)
test_result = pd.DataFrame(columns=["uid","score"])
test_result.uid = test_uid
test_result.score = test_y
test_result.to_csv("dels_result.csv",index=None,encoding='utf-8')
