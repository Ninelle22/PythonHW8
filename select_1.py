import read_write
import view

def Select_Menu():
    print ('Веберите критерий: ')
    print ('1 - Отобрать сотрудниов по оплате')
    print ('2 - Отобрать начальников отделов')   
    print ('3 - ')
    print ('0 - Выход')

def Criterion_Menu():
    print ('Веберите выберите критерий поиска оплаты: ')
    print ('1 - если меньше искомого')
    print ('2 - если больше искомого')   
    print ('3 - если равно искомому')
    print ('4 - если не меньше искомого')
    print ('5 - если не больше искомого')
    print ('0 - Выход')
    
    while True:
        criterion = int(input())
        if criterion == 0:
            break
        elif criterion in range(6):
            return (criterion)
            break
        else:
            print ('Некорректный ввод: ')

def Main_Select():
    while True:
        Select_Menu()
        operation =int(input())
        if operation == 0:
            break
        elif operation == 1:
            # salary_select = float(input('Введите искомый размер оплаты - '))
            # criterion = Criterion_Menu()
            Select_From_Salary(float(input('Введите искомый размер оплаты - ')), Criterion_Menu())
        elif operation == 2:
            print (operation)
        elif operation == 3:
            print ('В разработке')
        else:
            print ('Некорректный ввод: ')

def Select_From_Salary(salary_sel, crit):
    employeer = read_write.Read_json('employeer.json')
    positions = read_write.Read_json('positions.json')
    departments = read_write.Read_json('departments.json')
    gender = read_write.Read_json('gender.json')
    temp_list=[]
    temp = ''
    keys = ['Sec_name', 'Name', 'Third_name', 'ID_gender', 'ID_position', 'ID_department']
    for i in range(len(positions)):
        for key,value in positions[i].items(): 
            if key == 'salary':
                if ((crit == 1 and value < salary_sel) 
                    or (crit == 2 and value > salary_sel) 
                    or (crit == 3 and value == salary_sel) 
                    or (crit == 4 and value >= salary_sel) 
                    or (crit == 5 and value <= salary_sel)):
                    temp_list.append(positions[i]['ID_position'])
    id_position = 0
    for i in range(len(employeer)):
        if employeer[i]['ID_position'] in temp_list:             
            id_position = employeer[i]['ID_position']            
            for key,value in employeer[i].items(): 
                if key in keys:
                    if key == 'ID_gender':
                        temp += view.Select(employeer[i][key], 'ID_gender', gender, 'пол', 'gender')                         
                        continue   
                    elif key == 'ID_position':
                        temp += view.Select(employeer[i][key], 'ID_position', positions, 'должность', 'Name_position')   
                        continue      
                    elif key == 'ID_department':
                        temp += view.Select(employeer[i][key], 'ID_department', departments, 'отдел', 'Name_department')   
                        continue  
                    temp += str(value) + " "
            temp += view.Select(id_position, 'ID_position', positions, 'оплата', 'salary')
            print(temp)       
            temp = ''