import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            tk.Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=calculate
            ).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=lambda b=btn: button_click(b)
            ).pack(side="left", expand=True, fill="both")

tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill="both")

root.mainloop()