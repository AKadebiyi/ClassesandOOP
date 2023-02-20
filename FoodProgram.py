import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0
xaction_list = []
discount_total = 0

# customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)
customer = fc.Customer(
    569,
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True,
)
print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for i in dict:
    xaction = fc.Transaction(dict[i][0], dict[i][1], dict[i][2], dict[i][3])
    if customer.get_customerid() == xaction.get_customerid():
        if customer.get_member_status() == True:
            order_total += float(xaction.get_cost())
            discount_total += float(xaction.get_cost()) * 0.2
            xaction_list.append(f"Order Item: {dict[i][1]} Price: ${dict[i][2]}")
        else:
            order_total += xaction.get_cost()
            xaction_list.append(f"Order Item: {dict[i][1]} Price: ${dict[i][2]}")

for x in xaction_list:
    print(x)

if customer.get_member_status() == False:
    print(f"Total Cost: ${order_total}")
else:
    print(
        f"Total Cost: ${order_total:.2f}\nMember Discount: ${discount_total:.2f}\nTotal Cost after discount: ${order_total - discount_total:.2f}"
    )
