import read_write
import managment
import view

while True:
    managment.Menu()
    operation =int(input())
    if operation == 0:
        break
    elif operation == 1:
        view.Main_View()
    elif operation == 2:
        print(operation)
    elif operation == 3:
        print(operation)
    else:
        print ('Некорректный ввод: ')

    