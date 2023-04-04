import controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

criarArquivos('categoria.txt', 'clientes.txt',
              'estoque.txt', 'fornecedores.txt',
              'funcionarios.txt', 'venda.txt')

if __name__== '__main__':
    while True:
        local = int(input('Digite 1 para acessar CATEGORIAS \n'
                          'Digite 2 para acessar ESTOQUE \n'
                          'Digite 3 para acessar FORNECEDOR \n'
                          'Digite 4 para acessar CLIENTE \n'
                          'Digite 5 para acessar FUNCIONARIOS \n'
                          'Digite 6 para acessar VENDAS \n'
                          'Digite 7 para SAIR \n'))

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma nova categoria \n'
                                    'Digite 2 para remover uma categoria \n'
                                    'Digite 3 para alterar uma categoria \n'
                                    'Digite 4 para ver a lista de categorias \n'
                                    'Digite 5 para SAIR \n'))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar: ')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover: ')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar: ')
                    novaCategoria = input('Digite a categoria para qual deseja alterar: ')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    print('Você finalizou!')
                    break

        elif local == 2:
            est = controller.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um novo produto \n'
                                    'Digite 2 para remover um produto \n'
                                    'Digite 3 para alterar um produto \n'
                                    'Digite 4 para ver o estoque \n'
                                    'Digite 5 para SAIR \n'))
                if decidir == 1:
                    nome = input('Digite o nome do produto que deseja cadastrar: ')
                    preco = str(input('Digite o preco do produto: '))
                    categoria = input('Digite a categoria do produto: ')
                    quantidade = str(input('Digite a quantidade: '))
                    est.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input('Digite o nome do produto que deseja remover: ')
                    est.removerProduto(produto)
                elif decidir == 3:
                    nome = input('Digite o produto que deseja alterar: ')
                    novoNome = input('Digite o produto para qual deseja alterar: ')
                    novoPreco = input('Digite o valor do produto: ')
                    novaCategoria = input('Digite a categoria: ')
                    novaQuantidade = input('Digite a quantidade: ')
                    est.alterarProduto(nome, novoNome, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    est.mostrarEstoque()
                else:
                    print('Você finalizou!')
                    break

        elif local == 3:
            forn = controller.ControllerFornecedor()
            while True:
                decidir = int(input('Digite 1 para cadastrar fornecedor \n'
                                    'Digite 2 para alterar fornecedor \n'
                                    'Digite 3 para remover fornecedor \n'
                                    'Digite 4 para mostar lista de fornecedores \n'
                                    'Digite 5 para SAIR \n'))
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor que deseja cadastrar: ')
                    cnpj = str(input('Digite o CNPJ: '))
                    contato = input('Digite um telefone para contato: ')
                    categoria = input('Digite a categoria: ')
                    forn.cadastrarFornecedor(nome, cnpj, contato, categoria)
                elif decidir == 2:
                    nome = input('Digite o nome do fornecedor que deseja alterar: ')
                    novoNome = input('Digite o nome do fornecedor para qual deseja alterar: ')
                    novoCnpj = input('Digite o CNPJ: ')
                    novoContato = input('Digite um telefone para contato: ')
                    novaCategoria = input('Digite a categoria: ')
                    forn.alterarFornecedor(nome, novoNome, novoCnpj, novoContato, novaCategoria)
                elif decidir == 3:
                    nome = input('Digite o nome do fornecedor que deseja remover: ')
                    forn.removerFornecedor(nome)
                elif decidir == 4:
                    forn.mostrarFornecedor()
                else:
                    print('Você finalizou!')
                    break

        elif local == 4:
            cliente = controller.ControllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastrar cliente \n'
                                    'Digite 2 para alterar um cliente \n'
                                    'Digite 3 para remover um cliente \n'
                                    'Digite 4 para mostrar lista de clientes \n'
                                    'Digite 5 para SAIR \n'))
                if decidir == 1:
                    nome = input('Digite o nome do cliente: ')
                    cpf = input('Digite o CPF: ')
                    contato = input('Digite um telefone para contato: ')
                    endereco = input('Digite o endereco: ')
                    cliente.cadastrarCliente(nome, cpf, contato, endereco)
                elif decidir == 2:
                    nome = input('Digite o nome do cliente que deseja alterar: ')
                    novoNome = input('Digite o nome do cliente para qual deseja alterar: ')
                    novoCpf = input('Digite o CPF: ')
                    novoContato = input('Digite um telefone para contato: ')
                    novoEndereco = input('Digite o endereco: ')
                    cliente.alterarCliente(nome, novoNome, novoCpf, novoContato, novoEndereco)
                elif decidir == 3:
                    nome = input('Digite o nome do cliente que deseja remover: ')
                    cliente.removerCliente(nome)
                elif decidir == 4:
                    cliente.mostrarCliente()
                else:
                    print('Você finalizou!')
                    break

        elif local == 5:
            func = controller.ControllerFuncionario()
            while True:
                decidir = int(input('Digite 1 para cadastrar funcionários \n'
                                    'Digite 2 para remover funcionários \n'
                                    'Digite 3 para mostrar registro de funcionários \n'
                                    'Digite 4 para SAIR \n'))
                if decidir == 1:
                    cargo = input('Digite o cargo que o funcionário ocupará: ')
                    nome = input('Digite o nome: ')
                    cpf = input('Digite o CPF: ')
                    contato = input('Digite um telefone para contato: ')
                    endereco = input('Digite o endereco: ')
                    func.cadastrarFuncionario(cargo, nome, cpf, contato, endereco)
                elif decidir == 2:
                    nome = input('Digite o nome do funcionário que deseja remover: ')
                    func.removerFuncionario(nome)
                elif decidir == 3:
                    func.mostrarFuncionario()
                else:
                    print('Você finalizou!')
                    break

        elif local == 6:
            venda = controller.ControllerVenda()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma venda \n'
                                    'Digite 2 para relatório de produtos vendidos \n'
                                    'Digite 3 para mostrar as vendas \n'
                                    'Digite 4 para SAIR \n'))
                if decidir == 1:
                    nomeProduto = input('Digite o produto vendido: ')
                    quantidadeVendida = int(input('Digite a quantidade vendida: '))
                    venda.cadastrarVenda(nomeProduto, quantidadeVendida)
                elif decidir == 2:
                    venda.relatorioProdutos()
                elif decidir == 3:
                    dataInicio = input('Digite a data de início para filtrar: ')
                    dataTermino = input('Digite a data de término para filtrar: ')
                    venda.mostrarVenda(dataInicio, dataTermino)
                else:
                    print('Você finalizou!')
                    break


