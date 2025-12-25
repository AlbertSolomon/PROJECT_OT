from lang import row_number
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
            
    def insert_point_coordinate(self) -> str:
        #! TOTAL is found in column A,
        #! or we can return both the coordinate or just the number (list obviously)
        search_point = 'TOTAL'
        for cell in self.sheet['A']:
            if cell.value == search_point:
                # print(cell.coordinate)
                return cell.coordinate
            
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
        #! we are starting at row 3 to a row before insert_point_coordinate function.
        #! we need to check if a row contains a value,, if it doesnt, then we delete it.
        insert_row_coordinate = int(self.insert_point_coordinate().strip("A")) - 1
        row_list :list = []
        cell_val_counter:int = 0
        row_counter:int = 0

        for rows in self.sheet.iter_rows(min_row=4, max_row=insert_row_coordinate):
            row_list.append(rows)
                
        for row in range(len(row_list)):
            for cell in range(len(row_list[row])):
                print(row_list[row][cell])
                row_counter = row_number(row_list[row][cell].coordinate)
                if type(row_list[row][cell].value) == type(None):
                    cell_val_counter += 1
        
            print(cell_val_counter)
            print("row counter is: ",row_counter)
            if cell_val_counter == len(row_list[row]):
                print("row successfully deleted !!!")
                #! this implementation is buggy, it disrupts the format of the spread sheet.
                self.sheet.delete_rows(row_counter)
            else:
                print("Something went wrong ")

            cell_val_counter = 0
            row_counter = 0
        #print(row_list, len(row_list)) 
        #print("\n")
        #print(len(row_list[0]))
        #print("\n")
        #print(row_list_values, len(row_list_values))


    '''def insert_ot(self, day:str, start_time: float, end_time:float) -> dict:
        ot = {'day':day, 'start': start_time, 'end': end_time}

        return ot'''
    
    def search_job_description(self, job_titles) -> str:
        row_coordinate = self.insert_point_coordinate()
        row_number = int(row_coordinate.strip("A")) + 1
        cell_coordinate = 'F' + str(row_number)
        cell_job_title = self.sheet[cell_coordinate].value.upper()
        
        for job_title in job_titles:
            jt = job_title.replace("_", " ").upper()
            if jt == cell_job_title:
                print(f"{jt} equals {cell_job_title}")
                return jt

    def merger(self, start_point, end_point):
        self.sheet.merge_cells(f'{ start_point }:{ end_point }')

    def insert_row(self):
        cell_coordinate = self.insert_point_coordinate() # rememeber that this is a string, and an int is required
        #print(f"first state is { cell_coordinate }")
        for character in cell_coordinate: # or i could use the built in strip function, but i guess you are the smart one 😒
            if character == 'A':
                continue
            else:
                #print(character)
                cell_coordinate = character
                print(cell_coordinate)
        
        self.sheet.insert_rows(int(cell_coordinate))
        #print(f"the state after insertion is {cell_coordinate}")
        '''TODO from C to E'''
        C = 'C' + cell_coordinate
        E = 'E' + cell_coordinate
        I = 'I' + cell_coordinate

        #self.sheet[C] = "JOb discription"
        self.sheet[I] = 1.5 # this value should be dynamic, thus based on employees act
        # merging cells here and job desription insertion
        self.merger(C, E)
        
    def sync_json_data(self, ot_day: dict):
        # might use a helper function but who knows 
        from lang import data_path as data
        import json
        with open(data, 'r') as ot_data_file:
            ot_data = json.load(ot_data_file)
            print(ot_data)


    def update_ot(self, sheetname: str):
        pass

    def update_ot_json(self, json_file: str):
        pass