store_items = {
    "apple": 2,
    "banana": 1,
    "chocolate": 3,
    "bread": 4,
    "milk": 5,
    "eggs": 6,
    "cheese": 8
}
wallet = int(input("What is  the amount of money in your wallet: "))
affordable_items = []
for item, price in store_items.items():
    if price <= wallet:
        affordable_items.append(item)
affordable_items.sort()
if affordable_items:
    print(f"You can afford: {affordable_items}")
else:
    print("Nothing")