from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


##### Creating the Database for both user information and booking details #####

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

conn_2 = sqlite3.connect('bookings.db')
cursor_2 = conn_2.cursor()


##### Second screen after login, should show two different buttons for rooms and facilities #####
def main(username):
    global screen_2
    screen_2 = Tk()
    screen_2.geometry("530x440")
    screen_2.title("Main Menu")

    Label(screen_2,text = f"Welcome {username}!",fg='white', bg = "#535458", width = "300", height = "2", font = ("orbitron", 20,'bold')).pack()
    Label(text = "").pack()

    Button(screen_2,text='Rooms',command = lambda: rooms(username),relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12' , fg='black').pack(pady=(30,25))

    Button(screen_2,text='Facilities',command = lambda :facilities(username),relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12', fg='black').pack(pady=(15,0))

    Button(screen_2,text='Booked',command = lambda :bookedRooms() ,relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12', fg='black').pack(pady=(40,40))

    screen_2.mainloop()

###### Subroutine for the "Booked" button in the program, was added as a feature for users to see what is currently unavailable for booking ######     
def bookedRooms():
    screen_4 = Tk()
    screen_4.geometry("530x400")
    screen_4.title("Booked")

    Button(screen_4,text='Rooms Booked',command = lambda :roomBooked(), relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='15' , fg='black').pack(pady=(60,25))

    Button(screen_4,text='Facilities Booked',command = lambda :facilitiesBooked(),relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='15', fg='black').pack(pady=(15,0))


    screen_4.mainloop()

###### Subroutine for the "Facilities Booked" Button which allows users to view the facilities that are unavailable for booking, this is done using tree view ######
def facilitiesBooked():
    screen_5 = Tk()
    screen_5.geometry("830x400")
    screen_5.title("Facilities Booked")

    database=sqlite3.connect("bookings.db")

    bookedTable=ttk.Treeview(screen_5, height = 21)
    bookedTable["columns"] = ("Username","BookedItem", "Time")
    bookedTable.column("#0", width =0, stretch = NO)
    bookedTable.column("Username", anchor = CENTER, width = 265)
    bookedTable.column("BookedItem", anchor = CENTER, width = 265)
    bookedTable.column("Time", anchor = CENTER, width = 265)

    bookedTable.heading("#0", text = "", anchor = CENTER)
    bookedTable.heading("Username", text = "Name", anchor = CENTER)
    bookedTable.heading("BookedItem", text = "Facilities Booked", anchor = CENTER)
    bookedTable.heading("Time", text = "Times Booked", anchor = CENTER)

    c=database.cursor()
    c.execute("SELECT * FROM booking_f")
    data=c.fetchall()

    users = cursor.execute("SELECT name,username FROM user_info")
    user_data = users.fetchall()
    user_dict = {}
    for i in user_data:
        user_dict[i[1]] = i[0]

    if data:
        itemNumber=0
        for items in data:
            bookedTable.insert("", "end", iid = (itemNumber), text = "", values = (user_dict[items[0]].capitalize(),items[1].capitalize(), items[2].upper()))
            itemNumber+=1
    bookedTable.pack()

###### Same method above except instead of the users viewing facilities booked, they view the rooms that are booked #####
def roomBooked():
    screen_6 = Tk()
    screen_6.geometry("830x400")
    screen_6.title("Rooms Booked")

    database=sqlite3.connect("bookings.db")

    bookedTable=ttk.Treeview(screen_6, height = 21)
    bookedTable["columns"] = ("Username","BookedItem", "Time")
    bookedTable.column("#0", width =0, stretch = NO)
    bookedTable.column("Username", anchor = CENTER, width = 265)
    bookedTable.column("BookedItem", anchor = CENTER, width = 265)
    bookedTable.column("Time", anchor = CENTER, width = 265)

    bookedTable.heading("#0", text = "", anchor = CENTER)
    bookedTable.heading("Username", text = "Name", anchor = CENTER)
    bookedTable.heading("BookedItem", text = "Rooms Booked", anchor = CENTER)
    bookedTable.heading("Time", text = "Times Booked", anchor = CENTER)

    c=database.cursor()
    c.execute("SELECT * FROM booking_r")
    data=c.fetchall()

    users = cursor.execute("SELECT name,username FROM user_info")
    user_data = users.fetchall()
    user_dict = {}
    for i in user_data:
        user_dict[i[1]] = i[0]

    if data:
        itemNumber = 0
        for items in data:
            bookedTable.insert("", "end", iid=(itemNumber), text="",
                               values=(user_dict[items[0]].capitalize(), items[1].capitalize(), items[2].upper()))
            itemNumber += 1
    bookedTable.pack()


def check_availability(type, booking_list):

    data = cursor_2.execute(f"""SELECT * FROM {type}    
    """)                                                 #### Fetches the records from the database ####
    data = data.fetchall()

    for i in data:
        if (i[1],i[2]) == (booking_list[1],booking_list[2]):
            return False
    return True

    
###### Subroutine to create 2 different tables in the database, one table for rooms and one table for facilities ######
def book_now(type,username,booked_item,time):
    if type == "booking_r":
        cursor_2.execute("""
                        INSERT INTO booking_r(username, booked_item, time) VALUES(?,?,?)
                        """, (username,booked_item, time))
    elif type == "booking_f":
        cursor_2.execute("""
                                INSERT INTO booking_f(username, booked_item, time) VALUES(?,?,?)
                                """, (username, booked_item, time))
    conn_2.commit()

def booked(type,username,booked_item,time):

    if check_availability(type,(username,booked_item,time)) == True:
        book_now(type,username,booked_item,time)
        messagebox.showinfo("Successful", "Booked Successfully!")

    elif check_availability(type,(username,booked_item,time)) == False:
        messagebox.showerror("Not Available", "This booking has already been occupied!")

###### Subroutine to create the drop down menu for facilities ######
def facilities(username):
    screen_3 = Tk()
    screen_3.geometry("560x400")
    screen_3.title("Rooms")


    Label(screen_3,text = f"Facilities",fg='white', bg = "#535458", width = "300", height = "2", font = ("orbitron", 20,'bold')).pack()
    Label(text = "").pack()
    Label(screen_3,text = f"Select Facilities\tSelect Time",fg='white', width = "300", height = "2", font = ("orbitron", 20,'bold')).pack(pady=20)


    options_list = [
        "Sports hall",
        "Dance studio",
        "Library Learning facilities",
        "Astroturf",
        "Basketball court",
        "Post-16",
        "Auditorium",
        "Swimming pool",
        "GYM",
        "Netball court",
        "Drama studio",
        "Sprint track",
        "Art studio 1",
        "Art studio 2",
        "Science Lab 1",
        "Science Lab 2",
        "Computer Lab"

    ]

    value_inside = StringVar(screen_3)

    value_inside.set(options_list[0])

    facilities_menu = OptionMenu(screen_3, value_inside, *options_list)
    facilities_menu.config(font =("orbitron", 14), width=16)
    facilities_menu["menu"].config(font =("orbitron", 14))
    facilities_menu.place(x=40,y=170)

    options_list_2 = ['12:00 AM - 01:00 AM',
                      '01:00 AM - 02:00 AM',
                      '02:00 AM - 03:00 AM',
                      '03:00 AM - 04:00 AM',
                      '04:00 AM - 05:00 AM',
                      '05:00 AM - 06:00 AM',
                      '06:00 AM - 07:00 AM',
                      '07:00 AM - 08:00 AM',
                      '08:00 AM - 09:00 AM',
                      '09:00 AM - 10:00 AM',
                      '10:00 AM - 11:00 AM',
                      '11:00 AM - 12:00 AM',
                      '12:00 PM - 01:00 PM',
                      '01:00 PM - 02:00 PM',
                      '02:00 PM - 03:00 PM',
                      '03:00 PM - 04:00 PM',
                      '04:00 PM - 05:00 PM',
                      '05:00 PM - 06:00 PM',
                      '06:00 PM - 07:00 PM',
                      '07:00 PM - 08:00 PM',
                      '08:00 PM - 09:00 PM',
                      '09:00 PM - 10:00 PM',
                      '10:00 PM - 11:00 PM',
                      '11:00 PM - 12:00 AM'
                      ]

    value_inside_2 = StringVar(screen_3)

    value_inside_2.set(options_list_2[0])

    time_menu = OptionMenu(screen_3, value_inside_2, *options_list_2)
    time_menu.config(font=("orbitron", 14), width=16)
    time_menu["menu"].config(font=("orbitron", 14))
    time_menu.place(x=300, y=170)

    Label(text="").pack()
    Label(text="").pack()
    Button(screen_3,text='Book Now',command = lambda : booked('booking_f',username,value_inside.get(),value_inside_2.get()),relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12' , fg='black').pack(pady=(100,25))

    screen_3.mainloop()

###### Subroutine to create drop down menu for rooms ######
def rooms(username):
    screen_4 = Tk()
    screen_4.geometry("560x400")
    screen_4.title("Rooms")


    Label(screen_4,text = f"Rooms",fg='white', bg = "#535458", width = "300", height = "2", font = ("orbitron", 20,'bold')).pack()
    Label(text = "").pack()

    Label(screen_4,text = f"Select Rooms\tSelect Time",fg='white', width = "300", height = "2", font = ("orbitron", 20,'bold')).pack(pady=20)

    options_list = [
        "Study room 1",
        "Study room 2",
        "Study room 3",
        "Conference room 1",
        "Conference room 2",
        "Meeting room 1",
        "Meeting room 2",
        "BLP (Blended learning practice)",
        "Food technology room 1",
        "Food technology room 2",
        "Textiles, Resistant Material and Electronics room 1",
        "Textiles, Resistant Material and Electronics room 2",
        "Radio Station, Recording Studio",
        "Editing Studio",
        "I.T. Suite",
        "Outdoor learning classroom 1",
        "Outdoor learning classroom 2"
    ]

    value_inside = StringVar(screen_4)

    value_inside.set(options_list[0])

    rooms_menu = OptionMenu(screen_4, value_inside, *options_list)
    rooms_menu.config(font =("orbitron", 14), width=16)
    rooms_menu["menu"].config(font =("orbitron", 14))
    rooms_menu.place(x=40,y=170)


    options_list_2 = ['12:00 AM - 01:00 AM',
 '01:00 AM - 02:00 AM',
 '02:00 AM - 03:00 AM',
 '03:00 AM - 04:00 AM',
 '04:00 AM - 05:00 AM',
 '05:00 AM - 06:00 AM',
 '06:00 AM - 07:00 AM',
 '07:00 AM - 08:00 AM',
 '08:00 AM - 09:00 AM',
 '09:00 AM - 10:00 AM',
 '10:00 AM - 11:00 AM',
 '11:00 AM - 12:00 AM',
 '12:00 PM - 01:00 PM',
 '01:00 PM - 02:00 PM',
 '02:00 PM - 03:00 PM',
 '03:00 PM - 04:00 PM',
 '04:00 PM - 05:00 PM',
 '05:00 PM - 06:00 PM',
 '06:00 PM - 07:00 PM',
 '07:00 PM - 08:00 PM',
 '08:00 PM - 09:00 PM',
 '09:00 PM - 10:00 PM',
 '10:00 PM - 11:00 PM',
 '11:00 PM - 12:00 AM'
]

    value_inside_2 = StringVar(screen_4)

    value_inside_2.set(options_list_2[0])

    time_menu = OptionMenu(screen_4, value_inside_2, *options_list_2)
    time_menu.config(font =("orbitron", 14), width=16)
    time_menu["menu"].config(font =("orbitron", 14))
    time_menu.place(x=300,y=170)


    Label(text = "").pack()
    Label(text = "").pack()
    Button(screen_4,text='Book Now',command = lambda : booked('booking_r',username,value_inside.get(),value_inside_2.get()),relief=RAISED, font = ("orbitron", 20,'bold'), bg = "grey",width='12' , fg='black').pack(pady=(100,25))

    screen_4.mainloop()
