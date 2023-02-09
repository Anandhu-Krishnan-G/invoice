import qrcode
from datetime import datetime  

#  Return the current date of the system   
Current_date = datetime.now().date()   
print("The current date is :", Current_date)
Current_time = datetime.now().time()   
print("The current time is :", Current_time)
print("\n")
name=input("Enter the name of the customer ")
print("customer name:",name)
number_item=int(input("Enter the total number of items "))
cost=0
for item in range(number_item):
    name_item=input(f"Enter the name of item{item+1} ")
    item_cost=int(input(f"Enter the cost of {name_item} "))
    print("\n")
    cost=cost+item_cost
print(f"The total amount is :${cost}")

print("You can also view the total amount by scanning the below Qr code")
athentha=qrcode.QRCode()
athentha.add_data(cost)
athentha.print_ascii()
print("Thank you wisit again")