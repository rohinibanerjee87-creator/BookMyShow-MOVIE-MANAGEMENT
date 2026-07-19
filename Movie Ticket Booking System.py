from tkinter import *
from tkinter import ttk, messagebox
import random
from PIL import ImageTk, Image
import calendar
from datetime import datetime
import sqlite3



def init_db():
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        release_date TEXT,
        genre TEXT,
        language TEXT,
        duration TEXT,
        rating TEXT,
        demand TEXT,
        price REAL,
        status TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS theatres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rating TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS seats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seat_number TEXT,
        status TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_date TEXT,
        status TEXT,
        amount REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        method TEXT,
        seat TEXT,
        transaction_id TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cancellations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie TEXT,
        reason TEXT,
        other_reason TEXT
    )
    """)

    cur.execute("INSERT OR IGNORE INTO users(username,password) VALUES('admin','1234')")

    conn.commit()
    conn.close()


init_db()

#Login Page
def open_login():
    win = Toplevel(root)
    win.title("Login")
    win.geometry("1920x1032")
    win.configure(bg="lightblue")

    try:
        bg = Image.open(r"C:/Users/Rohini/OneDrive/Desktop/MOVIE MANAGEMENT SYSTEM/login.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    def login():
        conn = sqlite3.connect("movie.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (entry_user.get(), entry_pass.get())
        )

        user = cur.fetchone()
        conn.close()

        if user:
            current_user.set(f"Welcome, {entry_user.get()}")
        
            messagebox.showinfo("Login", "Login Successful")
        
            btn_login.pack_forget()
            win.destroy()
        
            show_main_menu()

        else:
            messagebox.showerror("Login", "Invalid Username or Password")

    Label(win, text="Login Page", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=20)
    Label(win, text="Username", bg="black", fg="white").pack()
    entry_user = Entry(win, width=30)
    entry_user.pack(pady=5)

    Label(win, text="Password", bg="black", fg="white").pack()
    entry_pass = Entry(win, width=30, show="*")
    entry_pass.pack(pady=5)

    Button(win, text="Login",bg="green",fg="white", command=login).pack(pady=20)
    
#Theater Page
def open_theatre():
    win = Toplevel(root)
    win.title("Theatre Details")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    def submit():
        conn = sqlite3.connect("movie.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO theatres(name, rating) VALUES (?,?)",
            (combo_theatre.get(), entry_rating.get())
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Theatre Saved")

    Label(win, text="Theatre Details", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=20)

    Label(win, text="Select Theatre", bg="black", fg="white").pack()
    combo_theatre = ttk.Combobox(win, values=["PVR", "INOX", "IMAX"], width=25)
    combo_theatre.pack(pady=5)

    Label(win, text="Rating", bg="black", fg="white").pack()
    entry_rating = Entry(win, width=30)
    entry_rating.pack(pady=5)

    Button(win, text="Submit",bg="green",fg="white", command=submit).pack(pady=20)

#Movie Page
def open_movie():
    win = Toplevel(root)
    win.title("Movie Details")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    def submit():
        conn = sqlite3.connect("movie.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO movies(name, release_date, genre, language, duration,
            rating, demand, price, status)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            combo_movie.get(),
            entry_date.get(),
            entry_genre.get(),
            combo_language.get(),
            entry_duration.get(),
            entry_rating.get(),
            combo_demand.get(),
            entry_price.get(),
            combo_status.get()
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Movie Saved")

    Label(win, text="Movie Details", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=10)

    Label(win, text="Movie", bg="black", fg="white").pack()
    combo_movie = ttk.Combobox(win, values=["Avatar", "Bahubali", "Project Hail Mary", "Mortal Kombat II"])
    combo_movie.pack()

    Label(win, text="Release Date", bg="black", fg="white").pack()
    entry_date = Entry(win)
    entry_date.pack()

    Label(win, text="Genre", bg="black", fg="white").pack()
    entry_genre = Entry(win)
    entry_genre.pack()

    Label(win, text="Language", bg="black", fg="white").pack()
    combo_language = ttk.Combobox(win, values=["English", "Hindi", "Bengali"])
    combo_language.pack()

    Label(win, text="Duration", bg="black", fg="white").pack()
    entry_duration = Entry(win)
    entry_duration.pack()

    Label(win, text="Rating", bg="black", fg="white").pack()
    entry_rating = Entry(win)
    entry_rating.pack()

    Label(win, text="Demand Level", bg="black", fg="white").pack()
    combo_demand = ttk.Combobox(win, values=["Low", "Medium", "High", "Trending", "Blockbuster"])
    combo_demand.pack()

    Label(win, text="Price", bg="black", fg="white").pack()
    entry_price = Entry(win)
    entry_price.pack()

    Label(win, text="Status", bg="black", fg="white").pack()
    combo_status = ttk.Combobox(win, values=["Upcoming", "Housefull", "Available"])
    combo_status.pack()

    Button(win, text="Submit",bg="green",fg="white", command=submit).pack(pady=15)

#Seat Page
def open_seat():
    win = Toplevel(root)
    win.title("Seat Booking")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    def submit():
        conn = sqlite3.connect("movie.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO seats(seat_number, status) VALUES (?,?)",
            (entry_seat.get(), combo_status.get())
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Seat Saved")

    
    Label(win, text="Seat Booking", font=("Arial", 18, "bold"),bg="black",fg="white").pack(pady=20)

    Label(win, text="Seat Number",bg="black", fg="white").pack()
    entry_seat = Entry(win)
    entry_seat.pack()

    Label(win, text="Seat Status",bg="black", fg="white").pack()
    combo_status = ttk.Combobox(win, values=["Occupied", "Booked", "Not Booked"])
    combo_status.pack()

    Button(win, text="Submit" ,bg="green",fg="white", command=submit).pack(pady=20)

#Ticket Booking Page
def open_ticket_booking():
    win = Toplevel(root)
    win.title("Ticket Booking")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    current_month = datetime.now().month
    current_year = datetime.now().year

    selected_date = StringVar()

    def choose_day(day):
        selected_date.set(
            f"{day:02d}/{current_month:02d}/{current_year}"
        )

    def draw_calendar():
        for widget in cal_frame.winfo_children():
            widget.destroy()

        month_label.config(
            text=f"{calendar.month_name[current_month]} {current_year}"
        )

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, day_name in enumerate(days):
            Label(
                cal_frame,
                text=day_name,
                width=5,
                bg="black",
                fg="white",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=col)

        month_days = calendar.monthcalendar(
            current_year,
            current_month
        )

        for r, week in enumerate(month_days, start=1):
            for c, day in enumerate(week):
                if day != 0:
                    Button(
                        cal_frame,
                        text=str(day),
                        width=4,
                        bg="white",
                        fg="black",
                        activebackground="lightgray",
                        activeforeground="black",
                        command=lambda d=day: choose_day(d)
                    ).grid(row=r, column=c, padx=2, pady=2)

    def next_month():
        nonlocal current_month, current_year

        current_month += 1

        if current_month > 12:
            current_month = 1
            current_year += 1

        draw_calendar()

    def prev_month():
        nonlocal current_month, current_year

        current_month -= 1

        if current_month < 1:
            current_month = 12
            current_year -= 1

        draw_calendar()

    def submit():
        if selected_date.get() == "":
            messagebox.showerror(
                "Error",
                "Please select a booking date"
            )
            return

        if entry_amount.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter amount"
            )
            return

        messagebox.showinfo(
            "Booking Details",
            f"Booking Date: {selected_date.get()}\n"
            f"Status: {combo_status.get()}\n"
            f"Amount: ₹{entry_amount.get()}"
        )

    Label(
        win,
        text="Ticket Booking",
        font=("Arial", 18, "bold"),
        bg="black",
        fg="white"
    ).pack(pady=10)

    
    nav_frame = Frame(win, bg="black")
    nav_frame.pack()

    Button(
        nav_frame,
        text="< Previous",
        bg="white",
        fg="black",
        activebackground="gray20",
        activeforeground="white",
        command=prev_month
    ).pack(side=LEFT, padx=5)

    month_label = Label(
        nav_frame,
        font=("Arial", 12, "bold"),
        bg="black",
        fg="white"
    )
    month_label.pack(side=LEFT, padx=10)

    Button(
        nav_frame,
        text="Next >",
        bg="white",
        fg="black",
        activebackground="gray20",
        activeforeground="white",
        command=next_month
    ).pack(side=LEFT, padx=5)

    
    cal_frame = Frame(win, bg="black")
    cal_frame.pack(pady=10)

    draw_calendar()

    
    Label(
        win,
        text="Selected Date",
        bg="black",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack()

    Label(
        win,
        textvariable=selected_date,
        bg="white",
        fg="black",
        width=20,
        relief="sunken",
        font=("Arial", 12)
    ).pack(pady=5)

   
    Label(
        win,
        text="Status",
        bg="black",
        fg="white"
    ).pack(pady=5)

    combo_status = ttk.Combobox(
        win,
        values=["Booked", "Cancelled", "Completed"],
        state="readonly"
    )
    combo_status.current(0)
    combo_status.pack()

 
    Label(
        win,
        text="Amount",
        bg="black",
        fg="white"
    ).pack(pady=5)

    entry_amount = Entry(win, bg="white", fg="black", insertbackground="white")
    entry_amount.pack()

   
    Button(
        win,
        text="Submit",
        bg="green",
        fg="white",
        command=submit
    ).pack(pady=20)

#Payment Page
def open_payment():
    win = Toplevel(root)
    win.title("Payment")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)
        
    def submit():
        seat = chr(random.randint(65, 70)) + str(random.randint(1, 50))
        txn = "TXN" + "".join(str(random.randint(0, 9)) for _ in range(6))

        messagebox.showinfo(
            "Payment Successful",
            f"Amount: â¹{entry_amount.get()}\n"
            f"Method: {combo_payment.get()}\n"
            f"Seat: {seat}\n"
            f"Transaction ID: {txn}"
        )

    Label(win, text="Payment Details", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=20)

    Label(win, text="Amount", bg="black", fg="white").pack()
    entry_amount = Entry(win)
    entry_amount.pack()

    Label(win, text="Payment Method", bg="black", fg="white").pack()
    combo_payment = ttk.Combobox(win, values=["UPI", "Debit Card", "Net Banking", "Cash"])
    combo_payment.pack()

    Button(win, text="Pay",bg="green",fg="white",command=submit).pack(pady=20)

#Cancellation Page
def open_cancellation():
    win = Toplevel(root)
    win.title("Movie Cancellation")
    win.geometry("1920x1032")
    
    try:
        bg = Image.open(r"C:\Users\Rohini\Downloads\popcorn.jpg")
        bg = bg.resize((1920, 1032), Image.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg, master=win)

        bg_label = Label(win)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

    except Exception as e:
        print("Login BG error:", e)

    def submit():
        conn = sqlite3.connect("movie.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO cancellations(movie, reason, other_reason)
            VALUES (?,?,?)
        """, (
            combo_movie.get(),
            combo_reason.get(),
            entry_other.get()
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Cancellation Saved")

    Label(win, text="Movie Cancellation", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=20)

    Label(win, text="Movie",bg="black", fg="white").pack()
    combo_movie = ttk.Combobox(win, values=["Avatar", "Bahubali"])
    combo_movie.pack()

    Label(win, text="Cancellation Reason", bg="black", fg="white").pack()
    combo_reason = ttk.Combobox(win, values=["Change", "Wrong Booking", "Health", "Payment"])
    combo_reason.pack()

    Label(win, text="Other Reason", bg="black", fg="white").pack()
    entry_other = Entry(win)
    entry_other.pack()

    Button(win, text="Submit" ,bg="green",fg="white", command=submit).pack(pady=20)


def show_main_menu():
    btn_theatre.pack(pady=5)
    btn_movie.pack(pady=5)
    btn_seat.pack(pady=5)
    btn_ticket.pack(pady=5)
    btn_payment.pack(pady=5)
    btn_cancel.pack(pady=5)
    btn_exit.pack(pady=5)

root = Tk()

current_user = StringVar()
current_user.set("")

root.title("Book My Seat")
root.geometry("1920x1080")

try:
    image = Image.open(r"C:/Users/Rohini/OneDrive/Desktop/MOVIE MANAGEMENT SYSTEM/login.jpg")
    
    image = image.resize((1920, 1080), Image.LANCZOS)

    bg_image = ImageTk.PhotoImage(image, master=root)

    bg_label = Label(root)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    bg_label.configure(image=bg_image)
    bg_label.image = bg_image

except Exception as e:
    print("Error loading image:", e)
    
Label(
root,
text="Book My Seat",
font=("Times New Roman", 18, "bold"),
bg="black",
fg="white"
).pack(pady=20)


btn_login = Button(root, text="Login", width=30, command=open_login)
btn_login.pack(pady=5)

btn_theatre = Button(root, text="Theatre Details", width=30, command=open_theatre)

btn_movie = Button(root, text="Movie Details", width=30, command=open_movie)

btn_seat = Button(root, text="Seat Booking", width=30, command=open_seat)

btn_ticket = Button(root, text="Ticket Booking", width=30, command=open_ticket_booking)

btn_payment = Button(root, text="Payment", width=30, command=open_payment)

btn_cancel = Button(root, text="Movie Cancellation", width=30, command=open_cancellation)

btn_exit = Button(root, text="Exit", width=30, command=root.destroy)


user_label = Label(
    root,
    textvariable=current_user,
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)

user_label.place(relx=0.98, y=10, anchor="ne")

root.mainloop()