from datetime import datetime

from MVC.dao import DaoCategoria, DaoEstoque, DaoVenda, DaoFornecedor, DaoPessoa, DaoFuncionario
from MVC.models import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario


class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        categoria = DaoCategoria.ler()
        for categoria in categoria:
            if categoria.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria ja existente!')

    def removerCategoria(self, categoriaRemover):
        categoria = DaoCategoria.ler()
        cat = list(filter(lambda categoria: categoria.categoria == categoriaRemover, categoria))

        if len(cat) == 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(categoria)):
                if categoria[i].categoria == categoriaRemover:
                    del categoria[i]
                    break
            print('Categoria removida com sucesso!')

            with open('categoria.txt', 'w') as arq:
                for i in categoria:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade)
                           if(x.produto.categoria == categoriaRemover) else (x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|"
                               + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')


    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        categoria = DaoCategoria.ler()
        cat = list(filter(lambda categoria: categoria.categoria == categoriaAlterar, categoria))

        if len(cat) > 0:
            cat1 = list(filter(lambda categoria: categoria.categoria == categoriaAlterada, categoria))
            if len(cat1) == 0:
                categoria = list(map(lambda categoria: Categoria(categoriaAlterada) if(categoria.categoria == categoriaAlterar) else(categoria), categoria))
                print('Alteração efetuada com sucesso!')

                estoque = DaoEstoque.ler()
                estoque = list(
                    map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                    if (x.produto.categoria == categoriaAlterar) else (x), estoque))

                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|"
                                       + i.produto.categoria + "|" + str(i.quantidade))
                        arq.writelines('\n')

            else:
                print('A categoria que deseja alterar já existe!')

        else:
            print('Categoria inexistente!')

        with open('categoria.txt', 'w') as arq:
            for categoria in categoria:
                arq.writelines(categoria.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        estoque = DaoEstoque.ler()
        cat = DaoCategoria.ler()
        h = list(filter(lambda estoque: estoque.categoria == categoria, cat))
        est = list(filter(lambda estoque: estoque.produto.nome == nome, estoque))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')

    def removerProduto(self, nome):
        estoque = DaoEstoque.ler()
        est = list(filter(lambda estoque: estoque.produto.nome == nome, estoque))
        if len(est) > 0:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == nome:
                    del estoque[i]
                    break
            print('O produto foi removido com sucesso!')
        else:
            print('O produto não existe!')
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|"
                               + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        estoque = DaoEstoque.ler()
        cat = DaoCategoria.ler()
        h = list(filter(lambda estoque: estoque.categoria == novaCategoria, cat))
        if len(h) > 0:
            est = list(filter(lambda estoque: estoque.produto.nome == nomeAlterar, estoque))
            if len(est) > 0:
                est = list(filter(lambda estoque: estoque.produto.nome == novoNome, estoque))
                if len(est) == 0:
                    estoque = list(map(lambda estoque: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (estoque.produto.nome == nomeAlterar) else (estoque), estoque))
                    print('Produto alterado com sucesso!')
                else:
                    print('Produto já cadastrado!')
            else:
                print('O produto não existe!')

            with open('estoque.txt', 'w') as arq:
                for estoque in estoque:
                    arq.writelines(estoque.produto.nome + "|" + str(estoque.produto.preco) + "|"
                                   + estoque.produto.categoria + "|" + str(estoque.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria não existe!')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print("========== Produtos ==========")
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                      f'Preco: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}'
                )
                print("--------------------")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, quantidadeVendida):
        estoque = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for estoque in estoque:
            if existe == False:
                if estoque.produto.nome == nomeProduto:
                    existe = True
                    if estoque.quantidade >= quantidadeVendida:
                        quantidade = True
                        estoque.quantidade = int(estoque.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(estoque.produto.nome, estoque.produto.preco, estoque.produto.categoria), quantidadeVendida)

                        valor_compra = int(quantidadeVendida) * int(estoque.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append([Produtos(estoque.produto.nome, estoque.produto.preco, estoque.produto.categoria), estoque.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write('')

        for produtos in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(produtos[0].nome + "|" + produtos[0].preco + "|" + produtos[0].categoria + "|" + str(produtos[1]))
                arq.writelines('\n')

        if existe == False:
            print('O produto não existe')
            # return None
        elif not quantidade:
            print('A quantidade não contém em estoque')
        else:
            print('Venda realizada com sucesso')
            return valor_compra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for venda in vendas:
            nome = venda.itensVendidos.nome
            quantidade = venda.quantidadeVendida
            tamanho = list(filter(lambda vendas: vendas['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda xvendas: {'produto': nome, 'quantidade': int(vendas['quantidade']) + int(quantidade)}
                if (vendas['produto'] == nome) else (vendas), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'======== Produtos [{a}] ========')
            print(f"Produto: {i['produto']}")
            print(f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%y') >= dataInicio1
                                                   and datetime.strptime(x.data, '%d/%m/%y') <= dataTermino1, vendas))

        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f"========== Venda [{cont}] ==========")
            print(f"Produto: {i.itensVendidos.nome}")
            print(f"Categoria: {i.itensVendidos.categoria}")
            print(f"Data: {i.data}")
            print(f"Quantidade: {i.quantidadeVendida}")
            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1

        print(f'Total vendido: {total}')

class ControllerFornecedor:

    def cadastrarFornecedor(self, nome, cnpj, contato, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaContato = list(filter(lambda x: x.contato == contato, x))

        if len(listaCnpj) > 0:
            print('O CNPJ já existe.')
        elif len(listaContato) > 0:
            print('O telefone já existe.')
        else:
            if len(cnpj) == 14 and len(contato) <= 11:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, contato, categoria))
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('Digite um CNPJ ou contato válido.')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoContato, novaCategoria):
        fornecedores = DaoFornecedor.ler()

        forn = list(filter(lambda fornecedores: fornecedores.nome == nomeAlterar, fornecedores))
        if len(forn) > 0:
            forn = list(filter(lambda fornecedores: fornecedores.cnpj == novoCnpj, fornecedores))
            if len(forn) == 0:
                fornecedores = list(map(lambda fornecedores: Fornecedor(novoNome, novoCnpj, novoContato, novaCategoria) if (fornecedores.nome == nomeAlterar) else (fornecedores), fornecedores))
            print('Fornecedor alterado com sucesso!')
        else:
            print('O fornecedor que deseja alterar não existe.')

        with open('fornecedores.txt', 'w') as arq:
            for fornecedor in fornecedores:
                arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.contato + "|" + str(fornecedor.categoria))
                arq.writelines('\n')
            # print('Fornecedor alterado com sucesso!')

    def removerFornecedor(self, nome):
        fornecedores = DaoFornecedor.ler()

        forn = list(filter(lambda fornecedores: fornecedores.nome == nome, fornecedores))
        if len(forn) > 0:
            for i in range(len(fornecedores)):
                if fornecedores[i].nome == nome:
                    del fornecedores[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe!')

        with open('fornecedores.txt', 'w') as arq:
            for i in fornecedores:
                arq.writelines(fornecedores.nome + "|" + fornecedores.cnpj + "|" + fornecedores.contato + "|" + str(fornecedores.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso!')

    def mostrarFornecedor(self):
        fornecedor = DaoFornecedor.ler()
        if len(fornecedor) == 0:
            print('Não há fornecedores cadastrados!')
        else:
            print('====== Fornecedores ======')
            for fornecedor in fornecedor:
                print(f'Nome: {fornecedor.nome}\n'
                      f'CNPJ: {fornecedor.cnpj}\n'
                      f'Contato: {fornecedor.contato}\n'
                      f'Categoria: {fornecedor.categoria}'
                      )
                print("--------------------")

class ControllerCliente:
    def cadastrarCliente(self, nome, cpf, contato, endereco):
        cliente = DaoPessoa.ler()
        listaCpf = list(filter(lambda cliente: cliente.cpf == cpf, cliente))

        if len(listaCpf) > 0:
            print('CPF já cadastrado!')
        elif len(cpf) == 11 and len(contato) <= 11:
            DaoPessoa.salvar(Pessoa(nome, cpf, contato, endereco))
            print('O cliente foi cadastrado com sucesso!')
        else:
            print('Digite um CPF ou contato válido!')

    def alterarCliente(self, nomeAlterar, novoNome, novoCpf, novoContato, novoEndereco):
        cliente = DaoPessoa.ler()
        listaNome = list(filter(lambda cliente: cliente.nome == nomeAlterar, cliente))

        if len(listaNome) > 0:
            cliente = list(map(lambda cliente: Pessoa(novoNome, novoCpf, novoContato, novoEndereco) if (cliente.nome == nomeAlterar)
            else (cliente), cliente))
            print('Alteração efetuada com sucesso!')
        else:
            print('O cliente que deseja alterar não existe.')

        with open('clientes.txt', 'w') as arq:
            for cliente in cliente:
                arq.writelines(
                    cliente.nome + "|" + cliente.cpf + "|" + cliente.contato + "|" + cliente.endereco)
                arq.writelines('\n')

    def removerCliente(self, nome):
        cliente = DaoPessoa.ler()
        nomeCliente = list(filter(lambda cliente: cliente.nome == nome, cliente))

        if len(nomeCliente) > 0:
            for i in range(len(cliente)):
                if cliente[i].nome == nome:
                    del cliente[i]
                    break
        else:
            print('O cliente que deseja remover não existe!')
            return None

        with open('clientes.txt', 'w') as arq:
            for cliente in cliente:
                arq.writelines(
                    cliente.nome + "|" + cliente.cpf + "|" + cliente.contato + "|" + cliente.endereco)
                arq.writelines('\n')
            print('O cliente foi removido com sucesso!')

    def mostrarCliente(self):
        cliente = DaoPessoa.ler()

        if len(cliente) == 0:
            print('Não existe clientes cadastrados!')
        else:
            print('======= CLIENTES: =======')
            for cliente in cliente:
                print(f'Nome: {cliente.nome}\n'
                      f'CNPJ: {cliente.cpf}\n'
                      f'Contato: {cliente.contato}\n'
                      f'Categoria: {cliente.endereco}'
                      )
                print("--------------------")

class ControllerFuncionario:
    def cadastrarFuncionario(self, cargo, nome, cpf, contato, endereco):
        funcionario = DaoFuncionario.ler()
        listaCpf = list(filter(lambda funcionario: funcionario.cpf == cpf, funcionario))

        if len(listaCpf) > 0:
            print('Funcionário já está cadastrado!')
        elif len(cpf) == 11 and len(contato) <= 11:
            DaoFuncionario.salvar(Funcionario(cargo, nome, cpf, contato, endereco))
            print('Funcionario cadastrado com sucesso!')
        else:
            print('Digite um CPF válido!')

    def removerFuncionario(self, nome):
        funcionario = DaoFuncionario.ler()
        nomeFuncionario = list(filter(lambda funcionario: funcionario.nome == nome, funcionario))

        if len(nomeFuncionario) > 0:
            for i in range (len(funcionario)):
                if funcionario[i].nome == nome:
                    del funcionario[i]
                    break
        else:
            print('O funcionário que deseja remover não existe!')
            return None

        with open('funcionarios.txt', 'w') as arq:
            for funcionario in funcionario:
                arq.writelines(
                    funcionario.cargo + "|" + funcionario.nome + "|" + funcionario.cpf + "|" + funcionario.contato + "|" + funcionario.endereco)
                arq.writelines('\n')
            print('O funcionario foi removido com sucesso!')

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print('Não existe funcionarios cadastrados!')
        else:
            print('======= FUNCIONARIOS: =======')
            for funcionario in funcionario:
                print(f'Cargo: {funcionario.cargo}\n'
                      f'Nome: {funcionario.nome}\n'
                      f'CPF: {funcionario.cpf}\n'
                      f'Contato: {funcionario.contato}\n'
                      f'Categoria: {funcionario.endereco}'
                      )
                print("--------------------")




