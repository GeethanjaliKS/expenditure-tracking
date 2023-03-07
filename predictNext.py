import pandas as pd
from sklearn.linear_model import LinearRegression
import pymongo
import numpy as np

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]
def predictAmt(exp):
    
    d=mycol.find({"Category":exp},{"Amount":1,"_id":0,"Date":1}).sort("Date")
    amt=[]
    data=[]
    for i in d:
      amt.append(i['Amount'])
      data.append(i['Date'])
    df = pd.DataFrame({'Date': data,'Amount': amt}, columns=['Date', 'Amount'])
    df['Gdate']=df['Date'].str[:7]
    res=df.groupby('Gdate')['Amount'].sum().reset_index()
    n=len(res)
    # print(res)
    # df_mean=res.rolling(5).mean()['Amount']
    # print(df_mean)
    index=np.arange(0,n)
    X = np.array(index).reshape(-1,1)
    y = np.array(res)[:,1].reshape(-1,1)
    # print("X=")
    # print(X)
    # print("y=")
    # print(y)
    to_predict_x= [n+1,n+2,n+3]
    to_predict_x= np.array(to_predict_x).reshape(-1,1)
    regsr=LinearRegression()
    regsr.fit(X,y)
    predicted_y= regsr.predict(to_predict_x)
    m= regsr.coef_
    c= regsr.intercept_
    # print("Predicted y:\n",predicted_y)
    # print("slope (m): ",m)
    # print("y-intercept (c): ",c)
    return predicted_y
# exp='Beauty'
# predictAmt(exp)

