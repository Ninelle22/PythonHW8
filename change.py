import read_write
import managment
import view

def Main_Change():
    while True:
        managment.Change_Menu()
        operation =int(input())
        if operation == 0:
            break
        elif operation == 1:
            Add_Information()
        elif operation == 2:
            print(operation)
        elif operation == 3:
            print ('В разработке')   
        else:
            print ('Некорректный ввод: ')
def Add_Another(list,ID,text):
    while True:
        op = input(f'Введите 1, если нужно добавить {text} или Enter, если не требуется - ')
        if op == str(1):
            list.append({"ID_employeer":ID}) 
            for key in list[0].keys():
                if key != "ID_employeer": 
                    list[len(list)-1][key] = input(f'Введите значение {key} - ')
        else:
            break    

def Add_Information():
    employeer = read_write.Read_json('employeer.json')
    # departments = read_write.Read_json('departments.json')
    # positions = read_write.Read_json('positions.json')
    # gender = read_write.Read_json('gender.json')
    adresses = read_write.Read_json('adresses.json')    
    email = read_write.Read_json('email.json')
    phones = read_write.Read_json('phones.json')
    adresses_count = len(adresses)
    email_count = len(email)
    phones_count = len(phones)
    id_empl = len(employeer)+1
    employeer.append({"ID_employeer":id_empl}) 
    for key in employeer[0].keys():
        if key != "ID_employeer": 
            employeer[len(employeer)-1][key] = input(f'Введите значение {key} - ')
    Add_Another(phones,id_empl,'телефон')
    Add_Another(email,id_empl,'e-mail')
    Add_Another(adresses,id_empl,'адрес')
    print('Добавлен новый сотрудник')
    while True:
        managment.Change_Confirm_Menu()
        operation = (input())
        if operation == 1:
            Add_Information()
        elif operation == 2:
            read_write.Write_json(employeer,'employeer1.json')
            if adresses_count < len(adresses):
                read_write.Write_json(adresses,'adresses1.json')
            if email_count < len(email):
                read_write.Write_json(email,'email1.json')
            if phones_count < len(phones):
                read_write.Write_json(phones,'phones1.json')
            break
        elif operation != str(1) or operation != str(1):
            break
Main_Change()