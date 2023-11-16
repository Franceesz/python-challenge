import os
import csv

bank_csv=os.path.join('budget_data.csv')

with open(bank_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

    total_months=[]
    profit=[]
    change_profit=[]   

    for row in csvreader:
       total_months.append(row[0])
       profit.append(int(row[1]))
       sum_months=len(total_months)
       sum_profit=sum(profit)

    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
        
monthly_change=sum(change_profit)/len(change_profit)
max_increase=max(change_profit)
max_decrease=min(change_profit)
increase_month=total_months[change_profit.index(max_increase)+1]
decrease_month=total_months[change_profit.index(max_decrease)+1]

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {sum_months}")
print(f"Total: ${sum_profit}")
print(f"Average Change : ${round((monthly_change),2)}")
print(f"Greatest Increase in Profits: {increase_month}  (${max_increase})")
print(f"Greatest Decrease in Profits: {decrease_month}  (${max_decrease})")
    
with open("output.txt", "wt") as new:
    new.write("Financial Analysis\n")
    new.write("------------------------\n")
    new.write(f"Total Months: {sum_months}\n")
    new.write(f"Total: ${sum_profit}\n")
    new.write(f"Average Change : ${round((monthly_change),2)}\n")
    new.write(f"Greatest Increase in Profits: {increase_month}  (${max_increase})\n")
    new.write(f"Greatest Decrease in Profits: {decrease_month}  (${max_decrease})\n")



  



