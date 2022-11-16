fil = '/Users/Swidi/Desktop/GBPythonSemnars_HomeWork/Seminar_10/phone_book.txt'

def importer(a,b,c):
    global fil
    with open(fil,'a') as f:
        f.writelines(f'{a} - {b} : {c}\n\n')

def exporter(word):
    global fil
    with open(fil,'r') as f:
        readfile = f.readlines()
        for line in readfile:
            if word in line:
                print(line)