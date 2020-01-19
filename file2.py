import file1
from file1 import window
from file1 import Person
import tkinter as tk
from tkinter import ttk


                         #------COMMAND FOR ECONOMY BUTTON------#

class ECONOMY(Person):
    def __init__(self):
        import tkinter as ttk
        from tkinter import ttk
        root2=tk.Tk()
        root2.title("INFORMATION")
        root2.config(bg="#BC8F8F")
       

        label1=ttk.Label(root2,text='Economy class selected',background='#BC8F8F')
        label1.grid(sticky=tk.W,ipadx=10,row=2,column=2,padx=6)
        Person.label(self,root2)
        Person.Entry_box(self,root2)
        Person.Combo_box(self,root2)
        Person.button(self,root2)

                    #-----COMMAND FOR BUSINESS BUTTON------#
class BUISNESS(Person):
    def __init__(self):
        import tkinter as ttk
        from tkinter import ttk
        root2=tk.Tk()
        root2.title("INFORMATION")
        root2.config(bg="#BC8F8F")
       

        label1=ttk.Label(root2,text='Business class selected',background='#BC8F8F')
        label1.grid(sticky=tk.W,ipadx=10,row=2,column=2,padx=6)
        Person.label(self,root2)
        Person.Entry_box(self,root2)
        Person.Combo_box(self,root2)
        Person.button(self,root2)


              #----------------ECONOMY AND BUSINESS BUTTONS-------------#
class button:
     def method(self,obj3):
        ecobtn=ttk.Button(obj3,text="Economy Class",command=ECONOMY)
        ecobtn.grid(sticky=tk.W,padx=10,row=4,column=0)

        busibtn=ttk.Button(obj3,text="Business Class",command=BUISNESS)
        busibtn.grid(sticky=tk.W,padx=150,row=4,column=0)    
    







#OVERRIDING

class ROOMS:
    def details(self):
        pass
    

class ECOCLASS_ROOMS(ROOMS):
    def details():
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk()
        root.geometry('500x300')
        point1=ttk.Label(root,text='ECONOMY CLASS ROOMS:').grid(row=0,sticky=tk.W)
        point1=ttk.Label(root,text='Spacious, bright and outward facing rooms measuring 19 m2 and totally').grid(row=1,sticky=tk.W)
        point1=ttk.Label(root,text='refurbished. The room comes with Dreamax bed (manufactured and designed').grid(row=2,sticky=tk.W)
        point1=ttk.Label(root,text='exclusively by Flex for Meliá Hotels International), a modern, fully').grid(row=3,sticky=tk.W)
        point1=ttk.Label(root,text='equipped bathroom finished in top quality bronze coloured ceramics and').grid(row=4,sticky=tk.W)
        point1=ttk.Label(root,text='an independent entrance. It also has a home automation system which').grid(row=4,sticky=tk.W)
        point1=ttk.Label(root,text='automatically regulates the temperature of the room based on guest').grid(row=5,sticky=tk.W)
        point1=ttk.Label(root,text='presence or absence from the room. They also provide an intelligent').grid(row=6,sticky=tk.W)
        point1=ttk.Label(root,text='temperature management system that automatically adjusts the temperature').grid(row=7,sticky=tk.W)
        point1=ttk.Label(root,text='depending on whether anyone is in the room.').grid(row=8,sticky=tk.W)

        point1=ttk.Label(root,text='Flat-screen TV Satellite Channels Safe large enough for laptop Minibar').grid(row=8,sticky=tk.W)

        point1=ttk.Label(root,text='Free toiletries Safe').grid(row=9,sticky=tk.W)
        point1=ttk.Label(root,text='').grid(row=10,sticky=tk.W)
        point1=ttk.Label(root,text='COST = 20,000 Rs/-').grid(row=11,sticky=tk.W)
        root.mainloop()
class BUISCLASS_ROOMS(ROOMS):
    def details():
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk()
        root.geometry('600x350')
        point1=ttk.Label(root,text='BUSINESS CLASS ROOMS:').grid(row=0,sticky=tk.W)
        point1=ttk.Label(root,text='Spacious, bright and outward facing rooms measuring 27 m2').grid(row=1,sticky=tk.W)
        point1=ttk.Label(root,text=' and totally refurbished. The room comes with double bed or twin').grid(row=2,sticky=tk.W)
        point1=ttk.Label(root,text='beds with Dreamax mattress (manufactured and designed exclusively by Flex for Meliá Hotels International').grid(row=3,sticky=tk.W)
        point1=ttk.Label(root,text='a modern, fully equipped bathroom finished in top').grid(row=4,sticky=tk.W)
        point1=ttk.Label(root,text='quality bronze coloured ceramics and an independent hallway-dressing').grid(row=5,sticky=tk.W)
        point1=ttk.Label(root,text='area. It also has a home automation system which automatically regulates').grid(row=6,sticky=tk.W)
        point1=ttk.Label(root,text='the temperature of the room based on guest presence or absence').grid(row=7,sticky=tk.W)
        point1=ttk.Label(root,text='from the room. All the rooms have a magnificent hallway-dressing area,').grid(row=8,sticky=tk.W)
        point1=ttk.Label(root,text='as well as a room off the bathroom, which is independent of the room as it has double doors.').grid(row=9,sticky=tk.W)
        point1=ttk.Label(root,text='Flat-screen TV Satellite Channels Safe large enough').grid(row=10,sticky=tk.W)
        point1=ttk.Label(root,text='for laptop Hairdryer Minibar Free toiletries').grid(row=11,sticky=tk.W)
        point1=ttk.Label(root,text='').grid(row=12,sticky=tk.W)
        point1=ttk.Label(root,text='COST = 35,000 Rs/-').grid(row=13,sticky=tk.W)
        root.mainloop()





