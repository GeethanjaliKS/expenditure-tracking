import pandas as pd
import pymongo
import matplotlib.pyplot as plt
import numpy as np


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]
def categoryExpense():

  d=mycol.find({},{"Category":1,"Amount":1,"_id":0})
  key=[]
  data=[]
  for i in d:
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
  
   
  y_pos=np.arange(len(col_amt))
  plt.bar(y_pos,col_amt)
  plt.xticks(y_pos,col_cat)
  plt.xlabel("category")
  plt.ylabel("Expense")
  # plt.xticks(x,key,color='red',fontweight='bold',fontsize='17' )
  plt.show()
categoryExpense()    
    