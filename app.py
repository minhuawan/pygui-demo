from tkinter import ttk, Tk
from components.content import Content
from components.file_list import FileList
from components.searcher import Searcher
from components.tabs import Tabs
from components.page_selector import PageSelector

from data.data import Data

class App():
    def __init__(self):
        self.create_data()
        
        self.master = Tk()
        self.master.title('PY GUI DEMO')
        self.master.minsize(width=900, height=800)
        # self.master.resizable(0, 0)
        # self.master['bg'] = '#AC99F2'
        
        self.initialize_components()
        self.initialize_style()
        self.layout()

        self.file_list.bind_select_callback(self.on_file_select)
        self.file_list.on_select(0)

        self.page_selector.bind_page_change(self.on_page_change)
        self.page_selector.refresh_page(0)

        self.searcher.bind_search_callback(self.on_search)

    def create_data(self):
        self.data = Data()
        self.data.read_filenames()
        self.data.read_data_from_filename(self.data.file_names[0])
        
    def initialize_style(self):
        s = ttk.Style()
        s.configure('tab.TFrame', background='#7AC5CD')
        s.configure('searcher.TFrame', background='#7A00CD')
        s.configure('file_list.TFrame', background='#FFC5CD')
        s.configure('content.TFrame', background='#7AFFCD')
        s.configure('content.Treeview')
        
        
    def initialize_components(self):
        self.content = Content(self)
        self.file_list = FileList(self)
        self.searcher = Searcher(self)
        self.tabs = Tabs(self)
        self.page_selector = PageSelector(self)

    def layout(self):
        self.master.grid()
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
    

        self.searcher.frame.grid(column=0, row=0, sticky='NSEW', columnspan=1, rowspan=1)
        self.searcher.layout()
        
        self.file_list.frame.grid(column=0, row=1, sticky='NSEW', columnspan=1, rowspan=4)
        self.file_list.layout()

        self.tabs.frame.grid(column=1, row=0, sticky='NSEW', columnspan=4, rowspan=1)
        self.tabs.layout()

        self.content.frame.grid(column=1, row=1, sticky='NSEW', columnspan=4, rowspan=4)
        self.content.layout()

        self.page_selector.frame.grid(column=1, row=2, sticky='NSEW', columnspan=4, rowspan=1)
        self.page_selector.layout()


    def on_page_change(self, page):
        self.content.refresh_page(page)

    def on_file_select(self, index):
        self.data.read_data_from_filename(self.data.file_names[index])
        self.page_selector.refresh_page(0)

    def on_search(self, input):
        self.file_list.on_search(input)

    def run(self):
        self.master.mainloop()