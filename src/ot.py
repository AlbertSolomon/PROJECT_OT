class OT:
    def __init__(self, workbook, sheetname):
        self.workbook = workbook
        self.sheetname = sheetname

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