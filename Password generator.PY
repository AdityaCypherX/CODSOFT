import tkinter as tk
import random
import string

# define a funtion to generate a random password
def generate_password():
    length = int(entry_length.get())  #user can take any number of password length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root, width=10)
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, width=30)
entry_password.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()  #run the application
