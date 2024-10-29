import datetime
import calendar

# Dicionário para armazenar os usuários e senhas
usuarios = {
    "Stephen": "1959",
    "Morrissey": "1982"
}

def calcular_idade(data_nascimento):
    today = datetime.date.today()
    idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def main():
    # Logon
    nome_usuario = input("Nome de usuário: ")
    senha_usuario = input("Senha: ")

    if nome_usuario in usuarios and usuarios[nome_usuario] == senha_usuario:
        print("Logon bem-sucedido!")
        
        # Cadastro
        nome = input("Nome: ")
        sexo = input("Sexo (M/F/O): ")
        
        while True:
            ano = input("Digite o ano de nascimento (aaaa): ")
            mes = input("Digite o mês de nascimento (1-12): ")
            dia = input("Digite o dia de nascimento: ")
            
            try:
                ano = int(ano)
                mes = int(mes)
                dia = int(dia)

                if mes < 1 or mes > 12 or dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
                    print("Data inválida. Tente novamente.")
                    continue

                data_nascimento = datetime.date(ano, mes, dia)
                idade = calcular_idade(data_nascimento)
                print(f"Data de Nascimento: {data_nascimento}, Idade: {idade} anos")
                break

            except ValueError:
                print("Entrada inválida. Tente novamente.")

        print("Cadastro finalizado com sucesso!")

    else:
        print("Nome de usuário ou senha incorretos.")

if __name__ == "__main__":
    main()
