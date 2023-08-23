from tkinter import CENTER, NO, YES, IntVar, ttk, PhotoImage



class Content():
    def __init__(self, app):
        self.app = app
        self.frame = ttk.Frame(app.master, padding=10, style='content.TFrame')
        self.tag_odd = ('odd')
        self.tag_event = ('event')

        self.has_created = False
        self.content_search_callback = None
    
    def bind_content_search_callback(self, callback):
        self.content_search_callback = callback

    def on_file_select(self):
        self.treeview_display_fields = self.app.data.fields
        for c in self.frame.winfo_children():
            c.destroy()

        self.create_field_selectors()
        self.create_tree()
        self.create_scroll()
        self.create_content_search()
        self.has_created = True
    
    def create_content_search(self):
        self.content_search = ttk.Entry(self.field_select_frame)
        self.content_search.bind('<KeyRelease>', self.on_content_search_event)
        self.content_search_state_image_ok = PhotoImage(file='./images/status_ok.png')
        self.content_search_state_image_error = PhotoImage(file='./images/status_error.png')
        
        self.content_search_state_label = ttk.Label(self.field_select_frame, image=self.content_search_state_image_ok)


    def create_field_selectors(self):
        self.field_select_frame = ttk.Frame(self.frame, style="searcher.TFrame")

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
    

    def refresh_page(self, data, page, page_size=None):
        self.current_page = page
        self.page_size = page_size or self.page_size

        start = page * self.page_size
        end = min(start + self.page_size, len(data))
        self.page_values_list = data[start:end]

        self.refresh_tree(self.page_values_list)
        self.layout()



    def refresh_tree(self, data):
        for i in self.tree.get_children():
            self.tree.delete(i)

            
        fields = self.app.data.fields
        self.tree['columns'] = fields
        self.tree['displaycolumns'] = self.treeview_display_fields
        for f in fields:
            self.tree.column(f, anchor=CENTER)
            self.tree.heading(f, text=f, anchor=CENTER)
        
        
        for i, values in enumerate(data):
            self.tree.insert('', 'end', values=values, iid=i, 
                             tags= self.tag_event if i % 2 == 0 else self.tag_odd)
        self.tree.update()



    def refill_data_by_selected_fields(self, selected_fields):
        self.treeview_display_fields = selected_fields
        self.refresh_tree(self.page_values_list)
        self.layout()

    def item_clicked(self):
        print('clicked')
            
    def content_search_command_test(self, command: str):
        values_list = self.page_values_list
        if len(values_list) == 0 or len(values_list[0]) == 0:
            return False, command # ok if values_list are empty
    
        values = values_list[0]
        for i in range(len(values)) :
            command = command.replace(f"#{i}", f'values[{i}]')
        try:
            result = eval(command)
            return type(result) is bool, command
        except:
            return False, command

    def on_content_search_event(self, event):
        def reset_all_data():
            self.app.data.set_display_values_list(self.app.data.total_values_list)
            self.refresh_page(self.app.data.display_values_list, 0, self.page_size)
            self.change_content_search_status(True)
            if self.content_search_callback:
                self.content_search_callback()
            return
        
        input = event.widget.get()
        if input.strip() == '':
            # when clean
            reset_all_data()

        ok, command = self.content_search_command_test(input)
        if not ok:
            reset_all_data()
            self.change_content_search_status(False)
            return

        values_list = self.app.data.total_values_list
        try:
            data = []
            for values in values_list:
                if eval(command) == True:
                    data.append(values)
            self.app.data.display_values_list = data
            self.refresh_page(data, 0, self.page_size)
            if self.content_search_callback:
                self.content_search_callback()
            self.change_content_search_status(True)
        except Exception as ex:
            print(ex)
            self.change_content_search_status(False)
    
    def change_content_search_status(self, status):
        if status == True:
            self.content_search_state_label.configure(image=self.content_search_state_image_ok)
        else:
            self.content_search_state_label.configure(image=self.content_search_state_image_error)
    

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
        r, c = None, None
        for i, s in enumerate(self.field_selectors):
            r, c = int(i / 5) + 1, i % 5
            s.grid(row=r, column=c, sticky='NW', padx=5)

        self.content_search.grid(row=r+1,column=0, columnspan=9, sticky="nsew")
        self.content_search_state_label.grid(row=r+1, column=c+1)
        # self.field_select_frame.grid_rowconfigure(r+1, weight=1)

        self.tree.grid(column=0, row=1, sticky="nsew", pady=0)
        self.tree_scroll.grid(column=0, row=2, sticky='EW', padx=8, pady=20) 

