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

def create_json_datafile():
    # we need to keep state that the file has been created 
    if not os.path.exists(data_path):
        print("creating file... ")
        with open(data_path, 'w') as datafile:
            try:
                json.dump(datafile,fp=True)
            except TypeError:
                print("file created while handling the typeerror....!")
    else:
        print("file existss")

def write_json_data(main_record_dict: dict):
    with open(data_path, 'w') as json_data:
        json.dump(main_record_dict, json_data, indent=4) 
    return json.dumps(main_record_dict, indent=4)

def post_rec(sheetname=0, date=0, holiday=0, start=0, finish=0):
    create_json_datafile()
    default=''
    sheet_name_list: list = ["albert"]
    sheet_name_data: list = []
    records:dict = {"date": date, "holiday": holiday, "start":start, "finish": finish}
    main_records: dict= {}
    main_records = {'albert': [{'date': '22/11/2025', 'holiday': 'Saturday', 'start': 7.00, 'finish': 16.02}]}
    if os.path.exists(data_path):
        try:
            with open(data_path, 'r') as file:
                data = json.load(file)
                print(data)

            # with open(data_file, 'w') as write_data:
            #     json.dump(data, data_file, indent=4)
            for name in sheet_name_list:
                if name == sheetname:
                   for key in main_records.keys():
                       if key == sheetname:
                           main_records[key].append(records)
                else:
                    main_records[sheetname]=records

        except json.JSONDecodeError:
            with open(data_path, 'w') as data_file:
                json.dump(default, data_file, indent=4)
    print(main_records)
    print(write_json_data(main_records))

post_rec("nathan", "23/11/2025", "Sunday", 6.02, 18.09)
post_rec('jon', '23/11/2025', 'Sunday', 7.30, 16.45)
post_rec("nathan", "23/11/2025", "Sunday", 6.02, 18.09)
post_rec('jon', '23/11/2025', 'Sunday', 7.30, 16.45)
