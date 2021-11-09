from tkinter import *
from random import randint

root_window = Tk()
root_window.geometry("400x300")
root_window.title("Password generator")



number_of_characters = LabelFrame(root_window,
                             text="Сколько символов?",
                             font=("arial"))
number_of_characters.pack(pady=20)

input_characters = Entry(number_of_characters, font=("arial", 14))
input_characters.pack(pady=20, padx=20)

psw_output = Entry(root_window, text="", font=("arial", 14))
psw_output.pack(pady=20)


def new_rand():
    input_characters.delete(0, END)
    psw_len = int(psw_output.get())
    new_password = chr(randint(33, 126))

def copy_password():
    pass


frame_for_buttons = Frame(root_window)
frame_for_buttons.pack(pady=20)

generator_button = Button(frame_for_buttons, text="Сгенерировать пароль", command=new_rand)
generator_button.grid(row=0, column=0, padx=10)

copy_button = Button(frame_for_buttons, text="Скопировать пароль", command=copy_password)
copy_button.grid(row=0, column=1, padx=10)

root_window.mainloop()


