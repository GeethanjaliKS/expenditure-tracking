import pymongo
import datetime

def currentMonth():
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["Expense_Trackerdb"]

  mycol = mydb["expense"]
  d=mycol.find()

# today = datetime.now()

  
# print("Current Date and Time :", today)
# print("Current Month :", today.month)

#provide month number
# month_num = "6"
# datetime_object = datetime.datetime.strptime(month_num, "%m")

# month_name = datetime_object.strftime("%b")
# print("Short name: ",month_name)

# 



  currentDateTime = datetime.datetime.now()
  date = str(currentDateTime.date())
  # print(date)
  y=date[0:7]
  # print(y)
#  year = date.strftime("%Y")
  dt=y+'-1'
  # print(dt)
  sum=0 
  for i in d:
   if i['Date']>=dt:
    sum=sum+(i['Amount'])
  return sum   


