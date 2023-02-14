import datetime

import json

filename = "phonebook.json"

try:
    with open(filename, "r") as f:
        phone_book = json.load(f)
except FileNotFoundError:
    phone_book = {}

def stats():
    return len(phone_book)

def add(name, number):
    phone_book.update({name: number})
    print(f'{name} is in phone book from now')
    with open(filename, "w") as f:
        json.dump(phone_book, f)

def delete_contact(name):
    phone_book.pop(name)
    print(f' {name} is removed')
    with open(filename, "w") as f:
        json.dump(phone_book, f)

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




def decorator(func):
    def wrapper(*args, **kwargs):
        with open('decoratorLogs.txt', 'a') as dl:
            dl.write(f'{func.__name__} called at {datetime.datetime.now()}\n')
        return func(*args, **kwargs)
    return wrapper


