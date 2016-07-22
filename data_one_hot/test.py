from sklearn import preprocessing
import pandas as pd

x_csv = "./2.csv"
t = pd.read_csv(x_csv)
train_x = t.x411
enc = preprocessing.OneHotEncoder()
enc.fit(t)
train_y = enc.transform(t).toarray()