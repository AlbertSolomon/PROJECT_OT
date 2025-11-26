import os
import json
import subprocess

path = os.path.join('./template/', 'overtime_template.xlsx')
t_path = os.path.join('./temp/')
settings_path = os.path.join('./utils/', 'settings.json')
rules_path = os.path.join('./utils/', 'rules.json')


def read_settings() -> str:
    try:
        with open(settings_path, "r") as current_month:
            location = json.load(current_month)

    except FileNotFoundError:
        with open(settings_path, "w") as config_file:
            json.dump(settings_path, config_file, indent=4)
        with open(settings_path, "r") as config_location:
            location = json.load(config_location)

        return location
    return location

# READING THE CURRENT OVERTIME MONTH ()
overtime_month = read_settings().__getitem__('current_month')
data_path = os.path.join('./data/', f'{overtime_month}.json')

def change_month(new_month):
    try:
        util_settings_r = read_settings()
        util_settings_r['current_month'] = new_month
        with open(settings_path, "w") as util_settings_w:
            json.dump(util_settings_r, util_settings_w, indent=4)

    except Exception:
        print("file not found or something...")
    else:
        util_settings_r['current_month'] = new_month

def read_rules() -> dict:
    try:
        with open(rules_path,'r') as rules_settings_r:
            rules = json.load(rules_settings_r)
            #for key in rules.keys():
            #    print(f"{ key }: { rules[key] }")
            return rules
    except Exception:
        print("file not found or something ")

def write_rules(finished=False, temporary_file=True, preparationDate=0):
    try:
        with open(rules_path,'r') as file:
            read_setting_data = json.load(file)

            for key in read_setting_data:
                if key == "finished" and finished:
                    read_setting_data[key] =True

                if key =="temporaryFile" and temporary_file==False:
                    read_setting_data[key]=False

                if key == "preparationDate":
                    # input next month, this will hardly be editted by the user
                    pass # for now 

        with open(rules_path, 'w') as rules:
            json.dump(read_setting_data,rules, indent=4)
    except Exception:
        print(FileNotFoundError)

def delisting(list: list) -> str:
    '''This exists for one single purpose, so don't judge..'''
    return list[0]

#print(change_month("july"))
#print(read_settings())
print(overtime_month)

# CHECKING IF SAVE FILE PATH EXISTS, CREATING IT IF IT DOESNT
def saved_file_location():
    if os.path.exists("../srcs/"):
        print("true")
        # pass
    else:
        # note that permission is required to perform this operation
        subprocess.run(f"mkdir /Final", shell=True)
        print("creating save file location")
#saved_file_location()

job_titles = {
    "Weighbridge_Operator": "Weighing loading and offloading",
    "Depot_Operator": "Offloading and loading trucks",
    "Depot_Clerk": "Documentation for offloading and loading trucks",
    "Security_Officer": "",
    "Groundsman": "",
    "Office_Assistant": "",
    "IT_Officer": "",
}

def row_number(string: str) -> int:
    try:
        character:str = ''
        lchar:str = []
        comma:str = ''
        for char in string:
            if char.isdigit(): 
                lchar.append(char)
            else:
                try:
                    character = '0'
                except ValueError:
                    print("No digit found ")
        character = comma.join(lchar)   
        return int(character)
    except TypeError:
        return int(str(string))

def create_json_datafile() -> bool:
    # we need to keep state that the file has been created 
    if not os.path.exists(data_path):
        print("creating file... ")
        with open(data_path, 'w') as datafile:
            try:
                json.dump(datafile,fp=True)
            except TypeError:
                print("file created while handling the typeerror....!")
    else:
        return True

def write_json_data(main_record_dict: dict):
    with open(data_path, 'w') as json_data:
        json.dump(main_record_dict, json_data, indent=4) 
    return json.dumps(main_record_dict, indent=4)

###!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def post_rec(sheetname:str ,date:str ,holiday:str ,start:float ,finish:float):
    #? initializing
    sheetname = sheetname.upper()
    sheetname_rec: list = []
    records:dict = {
        "date": date, 
        "holiday": holiday, 
        "start":start, 
        "finish": finish
    }   
    main_records: dict= {}

    #? checking if the json file has been created, and if it has any values 
    create_json_datafile()
    try:
        if create_json_datafile and os.path.getsize(data_path) > 0:
                with open(data_path, 'r') as json_data_file:
                    json_data = json.load(json_data_file)
                    print(type(json_data))
                    #! turn json data into dict here
                    main_records = json_data
                    print("from created file:::", json_data)
        else:
            #? remember that this fits for file that has just been created (empty json file)
            sheetname_rec.append(records)
            main_records = {sheetname:sheetname_rec}

        if sheetname in main_records:
            if records not in main_records[sheetname]:
                #print("available rec::",main_records[sheetname])
                #print(type(main_records[sheetname]))
                #sheetname_rec = main_records[sheetname]
                #sheetname_rec.append(records)
                #main_records = { sheetname: sheetname_rec}
                if not isinstance(main_records[sheetname], list):
                    main_records[sheetname] = [main_records[sheetname]]
                main_records[sheetname].append(records)
        else:
            sheetname_rec.append(records)
            main_records[sheetname] = sheetname_rec

        #? +++++++++++++++++++ writing data to json file ++++++++++++++++++++++++++++++++++++
        with open(data_path, 'w') as data_file:
            json.dump(main_records, data_file, indent=4)
        #? +++++++++++++++++++ writing data to json file ++++++++++++++++++++++++++++++++++++
    except json.JSONDecodeError:
        print("json file is empty ")

    print(json.dumps(main_records, indent=4))
    print("+++++ record added sucessfully +++++")
        
###!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
post_rec("nathan", "23/11/2025", "Sunday", 6.02, 18.09)
post_rec('jon', '23/11/2025', 'Sunday', 7.30, 16.45)
post_rec("nathan", "23/11/2025", "Sunday", 19.01, 23.09)
post_rec('jon', '22/11/2025', 'Saturday', 7.00, 19.45)
post_rec('mirrium', '22/11/2025', 'Saturday', 7.00, 19.45)
