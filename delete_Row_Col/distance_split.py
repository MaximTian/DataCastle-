import pandas as pd
#read the data file
train_x_csv = "../del_data/test_final.csv"

train = pd.read_csv(train_x_csv)

def func(col1, col, l):
    i = 0
    k = 0
    dis = [-10, -1, 0]
    
    rg = 1500
    if (l >= 1500):
        i = -l + 1
        rg = (14894 - l) / 10
    else:
        i = 0
        l = 0
    for val in col1:
        i = i + 1
        k = k + 1
        if (i > 0):
            if ((i % rg == 0 and i / rg < 10) or k == 14894):
                dis.append(val)
                print i, k, val
    print rg, dis
    cats = pd.cut(col,dis,labels=[-1,0,1,2,3,4,5,6,7,8,9,10],retbins = False).astype(int)
    res = list(cats)
    return res


col = train.x1
l = len(col[col <= 0])
l1 = len(col[col == 1])
print l, l1
col_order = col.order()
col = pd.Series(func(col_order, col, l))