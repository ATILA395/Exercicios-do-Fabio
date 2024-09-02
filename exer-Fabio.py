def gerar_tabuadas_com_parada():
    while True:
        # Solicita ao usuário o número máximo para gerar a tabuada
        numero_maximo = int(input("Digite o número máximo para parar (ou 0 para continuar indefinidamente): "))
        
        if numero_maximo == 0:
            # Continua gerando tabuadas indefinidamente
            num = 1
            while True:
                print(f"\nTabuada do {num}:")
                for i in range(1, 11):  # Tabuada de 1 até 10
                    print(f"{num} x {i} = {num * i}")
                num += 1
        else:
            # Gera tabuadas até o número máximo especificado
            for num in range(1, numero_maximo + 1):
                print(f"\nTabuada do {num}:")
                for i in range(1, 11):  # Tabuada de 1 até 10
                    print(f"{num} x {i} = {num * i}")
            break

# Chama a função
gerar_tabuadas_com_parada()
def gerar_tabuadas_com_parada():
    while True:
        # Solicita ao usuário o número máximo para gerar a tabuada
        numero_maximo = int(input("Digite o número máximo para parar (ou 0 para continuar indefinidamente): "))
        
        if numero_maximo == 0:
            # Continua gerando tabuadas indefinidamente
            num = 1
            while True:
                print(f"\nTabuada do {num}:")
                for i in range(1, 11):  # Tabuada de 1 até 10
                    print(f"{num} x {i} = {num * i}")
                num += 1
        else:
            # Gera tabuadas até o número máximo especificado
            for num in range(1, numero_maximo + 1):
                print(f"\nTabuada do {num}:")
                for i in range(1, 11):  # Tabuada de 1 até 10
                    print(f"{num} x {i} = {num * i}")
            break

# Chama a função
gerar_tabuadas_com_parada()
