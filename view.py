import read_write
import managment

def Select(ID, type_ID, list, text, select_key):
    temp = ''
    for i in range(len(list)):
        for key, value in list[i].items(): 
            if value == ID and key == type_ID:
                temp += text + ': ' + str(list[i][select_key]) + " "                            
        continue
    return(temp)   

def Select_adress(ID, list):
    temp_list = []
    for i in range(len(list)):
        for key, value in list[i].items(): 
            if value == ID and key == 'ID_employee':
                temp_list.append(list[i])
    for j in range(len(temp_list)):
        if j == 0:
            temp = 'адрес: '
        else: 
            temp = 'адрес ' + str(j+1) + ': '
        for key, value in temp_list[j].items():
            if key != 'ID_employee':
                temp += str(value) + ' '
        temp_list[j] = temp
        temp = ''
    return(temp_list)

def employees():
    employee = read_write.Read_json('employee.json')
    departments = read_write.Read_json('departments.json')
    positions = read_write.Read_json('positions.json')
    gender = read_write.Read_json('gender.json')
    keys = ['Sec_name', 'Name', 'Third_name', 'ID_gender', 'ID_position', 'ID_department']
    temp =''
    for i in range(len(employee)):
        for key,value in employee[i].items(): 
            if key in keys:
                if key == 'ID_gender':
                    temp += Select(employee[i][key], 'ID_gender', gender, 'пол', 'gender')                         
                    continue   
                elif key == 'ID_position':
                    temp += Select(employee[i][key], 'ID_position', positions, 'должность', 'Name_position')   
                    continue      
                elif key == 'ID_department':
                    temp += Select(employee[i][key], 'ID_department', departments, 'отдел', 'Name_department')   
                    continue                                           
                temp += str(value) + " "
        print(temp)
        temp = ''

def Phones():
    employee = read_write.Read_json('employee.json')
    phones = read_write.Read_json('phones.json')
    keys = ['Sec_name', 'Name', 'Third_name']
    temp_list = []
    temp = ''
    for i in range(len(employee)):
        for key,value in employee[i].items(): 
            if key in keys:
                temp += str(value) + " "
        temp_list.append(temp)
        temp = ''
    for j in range(len(employee)):
        for key,value in employee[j].items(): 
            if key == 'ID_employee':
                temp += Select(employee[j][key], 'ID_employee', phones, 'телефон', 'Phone')                           
                continue
        temp_list[j] += temp
        print (temp_list[j])
        temp = ''

def ID_employees():
    employee = read_write.Read_json('employee.json')    
    keys = ['ID_employee','Sec_name', 'Name', 'Third_name']
    temp =''
    for i in range(len(employee)):
        for key,value in employee[i].items(): 
            if key in keys:                             
                temp += str(value) + " "
        print(temp)
        temp = ''            

def All_employee(ID):
    employee = read_write.Read_json('employee.json')
    departments = read_write.Read_json('departments.json')
    positions = read_write.Read_json('positions.json')
    gender = read_write.Read_json('gender.json')
    adresses = read_write.Read_json('adresses.json')
    email = read_write.Read_json('email.json')
    phones = read_write.Read_json('phones.json')
    temp =''
    id_position = 0
    for i in range(len(employee)):
        if employee[i]['ID_employee'] == ID: 
            id_position = employee[i]['ID_position']
            for key,value in employee[i].items(): 
                if key == 'ID_gender':
                    temp += Select(employee[i][key], 'ID_gender', gender, 'пол', 'gender')                         
                    continue   
                elif key == 'ID_position':
                    temp += Select(employee[i][key], 'ID_position', positions, 'должность', 'Name_position')   
                    continue      
                elif key == 'ID_department':
                    temp += Select(employee[i][key], 'ID_department', departments, 'отдел', 'Name_department')   
                    continue  
                temp += str(value) + " "
            temp += Select(ID, 'ID_employee', phones, 'телефон', 'Phone')
            temp += Select(ID, 'ID_employee', email, 'e-mail', 'E-mail')
            adress_list = Select_adress(ID, adresses)
            for j in adress_list:
                temp += j
            temp += Select(id_position, 'ID_position', positions, 'оплата', 'salary')
            print(temp)   
   
def Main_View():                
    while True:
        managment.View_Menu()
        operation =int(input())
        if operation == 0:
            break
        elif operation == 1:
            employees()
        elif operation == 2:
            Phones()
        elif operation == 3:
            ID_employees()
        elif operation == 4:
            All_employee(int(input ('Введите ID острудника - ')))
        else:
            print ('Некорректный ввод: ')