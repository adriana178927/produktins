import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = float(entry.get())
    except:
        messagebox.showerror("Kļūda", "Ievadi skaitli!")
        return

    from_unit = from_var.get()
    to_unit = to_var.get()

    if from_unit == to_unit:
        result = value

    elif from_unit == "Celsijs" and to_unit == "Fārenheits":
        result = (value * 9/5) + 32
    elif from_unit == "Celsijs" and to_unit == "Kelvins":
        result = value + 273.15

    elif from_unit == "Fārenheits" and to_unit == "Celsijs":
        result = (value - 32) * 5/9
    elif from_unit == "Fārenheits" and to_unit == "Kelvins":
        result = (value - 32) * 5/9 + 273.15

    elif from_unit == "Kelvins" and to_unit == "Celsijs":
        result = value - 273.15
    elif from_unit == "Kelvins" and to_unit == "Fārenheits":
        result = (value - 273.15) * 9/5 + 32

    else:
        messagebox.showerror("Kļūda", "Nederīga konversija!")
        return

    result = round(result, 2)
    result_label.config(text=f"Rezultāts: {result} {to_unit}")

    history.insert(0, f"{value} {from_unit} → {result} {to_unit}")
    update_history()

def update_history():
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item)

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Rezultāts:")

root = tk.Tk()
root.title("Temperatūras pārveidotājs")
root.configure(bg="#ffc0cb")  # rozā fons

history = []

entry = tk.Entry(root, width=30, bg="#ffe4e1", fg="#d63384")
entry.pack(pady=5)

units = ["Celsijs", "Fārenheits", "Kelvins"]

from_var = tk.StringVar(value=units[0])
to_var = tk.StringVar(value=units[1])

from_menu = tk.OptionMenu(root, from_var, *units)
from_menu.config(bg="#ff69b4", fg="white")
from_menu.pack(pady=5)

to_menu = tk.OptionMenu(root, to_var, *units)
to_menu.config(bg="#ff69b4", fg="white")
to_menu.pack(pady=5)

btn_convert = tk.Button(root, text="Pārveidot", command=convert, bg="#ff1493", fg="white")
btn_convert.pack(pady=5)

btn_clear = tk.Button(root, text="Notīrīt", command=clear, bg="#db7093", fg="white")
btn_clear.pack(pady=5)

result_label = tk.Label(root, text="Rezultāts:", bg="#ffc0cb", fg="#c71585", font=("Arial", 12))
result_label.pack(pady=5)

history_list = tk.Listbox(root, width=40, bg="#ffe4e1", fg="#d63384")
history_list.pack(pady=5)

root.mainloop()
