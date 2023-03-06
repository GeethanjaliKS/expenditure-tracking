import db
import month
import cdate
import pandas as pd
import expenseStatistics
import chart 
import perticularExpenseChart


res1=db.CurrentYear()
res2=month.currentMonth()
res3=cdate.currentDate()
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
        cat=chart.categoryExpense()
        # print(cat)
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
        perticularExpenseChart.get_category()
        exp=input("Enter the expense to search : ")
        perticularExpenseChart.perticularExpense(exp) 
    elif(ch==5):
        exit   
    else:    
        print("Invalid choice")
                    

   