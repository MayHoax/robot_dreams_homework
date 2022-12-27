phone_book = {'George': 380684473465, 'Daria': 380986621468}

# while True:
#     command_input = input("Enter a command: ").lower()
#     match command_input:
#         case "stats":
#             print(len(phone_book))
#
#         case "list":
#             for i in phone_book.keys():
#                 print(i)
#
#         case "add":
#             name = input("Write name: ")
#
#             if name in phone_book.keys():
#                 print("Name already taken")
#                 continue
#
#             number = input("Write phone number: ")
#             phone_book.update({name: number})
#
#             print(f'{name} is in phone book from now')
#
#         case "delete":
#             name = input("Write name which u want to remove: ")
#             if name not in phone_book.keys():
#                 print("there is no contact with provided name")
#                 continue
#             phone_book.pop(name)
#             print(f' {name} is removed')
#
#         case "show":
#             name = input("Write name you want to see: ")
#             if name not in phone_book.keys():
#                 print("there is no contact with provided name")
#                 continue
#             print(name, phone_book.get(name))
#
#         case _:
#             print("SORRY CAN'T UNDERSTAND")


def stats():
    return len(phone_book)

def add(name, number):
    phone_book.update({name: number})
    print(f'{name} is in phone book from now')

def delete_contact(name):
    phone_book.pop(name)
    print(f' {name} is removed')


def list_all_contacts():
    for i in phone_book.keys():
        yield i

def show_name_info(name):
    print(name, phone_book.get(name))

def name_is_taken(name):
    return name in phone_book.keys()


while True:
    command_input = input("Enter a command: ").lower()
    match command_input:
        case "stats":
            print(stats())

        case "list":
            gen = list_all_contacts()
            for i in gen:
                print(i)

        case "add":
            name = input("Write name: ")

            if name_is_taken(name):
                print("Already taken")
                continue

            number = input("Write phone number: ")

            add(name, number)

        case "delete":
            name = input("Write name u want to remove: ")
            if not name_is_taken(name):
                print("There is no contact with provided name")
                continue
            delete_contact(name)

        case "show":
            name = input("Write name you want to see: ")
            if not name_is_taken(name):
                print("there is no contact with provided name")
                continue
            show_name_info(name)

        case _:
            print("SORRY CAN'T UNDERSTAND")