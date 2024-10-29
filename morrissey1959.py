import tkinter as tk
from tkinter import messagebox
import datetime
import calendar

# Dicionário para armazenar os usuários e senhas
usuarios = {
    "Stephen": "1959",
    "Morrissey": "1982"
}


class App:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Cadastro")

        self.current_frame = None
        self.show_login()

    def show_login(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.master)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Nome de usuário:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.current_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.current_frame, text="Senha:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.current_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.current_frame, text="Logon", command=self.logon).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.current_frame, text="Sair", command=master.quit).grid(row=3, columnspan=2)

    def logon(self):
        nome_usuario = self.username_entry.get()
        senha_usuario = self.password_entry.get()

        if nome_usuario in usuarios and usuarios[nome_usuario] == senha_usuario:
            messagebox.showinfo("Sucesso", "Logon bem-sucedido!")
            self.open_registration()
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

    def open_registration(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.master)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Nome:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.current_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.current_frame, text="Sexo (M/F/O):").grid(row=1, column=0)
        self.gender_entry = tk.Entry(self.current_frame)
        self.gender_entry.grid(row=1, column=1)

        tk.Button(self.current_frame, text="Selecionar Data de Nascimento", command=self.select_date).grid(row=2,
                                                                                                           columnspan=2,
                                                                                                           pady=10)
        tk.Button(self.current_frame, text="Finalizar Cadastro", command=self.finalize_registration).grid(row=3,
                                                                                                          columnspan=2)

        self.data_nascimento = None



