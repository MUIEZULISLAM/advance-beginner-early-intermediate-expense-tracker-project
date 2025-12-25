def add_expense():
    with open("expenses.txt","a") as f:
        while True:
            item=input("enter item :").strip().lower()
            if item=="no":
                break
            category=input("enter catigory of item e.g travelling,shopping,food etc :")
            price=int(input("enter expense of added item"))
            f.write(f"{item},{category},{price}\n")
def view_expenses():            
    with open("expenses.txt","r") as f:
        print(f.read())
def total_expense():        
    with open("expenses.txt","r") as f:
        total=0
        for line in f:
            line=line.strip()
            item,catigory,price=line.split(",")
            price=int(price)
            total+=price
        print(f"your total expense is {total}!")
def catigory_wise_total():            
    with open("expense.txt","r") as f:
        total=0
        category=input("enter catigory you want to know expense :").strip().lower()
        for line in f:
            line=line.strip()
            item,category1,price=line.split(",")
            price=int(price)
            if category==category1:
                total+=price
        print(f"your searched catigory has expense {total}")
def highest_spend_category():
    with open("expenses.txt","r") as f:
        category_total = {}

        for line in f:
            line = line.strip()
            item, category, price = line.split(",")
            price = int(price)

            if category in category_total:
                category_total[category] += price
            else:
                category_total[category] = price

        highest = max(category_total, key=category_total.get)
        print(f"Highest spending category is {highest}")
        print(f"Amount spent: {category_total[highest]}")

#menu
while True:
 print("1.add expense")
 print("2.view expense")           
 print("3.total expense")
 print("4.catigory wise total")
 print("5.highest spending catigory")
 print("6.exit")
 option=input("enter option of desire ")
 if option=="1":
    add_expense()
 elif option=="2":   
    view_expenses()
 elif option=="3":   
    total_expense()
 elif option=="4":   
    catigory_wise_total()
 elif option=="5":   
    highest_spend_category()
 elif option=="6":
     print("program exited")   
     break



            





