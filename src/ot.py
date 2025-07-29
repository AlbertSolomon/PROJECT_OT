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
        print(f"{new_sheet.title} was created ")