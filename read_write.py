import json

def Read_json(filename):      
    with open(filename, encoding="utf-8") as file:
        list_json = file.read()
        # list = json.loads(list_json.encode('cp1251').decode('utf-8')) 
        list = json.loads(list_json) 
    return(list)
def Write_json(list,filename):
    with open(filename, "w",  encoding="utf-8") as file:
        file.write(json.dumps(list,  sort_keys=False, indent=1, ensure_ascii=False, separators=(',', ':')))


# gender = Read_json('gender.json')
# adresses = Read_json('adresses.json')
# departments = Read_json('departments.json')
# email = Read_json('email.json')
# employeer = Read_json('employeer.json')
# phones = Read_json('phones.json')
# positions = Read_json('positions.json')
