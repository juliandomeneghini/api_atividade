from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Domeneghini', idade=25)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Julian').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Domeneghini').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
