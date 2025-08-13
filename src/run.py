
from openpyxl import Workbook, load_workbook
from ot import OT
from lang import path, overtime_month, delisting, settings_path
import json

workbook = load_workbook(path)
workbook.active

print(type(workbook.sheetnames))
print(delisting(workbook.sheetnames))

def command_prompter() -> list:
    """This function only exists for testing purposes """

    ot_details: list= []
    month = input("enter month for recording/retrieving ovetime details:", )
    new_sheet = input("enter new sheet name:")
    ot_details.append(month)
    ot_details.append(new_sheet)
    return ot_details

print(command_prompter())

workbook.save('./final/june.xlsx')
#workbook.save(f"./final/{ overtime_month }.xlsx")
