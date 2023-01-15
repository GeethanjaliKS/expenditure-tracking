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
  axis[0].bar(y_pos,col_amt)
  axis[0].set_xticks(y_pos,col_cat)
  axis[0].set_xlabel("category")
  axis[0].set_ylabel("Expense")
  # plt.show()
  
  
  d=mycol.find({},{"Category":1,"Amount":1,"_id":0,"Date":1})
  key=[]
  data=[]
  currentDateTime = datetime.datetime.now()
  date = str(currentDateTime.date())
  y=date[0:7]
  print(y)
  dt=y+'-01'
  print(dt)
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
  y_pos=np.arange(len(col_amt))
  axis[1].bar(y_pos,col_amt)
  axis[1].set_xticks(y_pos,col_cat)
  axis[1].set_xlabel("category")
  axis[1].set_ylabel("Expense")
  # plt.xticks(x,key,color='red',fontweight='bold',fontsize='17' )
  plt.show()
categoryExpense()    
    