import db
import month
import cdate
import pandas as pd
import expenseStatistics
import chart 



# res1=db.CurrentYear()
res1=chart.categoryExpense()
res2=month.currentMonth()
res3=cdate.currentDate()
a=[res1,res2,res3]
myvar = pd.Series(a, index = ["categoryExpense", "CurrentMonth", "CurrentDate"])
print("==========Year,Month and Day Expense==========")
print(myvar)
print("==============================================")


while True:
    print("==========Particular Expense Tracker==============")
    print("1.Check category Expense")
    print("2.Check most Expense ")
    print("3.Check least Expense ")
    print("4.Exit")

    ch=int(input("Enter a choice"))
    if(ch==1):
        print("===================================================")
        cat=expenseStatistics.categoryExpense()
        # cat=chart.categoryExpense()
        print(cat)
        print("===================================================")
    elif(ch==2):
        print("===================================================")
        exp=expenseStatistics.highestExpense()
        print(exp)
        print("===================================================")
    elif(ch==3):
        print("===================================================")
        mexp=expenseStatistics.minExpense()
        print(mexp)
        print("===================================================")
    elif(ch==4):
        exit    
    else:    
        print("Invalid choice")
                    

   