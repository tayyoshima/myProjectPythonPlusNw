food = []
while True:
    order = input("Your order: ")
    if order == "exit":
        break
    food.append(order)
    print(food)
print("Summary order",food)