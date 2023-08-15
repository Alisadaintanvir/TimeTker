import math
from tkinter import *
from tkinter import ttk

from storing_data import StoringData

PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"

is_running = False
counter_value = 0
updating_timer = False
storing_data = StoringData()


def start_counter():
    global is_running, updating_timer
    is_running = not is_running
    if is_running:
        start_button.config(text="Pause")
        if not updating_timer:
            updating_timer = True
            update_counter()
    else:
        start_button.config(text="Resume")


def stop_counter():
    global is_running, counter_value
    if counter_value > 0:
        storing_data.store_counter_value(counter_value - 1)
    counter_value = 0
    is_running = False
    start_button.config(text="Start")
    canvas.itemconfig(timer_text, text=f"00:00:00")


def update_counter():
    global counter_value, updating_timer
    min_count = math.floor(counter_value / 60)
    hour_count = math.floor(min_count / 60)
    sec_count = math.floor(counter_value % 60)

    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if min_count < 10:
        min_count = f"0{min_count}"
    if hour_count < 10:
        hour_count = f"0{hour_count}"

    if is_running:
        canvas.itemconfig(timer_text, text=f"{hour_count}:{min_count}:{sec_count}")
        window.after(1000, update_counter)
        counter_value += 1
    else:
        updating_timer = False


def add_window():
    def populate_table():
        timer_data = storing_data.fetch_data()

        for entry in timer_data:
            date = entry["date"]
            value = entry['value']
            minute = math.floor(value / 60)
            hour = math.floor(minute / 60)
            second = math.floor(value % 60)

            if second < 10:
                second = f"0{second}"
            if minute < 10:
                minute = f"0{minute}"
            if hour < 10:
                hour = f"0{hour}"

            time = f"{hour} : {minute} : {second}"

            tree.insert("", "end", values=(date, time))

    window2 = Toplevel()
    window2.title("Timer Data Table")

    tree = ttk.Treeview(window2, columns=("Date", "Value"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Value", text="Time")
    populate_table()
    tree.pack()


window = Tk()
window.title("TimeTker")
window.config(width=800, height=550)
canvas = Canvas(width=800, height=500, bg="#b4b4b4")
canvas_bg = PhotoImage(file="images/3.png")
canvas.create_image(400, 285, image=canvas_bg)
timer_text = canvas.create_text(380, 230, text="00:00:00", fill=RED, font=("Arial", 45, "bold"))
canvas.pack()
start_button = Button(text="Start", height=2, width=15, bg=RED, fg="#fff",
                      highlightthickness=0, borderwidth=1, command=start_counter)
start_button_window = canvas.create_window(380, 300, window=start_button)
reset_button = Button(text="Reset", height=2, width=15, bg=RED, fg="#fff",
                      highlightthickness=0, borderwidth=1, command=stop_counter)
reset_button_window = canvas.create_window(380, 350, window=reset_button)

new_window_button = Button(text="Show Timer Info", height=1, width=15, bg=RED, fg="#fff",
                           highlightthickness=0, borderwidth=1, command=add_window)
new_window_button_window = canvas.create_window(730, 30, window=new_window_button)

window.mainloop()
