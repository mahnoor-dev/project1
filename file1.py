import tkinter as tk
from tkinter import ttk



class window():
    def __init__(self,obj):
        
        welcome_label=ttk.Label(obj, text="WElCOME TO ABC HOTEL",font=('Georgia',26,'bold','italic'))
        welcome_label.grid( row=1, column=0, padx=8)

        RB_label=ttk.Label(obj, text="ROOM BOOKING SERVICE",font=('Arial',18,"bold"))
        RB_label.grid(row=2 , column=0)

        choice_label=ttk.Label(obj,text='Please select your room type',font=('rockwell',14,'italic'))
        choice_label.grid(sticky=tk.W,ipadx=10,ipady=8,row=3,padx=2,column=0)
    




                          #------------------PERSONAL INFORMATION OF USER-------------#

        
class Person():
    #LABELS
    def label(self,obj2):    
        name=ttk.Label(obj2, text="Name",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=6, column=1,sticky=tk.W)
        age=ttk.Label(obj2, text="Age",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=7, column=1,sticky=tk.W)
        cnic=ttk.Label(obj2, text="CNIC",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=8, column=1,sticky=tk.W)
        contact=ttk.Label(obj2, text="Contact No",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=9, column=1,sticky=tk.W)
        person=ttk.Label(obj2, text=" No of Persons",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=10, column=1,sticky=tk.W)
        

        country=ttk.Label(obj2, text="Country",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=6, column=3,sticky=tk.W)
        city=ttk.Label(obj2, text="City",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=7, column=3,sticky=tk.W)
        datein=ttk.Label(obj2, text="Date in",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=8, column=3,sticky=tk.W)
        dateout=ttk.Label(obj2, text="Date out",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=9, column=3,sticky=tk.W)
        maonthin=ttk.Label(obj2, text="Month in",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=10, column=3,sticky=tk.W)
        maonthout=ttk.Label(obj2, text="Month out",font=("Arial",12, "bold"),background="#BC8F8F").grid(row=11, column=3,sticky=tk.W)
    
            
            

     #ENTRY BOXES
    def Entry_box(self,obj2,age_entry=20,name_entry="mahnoor",cnic_entry="42101-62449928",country_entry="pakistan",city="karachi"):   #entrybox
        global age_var
        age_var=tk.IntVar()
        age_entry=ttk.Entry(obj2, width=20, textvariable=age_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=7, column=1, padx=100,sticky=tk.W)
        name_var=tk.StringVar()
        name_entry=ttk.Entry(obj2, width=20, textvariable=name_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=6, column=1,padx=100, sticky=tk.W)
        cnic_var=tk.StringVar()
        cnic_entry=ttk.Entry(obj2, width=20, textvariable=cnic_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=8, column=1, padx=100,sticky=tk.W) 
        contact_var=tk.IntVar()
        contact_entry=ttk.Entry(obj2, width=20, textvariable=contact_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=9, column=1, padx=100,sticky=tk.W) 
        country_var=tk.StringVar()
        country_entry=ttk.Entry(obj2, width=20, textvariable=country_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=6, column=3, padx=100, sticky=tk.W) 
        city_var=tk.StringVar()
        city_entry=ttk.Entry(obj2, width=20, textvariable=city_var, font=("Arial",12, "bold"), background="#BC8F8F").grid(row=7, column=3, padx=100, sticky=tk.W) 

    def Combo_box(self, obj2):
        #combo box for no of persons
        NOP_var=tk.IntVar()
        NOP_combo=ttk.Combobox(obj2, width=10, textvariable=NOP_var, state="read only")
        NOP_combo['value']=list([i for i in range(0,8)])
        NOP_combo.grid(row=10, column=1, padx=100, sticky=tk.E)
        NOP_combo.current(1)

        #datein combobox
        Din_var=tk.IntVar()
        Din_combo=ttk.Combobox(obj2, width=10, textvariable=Din_var, state="read only")
        Din_combo['values']=list(i for i in range(0,31))
        Din_combo.grid(row=8, column=3, padx=100, sticky=tk.E)
        Din_combo.current(7)


        #monthin combobox
        Min_var=tk.IntVar()
        Min_combo=ttk.Combobox(obj2, width=10, textvariable=Min_var, state="read only")
        Min_combo['values']=list(i for i in range(1,13))
        Min_combo.grid(row=10, column=3, padx=100, sticky=tk.E)
        Min_combo.current(1)


        #dateout combobox
        Dout_var=tk.IntVar()
        Dout_combo=ttk.Combobox(obj2, width=10, textvariable=Dout_var, state="read only")
        Dout_combo['values']=tuple([i for i in range(1,32)])
        Dout_combo.grid(row=9, column=3, padx=100, sticky=tk.E)
        Dout_combo.current(6)

       #monthout combobox
        Mout_var=tk.IntVar()
        Mout_combo=ttk.Combobox(obj2, width=10, textvariable=Mout_var, state="read only")
        Mout_combo['values']=list(i for i in range(1,13))
        Mout_combo.grid(row=11, column=3, padx=100, sticky=tk.E)
        Mout_combo.current(1)


    
        #BUTTON
    def button(self,obj2):
        done=ttk.Button(obj2,text="done",command=finish)
        done.grid(sticky=tk.W,ipadx=90,padx=10,pady=40,row=15,column=3)
    
   
def finish():
    a=age_var.get()
    try:
        if a==int():
            
            import tkinter
            root=tk.Tk()
            output="HELLO your room has been booked!!"
            ml=ttk.Label(root,text=output).grid(row=1)
        else:
            raise Exception
            
    except Exception as e:
        pass
