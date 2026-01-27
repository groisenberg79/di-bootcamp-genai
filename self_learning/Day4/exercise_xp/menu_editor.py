from menu_item import MenuItem
from menu_manager import MenuManager as man

def process_string(string: str) -> str:
    word_list = string.strip().title().split()
    return " ".join(word_list)

def is_int(string: str) -> bool:
    try:
        int(string)
        return True
    except (ValueError, TypeError):
        return False

def show_user_menu():
    print("Welcome to the Restaurant Manager!\n")
    while True:
        print("Select one of the options:\n")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit the Manager\n")

        user_option = input(">> ").strip().upper()

        if user_option not in {"V", "A", "D", "U", "S", "E"}:
            print("Invalid option.\n")
            continue

        if user_option == "E":
            print()
            show_restaurant_menu()
            print("\nThanks for using the Restaurant Manager!")
            break

        if user_option == "V":
            print()
            user_item = input("Enter the name of the item: ")
            proc_name = process_string(user_item)
            item = man.get_by_name(proc_name)
            if item is None:
                print("\nThis item is not on the menu.\n")
            else:
                print(f"Item: {item.name} | Price: ${item.price}\n")
            continue

        if user_option == "A":
            add_item_to_menu()

        if user_option == "D":
            remove_item_from_menu()

        if user_option == "U":
            update_item_from_menu()

        if user_option == "S":
            show_restaurant_menu()


def add_item_to_menu() -> None:
    print()
    item_name = input("Enter the name of the item: ")
    proc_name = process_string(item_name)

    item_price = input("Enter price of item: ")
    if not is_int(item_price):
        print("Invalid price (must be an integer).\n")
        return

    new_item = MenuItem(proc_name, int(item_price))
    if new_item.save():
        print("Item was added successfully.\n")
    else:
        print("Item already exists in menu.\n")


def remove_item_from_menu() -> None:
    print()
    item_name = input("Enter the name of the item: ")
    proc_name = process_string(item_name)

    item = man.get_by_name(proc_name)
    if item is None:
        print("\nItem not in the menu.\n")
        return

    if item.delete():  # returns deleted row tuple or None
        print("\nItem was successfully removed from menu.\n")
    else:
        print("\nUnable to remove the item.\n")


def update_item_from_menu() -> None:
    print()
    old_name = input("Enter the name of the item in the menu you wish to change: ")
    proc_old_name = process_string(old_name)

    old_price = input("Enter the price of the item you wish to change: ")
    if not is_int(old_price):
        print("Invalid price.\n")
        return

    new_name = input("Enter the new name: ")
    proc_new_name = process_string(new_name)

    new_price = input("Enter the new price: ")
    if not is_int(new_price):
        print("Invalid price.\n")
        return

    item = MenuItem(proc_old_name, int(old_price))
    if item.update(proc_new_name, int(new_price)):
        print("Item updated successfully.\n")
    else:
        print("Unable to update item.\n")


def show_restaurant_menu() -> None:
    menu = man.all_items()  # returns list[MenuItem]
    if not menu:
        print("\n(Menu is empty)\n")
        return
    print()
    for item in menu:
        print(f"Item: {item.name} | Price: ${item.price}")
    print()


if __name__ == "__main__":
    show_user_menu()

