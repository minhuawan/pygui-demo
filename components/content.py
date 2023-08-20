from tkinter import ttk
from tkinter import NO, YES, CENTER

class Content():
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.master, padding=10, style='content.TFrame')
        self.create_tree()

        self.tag_odd = ('odd')
        self.tag_event = ('event')
    

    def create_tree(self):
        self.tree_scroll = ttk.Scrollbar(self.frame)
        self.tree = ttk.Treeview(self.frame, padding=10
                                 , style='content.Treeview'
                                 , yscrollcommand=self.tree_scroll.set
                                 )

        
        
        self.tree.tag_configure('odd', background='#edede9')
        self.tree.tag_configure('event')
        self.tree.configure(show='headings')

        
    def refresh_page(self, page):
        SIZE = self.app.data.PAGE_SIZE
        start = page * SIZE
        end = min(start + SIZE, len(self.app.data.values_list))
        page_values_list = self.app.data.values_list[start:end]
    
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        self.tree['columns'] = self.app.data.fields
        for f in self.app.data.fields:
            self.tree.column(f, anchor=CENTER)
            self.tree.heading(f, text=f, anchor=CENTER)
        
        for i, values in enumerate(page_values_list):
            self.tree.insert('', 'end', values=values, iid=i, 
                             tags= self.tag_event if i % 2 == 0 else self.tag_odd)

        self.tree.update()

    def item_clicked(self):
        print('clicked')
    

    def layout(self):
        self.frame.grid()
        # self.frame.grid_columnconfigure(0, weight=1)
        # self.frame.grid_rowconfigure(0, weight=1)
        self.tree.grid(column=0, row=0)
        # self.tree_scroll.pack(fill='y')
        self.tree.pack(fill='y', expand=True, anchor='w')

