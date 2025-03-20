from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

###### CREATING A CLASS FOR THE CREATE ACCOUNT FEATURE OF THE PROGRAM ######

class create_account:
    def __init__(self):

        self.ws = Tk()
        self.ws.title('Create Account')
        self.ws.geometry('640x330')
        
            ######  THIS PART OF THE CODE IS THE DESIGN FOR HOW THE WINDOW WILL LOOK ; CREATING LABELS, USING SEPARATOR'S AND ETC. ######
        

        self.label_1 = Label(self.ws, text='Create Account', font=("Helvetica", 12))
        self.label_1.place(x=30, y=7)

        self.separator = ttk.Separator(self.ws, orient='horizontal')
        self.separator.place(x=0, y=45, relwidth=1)

        self.name_label = Label(self.ws, text='Name', font=("Helvetica", 12))
        self.name_label.place(x=70, y=80)

        self.username_label = Label(self.ws, text='Username', font=("Helvetica", 12))
        self.username_label.place(x=70, y=120)

        self.password = Label(self.ws, text='Password', font=("Helvetica", 12))
        self.password.place(x=70, y=160)

        self.verifypassword = Label(self.ws, text='Re-enter password', font=("Helvetica", 12))
        self.verifypassword.place(x=70, y=200)

        self.name_entry = Entry(self.ws, width=35, font=("Helvetica", 12))
        self.name_entry.place(x=250, y=80)

        self.username_entry = Entry(self.ws, width=35, font=("Helvetica", 12))
        self.username_entry.place(x=250, y=120)

        self.password_entry = Entry(self.ws, width=35, font=("Helvetica", 12),show="*")
        self.password_entry.place(x=250, y=160)

        self.verifypassword_entry = Entry(self.ws, width=35, font=("Helvetica", 12),show="*")
        self.verifypassword_entry.place(x=250, y=200)

        self.separator = ttk.Separator(self.ws, orient='horizontal')
        self.separator.place(x=0, y=250, relwidth=1)

        self.create_account_btn = Button(self.ws, width=15, height=2, text='Create Account',
                                         font=("Helvetica", 11), command=self.create_account_function)
        self.create_account_btn.place(x=480, y=265)

        self.ws.mainloop()



        ###### CREATING A SUBROUTINE WITHIN THE CLASS ######

        
    def create_account_function(self):

        if self.password_entry.get() == '' or self.verifypassword_entry.get() == '' or self.name_entry == '' or self.username_entry =='':
            messagebox.showerror('Error', 'Please enter all the required information!')

        else:

            if self.password_entry.get() != self.verifypassword_entry.get():
                messagebox.showerror('Error','The entered passwords do not match!')                        ###### THIS SUBROUTINE IS CREATED SO THAT THE USER HAS TO INPUT ALL THE INFORMATION REQUIRED ######
            else:                                                                                          ###### BASICALLY A VALIDATION, FOR THE PROGRAM TO RUN SMOOTHLY ####################################
                try:
                    dictionary = None
                    cursor.execute("""
                    INSERT INTO user_info(name, username, password) VALUES(?,?,?)
                    """, (self.name_entry.get(), self.username_entry.get(), self.password_entry.get()))

                    conn.commit()

                    messagebox.showinfo("Successful", "Account created!")
                    self.ws.destroy()

                except:
                    messagebox.showerror("Error", "There is already another account with that username!")
