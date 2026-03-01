"""
CLASSES E ORIENTAÇÃO A OBJETOS EM PYTHON
Autor: Paulo Vinícius

Conteúdo:
- Criar classes
- Atributos
- Métodos
- Método __init__
- Método __str__
- Métodos com retorno
- Classes com listas
- Encapsulamento simples
"""

# ======================================================
# 1. CLASSE SIMPLES
# ======================================================

class Pessoa:
    pass

# criando objeto
pessoa1 = Pessoa()

print("Objeto criado:", pessoa1)

print()

# ======================================================
# 2. CLASSE COM ATRIBUTOS
# ======================================================

class Pessoa:
    nome = "Paulo"
    idade =  26

p = Pessoa()

print("Nome:", p.nome)
print("Idade:", p.idade)

print()


# ======================================================
# 3. MÉTODO __init__ (CONSTRUTOR)
# ======================================================

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

p1 = Pessoa("Paulo", 25)
p2 = Pessoa("KS", 27)

print("Nome:", p1.nome)
print("Idade:", p1.idade)

print("Nome:", p2.nome)
print("Idade:", p2.idade)
        
print()

# ======================================================
# 4. MÉTODOS DA CLASSE
# ======================================================

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print("Olá, meu nome é", self.nome)

p = Pessoa("Molodoy")

p.saudacao()

print()

# ======================================================
# 5. MÉTODO COM RETORNO
# ======================================================

class Calculadora:
    def somar(seff, a, b):
        return a + b
    
calc = Calculadora()

resultado = calc.somar(10, 5)

print("Resultados", resultado)

print()

# ======================================================
# 6. MÉTODO __str__
# ======================================================

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}"
    
produto = Produto("NOtebook", 3500)

print(produto)


# ======================================================
# 7. CLASSE COM LISTA
# ======================================================

class ListaNumeros:

    def __init__(self, numeros):
        self.numeros = numeros

    def somar(self):

        total = 0

        for numero in self.numeros:
            total += numero

        return total

lista = ListaNumeros([10, 20, 30])

print("Soma:", lista.somar())


# ======================================================
# 8. CLASSE COM LOOP
# ======================================================

class MostrarLista:

    def __init__(self, lista):
        self.lista = lista

    def mostrar(self):

        for item in self.lista:
            print(item)

obj = MostrarLista(["Python", "SQL", "Power BI"])

obj.mostrar()


# ======================================================
# 9. ENCAPSULAMENTO SIMPLES
# ======================================================

class Conta:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):

        self.saldo += valor

    def sacar(self, valor):

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta = Conta(1000)

conta.depositar(500)
conta.sacar(200)

print("Saldo:", conta.saldo)


# ======================================================
# 10. EXEMPLO PRÁTICO (DADOS)
# ======================================================

class Aluno:

    def __init__(self, nome, notas):

        self.nome = nome
        self.notas = notas

    def calcular_media(self):

        soma = 0

        for nota in self.notas:
            soma += nota

        media = soma / len(self.notas)

        return media

aluno = Aluno("Paulo", [7, 8, 9])

print("Aluno:", aluno.nome)
print("Média:", aluno.calcular_media())
