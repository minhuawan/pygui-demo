from tkinter import ttk
from tkinter import *

class FileList():
    def __init__(self, app):
        self.select_callback = None
        self.app = app
        self.frame = ttk.Frame(app.master, padding=10, style='file_list.TFrame')
        self.list_box = Listbox(self.frame, selectmode=SINGLE)
        self.list_box.bind('<<ListboxSelect>>', self.list_box_select)
        self.display_file_names = app.data.file_names
        self.lower_file_names = [x.lower() for x in app.data.file_names]
        self.create_list_items(self.display_file_names)

        self.layout()


    def list_box_select(self, event):
        t = event.widget.curselection()
        if len(t) > 0: 
            self.on_select(t[0], change_list=True)

    def bind_select_callback(self, callback):
        self.select_callback = callback

    def on_select(self, index, change_list=False):
        if self.select_callback is not None:
            if change_list:
                self.list_box.selection_set(index)
            filename = self.display_file_names[index]
            actual_index = self.app.data.file_names.index(filename)
            self.select_callback(actual_index)
    
    def create_list_items(self, names):
        self.list_box.delete(0, END)

        for i, name in enumerate(names):
            self.list_box.insert(i, name)
        self.list_box.update()

    def on_search(self, input : str):
        input = input.strip().lower()
        if input == '':
            self.display_file_names = self.app.data.file_names
        else:
            self.display_file_names = [self.app.data.file_names[i] for i, x in enumerate(self.lower_file_names) if input in x]    
        self.create_list_items(self.display_file_names)


    def layout(self):
        self.frame.grid()
        self.list_box.grid(column=0, row=0)
        self.list_box.pack(fill='y', expand=True)
