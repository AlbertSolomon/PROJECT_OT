import os
import json
import subprocess

path = os.path.join('./template/', 'overtime_template.xlsx')
settings_path = os.path.join('./utils/', 'settings.json')

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

def delisting(list: list) -> str:
    '''This exists for one single purpose, so don't judge..'''
    return list[0]

#print(change_month("july"))
#print(read_settings())

# READING THE CURRENT OVERTIME MONTH ()
overtime_month = read_settings().__getitem__('current_month')
print(overtime_month)

# CHECKING IF SAVE FILE PATH EXISTS, CREATING IT IF IT DOESNT
def saved_file_location():
    if os.path.exists("../srcs/"):
        print("true")
        # pass
    else:
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