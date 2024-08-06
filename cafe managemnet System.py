# Cafe Management System


# items to be served 
menu = {
   "coffee" : 60,
   "Tea" : 40,
   "Burger" : 70,
   "Sandwiches" : 80,
   "Salads" : 60,
   "Pancakes" : 100,
   "Pizza" : 120

}

print("Welcome to our Python Cafe!")
print("Here is the Menu ")

print("coffee : 60rs\nTea : 40rs\nBurger : 70rs\nSandwiches : 80rs\nSalads : 60rs\nPancakes : 100rs\nPizza : 120rs")

item_1 = input("What would you like to order : ")  #asking the user to add items from menu

order_bill = 0   #bill amount
if(item_1 in menu):
    order_bill += menu[item_1]
    print(f"Your order for {item_1} is added")
else:
    print(f"Your order for {item_1} is not avaliable")
    print(f"Your total amount is {order_bill}")

# asking the user if he wants to order anything else

another_choice = input("Do you want to order anything else ? (Yes/No): ")
if another_choice == "Yes":
    item_2 = input("What would you like to order : ")
    print(f"Your order for {item_2} is added")
    if(item_2 in menu):
      order_bill += menu[item_2]
      print(f"Your total amount is {order_bill}Rs")

else:
    print(f"Your total amount is {order_bill}Rs")

print("Thanks for placing your order")

    


