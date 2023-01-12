import db
import month
import cdate
import pandas as pd

res1=db.CurrentYear()
res2=month.currentMonth()
res3=cdate.currentDate()
a=[res1,res2,res3]
myvar = pd.Series(a, index = ["CurrentYear", "CurrentMonth", "CurrentDate"])
print(myvar)