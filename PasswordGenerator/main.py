import customtkinter as ct
import random
import string
import pyperclip

app = ct.CTk()

def slider_cmd(val):
    label_info_length.configure(text=int(val))

def gen_passwd():
    length = int(slider.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    label_password.configure(text=password)

def copy_passwd():
    password = label_password.cget("text")
    pyperclip.copy(password)

app.geometry('500x300')
app.resizable(False, False)
app.title("Password Generator")

slider_frame = ct.CTkFrame(app, width=500, height=70)
slider_frame.pack(side='top', pady=5)
slider_label = ct.CTkLabel(slider_frame, text='Password Length:  ', font=('Arial', 12))
slider_label.pack(side='left')
slider = ct.CTkSlider(slider_frame, command=slider_cmd, from_=10, to=50)
slider.set(15) 
slider.pack(side='left')

label_info_length = ct.CTkLabel(slider_frame, text='15')
label_info_length.pack(side='left', pady=20)


generate_btn = ct.CTkButton(app, text='Generate', width=150, height=50, command=gen_passwd)
generate_btn.pack(side='top', padx=10,pady=10)
copy_btn = ct.CTkButton(app, text='Copy', width=100, height=50, command=copy_passwd)
copy_btn.pack(side='bottom', padx=10,pady=10)

passwd_frame = ct.CTkFrame(app, width=500, height=150)
passwd_frame.pack(anchor='n', pady=5)
label_password = ct.CTkLabel(passwd_frame, text='hello', width=500, height=150, font=('Arial', 18))
label_password.pack()

app.mainloop()
