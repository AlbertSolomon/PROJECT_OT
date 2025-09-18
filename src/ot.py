from typing import Union
class OT:
    def __init__(self, workbook, sheetname):
        self.workbook = workbook
        self.sheetname = sheetname
        self.sheet = self.workbook[self.sheetname]

    def finder(self) -> bool:
        for name in self.workbook.sheetnames:
            if name == self.sheetname:
                return True
            else:
                return False
            
    def create_worksheet(self, starter_workbook):
        source_sheet = self.workbook[starter_workbook]
        new_sheet = self.workbook.copy_worksheet(source_sheet)
        new_sheet.title = self.sheetname
        print(f"{ new_sheet.title } was created ")

    def delete_worksheet(self, worksheet_name):
        if worksheet_name in self.workbook.sheetnames:
            worksheet = self.workbook[worksheet_name]
            self.workbook.remove(worksheet)
            print(f"{ worksheet } has been deleted...")

    def delete_copies(self):
        for worksheet_name in self.workbook.sheenames:
            if "Copy" in worksheet_name or any(digit.isdigit() for digit in worksheet_name):
                copy = self.workbook[worksheet_name]
                self.workbook.remove(copy)

    '''def insert_ot(self, day:str, start_time: float, end_time:float) -> dict:
        ot = {'day':day, 'start': start_time, 'end': end_time}

        return ot'''
    
    def insert_position(self) -> str:
        # TOTAL is found in column A, hence we need to search for in it
        search_point = 'TOTAL'
        #sheet = self.workbook[self.sheetname]
        for cell in self.sheet['A']:
            if cell.value == search_point:
                print(cell.coordinate)
                return cell.coordinate
            
    def merger(self, start_point, end_point):
        self.sheet.merge_cells(f'{ start_point }:{ end_point }')

    def insert_row(self, insert_position):
        state = insert_position()
        self.sheet.insert_rows(state)
        
    def insert_ot_json(self, ot_day: dict):
        if type(ot_day) == dict:
            print("printing dict:")