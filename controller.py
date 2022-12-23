import view, mysql_connect

def CommandProcessing():
    view.Menu()
    view.Staff()
    team = 's'

    while team != 'x':
        team = view.Team()
        if team == 's':
            view.Staff()
        elif team == 'p':
            view.Accepted()
        elif team == '*':
            view.EmployeeSearch()
        elif team == 'r':
            view.Edit()
        elif team == 'j':
            view.export_json()
        elif team == 'm':
            view.export_xml()
        elif team == 'k':
            view.cards()
    mysql_connect.connection.close()