# shopping_list_manager.py

def display_menu():
    print(f"\nShopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View Shopping List")
    print(f"4. Clear List")
    print(f"5. Exit")

def view_shopping_list(shopping_list):
    if not shopping_list:
        print(f"\nYour shopping list is empty.")
    else:
        print(f"\nYour shopping list:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

def add_item(shopping_list):
    item = input(f"\nEnter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print(f"Invalid item. Please enter a valid item.")

def remove_item(shopping_list):
    view_shopping_list(shopping_list)
    if shopping_list:
        try:
            item_index = int(input(f"\nEnter the number of the item to remove: "))
            if 1 <= item_index <= len(shopping_list):
                removed_item = shopping_list.pop(item_index - 1)
                print(f"'{removed_item}' has been removed from the list.")
            else:
                print(f"Invalid number. Please select a valid item number.")
        except ValueError:
            print(f"Invalid input. Please enter a number.")

def clear_list(shopping_list):
    shopping_list.clear()
    print(f"\nShopping list cleared.")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        try:
            choice = int(input(f"\nSelect an option (1-5): "))
            if choice == 1:
                add_item(shopping_list)
            elif choice == 2:
                remove_item(shopping_list)
            elif choice == 3:
                view_shopping_list(shopping_list)
            elif choice == 4:
                clear_list(shopping_list)
            elif choice == 5:
                print(f"\nExiting the shopping list manager. Goodbye!")
                break
            else:
                print(f"Invalid choice. Please select a valid option.")
        except ValueError:
            print(f"Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
