import datetime
import pymongo
def CurrentYear(mycol):
  # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  # mydb = myclient["Expense_Trackerdb"]

  # mycol = mydb["expense"]

# myquery={{"Date":{"$gt":1-1-2023}}}
# mydoc=mycol.find(myquery)
# for x in mydoc:
#   print(x)
  d=mycol.find()
# for i in d:
#   print(i)
# print(datetime.datetime.now())
  currentDateTime = datetime.datetime.now()
  date = str(currentDateTime.date())
  # print(date)
  y=date[0:4]
#  year = date.strftime("%Y")
  dt=y+'-01-01'
  # print(dt)
  sum=0
  for i in d:
    if i['Date']>=dt:
      if(i['Amount']) >= 0:
        sum=sum+(i['Amount'])
  return sum   

# for date in Date():
#   print(date)
  