import random
import os
import csv
from prettytable import PrettyTable

if not os.path.exists('cache.txt'):
    with open('cache.txt', 'w') as f:
        f.write('{}')

with open('cache.txt', 'r') as f:
    items = eval(f.read())


def addItem():
    id = random.randint(1, 9999)
    x = input("Enter Expense: ")
    y = input("Enter the cost: ")

    items[id] = {'expense': x, 'cost': y}


def removeItem():
    x = input("Enter ID of the item to remove: ")
    if x in items:
        del items[x]
    else:
        print("Item not found")


def listItems():
    x = PrettyTable()
    x.field_names = ["ID", "Expense", "Cost"]
    for i in items:
        x.add_row([i, items[i]['expense'], items[i]['cost']])
    print(x)

    input("Press enter to continue")


def exportItems():
    with open('items.csv', 'w') as f:
        csv.writer(f).writerow(['ID', 'Expense', 'Cost'])
        for key in items.keys():
            csv.writer(f).writerow(
                [key, items[key]['expense'], items[key]['cost']])
    print("Items exported to ./items.csv")
    input("Press enter to continue")


def main():
    while True:
        print("\n\n\nWelcome to the Expense Tracker\n\n")
        print("Please select an option from the menu below:\n")
        print("\t1. Add an expense")
        print("\t2. Remove an expense")
        print("\t4. List all expenses")
        print("\t5. Export expenses to a file")
        print("\t6. Exit the program")
        choice = int(input("\n\nEnter your choice: "))
        if choice == 1:
            addItem()
        elif choice == 2:
            removeItem()
        elif choice == 4:
            listItems()
        elif choice == 5:
            exportItems()
        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        with open('cache.txt', 'w') as f:
            f.write(str(items))


main()
