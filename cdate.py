import pymongo
import datetime
def currentDate(mycol):
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["Expense_Trackerdb"]

    # mycol = mydb["expense"]
    d=mycol.find()

    currentDateTime = datetime.datetime.now()
    date = str(currentDateTime.date())
# print(date)
# y=date[0:7]
# print(y)
#  year = date.strftime("%Y")
# dt=y+'-11'
# print(dt)
    sum=0
    for i in d:
      if i['Date']==date:
        sum=sum+(i['Amount'])
    return sum   
