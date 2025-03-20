import sqlite3
from create_account import create_account
from tkinter import ttk, messagebox

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()
from app import *


class login:
    def __init__(self):

        self.ws = Tk()
        self.ws.title('Login')
        self.ws.geometry('640x330')

        self.label_1 = Label(self.ws, text='Login',font=("Helvetica",12))
        self.label_1.place(x=30, y=7)

        self.separator = ttk.Separator(self.ws, orient='horizontal')
        self.separator.place(x=0,y=45, relwidth=1)


        self.username_label = Label(self.ws, text='Username',font=("Helvetica",12))
        self.username_label.place(x=70,y=100)

        self.password = Label(self.ws, text='Password',font=("Helvetica",12))
        self.password.place(x=70,y=160)

        self.username_entry = Entry(self.ws,width=35,font=("Helvetica",12))
        self.username_entry.place(x=250,y=100)

        self.password_entry = Entry(self.ws,width=35,font=("Helvetica",12), show="*")
        self.password_entry.place(x=250,y=160)

        self.separator = ttk.Separator(self.ws, orient='horizontal')
        self.separator.place(x=0,y=250, relwidth=1)

        self.login_btn = Button(self.ws,width=15,height=2, text='Login',font=("Helvetica",11), command=self.login)
        self.login_btn.place(x=480,y=265)

        self.create_account_label = Label(self.ws,text='Create an account',font=("Helvetica",12), cursor='hand2')
        self.create_account_label.place(x=40, y=220)
        self.create_account_label.bind("<Button-1>", lambda e: create_account())

        self.logged_in = False


        self.ws.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        data = cursor.execute("""
        SELECT * from user_info WHERE username is (?) AND password is (?)
        """, (username, password))

        check = data.fetchall()

        if len(check) == 0:
            messagebox.showerror("Error", "Invalid User Name Or Password")

        else:
            messagebox.showinfo("Successful", "Logged In")
            self.logged_in = True
            self.ws.destroy()
            screen.destroy()
            run = main(username)

            if run == 'Logout':
                login()




screen = Tk()
screen.geometry("530x400")
screen.title("Booking System")




Label(screen,text = "Booking System",fg='white', bg = "#535458", width = "300", height = "2", font = ("orbitron", 20,'bold')).pack()
Label(screen,text = "").pack()

Button(screen,text='Login',command = login,relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12' , fg='black').pack(pady=(25,25))

Button(screen,text='Register',command = create_account,relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12', fg='black').pack(pady=(15,0))



screen.mainloop()
