import os
import csv

PATH = r'D:\repo\bili\galaxy_studio\Assets\Bundles\Data'

class Data():
    def __init__(self):
        self.PAGE_SIZE = 30
    
    def read_data_from_filename(self, filename : str):

        # values_list
        # fields
        target = os.path.join(PATH, filename)
        if not os.path.exists(target):
            print(f'path not existed: {target}')
            return

        with open(target, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            self.fields = reader.fieldnames
            self.total_values_list = []
            self.display_values_list = []
            for row in reader:
                self.total_values_list.append(list(row.values()))
            
            self.display_values_list = self.total_values_list # weak copy
        

    
    def set_display_values_list(self, display_values):
        if display_values != None:
            self.display_values_list = display_values
        else:
            self.display_values_list = self.total_values_list
        

    def read_filenames(self):
        self.file_names = [p for p in os.listdir(PATH) if p.endswith('.csv')]