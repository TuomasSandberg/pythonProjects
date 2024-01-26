import tkinter

window = tkinter.Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label

# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label["text"] = "New Text"   # either way works
# my_label.config(text="New Text") # either way works
# # my_label.place(x=0, y=0) # like pack but you can define place more precise
# my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("i got clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)





window.mainloop()