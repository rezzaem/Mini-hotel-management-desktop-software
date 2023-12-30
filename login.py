from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image
from tkinter import messagebox
import sqlite3
class LoginInterface:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("600x480")
        self.app.resizable(0,0)
        self.app.title('HMS')


        side_img_data = Image.open("IMG//side-img.png")
        self.email_icon_data = Image.open("IMG//email-icon.png")
        password_icon_data = Image.open("IMG//password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        self.email_icon = CTkImage(dark_image=self.email_icon_data, light_image=self.email_icon_data, size=(20,20))
        self.password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self.app, text="", image=side_img).pack(expand=True, side="left") 
        self.main_frame()

        
    def main_frame(self):
        self.frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#ffffff",corner_radius=0)
        self.frame.pack_propagate(0) # Don't allow the widgets inside to determine the self.frame's width / height
        self.frame.pack(expand=True, side="right") # Expand the self.frame to fill the root window

        CTkLabel(master=self.frame, text="خوش آمدید", text_color="#2E3C48", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="e", pady=(50, 5), padx=(0, 25))
        CTkLabel(master=self.frame, text="نام کاربری و رمز عبور خود را وارد کنید", text_color="#7E7E7E", anchor="w", justify="left", font=("vazir", 12)).pack(anchor="e", padx=(0, 25))

        CTkLabel(master=self.frame, text=": نام کاربری", text_color="#2E3C48", anchor="e", justify="left", font=("Arial Bold", 14), image=self.email_icon, compound="right").pack(anchor="e", pady=(38, 0), padx=(0, 25))
        self.user_input=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#2E3C48", border_width=1, text_color="#000000")
        self.user_input.pack(anchor="e", padx=(0, 25))
        
        CTkLabel(master=self.frame, text=": رمز عبور", text_color="#2E3C48", anchor="e", justify="left", font=("Arial Bold", 14), image=self.password_icon, compound="right").pack(anchor="e", pady=(21, 0), padx=(0, 25))
        self.pass_input=CTkEntry(master=self.frame, width=225, fg_color="#EEEEEE", border_color="#2E3C48", border_width=1, text_color="#000000")
        self.pass_input.pack(anchor="e", padx=(0, 25))

        CTkButton(master=self.frame, text="ورود", fg_color="#2E3C48", hover_color="#FCB830", font=("Arial Bold", 12), text_color="#ffffff", width=225,command=self.login).pack(anchor="w", pady=(40, 0), padx=(49, 0))
        CTkButton(master=self.frame, text="فراموشی رمز عبور", fg_color="#EEEEEE", hover_color="#FCB830", font=("Arial Bold", 9), text_color="#2E3C48", width=225,command=self.reset_pass).pack(anchor="w", pady=(20, 0), padx=(49, 0))
    def login(self):
        print(self.user_input)
        username = self.user_input.get()
        password = self.pass_input.get()
        self.db = sqlite3.connect("DB//database.db")
        self.cursor = self.db.cursor()
    

        try:
            self.cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''',(username, password))
            user=self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

        if user:
            print("Login successful!")
            wait_to_close=CTkMessagebox(message="ورود شما موفقیت آمیز بود",font=("Arial Bold", 12),
                  icon="check", option_1="سپاس",master=self.app)
            wait_to_close.get()
            self.db.close()
            self.app.destroy()
            return True

        else:
            print("Invalid username or password.")
            CTkMessagebox(title="ورود نادرست", message="نام کاربری یا رمز عبور اشتباه است",font=("Arial Bold", 12), icon="cancel",master=self.app)


    def reset_pass(self):
        # hide login frame
        self.frame.pack_forget()
        # create reset password frame
        self.reset_frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#ffffff",corner_radius=0)
        self.reset_frame.pack_propagate(0)
        self.reset_frame.pack(expand=True, side="right")

        CTkLabel(master=self.reset_frame, text="بازیابی رمز عبور", text_color="#2E3C48", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="e", pady=(50, 5), padx=(0, 25))
        CTkLabel(master=self.reset_frame, text="ایمیل خود را وارد کنید", text_color="#7E7E7E", anchor="w", justify="left", font=("vazir", 12)).pack(anchor="e", padx=(0, 25))

        CTkLabel(master=self.reset_frame, text=": ایمیل", text_color="#2E3C48", anchor="e", justify="left", font=("Arial Bold", 14), image=self.email_icon, compound="right").pack(anchor="e", pady=(38, 0), padx=(0, 25))
        self.email_input=CTkEntry(master=self.reset_frame, width=225, fg_color="#EEEEEE", border_color="#2E3C48", border_width=1, text_color="#000000")
        self.email_input.pack(anchor="e", padx=(0, 25))

        CTkButton(master=self.reset_frame, text="بازیابی", fg_color="#2E3C48", hover_color="#FCB830", font=("Arial Bold", 12), text_color="#ffffff", width=225,command=self.reset).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=self.reset_frame, text="بازگشت", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#2E3C48", width=225,command=self.back).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    def reset(self):
        email = self.email_input.get()
        self.db = sqlite3.connect("DB//database.db")
        self.cursor = self.db.cursor()
    

        try:
            self.cursor.execute('''
            SELECT username,password,email,first_name,last_name FROM users WHERE email = ?
        ''',(email,))
            user=self.cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

        if user:
            print("Email found!")
            self.reset_password(user)
            messagebox.showinfo("بازیابی", "ایمیل با موفقیت ارسال شد", parent=self.app)
            self.db.close()

        else:
            print("Invalid email.")
            messagebox.showerror("بازیابی نادرست", "ایمیل اشتباه است", parent=self.app)
            # CTkMessagebox(title="بازیابی نادرست", message="نام کاربری یا رمز عبور اشتباه است",font=("Arial Bold", 12), icon="cancel",master=self.app)
    def reset_password(self,user):
        # user = username , password,email,first_name,last_name

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        Message = MIMEMultipart()
        Message["To"] = user[2]
        Message["From"] = 'managment'
        Message["Subject"] = 'User and Password recovery'

        title = f'<b> reset password </b>'
        messageText = MIMEText(f'''
<html lang="fa">
    <body>
        <h1>بازیابی رمز عبور</h1>
        <p>عزیز {user[3]}،</p>
        <p>شما درخواست کرده‌اید که جزئیات حساب کاربری خود را بازیابی کنید. در ادامه آنها آمده است:</p>
        <table>
            <tr>
                <td><strong>نام کاربری:</strong></td>
                <td>{user[0]}</td>
            </tr>
            <tr>
                <td><strong>رمز عبور:</strong></td>
                <td>{user[1]}</td>
            </tr>
        </table>
        <p>لطفاً به منظور دلایل امنیتی، هر چه سریعتر پسورد خود را تغییر دهید.</p>
        <p>با احترام،</p>
        <p>تیم بوشهر بوم</p>
    </body>
</html>

''','html')
        Message.attach(messageText)

        email = 'bushehrboom@gmail.com'
        password = 'bdje mlil rgmv wauc'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo('Gmail')
        server.starttls()
        server.login(email,password)
        fromaddr = 'bushehrboom@gmail.com'
        toaddrs  = user[2]
        server.sendmail(fromaddr,toaddrs,Message.as_string())

        server.quit()



    def back(self):
        # hide reset password frame
        self.reset_frame.pack_forget()
        # create login frame
        self.main_frame()
    
    # def reset_pass(self,user):
    #     print(user)
        
    def run(self):
        self.app.mainloop()

# To use the class
login = LoginInterface()
login.run()