text = input('Hey, mate, just write something ')
print("okay, let's go")
if text.isdigit():
    if int(text) % 2 == 0:
        print(f"Number {text} is even number")
    else:
        print(f"Number {text} is odd number")
else:
    print(f" {text} {len(text)} letters long")
