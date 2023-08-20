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
            self.values_list = []
            for row in reader:
                self.values_list.append(list(row.values()))
        

        
        

    def read_filenames(self):
        self.file_names = [p for p in os.listdir(PATH) if p.endswith('.csv')]