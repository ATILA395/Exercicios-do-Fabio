import calendar
import datetime
import tkinter as tk
from tkinter import messagebox

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

        tk.Button(self.current_frame, text="Selecionar Data de Nascimento", command=self.select_date).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.current_frame, text="Finalizar Cadastro", command=self.finalize_registration).grid(row=3, columnspan=2)

        self.data_nascimento = None

    def select_date(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.master)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Digite o ano (aaaa):").grid(row=0, column=0)
        self.year_entry = tk.Entry(self.current_frame)
        self.year_entry.grid(row=0, column=1)

        tk.Label(self.current_frame, text="Digite o mês (1-12):").grid(row=1, column=0)
        self.month_entry = tk.Entry(self.current_frame)
        self.month_entry.grid(row=1, column=1)

        tk.Label(self.current_frame, text="Digite o dia:").grid(row=2, column=0)
        self.day_entry = tk.Entry(self.current_frame)
        self.day_entry.grid(row=2, column=1)

        tk.Button(self.current_frame, text="Confirmar Data", command=self.confirm_date).grid(row=3, columnspan=2)

    def confirm_date(self):
        try:
            ano = int(self.year_entry.get())
            mes = int(self.month_entry.get())
            dia = int(self.day_entry.get())

            if mes < 1 or mes > 12 or dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
                messagebox.showerror("Erro", "Data inválida. Tente novamente.")
                return

            self.data_nascimento = datetime.date(ano, mes, dia)
            idade = self.calcular_idade(self.data_nascimento)
            messagebox.showinfo("Data Confirmada", f"Data de Nascimento: {self.data_nascimento}, Idade: {idade} anos")
            self.open_registration()
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Tente novamente.")

    def calcular_idade(self, data_nascimento):
        today = datetime.date.today()
        idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
        return idade

    def finalize_registration(self):
        nome = self.name_entry.get()
        sexo = self.gender_entry.get()
        if not nome or not sexo or not self.data_nascimento:
            messagebox.showerror("Erro", "Preencha todos os campos antes de finalizar.")
            return
        messagebox.showinfo("Sucesso", "Cadastro finalizado com sucesso!")
        self.show_login()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
