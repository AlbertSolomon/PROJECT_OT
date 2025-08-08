import os
from openpyxl import Workbook, load_workbook
from ot import OT
import json

path = os.path.join('./template/', 'overtime_template.xlsx')
workbook = load_workbook(path)
workbook.active

print(workbook.sheetnames)


# workbook.save("new workbook ")
