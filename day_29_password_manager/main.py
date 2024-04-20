# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=200, height=200)

window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

img = tkinter.PhotoImage(file="./logo.png")

canvas.create_image(100, 100, image=img)

canvas.pack()
window.mainloop()
