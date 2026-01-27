from menu_item import MenuItem
from menu_manager import MenuManager as man

def process_string(string: str) -> str:
    """
    strip string of trailing white space characters,
    title case all words and reduce sequences of blank spaces to a single space.
    
    :param string: a (multi-)word literal
    :type string: str
    :return: properly processed string
    :rtype: str
    """
    word_list = string.strip().title().split()
    return ' '.join(word_list)

def is_float(string: str) -> bool:
    try:
        float(string)
        return True
    except (ValueError, TypeError):
        return False


def show_user_menu():
    print('Welcome to the Restaurant Manager!')
    print()
    while True:
        print('Select one of the options:')
        print()
        print('(V) View an Item')
        print('(A) Add an Item')
        print('(D) Delete an Item')
        print('(U) Update an Item')
        print('(S) Show the Menu')
        print('(E) Exit the Manager')
        print()

        user_option = input('>> ').strip().upper()

        if user_option not in {'V', 'A', 'D', 'U', 'S', 'E'}:
            print('Invalid option.')
            print()
            continue
        
        # exit the program
        if user_option == 'E':
            print()
            show_restaurant_menu()
            print()
            print('Thanks for using the Restaurant Manager!')
            break

        # get an item from the menu
        if user_option == 'V':
            print()
            user_item = input('Enter the name of the item: ')
            item = man.get_by_name(user_item)
            if item is None:
                print()
                print('This item is not on the menu.')
                print()
                continue
            else:
                print(f"Menu item: {item[0]} | Price: {item[1]} ")
                print()
                continue
        
        # add an item to the menu


def add_item_to_menu() -> None:
    print()
    item_name = input('Enter the name of the item: ')
    proc_name = process_string(item_name)

    item_price = input('Enter price of item: ')
    if is_float(item_price):
        new_item = MenuItem(proc_name, float(item_price))
        if new_item.save():
            print('Item was added successfully.')
            print()
        else:
            print('Item already exists in menu.')
            print()
    else:
        print('Invalid price (must be a number).')
        print()
        


    

def remove_item_from_menu():
    pass

def update_item_from_menu():
    pass

def show_restaurant_menu():
    pass

