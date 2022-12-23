import mysql_connect, view

def AllStaff():
    print('НОВЫЕ АНКЕТЫ СОИСКАТЕЛЕЙ:')
    print('------------------------------------------------------------------------------------------------------------')
    cur = mysql_connect.connection.cursor()
    cur.execute("SELECT * FROM `staff` WHERE `status` = 1;")
    rows = cur.fetchall()
    print(f"{view.fields[0]:<3} {view.fields[1]:<19} {view.fields[3]:<12} {view.fields[4]:<10} {view.fields[6]:<6} {view.fields[7]:<14} {view.fields[8]:<14} {view.fields[9]:<8} {view.fields[10]}")
    print('------------------------------------------------------------------------------------------------------------')
    for row in rows:
        print(f"{row[0]:<3} {row[1]} {row[3]:<12} {row[4]:<10} {row[6]:^8} {row[7]:<14} {row[8]:<14} {row[9]:<8} {row[11]}")
    print('------------------------------------------------------------------------------------------------------------')