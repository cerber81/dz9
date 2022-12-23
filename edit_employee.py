import mysql_connect, view, datetime


def EditEmployee():
    print('РЕДАКТИРОВАНИЕ АНКЕТ:')
    print(
        '------------------------------------------------------------------------------------------------------------')
    team = str(input('Введите ID анкеты: '))
    cur = mysql_connect.connection.cursor()
    cur.execute(f"SELECT * FROM `staff` WHERE `id` = '{team}';")
    rows = cur.fetchall()
    print(
        f"{view.fields[0]:<3} {view.fields[1]:<19} {view.fields[3]:<12} {view.fields[4]:<10} {view.fields[6]:<6} {view.fields[7]:<14} {view.fields[8]:<14} {view.fields[9]:<8} {view.fields[10]}")
    print(
        '------------------------------------------------------------------------------------------------------------')
    for row in rows:
        print(
            f"{row[0]:<3} {row[1]} {row[3]:<12} {row[4]:<10} {row[6]:^8} {row[7]:<14} {row[8]:<14} {row[9]:<8} {row[11]}")
    print(
        '------------------------------------------------------------------------------------------------------------')

    dt_now = datetime.datetime.now()
    post = input("Должность: ")
    salary = input("Оклад: ")

    with mysql_connect.connection.cursor() as cursor:
        update_query = f"UPDATE `staff` SET `adopted` = '{dt_now}', `post` = '{post}', `salary` = '{salary}', `status` = '2' WHERE `id` = '{team}';"
        cursor.execute(update_query)
        mysql_connect.connection.commit()