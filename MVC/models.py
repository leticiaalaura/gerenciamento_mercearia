from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, quantidadeVendida, data = datetime.now().strftime("%d/%m/%y")):
        self.itensVendidos = itensVendidos
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, contato, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.contato = contato
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, contato, endereco):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, cargo, nome, cpf, contato, endereco):
        self.cargo = cargo
        super(Funcionario, self).__init__(nome, cpf, contato, endereco)
