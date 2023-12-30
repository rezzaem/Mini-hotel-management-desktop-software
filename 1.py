from tkinter import *
from PIL import Image,ImageTk
from customer import cust_win


class HotelManagmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Tourist accommodation")
        self.root.state("zoomed")
        self.root.geometry("1980x1080+0+0")
       
        #============ header img================
        img_header=Image.open(r"C:\Users\turbo\OneDrive\Desktop\Py\Mini Hotel managment desktop app\IMG\header-mainpage.png")
        self.window_img_header=ImageTk.PhotoImage(img_header)
        lbl_img_header=Label(self.root,image=self.window_img_header,bd=4)
        lbl_img_header.place(x=0,y=0,width=1920,height=176)

        #============ logo img================
        img_logo=Image.open(r"C:\Users\turbo\OneDrive\Desktop\Py\Mini Hotel managment desktop app\IMG\logo_without_text.png")
        img_logo=img_logo.resize((176,176))
        self.window_img_logo=ImageTk.PhotoImage(img_logo)
        lbl_img_logo=Label(self.root,image=self.window_img_logo,bd=4,bg="black",relief="ridge")
        lbl_img_logo.place(x=0,y=0,width=240,height=176)

        #=========== title =================
        lbl_title=Label(self.root,text="سیستم مدیریت اقامتگاه",font=("Vazir",25,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=-200,y=176,width=2000,height=50)

        #=========== main frame=============
        main_frame=Frame(self.root,bd=4)
        main_frame.place(x=0,y=226,width=1980,height=854)
        
        #=========== Menu =============
        lbl_menu=Label(main_frame,text="منو",font=("Vazir",20,"bold"),bg="black",fg='gold',bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=========== Button frame =============
        btn_frame=Frame(main_frame,bd=4,relief="ridge")
        btn_frame.place(x=0,y=55,width=228,height=260)

        customer_btn=Button(btn_frame,command=self.customer_panel,text="مشتریان",width=22,font=("Vazir",14,"bold"),bg="black",fg='gold',bd=0,cursor='hand1')
        customer_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="اتاق ها",width=22,font=("Vazir",14,"bold"),bg="black",fg='gold',bd=0,cursor='hand1')
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="جزئیات",width=22,font=("Vazir",14,"bold"),bg="black",fg='gold',bd=0,cursor='hand1')
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="آمار",width=22,font=("Vazir",14,"bold"),bg="black",fg='gold',bd=0,cursor='hand1')
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="خروج",width=22,font=("Vazir",14,"bold"),bg="black",fg='gold',bd=0,cursor='hand1')
        logout_btn.grid(row=4,column=0,pady=1)


        #=========== right side image =============

        img_right_panel_bg=Image.open(r"C:\Users\turbo\OneDrive\Desktop\Py\Mini Hotel managment desktop app\IMG\right_panel_bg.png")
        self.frame_img_right_panel=ImageTk.PhotoImage(img_right_panel_bg)
        lbl_img_right_panel=Label(main_frame,image=self.frame_img_right_panel,bd=4,relief="ridge")
        lbl_img_right_panel.place(x=230,y=0,width=1295,height=605)

        #=========== left side down image =============

        img_left_panel_down=Image.open(r"C:\Users\turbo\OneDrive\Desktop\Py\Mini Hotel managment desktop app\IMG\left_panel_down.png")
        img_left_panel_down=img_left_panel_down.resize((230,295))
        self.frame_img_left_panel=ImageTk.PhotoImage(img_left_panel_down)
        lbl_img_left_panel=Label(main_frame,image=self.frame_img_left_panel,bd=4,relief="ridge")
        lbl_img_left_panel.place(x=0,y=310,width=230,height=295)

    def customer_panel(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=HotelManagmentSystem(root)
    root.mainloop()
