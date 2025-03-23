import csv

with open("C:\\Users\\Admin\\OneDrive\\Desktop\\TestData\\employee_data.csv", 'r') as file:
    file_data = csv.DictReader(file)
    name_data = []
    loc_data = []
    for row in file_data:
        dict_data = dict(row)
        f = dict_data["EMP_NAME"]
        a = dict_data["EMP_LOC"]
        name_data.append(f)
        loc_data.append(a)

    name_data_total = len(name_data)
    loc_data_total = len(loc_data)
    data_count_variable1=name_data_total
    data_count_variable2=loc_data_total
    if name_data_total==data_count_variable1 and loc_data_total == data_count_variable2:
        print("name data count is",data_count_variable1)
        print("loc data count is",data_count_variable2)
    else:
        print("Error")
    
    mapping_dot=list(map(lambda x,y:x+'.'+y,name_data,loc_data))
    email=[]  # target system
    domain = '@gmail.com'
    for i in mapping_dot:
        email_creation=i+domain
        email.append(email_creation)
    print(email)
    email_data_tottal = len(email)
    if name_data_total == loc_data_total == email_data_tottal:
        print("all done")
    else:
        print("error")