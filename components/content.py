from tkinter import CENTER, NO, YES, IntVar, ttk


class Content():
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.master, padding=10, style='content.TFrame')
        self.create_field_selectors()
        self.create_tree()
        self.create_scroll()

        self.tag_odd = ('odd')
        self.tag_event = ('event')
    

    def create_field_selectors(self):
        fields = self.app.data.fields
        self.field_selectors = []
        callback = lambda i : print(i, self.field_selector_vars[i].get())
        self.field_selector_vars = []
        for f in fields:
            var = IntVar()
            self.field_selector_vars.append(var)
        for i, f in enumerate(fields):
            j = i
            cb = ttk.Checkbutton(self.frame, text=f, variable=self.field_selector_vars[i], command=lambda: callback( j))
            self.field_selectors.append(cb)

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

    def refresh_page(self, page):
        SIZE = self.app.data.PAGE_SIZE
        start = page * SIZE
        end = min(start + SIZE, len(self.app.data.values_list))
        page_values_list = self.app.data.values_list[start:end]
    
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        fields = self.app.data.fields
        self.tree['columns'] = fields
        for f in fields:
            self.tree.column(f, anchor=CENTER)
            self.tree.heading(f, text=f, anchor=CENTER)
        
        for i, values in enumerate(page_values_list):
            self.tree.insert('', 'end', values=values, iid=i, 
                             tags= self.tag_event if i % 2 == 0 else self.tag_odd)

        
        self.layout()
        self.tree.update()

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

        for i, s in enumerate(self.field_selectors):
            s.grid(column=i, row=0, sticky='n')

        self.tree.grid(column=0, row=1, sticky="nsew", pady=0)
        self.tree_scroll.grid(column=0, row=2, sticky='EW', padx=8, pady=20) 

