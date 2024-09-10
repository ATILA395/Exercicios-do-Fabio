class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def falar(self, mensagem):
        return f"{self.nome} diz: {mensagem}"

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.altura += 0.005  # Cresce 0,5 cm (0,005 m) por ano
            self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos e {self.altura:.2f}m de altura."

    def emagrecer(self, quilos):
        self.peso -= quilos
        if self.peso < 0:
            self.peso = 0
        return f"{self.nome} agora pesa {self.peso}kg."

    def engordar(self, quilos):
        self.peso += quilos
        return f"{self.nome} agora pesa {self.peso}kg."

    def crescer(self, metros):
        self.altura += metros
        return f"{self.nome} agora tem {self.altura}m de altura."

    def imc(self):
        return self.peso / (self.altura ** 2)

    def __str__(self):
        return (f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg, "
                f"Altura: {self.altura:.2f}m, IMC: {self.imc():.2f}")

# Exemplo de uso
pessoa = Pessoa("Ana", 18, 60, 1.65)
print(pessoa.falar("Olá!"))
print(pessoa.envelhecer(3))  # Envelhece 3 anos
print(pessoa.emagrecer(5))
print(pessoa.engordar(10))
print(pessoa.crescer(0.05))
print(pessoa)
