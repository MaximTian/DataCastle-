import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from minepy import MINE

fs = ['P_7094_onehot','P_7111','R_7211','R_7500_del_oh','R_8000','svm_6997']

res = []
res.append(pd.read_csv('P_7094_onehot.csv').score.values)
res.append(pd.read_csv('P_7111.csv').score.values)
res.append(pd.read_csv('R_7211.csv').score.values)
res.append(pd.read_csv('R_7500_del_oh.csv').score.values)
res.append(pd.read_csv('R_8000.csv').score.values)
res.append(pd.read_csv('svm_6997.csv').score.values)

cm = []
for i in range(6):
    tmp = []
    for j in range(6):
        m = MINE()
        m.compute_score(res[i], res[j])
        tmp.append(m.mic())
    cm.append(tmp)

def plot_confusion_matrix(cm, title, cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(6)
    plt.xticks(tick_marks, fs, rotation=45)
    plt.yticks(tick_marks, fs)
    plt.tight_layout()

plot_confusion_matrix(cm, title='mic')
plt.show()