import read_write
import view
import managment

def Criterion_Menu():
    managment.Criterion_Menu()    
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
        managment.Select_Menu()
        operation =int(input())
        if operation == 0:
            break
        elif operation == 1:
            Select_From_Salary(float(input('Введите искомый размер оплаты - ')), Criterion_Menu())
        elif operation == 2:
            Select_Department_Head()
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

def Select_Department_Head():
    departments = read_write.Read_json('departments.json')
    temp_list=[]
    for i in departments:        
        temp_list.append(i['Id_department_head'])
    for i in temp_list:
        view.All_Employeer(i)