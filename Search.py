
import pandas as pd
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]



def Search():
        print("===========Search Particular Expense===========")
        ch=mycol.find({"Category":"Fashion"},{"Amount":1,"_id":0})
        print(ch)
        # total_amt=[]
        for i in ch:
                print(i)
        #  total_amt.append(i['Amount'])
Search()        
    