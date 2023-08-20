
from tkinter import ttk
class PageSelector():
    def __init__(self, app):
        self.callback = None
        self.app = app
        self.frame = ttk.Frame(app.master)
        self.initialize_components()
        self.layout()

    def initialize_components(self):
        values_list = self.app.data.values_list
        r1 = len(values_list) / self.app.data.PAGE_SIZE
        r2 = (int)(len(values_list) / self.app.data.PAGE_SIZE)
        self.total_page_count = r2 if r1 == r2 else r2 + 1
        self.label = ttk.Label(self.frame, width=15, anchor='center')
        self.button_left = ttk.Button(self.frame, text='<', width=3)
        self.button_right = ttk.Button(self.frame, text='>', width=3)
        self.button_first = ttk.Button(self.frame, text='<<', width=3)
        self.button_last = ttk.Button(self.frame, text='>>', width=3)
        self.combo_box = ttk.Combobox(self.frame
                                      , values=[x+1 for x in range(self.total_page_count)]
                                      , state='readonly'
                                      , width=5
                                      , justify='center'
                                      )
    
        self.button_left.configure(command=lambda: self.refresh_page(self.current_page - 1, change_combo=True))
        self.button_right.configure(command=lambda: self.refresh_page(self.current_page + 1, change_combo=True))
        self.button_first.configure(command=lambda: self.refresh_page(0, change_combo=True))
        self.button_last.configure(command=lambda: self.refresh_page(self.total_page_count - 1, change_combo=True))
        self.combo_box.bind('<<ComboboxSelected>>', lambda e : self.refresh_page(int(e.widget.get()) - 1))

    def bind_page_change(self, callback):
        self.callback = callback

    def refresh_page(self, page, change_combo=False):
        if 0 <= page < self.total_page_count:
            self.current_page = page
            self.label.configure(text=f'{page + 1}/{self.total_page_count}')
            if change_combo:
                self.combo_box.current(page)

            if self.callback is not None:
                self.callback(self.current_page)
        
        

    def layout(self):
        self.frame.grid()
        self.label.grid(column=0, row=0)
        self.button_first.grid(column=1, row=0)
        self.button_left.grid(column=2, row=0)
        self.combo_box.grid(column=3, row=0)
        self.button_right.grid(column=4, row=0)
        self.button_last.grid(column=5, row=0)
        