text = input("Okay, let's check your text")
for i in text:
    if i.isdigit():
        if int(i) % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
    elif i.isalnum():
        if i.isupper():
            print(i, "is UPPER")
        else:
            print(i, "is lower")
    else:
        print("That's a symbol")