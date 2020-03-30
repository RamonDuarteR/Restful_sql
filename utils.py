from models import Pessoas

def insere():
    pessoa=Pessoas(nome="Ruan",idade="28")
    # print(pessoa)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome="Ruan").first()
    # print(pessoa.idade)

def altera():
    pessoa = Pessoas.query.filter_by(nome="Ruan").first()
    pessoa.idade=45

def deleta():
    pessoa = Pessoas.query.filter_by(nome="Rodrigues").first()
    pessoa.delete()

if __name__ == '__main__':
    # insere()
    # altera()
    # consulta()
    # deleta()

