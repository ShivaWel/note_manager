username = input('Введите имя пользователя: ')
print(username)

title = input('Введите заголовок проекта: ')
print(title)

title1 = input('1.Введите область проекта: ')
title2 = input('2.Введите тему проекта: ')
title3 = input('3.Введите предмет проекта: ')
titles = [title1, title2, title3]
print("Область проекта: ", titles[0])
print("Тема проекта: ", titles[1])
print("Предмет проекта: ", titles[2])

content = input('Введите описание заметки: ')
print(content)

status = input('Введите статус заметки: ')
print(status)

created_date = input('Дата создания заметки (в формате: число-месяц-год): ')
print(created_date[0:5])

issue_date = input('Дата истечения заметки (в формате: число-месяц-год): ')
print(issue_date[0:5])

note = [username, title, titles, content, status, created_date, issue_date]
print(note)
