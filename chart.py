import dataclasses
import keyword
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
plt.hist(key,data)
plt.ylabel("category")
plt.xlabel("Expense")
plt.show()
categoryExpense()    
    