import mysql_connect, view
def QuestionnaireCard():
    print('КАРТОЧКА СОИСКАТЕЛЯ:')
    print('------------------------------------------------------------------------------------------------------------')
    team = str(input('Введите ID анкеты: '))
    print('------------------------------------------------------------------------------------------------------------')
    cur = mysql_connect.connection.cursor()
    cur.execute(f"SELECT * FROM `staff` WHERE `id` = '{team}';")
    rows = cur.fetchall()
    for row in rows:
        print(f"{view.fields[3]:<10} {row[3]}")
        print(f"{view.fields[4]:<10} {row[4]}")
        print(f"{view.fields[5]:<10} {row[5]}")
        print(f"{view.fields[6]:<10} {row[6]}")
        print(f"{view.fields[7]:<10} {row[7]}")
        print(f"{view.fields[8]:<10} {row[8]}")
        print(f"{view.fields[9]:<10} {row[9]}")
        print(f"{view.fields[10]:<10} {row[11]}")
        print(f"{view.fields[11]:<10} {row[12]}")
        print(f"{view.fields[12]:<10} {row[13]}")
        if row[14] == 2:
            print(f"{view.fields[13]:<10} Работает")
            print(f"{view.fields[2]:<10} {row[2]}")
        else:
            print(f"{view.fields[13]:<10} Соискатель")
            print(f"{view.fields[1]:<10} {row[1]}")
    print('------------------------------------------------------------------------------------------------------------')