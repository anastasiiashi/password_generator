from tkinter import *
from random import randint

root_window = Tk()
root_window.geometry("400x300")
root_window.title("Password generator")


def new_rand():
    psw_output.delete(0, END)
    psw_len = int(input_characters.get())
    password = ''
    for _ in range(psw_len):
        password += chr(randint(33, 126))
    psw_output.insert(0, password)


def copy_password():
    root_window.clipboard_clear()
    root_window.clipboard_append(psw_output.get())


number_of_characters = LabelFrame(root_window, text="Сколько символов?", font="arial")
number_of_characters.pack(pady=20)

input_characters = Entry(number_of_characters, font=("arial", 14))
input_characters.pack(pady=20, padx=20)

psw_output = Entry(root_window, text="", font=("arial", 14), bd=0, bg="SystemButtonFace")
psw_output.pack(pady=10)


frame_for_buttons = Frame(root_window)
frame_for_buttons.pack(pady=20)

generator_button = Button(frame_for_buttons, text="Сгенерировать пароль", command=new_rand)
generator_button.grid(row=0, column=0, padx=10)

copy_button = Button(frame_for_buttons, text="Скопировать пароль", command=copy_password)
copy_button.grid(row=0, column=1, padx=10)

root_window.mainloop()
