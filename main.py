print("Hello! I`m your contacts helper")
notebook = {}


def input_error(func):
    def inner1(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as error:
            print("Something went wrong", error)

    return inner1


@input_error
def add_contact(notebook):
    name = input("Enter user name: ")
    phone_number = input("Give me phone please: ")
    if name not in notebook:
        notebook[name] = phone_number
    else:
        raise ValueError("This contact already exists")


@input_error
def change_contact(notebook):
    name = input("Enter user name: ")
    if name in notebook:
        print(notebook[name])
        change_number = input("Enter new phone number: ")
        notebook[name] = change_number
    else:
        raise KeyError("Don`t find this contact")


@input_error
def find_contact(notebook):
    name = input("Enter user name: ")
    if name in notebook:
        print(notebook[name])
    else:
        raise KeyError("Don`t find this contact")
    print(notebook)


@input_error
def show_all_contact(notebook):
    for name, phone_number in notebook.items():
        print(f"{name}: {phone_number}")


while True:
    answer = input(
        "Add new contact [Add]\n"
        "Change number in existing contact [Change]\n"
        "Find number by name [Phone]\n"
        "Show all contacts information [Show]\n"
        "Stop bot [Good bye, close or exit]\n"
    )
    answer = answer.lower()
    if answer == "add":
        add_contact(notebook)
    elif answer == "change":
        change_contact(notebook)
    elif answer == "phone":
        find_contact(notebook)
    elif answer == "show":
        show_all_contact(notebook)
    elif answer in ["Good bye", "close", "exit"]:
        print("Good bye")
        break
