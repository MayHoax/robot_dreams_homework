import re

while True:
    filename = input("What file do I need to read? \n")
    try:
        with open(filename) as f:
            filedata = f.read()
            email_regex = r'[\w\.-]+@[\w\.-]+'
            emails = re.findall(email_regex, filedata)
            for email in emails:
                filedata = filedata.replace(email, "*@*")
            print(filedata)
    except FileNotFoundError:
        print(f"There are no files with {filename} name")


