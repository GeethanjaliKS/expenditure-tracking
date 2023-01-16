import datetime
import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import numpy as np


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]
def categoryExpense():

  d=mycol.find({},{"Category":1,"Amount":1,"_id":0,"Date":1})
  key=[]
  data=[]
  currentDateTime = datetime.datetime.now()
  date = str(currentDateTime.date())
  # print(date)
  y=date[0:4]
  # y=date[0:7]
  # print(y)
  
  # print(dt)
#  year = date.strftime("%Y")
  dt=y+'-01-01'
  # dt=y+'-1'
  for i in d:
    if i['Date']>=dt:
      key.append(i['Category'])
      data.append(i['Amount'])
  df = pd.DataFrame({'Category': key,'Amount': data}, columns=['Category', 'Amount'])
  res=df.groupby('Category').sum().reset_index()
  # print(res.Category)
  col_cat=list(res["Category"])
  print(col_cat) 
  col_amt=list(res["Amount"])
  print(col_amt) 
  # x=[key]
  # y=[data]  
  
  figure, axis = plt.subplots(2)
  y_pos=np.arange(len(col_amt))
  axis[0].set_title("YEARLY EXPENSE",fontweight='bold',color="#4DBEEE",fontsize='25')
  axis[0].bar(y_pos,col_amt,color='#000099')

  for i in range(len(y_pos)):
           axis[0].text(i,col_amt[i],col_amt[i])

  axis[0].set_xticks(y_pos,col_cat,color='red',fontsize='10',horizontalalignment='right',rotation=2)
  axis[0].set_xlabel("Category",fontweight='bold')
  axis[0].set_ylabel("Expense",fontweight='bold')
  # plt.show()
  
  # monthly chart
  d=mycol.find({},{"Category":1,"Amount":1,"_id":0,"Date":1})
  key=[]
  data=[]
  currentDateTime = datetime.datetime.now()
  date = str(currentDateTime.date())
  y=date[0:7]
  print(y)
  dt=y+'-01'
  de=y+'-31'
  print(dt)
  for i in d:
    if i['Date']>=dt and i['Date']<=de:
      key.append(i['Category'])
      data.append(i['Amount'])
  df = pd.DataFrame({'Category': key,'Amount': data}, columns=['Category', 'Amount'])
  res=df.groupby('Category').sum().reset_index()
  # print(res.Category)
  col_cat=list(res["Category"])
  print(col_cat) 
  col_amt=list(res["Amount"])
  print(col_amt) 
  y_pos=np.arange(len(col_amt))
  axis[1].set_title("MONTHLY EXPENSE",fontweight='bold',color='#4DBEEE',fontsize='25')
  axis[1].bar(y_pos,col_amt,color='#660033')

  for i in range(len(y_pos)):
        axis[1].text(i,col_amt[i],col_amt[i])

  axis[1].set_xticks(y_pos,col_cat,color='red',fontsize='10',horizontalalignment='right',rotation=2)
  axis[1].set_xlabel("category",fontweight='bold')
  axis[1].set_ylabel("Expense",fontweight='bold')
  # plt.xticks(x,key,color='red',fontweight='bold',fontsize='17' )
  plt.tight_layout()
  plt.show()
categoryExpense()    
    