from tkinter import *
from passgen import password_with_spec, password_without_spec
from tkinter import messagebox

def create_passwords(length: int):
    if not length.isdigit() or int(length) < 0:
        messagebox.showerror("Error", "Please enter a positive integer value.")
        return
    else:
        length = int(length)

    global password_default, password_special
    # Clear previous passwords if they exist
    if 'password_default' in globals():
        password_default.destroy()
    if 'password_special' in globals():
        password_special.destroy()

    password_default = Text(root, width=20, height=1)
    password_special = Text(root, width=20, height=1)
    password_default.insert(END, password_without_spec(length))
    password_special.insert(END, password_with_spec(length))
    password_default.place(x=200, y=100)
    password_special.place(x=200, y=160)
    password_default.configure(state='disabled')
    password_special.configure(state='disabled')

main_font=("Courier", 13)
root = Tk()
root.geometry("500x250")
root.resizable(False, False)
root.config(bg="#C5EBAA")
root.title("Password Generator")

instructions_label = Label(root, text="Enter the length of the password", font=main_font, background="#C5EBAA")
user_input = Entry(root, width=25)

password_default = Text(root, width=20, height=1)
password_special = Text(root, width=20, height=1)

generating_button = Button(root, text="Generate", padx=25, pady=8, background="#F6F193", activebackground="#FC6736", command=lambda: create_passwords(user_input.get()))
password_label_default = Label(root, text="Default password:", font=main_font, background="#C5EBAA")
password_label_special = Label(root, text="Special password:", font=main_font, background="#C5EBAA")

instructions_label.place(x=90, y=5)
user_input.place(x=95, y=40)
generating_button.place(x=280, y=30)
password_label_default.place(x=20, y=100)
password_label_special.place(x=20, y=160)

root.mainloop()
