import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


is_running = False
counter_value = 0
timer = None


def start_counter():
    global is_running
    is_running = not is_running
    if is_running:
        start_button.config(text="Pause")
        update_counter()
    else:
        start_button.config(text="Start")


def pause_counter():
    global is_running
    is_running = False


def stop_counter():
    global is_running, counter_value
    counter_value = 0
    update_counter()
    is_running = False


def update_counter():
    global counter_value
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
        counter_value += 1
        canvas.itemconfig(timer_text, text=f"{hour_count}:{min_count}:{sec_count}")
        window.after(1000, update_counter)


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
                          highlightthickness=0, borderwidth=1, command= stop_counter)
pause_window = canvas.create_window(380, 350, window=stop_button)

window.mainloop()
