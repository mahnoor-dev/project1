from file1 import window
from file2 import button
from file2 import ECOCLASS_ROOMS
from file2 import BUISCLASS_ROOMS 
import tkinter as tk
from tkinter import ttk






                 #----------MENU-----------#

class MENU:
    def ECOavb():  #ECONOMY CLASS MENU
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk()
        point1=ttk.Label(root,text='Economy class rooms are available!').pack()
        root.mainloop()
        
    def BUSIavb(): #BUSINESS CLASS MENU
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk()
        point1=ttk.Label(root,text='Business class rooms are available!').pack()
        root.mainloop()

    def method(self,obj4):
        menu=tk.Menu(obj4)
        obj4.config(menu=menu)

        subMenu=tk.Menu(menu)
        menu.add_cascade(label="Room Details",menu=subMenu)
        subMenu.add_command(label='Economy Class',command=ECOCLASS_ROOMS.details)
        subMenu.add_separator()
        subMenu.add_command(label='Business Class',command=BUISCLASS_ROOMS.details)
        subMenu.add_separator()

        avbMenu=tk.Menu(menu)
        menu.add_cascade(label='Rooms Available',menu=avbMenu)
        avbMenu.add_command(label='Economy Class',command=MENU.ECOavb)
        avbMenu.add_separator()
        avbMenu.add_command(label='Business Class',command=MENU.BUSIavb)
        avbMenu.add_separator()    
        







win=tk.Tk()
win.title("room booking system")
win.geometry("1200x900")
#canvas=tk.Canvas(win,width=1200,height=800)
#canvas.grid(row=6,column=0)

#photo=tk.PhotoImage(file="F:\\OOP PROJRECT\\pic.png")
#canvas.create_image(0,0,image=photo, anchor=tk.NW)
#win.config(bg="#BC8F8F")
c=window(win)
m=MENU()
m.method(win)




b=button()
b.method(win)

win.mainloop()



