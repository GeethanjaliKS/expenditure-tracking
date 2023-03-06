
import pandas as pd
import pymongo
import matplotlib.pyplot as plt

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Expense_Trackerdb"]

# mycol = mydb["expense"]

def perticularExpense(exp,mycol):
    d=mycol.find({"Category":exp},{"Amount":1,"_id":0,"Date":1}).sort("Date")
    amt=[]
    data=[]
    for i in d:
      amt.append(i['Amount'])
      data.append(i['Date'])
    df = pd.DataFrame({'Date': data,'Amount': amt}, columns=['Date', 'Amount'])
    # a= df.isnull().sum()
    # print(a)
    # per = df.Date.dt.to_period("M")
    # g = df.groupby(per)
    # print(g.sum())
    # print(g)
    df['Gdate']=df['Date'].str[:7]
    res=df.groupby('Gdate')['Amount'].sum().reset_index()
    col_date=list(res["Gdate"])
    col_amt=list(res["Amount"])
    # print(col_date)
    # print(col_amt)
    plt.plot(col_date, col_amt,"-o",color='maroon')
    plt.xlabel("Date",fontweight='bold',color='black',fontsize='15')  # add X-axis label
    plt.ylabel("Amount",fontweight='bold',color='black',fontsize='15')  # add Y-axis label
    plt.title(exp,color='blue',fontweight='bold',fontsize='25')
    plt.xticks(rotation = 25)
    plt.grid()
    plt.show()
    
def get_category(mycol):
     c=mycol.distinct("Category")
     print(c)


    

    
