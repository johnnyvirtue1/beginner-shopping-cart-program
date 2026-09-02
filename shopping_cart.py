total=0
while True:
    item=input(
        "\nwhat would you like to order?"
        "\n1.pen \n2.pencil\n3.book\n4.copy \n5.bag \n6.charger \n7.chips \n8.coke \n= "
    ).lower()
    if item=="pen":
        price=10
    elif item=="copy":
        price=70
    elif item=="pencil":
        price=5
    elif item=="book":
        price=900
    elif item=="charger":
        price=400
    elif item=="bag":
        price=500
    elif item=="chips":
        price=20
    elif item=="coke":
        price=40
    else:
        print("\ninvalid item")
        continue
    quantity=int(input("how many would you like to order = "))
    total_item=quantity*price
    total+=total_item
    print(f"{quantity} {item}(s) has beed added ")
    print(f"your current total is {total}₹")
    another_item=input("is there anything you would like to order (yes/no) \n=").lower()
    if another_item!="yes":
        break
print("\n-------------------------")
print(f"your final total is {total}₹")
if total <=10000:
    print("thank you for shopping 🤡")
else:
    print("thank you for shopping 🗿")
print("---------------------------")
