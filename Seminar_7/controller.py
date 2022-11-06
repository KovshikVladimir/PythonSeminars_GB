import view

fil = '/Users/Swidi/Desktop/GBPythonSemnars_HomeWork/Seminar_7/final_file.txt'

def importer():
    a = view.get_name()
    b = view.get_number()
    c = view.get_description()
    global fil
    with open(fil,'a') as f:
        f.writelines(f'{a} - {b} : {c}\n\n')

def exporter():
    global fil
    word = view.get_keyword()
    with open(fil,'r') as f:
        readfile = f.readlines()
        for line in readfile:
            if word in line:
                print(line)
            # else:
            #     print('слова нет')
            #     break
    