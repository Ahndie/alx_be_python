# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. View shopping list")
    print("2. Add item to the list")
    print("3. Remove item from the list")
    print("4. Clear the list")
    print("5. Exit")

def view_shopping_list(shopping_list):
    if not shopping_list:
        print("\nYour shopping list is empty.")
    else:
        print("\nYour shopping list:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

def add_item(shopping_list):
    item = input("\nEnter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Invalid item. Please enter a valid item.")

def remove_item(shopping_list):
    view_shopping_list(shopping_list)
    if shopping_list:
        try:
            item_index = int(input("\nEnter the number of the item to remove: "))
            if 1 <= item_index <= len(shopping_list):
                removed_item = shopping_list.pop(item_index - 1)
                print(f"'{removed_item}' has been removed from the list.")
            else:
                print("Invalid number. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def clear_list(shopping_list):
    shopping_list.clear()
    print("\nShopping list cleared.")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        try:
            choice = int(input("\nSelect an option (1-5): "))
            if choice == 1:
                view_shopping_list(shopping_list)
            elif choice == 2:
                add_item(shopping_list)
            elif choice == 3:
                remove_item(shopping_list)
            elif choice == 4:
                clear_list(shopping_list)
            elif choice == 5:
                print("\nExiting the shopping list manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
