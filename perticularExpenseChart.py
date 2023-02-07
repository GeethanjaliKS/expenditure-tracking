import pandas as pd
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]

def perticularExpense():
    d=mycol.find({"Category":"Fashion"},{"Amount":1,"_id":0,"Date":1})
    amt=[]
    data=[]
    for i in d:
      amt.append(i['Amount'])
      data.append(i['Date'])
    df = pd.DataFrame({'Date': data,'Amount': amt}, columns=['Date', 'Amount'])
    # per = df.Date.dt.to_period("M")
    # g = df.groupby(per)
    # print(g.sum())
    # print(g)
    df['Gdate']=df['Date'].str[:6]
    a=df.groupby('Gdate')['Amount'].sum()
    print(a)
perticularExpense()