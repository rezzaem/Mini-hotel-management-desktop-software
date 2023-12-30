from tkinter import *
from tkinter import ttk #
from customtkinter import CTkOptionMenu
class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Tourist accommodation")

        self.root.overrideredirect(True)
        self.root.geometry("1290x600+235+255")
        #=========== title =================
        lbl_title=Label(self.root,text="افزودن اطلاعات مشتری",font=("Vazir",25,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)

        close_button = Label(self.root, text="X", font=("Arial", 12), bg="red", fg="white")
        close_button.place(x=1270, y=0)
        close_button.bind("<Button-1>", self.close_window)

        #=========== labelFrame =================
        labelframeleft=LabelFrame(self.root,bd=2,relief="ridge",text="اطلاعات مشتری",font=("Vazir",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=540)

        #=========== labels and entitys =================
        # shomare paziresh (refrence)
        lbl_cust_ref=Label(labelframeleft,text="شماره پذیرش",font=("Vazir",12,),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky="w")

        entry_ref=Entry(labelframeleft,width=22,font=("Vazir",12,))
        entry_ref.grid(row=0,column=1)

        # name
        lbl_cust_ref=Label(labelframeleft,text="نام",font=("Vazir",12,),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky="w")

        entry_ref=Entry(labelframeleft,width=22,font=("Vazir",12,))
        entry_ref.grid(row=1,column=1)

        # family name
        lbl_cust_ref=Label(labelframeleft,text="نام خانوادگی",font=("Vazir",12,),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky="w")

        entry_ref=Entry(labelframeleft,width=22,font=("Vazir",12,))
        entry_ref.grid(row=2,column=1)

        # jensiat
        # made by custom tkinter - gender choose with optionmenu_callback
        lbl_gender=Label(labelframeleft,text="جنسیت",font=("Vazir",12,),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky="w")

        gender_menu = CTkOptionMenu(labelframeleft, values=["آقا", "خانم"],width=205,font=("Vazir",16),corner_radius=0,dropdown_font=("Vazir",18),
                                         fg_color='#ffffff',text_color='black',button_color='grey',
                                         command=self.optionmenu_callback)
        gender_menu.set("آقا")
        gender_menu.grid(row=3,column=1)


        # phone number 1
        lbl_phone_num=Label(labelframeleft,text="شماره تماس",font=("Vazir",12,),padx=2,pady=6)
        lbl_phone_num.grid(row=4,column=0,sticky="w")

        entry_ref=Entry(labelframeleft,width=22,font=("Vazir",12,))
        entry_ref.grid(row=4,column=1)




    def optionmenu_callback(self,choice):
        print("optionmenu dropdown clicked:", choice)     

    def close_window(self, event):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()