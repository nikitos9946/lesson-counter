# Создать программу учета сделанных задач
# Программа увключает в себя меню:
# 1. Новое задание
# 2. Список заданий
# 3. Выход

# -- Новое задание
# Задание содержит поля Номер по порядку, Название, Дата создания, Дата завершения, Вознаграждение, Оплачено


lessons_list = []
def data():
    try:
        with open("lessons.txt", "r") as file:
            for line in file:
                raw_lesson = line.strip().split(";")
                lesson = dict(number = raw_lesson[0], name = raw_lesson[1], cr_date = raw_lesson[2], end_date = raw_lesson[3], raw_paid = raw_lesson[4], paid = raw_lesson[5])
                lessons_list.append(lesson)
    except FileNotFoundError:
        open("lessons.txt", "w", encoding = 'utf-8').close()
    return lessons_list
def menu():
    print("Учёт заданий")
    print("___________________")
    print("1. Новое задание")
    print("2. Список заданий")
    print("3. Выход")

def menu1():
    print("Новое задание")
    lesson_number = input("Введите номер занятия ")
    lesson_name = input("Введите имя занятия ")
    lesson_cr_date = input("Введите дату создания занятия ")
    lesson_end_date = input("Введите дату окончания занятия ")
    lesson_raw_paid = input("Введите вознаграждение ")
    lesson_paid = input("Занятие оплачено? (Да/Нет) ")
    with open("lessons.txt", "a", encoding = 'utf-8') as file:
        lesson = dict(number = lesson_number, name = lesson_name, cr_date = lesson_cr_date, end_date = lesson_end_date, raw_paid = lesson_raw_paid, paid = lesson_paid)
        lessons_list.append(lesson)
        file.write(lesson['number'] + "; " + lesson['name'] + "; " + lesson['cr_date'] + "; " + lesson['end_date'] + "; " + lesson['raw_paid'] + "; " + lesson['paid'] + "\n" )

def menu2():
    print("Список занятий")
    print("____________________")
    for lesson in lessons_list:
        print("Номер - " + lesson['number'] + "; " + "Название - " + lesson['name'] + "; " + "Дата создания - " + lesson['cr_date'] + "; " + "Дата завершения - " + lesson['end_date'] + "; " + "Вознаграждение - " + lesson['raw_paid'] + "; " + "Оплачено - " + lesson['paid'])
data()
while True:
    menu()
    menu_number = input("Введите номер ")

    if menu_number == "1":
        menu1()
    if menu_number == "2":
        menu2()
    if menu_number == "3":
        print("\n""Выход")
        exit()