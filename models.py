from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///atividade.db", convert_unicode= True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
base = declarative_base()
base.query = db_session.query_property()

class Pessoas(base):
    __tablename__="Pessoas"
    id = Column(Integer,primary_key=True)
    nome = Column(String(40),index=True)
    idade = Column(Integer)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

class Atividades(base):
    __tablename__= "Atividades"
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    Pessoa = relationship("Pessoas")
    Pessoa_id = Column(Integer, ForeignKey("Pessoas.id"))

    # def __repr__(self):
    #     return "<Atividade {}>".format(self.nome)

def init_db():
    base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()