import tkinter

window = tkinter.Tk()

r = tkinter.Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = tkinter.Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = tkinter.Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)

window.mainloop()
