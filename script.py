import string
def search_document(word):
        indexes = []
        with open("ap_docs.txt","r") as f:
            list = f.read().split("<NEW DOCUMENT>")
            word = word.split(" ")
            for index,value in enumerate(list):
                allExists = True
                for i in string.punctuation:
                    line = value.replace(i,'')
                for i in word:
                    if i.lower() not in line.lower():
                        allExists =False
                        break
                if allExists:
                    indexes.append(index)
            print(set(indexes)) 
def search_number(number):
    with open("ap_docs.txt","r") as f:
        list = f.read().split("<NEW DOCUMENT>")
        for index,value in enumerate(list):
            if index == number:
                print(value)
            else:
                print("Wrong number!")

