import customtkinter as ctk
from tkinter import messagebox

book = ctk.CTk(fg_color="#FF4F0F")
book.title("Minhas Leituras")
book.geometry("700x700")

label_titulo = ctk.CTkLabel(book,text="Minhas Leituras📖", font=("Rubik", 50), text_color="#FFA673" )
label_titulo.pack(pady=30)

entry_nome = ctk.CTkEntry(book,placeholder_text="digite seu nome",fg_color="#BB3E00", border_color="white", placeholder_text_color="white", width=300, height=25)
entry_nome.pack(padx=40)

label_resp = ctk.CTkLabel(book, text="Bem Vindo(a) ao programa Minha Leitura ",font=("Rubik", 30), text_color="#FFA673")
label_resp.pack(pady=50)



book.mainloop()