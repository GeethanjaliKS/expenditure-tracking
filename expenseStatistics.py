import pandas as pd
import pymongo
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
  # print(key)
  # print(data)
  df = pd.DataFrame({'Category': key,'Amount': data}, columns=['Category', 'Amount'])
#   print(df)
  res=df.groupby('Category').sum().reset_index()
#   print('----------------------------------------------------')
#   print('EXPENSE BY CATEGORIES')
#   print('----------------------------------------------------')
# #   print(res.mode())
  # print(res)
  return res
categoryExpense()




def highestExpense():
  d=mycol.find({},{"Category":1,"Amount":1,"_id":0})
  key=[]
  data=[]
  for i in d:
    key.append(i['Category'])
    data.append(i['Amount'])
#   print(key)
#   print(data)
  df = pd.DataFrame({'Category': key,'Amount': data}, columns=['Category', 'Amount'])
#   print(df)
  res=df.groupby('Category').sum().reset_index()
#   print(res.mode())
  value=res.query('Amount == Amount.max()')
  
  # print('----------------------------------------------------')
  # print('MOST EXPENSE')
  # print('----------------------------------------------------')
  # # print(value)
  return value

highestExpense()

def minExpense():
  d=mycol.find({},{"Category":1,"Amount":1,"_id":0})
  key=[]
  data=[]
  for i in d:
    key.append(i['Category'])
    data.append(i['Amount'])
#   print(key)
#   print(data)
  df = pd.DataFrame({'Category': key,'Amount': data}, columns=['Category', 'Amount'])
#   print(df)
  res=df.groupby('Category').sum().reset_index()
#   print(res.mode())
  value=res.query('Amount == Amount.min()')
  
  # print('----------------------------------------------------')
  # print('MOST EXPENSE')
  # print('----------------------------------------------------')
  # # print(value)
  return value

minExpense()




