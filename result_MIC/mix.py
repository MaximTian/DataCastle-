import pandas as pd

P7111 = pd.read_csv("P_7111.csv")
svm6997 = pd.read_csv('svm_6997.csv')
R7211 = pd.read_csv('R_7211.csv')

uid = R7211.uid
#score = 0.5*R7211.score + 0.28*P7111.score + 0.22*svm6997.score 7223
#score = 0.6*R7211.score + 0.2*P7111.score + 0.2*svm6997.score 7222
#score = 0.7*R7211.score + 0.2*P7111.score + 0.1*svm6997.score 7221
score = 0.618*R7211.score + 0.382*P7111.score
pred = pd.DataFrame(uid,columns=['uid'])
pred['score'] = score

pred.to_csv('three_merge2.csv',index=None,encoding='utf-8')