from sqlalchemy import Column, String, Integer, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    cpf = Column(String(14))
    nome = Column(String(45))
    senha = Column(String(45))
    email = Column(String(45), unique=True)
    telefone = Column(String(45))
    cep = Column(String(45))
    endereco = Column(String(45))
    numero = Column(String(10))
    bairro = Column(String(45))
    cidade = Column(String(45))
    uf = Column(String(2))


    def __init__(self, cpf, nome, senha, email, telefone, cep,
                 endereco, numero, bairro, cidade, uf):
        """
        Cria o usuário que vai utilizar o sistema

        :param cpf: número do CPF
        :param nome: nome do usuário
        :param senha: senha do usuário
        :param email: email de contato
        :param telefone: telefone de contato
        :param endereço: endereço residencial
        :param número: número do imóvel
        :param bairro: bairro da residência
        :param cidade: cidade onde localiza o imóvel
        :param estado: estado onde localiza o imóvel - abreviado
        """

        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

