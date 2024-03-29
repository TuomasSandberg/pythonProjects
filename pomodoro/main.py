import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    check_mark_text = ""

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer=  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        for _ in range(math.floor(reps/2)):
            check_mark_text += "✔"
        checkmark.config(text=check_mark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
grid = tkinter.Grid()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

"""Image"""
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

"""Buttons"""
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

stop_button = tkinter.Button(text="Reset", command=reset_timer)
stop_button.grid(column=2, row=2)

""""Checkmark"""
checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark.grid(column=1, row=3)

canvas.grid()

window.mainloop()
