from datetime import datetime, timedelta
date_format = "%d-%m-%Y"

current_date = datetime.now().date().strftime("%d-%m-%Y")
print('Текущая дата: ', current_date)
deadline_date = input('Введите дату дедлайна (в формате: день-месяц-год,'
                          'например "19-01-2025"): ')












