#initialize the dictionary
stock_infor = {}


# add items to the dictionary
def add_items(item_name="coins", item_quantity=10):
  item_name = input(
      "Please enter the item name: ").strip().lower()  # avoid case sensitive
  item_quantity = int(input(
      "Please enter the quantity of the item: "))  # convert string to integer
  if not item_name:  # if no input, use default values
    item_name = "coins"
    item_quantity = 10

  if item_name in stock_infor:  #update the value if item in stock
    stock_infor[item_name] += item_quantity
  else:  #if new item, just add quantity into system
    stock_infor[item_name] = item_quantity


# remove items from the dictionary
def remove_items():
  item_name = input("Enter the item name to remove: ").strip().lower()
  if item_name in stock_infor:  # check if the item in system
    del stock_infor[item_name]  # if yes, delete it
    print(f"The item '{item_name}' has been removed from the stock.")
  else:
    print(f"The item '{item_name}' is not in the stock.")


# print values of a specific item in the dictionary
def print_value(item_name):
  item_name = item_name.strip().lower()
  if item_name not in stock_infor:  # check if the item in system
    print(f"The item {item_name} is not in stock.")
  else:
    print(f"The inventory of {item_name} are: {stock_infor[item_name]}")


# print all items in the dictionary
def print_all():
  if not stock_infor:  # check if the system empty
    print("The inventory is empty.")
  else:  # iterate the dictionary and print all items
    for i, (item, quantity) in enumerate(stock_infor.items(), start=1):
      print(f"{i}: Item name is: {item}, and the quantity are: {quantity}")


print("Welcome to the inventory system!")

while True:
  print("Please choose one of the following options: ")
  print("1. Add items")
  print("2. Print the value of an item")
  print("3. Print all the items and quantities in the system")
  print("4. Remove an item")
  print("5. Quit")

  choice = input()
  if choice == "1":
    add_items()
    print("\n")
  elif choice == "2":
    key = input("Please enter the item name: ")
    print_value(key)
    print("\n")
  elif choice == "3":
    print_all()
    print("\n")
  elif choice == "4":
    remove_items()
    print("\n")
  elif choice == "5":
    print("Goodbye!")
    break
  else:
    print("Invalide choice. Please try again.")

print("Program ended!")
