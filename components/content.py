from tkinter import CENTER, NO, YES, IntVar, ttk


class Content():
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.master, padding=10, style='content.TFrame')
        self.tag_odd = ('odd')
        self.tag_event = ('event')

        self.has_created = False
    

    def on_file_select(self):
        self.treeview_display_fields = self.app.data.fields
        for c in self.frame.winfo_children():
            c.destroy()

        self.create_field_selectors()
        self.create_tree()
        self.create_scroll()
        self.has_created = True

    def create_field_selectors(self):
        self.field_select_frame = ttk.Frame(self.frame)

        fields = self.app.data.fields
        self.field_selectors = []
        self.field_selector_vars = []

        callback = lambda : self.refill_data_by_selected_fields(self.get_selected_fields())
        for f in fields:
            var = IntVar(value=1) # default selected
            self.field_selector_vars.append(var)
        for i, f in enumerate(fields):
            cb = ttk.Checkbutton(self.field_select_frame, text=f'#{i} {f}', variable=self.field_selector_vars[i], command=callback)
            self.field_selectors.append(cb)
        
        def change_all(is_on: bool):
            for v in self.field_selector_vars:
                v.set(1 if is_on else 0)
            self.refill_data_by_selected_fields(self.get_selected_fields())

        self.field_select_button_all = ttk.Button(self.field_select_frame, command=lambda : change_all(True), text='Select All')
        self.field_select_button_none = ttk.Button(self.field_select_frame, command=lambda: change_all(False), text='Unselect All')


    def create_tree(self):
        self.tree = ttk.Treeview(self.frame, padding=10
                                 , style='content.Treeview'
                                 )
        self.tree.tag_configure('odd', background='#edede9')
        self.tree.tag_configure('event')
        self.tree.configure(show='headings')

    def create_scroll(self):
        self.tree_scroll = ttk.Scrollbar(self.frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(xscroll=self.tree_scroll.set)


    def get_selected_fields(self):
        selected_fields = []
        for i, var in enumerate(self.field_selector_vars):
            if var.get() == 1: # on
                selected_fields.append(self.app.data.fields[i])
        return selected_fields
    

    def refresh_page(self, page, page_size=None):
        self.refresh_tree(page, page_size)
        self.layout()


    def refresh_tree(self, page, page_size):
        self.current_page = page
        self.page_size = page_size or self.page_size
        start = page * self.page_size
        end = min(start + self.page_size, len(self.app.data.values_list))
        page_values_list = self.app.data.values_list[start:end]
    
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        fields = self.app.data.fields
        self.tree['columns'] = fields
        self.tree['displaycolumns'] = self.treeview_display_fields
        for f in fields:
            self.tree.column(f, anchor=CENTER)
            self.tree.heading(f, text=f, anchor=CENTER)
        
        
        for i, values in enumerate(page_values_list):
            self.tree.insert('', 'end', values=values, iid=i, 
                             tags= self.tag_event if i % 2 == 0 else self.tag_odd)
        self.tree.update()



    def refill_data_by_selected_fields(self, selected_fields):
        self.treeview_display_fields = selected_fields
        self.refresh_page(self.current_page)

    def item_clicked(self):
        print('clicked')
    

    def layout(self):
        self.frame.grid()
        # self.frame.grid_columnconfigure(0, weight=1)
        # self.frame.grid_rowconfigure(0, weight=1)
        # self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=10)
        self.frame.grid_rowconfigure(2, weight=0)

        if not self.has_created:
            return
        self.field_select_frame.grid(column=0, row=0, sticky="NW")

        self.field_select_button_all.grid(column=0, row=0, sticky='NW', padx=5, pady=5)
        self.field_select_button_none.grid(column=1, row=0, sticky='NW', padx=5, pady=5)
        for i, s in enumerate(self.field_selectors):
            s.grid(row=int(i / 5) + 1, column= i % 5, sticky='NW', padx=5)

        self.tree.grid(column=0, row=1, sticky="nsew", pady=0)
        self.tree_scroll.grid(column=0, row=2, sticky='EW', padx=8, pady=20) 

