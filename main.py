import read_write
import managment
import view
import select_1
import change

while True:
    managment.Menu()
    operation = int(input())
    if operation == 0:
        break
    elif operation == 1:
        view.Main_View()
    elif operation == 2:
        select_1.Main_Select()
    elif operation == 3:
        change.Main_Change()
    else:
        print ('Некорректный ввод: ')

    