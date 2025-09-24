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
        #print(f"{ new_sheet.title } was created ")

    def delete_worksheet(self, worksheet_name):
        if worksheet_name in self.workbook.sheetnames:
            worksheet = self.workbook[worksheet_name]
            self.workbook.remove(worksheet)
            #print(f"{ worksheet } has been deleted...")

    def delete_copies(self):
        for worksheet_name in self.workbook.sheenames:
            if "Copy" in worksheet_name or any(digit.isdigit() for digit in worksheet_name):
                copy = self.workbook[worksheet_name]
                self.workbook.remove(copy)
    
    def delete_empty_rows(self):
        pass

    '''def insert_ot(self, day:str, start_time: float, end_time:float) -> dict:
        ot = {'day':day, 'start': start_time, 'end': end_time}

        return ot'''
    
    def insert_point_location(self) -> str:
        # TOTAL is found in column A, 
        search_point = 'TOTAL'
        for cell in self.sheet['A']:
            if cell.value == search_point:
                # print(cell.coordinate)
                return cell.coordinate
    
    def search_job_description(self, job_title):
        row_coordinate = self.insert_point_location()
        row_number = int(row_coordinate.strip("A")) + 1
        cell_coordinate = 'F' + str(row_number)
        print(self.sheet[cell_coordinate].value)
        
        for self.sheet[cell_coordinate].value in job_title:
            cell = self.sheet[cell_coordinate].value

            print(f" the is {cell}")
            return True

            
    def merger(self, start_point, end_point):
        self.sheet.merge_cells(f'{ start_point }:{ end_point }')

    def insert_row(self):
        cell_coordinate = self.insert_point_location() # rememeber that this is a string, and an int is required
        #print(f"first state is { cell_coordinate }")
        for character in cell_coordinate: # or i could use the built in strip function, but i guess you are the smart one 😒
            if character == 'A':
                continue
            else:
                #print(character)
                cell_coordinate = character
        
        self.sheet.insert_rows(int(cell_coordinate))
        #print(f"the state after insertion is {cell_coordinate}")
        # merging cells here and job desription insertion 
        '''TODO from C to E'''
        C = 'C' + cell_coordinate
        E = 'E' + cell_coordinate
        I = 'I' + cell_coordinate

        #self.sheet[C] = "JOb discription"
        #self.sheet[I] = 1.5
        #self.merger(C, E)
        
    def insert_ot_json(self, ot_day: dict):
        if type(ot_day) == dict:
            print("printing dict:")