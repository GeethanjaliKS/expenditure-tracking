import db
import month
import cdate
import pandas as pd
import expenseStatistics
import chart 
import perticularExpenseChart
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expense_Trackerdb"]

mycol = mydb["expense"]


res1=db.CurrentYear(mycol)
res2=month.currentMonth(mycol)
res3=cdate.currentDate(mycol)
a=[res1,res2,res3]
myvar = pd.Series(a, index = ["Current Year Expense", "Current Month Expense", "Current Day Expense"])
print("==========Year,Month and Day Expense==========")
print("==============================================")
print(myvar)

while True:
    print("==========Particular Expense Tracker==============")
    print("1.Check category Expense")
    print("2.Check most Expense ")
    print("3.Check least Expense ")
    print("4.Check for perticular expense ")
    print("5.Exit")

    ch=int(input("Enter a choice"))
    if(ch==1):
        print("===================================================")
        # cat=expenseStatistics.categoryExpense()
        cat=chart.categoryExpense(mycol)
        # print(cat)
        print("===================================================")
    elif(ch==2):
        print("===================================================")
        exp=expenseStatistics.highestExpense(mycol)
        print(exp)
        print("===================================================")
    elif(ch==3):
        print("===================================================")
        mexp=expenseStatistics.minExpense(mycol)
        print(mexp)
        print("===================================================")
    elif(ch==4):
        perticularExpenseChart.get_category(mycol)
        exp=input("Enter the expense to search : ")
        perticularExpenseChart.perticularExpense(exp,mycol) 
    elif(ch==5):
        exit   
    else:    
        print("Invalid choice")
                    

   