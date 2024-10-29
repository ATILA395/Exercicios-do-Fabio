import datetime
import calendar
import pyinstaller

# Dicionário para armazenar os usuários e senhas
usuarios = {
    "Stephen": "1959",
    "Morrissey": "1982"
}


def calcular_idade(data_nascimento):
    today = datetime.date.today()
    idade = today.year - data_nascimento.year - (
                (today.month, today.day) < (data_nascimento.month, data_nascimento.day))
    return idade


def login(screen):
    screen.clear()
    screen.addstr("Nome de usuário: ")
    nome_usuario = screen.getstr().decode("utf-8")

    screen.addstr("Senha: ")
    senha_usuario = screen.getstr().decode("utf-8")

    if nome_usuario in usuarios and usuarios[nome_usuario] == senha_usuario:
        screen.addstr("Logon bem-sucedido!\n")
        screen.addstr("Pressione qualquer tecla para continuar...")
        screen.getch()
        return True
    else:
        screen.addstr("Nome de usuário ou senha incorretos.\n")
        screen.addstr("Pressione qualquer tecla para tentar novamente...")
        screen.getch()
        return False


def cadastro(screen):
    screen.clear()
    screen.addstr("Nome: ")
    nome = screen.getstr().decode("utf-8")

    screen.addstr("Sexo (M/F/O): ")
    sexo = screen.getstr().decode("utf-8")

    while True:
        screen.clear()
        screen.addstr("Digite o ano de nascimento (aaaa): ")
        ano = int(screen.getstr().decode("utf-8"))

        screen.addstr("Digite o mês de nascimento (1-12): ")
        mes = int(screen.getstr().decode("utf-8"))

        screen.addstr("Digite o dia de nascimento: ")
        dia = int(screen.getstr().decode("utf-8"))

        try:
            if mes < 1 or mes > 12 or dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
                screen.addstr("Data inválida. Tente novamente.\n")
                screen.addstr("Pressione qualquer tecla para continuar...")
                screen.getch()
                continue

            data_nascimento = datetime.date(ano, mes, dia)
            idade = calcular_idade(data_nascimento)
            screen.addstr(f"Data de Nascimento: {data_nascimento}, Idade: {idade} anos\n")
            screen.addstr("Cadastro finalizado com sucesso!\n")
            break

        except ValueError:
            screen.addstr("Entrada inválida. Tente novamente.\n")
            screen.addstr("Pressione qualquer tecla para continuar...")
            screen.getch()


def main(screen):
    while True:
        screen.clear()
        screen.addstr("1. Login\n2. Sair\nEscolha uma opção: ")
        opcao = screen.getch()

        if opcao == ord('1'):
            if login(screen):
                cadastro(screen)
        elif opcao == ord('2'):
            break


if __name__ == "__main__":
    curses.wrapper(main)
