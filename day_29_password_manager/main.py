# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

window = tkinter.Tk()
grid = tkinter.Grid()
canvas = tkinter.Canvas(window, width=200, height=200)


window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

img = tkinter.PhotoImage(file="./logo.png")

canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

"""Website"""
website_label = tkinter.Label(text="Website:", bg="white", padx=20)
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

"""Email/Username"""
username_label = tkinter.Label(text="Email/Username:", bg="white", padx=20)
username_label.grid(column=0, row=2)

username_entry = tkinter.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

"""Password"""
password_label = tkinter.Label(text="Password:", bg="white", padx=20)
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", bg="white", padx=20)
password_button.grid(column=2, row=3)

"""Add button"""
add_button = tkinter.Button(text="Add", width=36, bg="white", padx=20)
add_button.grid(column=1, row=4)


canvas.grid()

# label, entry and button
window.mainloop()