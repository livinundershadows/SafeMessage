import tkinter as tk
from tkinter import *
from main import generate_keys
from functools import partial

cyber = generate_keys()

def encrypt_path(e1, e2):
    cyber.open_encry_file(str(e1.get()))    #'dat.txt'
    cyber.encrypt_txt(str(e2.get()))
    return

def decrypt_path(e3):
    cyber.decrypt_txt(str(e3.get()))
    return

root = tk.Tk()
root.title("Safe Message")
root.geometry('800x600')
file1 = tk.StringVar()
file2 = tk.StringVar()
file3 = tk.StringVar()

file_path_1 = tk.Label(root, text='File Path').place(x=50, y=50)
file_path_2 = tk.Label(root, text="New File Name").place(x=50, y=100)
file_path_3 = tk.Label(root, text='File Path').place(x=50, y=200)
e1 = tk.Entry(root, textvariable=file1).place(x=200,y=50)
e2 = tk.Entry(root, textvariable=file2).place(x=200, y=100)
e3 = tk.Entry(root, textvariable=file3).place(x=200, y=200)

encrypt_path = partial(encrypt_path, file1, file2)
decrypt_path = partial(decrypt_path, file3)

encode_button = tk.Button(root, text='Encrypt', command=encrypt_path, activebackground='Pink').place(x=400,y=150)
decode_button = tk.Button(root, text='Decrypt', command=decrypt_path, activebackground='Blue').place(x=400, y=250)
msg0 = tk.Message(root, text='Encrypted!')

root.mainloop()