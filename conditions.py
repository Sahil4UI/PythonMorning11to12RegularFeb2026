#MATCH CASE
msg = '''
Press 1 to Order Pizza
Press 2 to Order Burger
Press 3 to Order Dessert
'''
choice = int(input(msg))
match choice:
    case 1:print("Pizza Ordered Successfully...")
    case 2:print("Burger Ordered Successfully...")
    case 3:print("Dessert Ordered Successfully...")
    case _:print("Invalid Choice")
