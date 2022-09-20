import tkinter as tk

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = tk.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=7)
miles_input.grid(column=2, row=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)
miles_label.config(padx=20, pady=20)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

km_result_label = tk.Label(text=0)
km_result_label.grid(column=2, row=2)

km_label = tk.Label(text="Km")
km_label.grid(column=3, row=2)

calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)

window.mainloop()