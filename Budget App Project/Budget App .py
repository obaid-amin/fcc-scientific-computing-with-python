
import math



class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger=[]
        self.balance=0

    def prin_category(self) :
        print("this is my category: ",self.category_name)

    def deposit(self,amount,description=''):
        self.balance+=amount
        temp= {"amount": amount, "description": description}
        self.ledger.append(temp)

    def withdraw(self,Wamount,Wdescription=''):
        if self.check_funds(Wamount):
            self.balance -= Wamount
            temp = {"amount": -Wamount, "description": Wdescription}
            self.ledger.append(temp)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance


    def transfer(self,amount,category):
        if self.withdraw(amount,f"Transfer to {category.category_name}"):
            category.deposit(amount,f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def add_withdraw(self,categories):
        add=[]
        total=0
        temp=0
        for x in range(0,(len(categories))):
            temp=0
            for entry in categories[x].ledger:
                if entry["amount"] < 0 :
                    temp+=entry["amount"]
            add.append(temp)
        for k in add:
            total+=k
        for i in add:
            i=round((i/total)*100)
        return add



    def check_funds(self,amount):
        return self.balance >= amount

    def __str__(self):
        temp=self.category_name
        output =temp.center(30, "*") + "\n"
        for item in self.ledger:
            desc = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:>7.2f}"
            output += f"{desc}{amount}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

# Percentage spent by category
# 100|
#  90|
#  80|
#  70|
#  60| o
#  50| o
#  40| o
#  30| o
#  20| o  o
#  10| o  o  o
#   0| o  o  o
#     ----------
#      F  C  A
#      o  l  u
#      o  o  t
#      d  t  o
#         h
#         i
#         n
#         g


def create_spend_chart(categories):
    ip = 100
    add = []
    total = 0
    temp = 0
    for x in range(0, (len(categories))):
        temp = 0
        for entry in categories[x].ledger:
            if entry["amount"] < 0:
                temp += -entry["amount"]
        add.append(temp)
    for k in add:
        total += k
    for i in add:
        i = math.floor((i / total) * 100)

    bar_chart = ""
    bar_chart+="Percentage spent by category\n"
    max_len = max(len(name.category_name) for name in categories)  # longest category name
    while ip >= 0:
        if len(str(ip)) < 3:
            bar_chart += " "
        if len(str(ip)) < 2:
            bar_chart += " "
        bar_chart += str(ip)
        bar_chart += "|"

        for p in add:
            if p >= ip:
                bar_chart += " o "
            else:
                bar_chart += "   "
        bar_chart+="\n"
        ip-= 10
    bar_chart += " " * 4 + "---" * len(categories) + "\n"
    for j in range(max_len):  # row = character index
        bar_chart += "    "  # 5 spaces to align under the chart
        for k in range(len(categories)):  # go through each category
            name = categories[k]
            if j < len(name.category_name):
                bar_chart += " " + name.category_name[j] + " "
            else:
                bar_chart += "   "
        bar_chart += " \n"
    print(bar_chart)



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(1000,'kardia')
clothing.withdraw(100,'hello')
food.transfer(50, clothing)
print(food)
print(clothing)
categories=[food,clothing]
create_spend_chart(categories)
food.add_withdraw(categories)