import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=200)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0, pady=(50,5))

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0, pady=(50,5))

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=(30,5))

kilometer=0
km_label=tkinter.Label(text=kilometer)
km_label.grid(column=1, row=1)

km_text=tkinter.Label(text="Km")
km_text.grid(column=2, row=1)

def button_clicked():
    miles_to_km = int(input_miles.get()) * 1.609344
    km_label.config(text=round(miles_to_km,2))

calc_button = tkinter.Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2, pady=(5,50))



window.mainloop()