# Импортируем необходимые модули для работы с датами
from datetime import datetime, date
notes=[]  # создаем список для заметок

# Запрашиваем и вводим данные по заметкам
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
new_note = (input('Создать новую заметку (да/нет)? '))

while new_note.strip() == 'да': # удаление начальных/конечных пробелов
    note = {} # теперь создаем словарь для ввода заметки

# Ввод и проверка формата ввода имени
    while True:  # цикл проверки правильного формата имени
            note["Имя"] = input("Введите Имя пользователя: ")
            if note["Имя"].strip() == "":
                print("Некорректные данные. Повторите ввод.")
            else:
                break  # выход из цикла

# Ввод и проверка формата заголовка
    while True:  # цикл проверки правильного формата имени
        note["Заголовок"] = input("Введите Заголовок заметки: ")
        if note["Заголовок"].strip() == "":
            print("Некорректные данные. Повторите ввод.")
        else:
            break  # выход из цикла
# Ввод и проверка формата ввода описания
    while True:  # цикл проверки правильного формата описания
        note["Описание"] = input("Введите Описание заметки: ")
        if note["Описание"].strip() == "":
            print("Некорректные данные. Повторите ввод.")
        else:
            break  # выход из цикла

# Ввод и проверка формата ввода статуса заметки
    status = ['новая', 'в процессе', 'выполнена']  # список возможных значений заметки
    while True:  # цикл проверки правильного формата ввода статуса заметки
        note["Статус"] = input('Введите Статус заметки (новая; в процессе; выполнена): ')
        if note["Статус"].strip() in status: #проверка существующего статуса
            break  # выход из цикла
        else:
            # Запрашиваем корректный статус заметки
            print("Некорректные данные. Повторите ввод Статус заметки.")

# Ввод и проверка формата ввода даты создания заметки
    while True:  # цикл проверки правильного формата ввода даты создания заметки
        try:
            note["Дата создания"] = input("Введите Дату создания заметки в формате 'день-месяц-год': ")
            datetime.strptime(note["Дата создания"], "%d-%m-%Y")
            break  # выход из цикла
        except ValueError:  # обработка ошибки
            print("Дата некорректна. Повторите ввод Дату создания заметки в требуемом формате.")

    # Ввод и проверка формата ввода даты дедлайна
    while True:  # цикл проверки правильного формата ввода дедлайна
        try:
            note["Дедлайн"] = input("Введите дату истечения заметки (дедлайн) в формате 'день-месяц-год': ")
            datetime.strptime(note["Дедлайн"], "%d-%m-%Y")  # Если строка "Дедлайн" и код формата (%d.%m.%Y),
                                                                   # не совпадают, возникает ошибка ValueError.
            break  # выход из цикла
        except ValueError:  # обработка ошибки
            print("Дата Дедлайна некорректна. Повторите ввод Дедлайна в требуемом формате.")
    notes.append(note)
    new_note = (input('Создать новую заметку (да/нет)?  '))
print('Ввод заметок завершен.')
print(f"Введено заметок - {len(notes)}.")

# Вывод введенных заметок на экран
print("\nСписок заметок.")
for i in range(len(notes)):
    print(f"\nЗаметка № {i+1}: ") # нумерация сохраненных заметок
    for key,value in notes[i].items():# вывод на экран всех данных ключ:значение
            print(key, "-", value )