import read_write

def Delete_ID(list,ID):
    item = []
    for i in range(len(list)):
        for key , value in list[i].items():
            if key == "ID_employeer" and value == ID: 
                item.append(i)
    item.sort(reverse = True)            
    for j in item:
        list.pop(j)


employeer = read_write.Read_json('employeer.json')
adresses = read_write.Read_json('adresses.json')    
email = read_write.Read_json('email.json')
phones = read_write.Read_json('phones.json')
ID = input('Введите ID сотрудника, информацию о котором нужно удалить - ')
# Delete_ID(employeer,ID)
# Delete_ID(adresses,ID)
# Delete_ID(email,ID)
# Delete_ID(phones,ID)
item = []
for i in range(len(employeer)):
    for key , value in employeer[i].items():
        if key == "ID_employeer" and str(value) == str(ID): 
            item.append(i)
print(item)            
item.sort(reverse = True)            
print(item)
for j in item:
        employeer.pop(j)

print(f'Удалена информация о сотруднике с ID = {ID}')
print (employeer)