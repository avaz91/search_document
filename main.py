import inquirer
from script import search_document,search_number

while True:
    questions = [
    inquirer.List('select',
                    message="What would you like to do?",
                    choices=['1.Search for documents', '2.Read documents', '3.Quit'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers["select"]=="1.Search for documents":
        word = input("Enter search word: ")
        search_document(word)
        continue
    if answers["select"]=="2.Read documents":
        number = int(input("Enter document number: "))
        print("Document #",number)
        search_number(number)
        continue
    if answers["select"]=="3.Quit":
        exit()