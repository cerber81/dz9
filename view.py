from os import system, name
import all_employees, employee_search, accepted_employees, edit_employee, export, card

fields = ['№', 'Дата регистрации:', 'Принят на работу:', 'Фамилия:', 'Имя:', 'Отчество:', 'Возраст:', 'Город:', 'Категория:', 'Оклад:', 'Телеграм:', 'Резюме:', 'Портфолио:', 'Статус:']

def Сlear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Team():
    team = str(input('Введите команду: '))
    return team

def Menu():
    Сlear()
    print('СОТРУДНИКИ:v2.0:--------------------------------------------------------------------------------------------')
    print('НОВЫЕ АНКЕТЫ: s | ПРИНЯТЫЕ: p | КАРТОЧКА: k | ТРУДОУСТРОЙТВО: r | ПОИСК: * | ВЫХОД: x')
    print('------------------------------------------------------------------------------------------------------------')

def Staff(): # новые анкеты
    Menu()
    all_employees.AllStaff()

def Accepted(): # принятые сотрудники
    Menu()
    accepted_employees.AcceptedAmployees()

def Edit():
    Menu()
    edit_employee.EditEmployee()

def export_json():
    Menu()
    export.ExportJson()

def export_xml():
    Menu()
    export.ExportXML()

def cards():
    Menu()
    card.QuestionnaireCard()

def EmployeeSearch(): # поиск сотрудника
    Menu()
    employee_search.EmployeeSearch()