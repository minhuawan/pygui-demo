from tkinter import ttk

class Tabs():
    def __init__(self, app):
        self.frame = ttk.Frame(app.master, padding=10, style='tab.TFrame')
        self.items = []
        for i in range(3):
            self.items.append(ttk.Label(self.frame, text=f'Tab {i}'))

    def layout(self):
        self.frame.grid()
        for i, tab in enumerate(self.items):
            tab.grid(column=i, row=0)