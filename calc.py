import tkinter as tk

def on_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+']

# Create buttons
for i, btn in enumerate(buttons):
    tk.Button(root, text=btn, width=5, height=3, command=lambda b=btn: on_click(b)).grid(row=(i // 5) + 1, column=i % 4)

root.mainloop()
