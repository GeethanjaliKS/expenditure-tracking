import pandas as pd
import pymongo
import matplotlib.pyplot as plt

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]

def perticularExpense(exp):
    d=mycol.find({"Category":exp},{"Amount":1,"_id":0,"Date":1}).sort("Date")
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
    df['Gdate']=df['Date'].str[:7]
    res=df.groupby('Gdate')['Amount'].sum().reset_index()
    col_date=list(res["Gdate"])
    col_amt=list(res["Amount"])
    print(col_date)
    print(col_amt)
    plt.plot(col_date, col_amt,"-o")
    plt.xlabel("Date")  # add X-axis label
    plt.ylabel("Amount")  # add Y-axis label
    # plt.title("Category")
    plt.show()
    
def get_category():
     c=mycol.distinct("Category")
     print(c)

    
