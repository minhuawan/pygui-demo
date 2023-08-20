from tkinter import ttk
from tkinter import *


class Searcher():
    def __init__(self, app):
        self.callback = None
        self.frame = ttk.Frame(app.master, padding=10, style='searcher.TFrame')
        self.input = ttk.Entry(self.frame)
        self.input.bind('<KeyRelease>', self.on_key_release)
        
    def on_key_release(self, event):
        input = event.widget.get()
        if self.callback is not None:
            self.callback(input)

    def bind_search_callback(self, callback):
        self.callback = callback

    def layout(self, **kw):
        self.frame.grid()
        self.input.grid(column=0,row=0)

