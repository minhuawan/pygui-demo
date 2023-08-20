





# from tkinter import *

# def toplevelwin():
#     def clear(): return
#     select = unselect = done = enter = clear
#     window = Toplevel()
#     window.minsize(900, 500)
    

#     frame0 = Frame(window)
#     frame0.grid(row=0, column=0, sticky='WE', padx=5, pady=5, columnspan=3)
#     frame0.grid_columnconfigure(0, weight=1)
#     lblentry = Label(frame0, text="Entry Box:")
#     lblentry.grid(row=0, column=0, sticky='W')
#     entrybx = Entry(frame0)
#     entrybx.grid(row=1, column=0, sticky='NSEW', columnspan=2)
#     entrybt = Button(frame0, text=' Enter ', command=enter)
#     entrybt.grid(row=1, column=2, sticky='NW', padx=3)

#     frame1 = Frame(window)
#     frame1.grid(row=1, column=0, sticky='EW', padx=5, pady=5)
#     lblshow_lst = Label(frame1, text="List Box 1:")
#     lblshow_lst.grid(row=0, sticky='W')
#     show_lst = Listbox(frame1)
#     show_lst.grid(row=1, sticky='W')

#     frame2 = Frame(window)
#     frame2.grid(row=1, column=1, sticky='W')
#     selbtn = Button(frame2, text='Select', command=select)
#     selbtn.grid(row=0, padx=5, sticky='EW')
#     uselbtn = Button(frame2, text='Unselect', command=unselect)
#     uselbtn.grid(row=1, padx=5, sticky='EW')

#     frame3 = Frame(window)
#     frame3.grid(row=1, column=2, sticky='W', padx=5, pady=5)
#     lblsel_lst = Label(frame3, text="List Box 2:")
#     lblsel_lst.grid(row=0, sticky='W')
#     sel_lst = Listbox(frame3)
#     sel_lst.grid(row=1, column=0, sticky='W')

#     frame4 = Frame(window)
#     frame4.grid(row=2, column=0, sticky='WE', padx=5, pady=5, columnspan=3)
#     frame4.grid_columnconfigure(0, weight=1)
#     Button(frame4, text=' Done ', command=done).grid(
#         row=0, column=0, padx=7, pady=2, sticky='E')
#     Button(frame4, text='Clear', command=clear).grid(
#         row=0, column=1, padx=7, pady=2, sticky='E')

#     window.wait_window(window)


# # root = Tk()
# # toplevelwin()
# # root.mainloop()



from app import App
if __name__ == "__main__":
    app = App()
    app.run()