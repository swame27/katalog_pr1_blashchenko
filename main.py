from datetime import date
 
#простые типы данных
title = "Звёздная ночь"
author_name = "Винсент ван Гог"
creation_year = 1889
technique = "масло, холст"
category = "постимпрессионизм"
is_in_permanent_collection = True
 
#текущий год берём из модуля datetime
current_year = date.today().year
 
#операции и преобразование типов 
artwork_age = current_year - creation_year
age_message = "Возраст произведения: " + str(artwork_age) + " лет"
 
#ветвления
def get_period_status(age):
    if age >= 100:
        return "Историческое произведение"
    elif age >= 30:
        return "Произведение классического периода"
    else:
        return "Современное произведение"
 
period_status = get_period_status(artwork_age)
 
if is_in_permanent_collection:
    collection_note = "Находится в постоянной коллекции"
else:
    collection_note = "Не входит в постоянную коллекцию"
 
#вывод карточки произведения
print("=== Карточка произведения искусства ===")
print(f"Название: {title}")
print(f"Автор: {author_name}")
print(f"Год создания: {creation_year}")
print(f"Техника: {technique}")
print(f"Категория: {category}")
print(age_message)
print(f"Статус: {period_status}")
print(collection_note)