text = input()
if text.isdigit():
    if int(text) % 2 == 0:
        print(f"Число {text} парное ")
    else:
        print(f"Число {text} непарное")
else:
    print(len(text))