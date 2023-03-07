
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import predictNext
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Expense_Trackerdb"]

# mycol = mydb["expense"]

def perticularExpense(exp,mycol):
#  try:
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
   
   # For getting months to plot 
    pred_amt=[]
    m=col_date[len(col_date)-1]
    pred_amt.append(col_amt[len(col_amt)-1])
   #  print("Last Month",m)
    pred_date=[m]
    for  i in range(0,3):
       d=pred_date[len(pred_date)-1]
       y=d[0:4]
       mn=d[5:7]
      #  print(mn)
       if(mn=='12'):
          y=int(y)+1
          mn=1
          pred_date.append(str(y)+'-'+str(mn).zfill(2))
       else:
          mn=int(mn)+1
          pred_date.append(str(y)+'-'+str(mn).zfill(2))
   #  print(pred_date)
    # print(col_amt)
    plt.plot(col_date, col_amt,"-o",color='maroon')
    plt.xlabel("Date",fontweight='bold',color='black',fontsize='15')  # add X-axis label
    plt.ylabel("Amount",fontweight='bold',color='black',fontsize='15')  # add Y-axis label
    plt.title(exp,color='blue',fontweight='bold',fontsize='25')
    plt.xticks(rotation = 25)
    plt.grid()
    pred=[]
    predicted=predictNext.predictAmt(exp)
    for i in predicted:
       for j in i:
          pred.append(int(j))
   #  print(pred)
    pred_amt= pred_amt+pred
   #  print(pred_date)
   #  print(pred_amt)
    plt.plot(pred_date, pred_amt,"-o",color='green')

    #plotting graph for predictions


    plt.show()
#  except:
#     print("Category not found... Please provide the correct category")


def get_category(mycol):
     c=mycol.distinct("Category")
     print(c)


    

    
