import mysql_connect
def ExportJson():
    file_json = open('staff.json', 'w', encoding='utf-8')
    file_json.write('{ "staff": [\n')

    cur = mysql_connect.connection.cursor()
    cur.execute("SELECT * FROM `staff` WHERE `status` = 2;")
    rows = cur.fetchall()

    simvol1 = '{'
    simvol2 = '}'

    for row in rows:
            file_json.write(
                f'{simvol1} "id": {row[0]}, "adopted": "{row[2]}", "surname": "{row[3]}", "name": "{row[4]}", "first_name": "{row[5]}", "years": "{row[6]}", "city": "{row[7]}", "post": "{row[8]}", "salary": "{row[9]}", "telegram": "{row[11]}", "resume": "{row[12]}", "portfolio": "{row[13]}" {simvol2},\n')
    file_json.write(']}')
    file_json.close()
    print('Данные успешно экспортированы в файл staff.json')
    print(
        '------------------------------------------------------------------------------------------------------------')

def ExportXML():
    file_json = open('staff.xml', 'w', encoding='utf-8')
    file_json.write('<list>\n')

    cur = mysql_connect.connection.cursor()
    cur.execute("SELECT * FROM `staff` WHERE `status` = 2;")
    rows = cur.fetchall()

    for row in rows:
        file_json.write(
            f'<staff>\n<id>{row[0]}</id>\n<adopted>{row[2]}</adopted>\n<surname>{row[3]}</surname>\n<name>{row[4]}</name>\n<first_name>{row[5]}</first_name>\n<years>{row[6]}</years>\n<city>{row[7]}</city>\n<post>{row[8]}</post>\n<salary>{row[9]}</salary>\n<telegram>{row[11]}</telegram>\n<resume>{row[12]}</resume>\n<portfolio>{row[13]}</portfolio>\n</staff>\n')
    file_json.write('</list>')
    file_json.close()
    print('Данные успешно экспортированы в файл staff.xml')
    print(
        '------------------------------------------------------------------------------------------------------------')