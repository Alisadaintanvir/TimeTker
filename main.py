import json
import math
from tkinter import *
from datetime import datetime

PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"

is_running = False
counter_value = 0
updating_timer = False
now = datetime.now()
date = now.strftime("%d/%m/%Y")


def store_counter_value(current_date, value):
    new_entry = {
        "date": current_date,
        "value": value
    }

    existing_data = []

    try:
        with open("timer_data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        pass

    for entry in existing_data:
        if entry['date'] == date:
            entry['value'] += value
            updated = True
            break
    else:
        existing_data.append(new_entry)
    with open("timer_data.json", "w") as json_file:
        json.dump(existing_data, json_file)


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
        store_counter_value(date, counter_value)
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
        print(counter_value)
    else:
        updating_timer = False


window = Tk()
window.title("My Timer")
window.config(width=800, height=550)

canvas = Canvas(width=800, height=500, bg="#b4b4b4")
canvas_bg = PhotoImage(file="images/3.png")
canvas.create_image(400, 285, image=canvas_bg)
timer_text = canvas.create_text(380, 230, text="00:00:00", fill=RED, font=("Arial", 45, "bold"))
canvas.pack()

start_button = Button(text="Start", height=2, width=15, bg=RED, fg="#fff",
                      highlightthickness=0, borderwidth=1, command=start_counter)
button_window = canvas.create_window(380, 300, window=start_button)

stop_button = Button(text="Stop", height=2, width=15, bg=RED, fg="#fff",
                     highlightthickness=0, borderwidth=1, command=stop_counter)
pause_window = canvas.create_window(380, 350, window=stop_button)

window.mainloop()
