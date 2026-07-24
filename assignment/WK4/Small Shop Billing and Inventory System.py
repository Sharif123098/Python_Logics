def process_order(inventory, cart):
    total_bill = 0
    print("---- Bill ----")

    for item, quantity in cart.items():
        if item in inventory:
            if quantity <= inventory[item]["stock"]:
                cost = inventory[item]["price"] * quantity
                total_bill += cost
                inventory[item]["stock"] -= quantity
                print(f"{item} x{quantity} = NPR {cost}")
            else:
                print(f"Sorry, not enough stock for {item}")
        else:
            print(f"Sorry, {item} not available")

    print(f"Grand Total: NPR {total_bill}")
    print("--------------")

    stock_list = []
    for item, details in inventory.items():
        stock_list.append(f"{item}={details['stock']}")
    print(f"Updated stock: {', '.join(stock_list)}")


inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

process_order(inventory, cart)
