import re

while True:
    open_write = int(input('выберите действие: \n'
                           '1-Считать имена и фамилии \n'
                           '2-Считать все емайлы\n'
                           '3-Считать названия файлов\n'
                           '4-Считать цвета\n'
                           '5-Выход\n'))
    if open_write == 1:
        with open('MOCK_DATA.txt', 'r') as file:
            names = []
            for i in file:
                names.append(*re.findall(r'(\b[A-Z][a-zA-Z\.\'\-]+[\s]+[a-zA-Z\.\'\- ]+\b)', i))
            with open('names.txt', 'w') as name:
                for i in names:
                    name.write(f'{i}\n')
        print('файл успешно записан')
    elif open_write == 2:
        with open('MOCK_DATA.txt', 'r') as file:
            mail = file.read()
            emails = re.findall(r'[\w]+@[\w.]+', mail)
            with open('emails.txt', 'w') as f:
                for i in emails:
                    f.write(f'{i} \n')
        print('файл успешно записан')
    elif open_write == 3:
        with open('MOCK_DATA.txt', 'r') as file:
            note = []
            for i in file:
                note.append(*re.findall(r'\s[A-Za-z]+\.[A-Za-z]+', i))
            with open('files.txt', 'w') as f:
                for i in note:
                    f.write(f'{i}\n')
        print('файл успешно записан')
    elif open_write ==4:
        with open('MOCK_DATA.txt', 'r') as file:
            data = file.read()
            colors = re.findall(r'#[a-f0-9]+', data)
            with open('colors.txt', 'w') as f:
                for i in colors:
                    f.write(f'{i}\n')
        print('файл успешно записан')

    elif open_write == 5:
        print('Выход из программы успешно завершен')
        break

    else:
        print('Ввкдите актуальные команды!!!\n')




