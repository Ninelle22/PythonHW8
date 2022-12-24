import read_write
import managment
employee = read_write.Read_json('employee.json')
print(employee)

while True:
    managment.Menu()
    operation =int(input())
    if operation == 0:
        break
    elif operation == 1:
        print(operation)
        break
    elif operation == 2:
        print(operation)
        break
    elif operation == 3:
        print(operation)
        break   
    else:
        print ('Некорректный ввод: ')

    