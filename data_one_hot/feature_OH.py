from sklearn import preprocessing
import pandas as pd
import numpy
x_csv = "./some_feature.csv"
t = pd.read_csv(x_csv)


enc = preprocessing.OneHotEncoder()
enc.fit(t)
train_y = enc.transform(t).toarray()


train = train_y.astype(bool)

numpy.savetxt('some_feature_OH.csv', train, delimiter=',', fmt='%d')