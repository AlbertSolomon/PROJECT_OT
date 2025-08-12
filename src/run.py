
from openpyxl import Workbook, load_workbook
from ot import OT
from lang import path, overtime_month
import json

workbook = load_workbook(path)
workbook.active

print(workbook.sheetnames)

#workbook.save(f"./final/{ overtime_month }")
