from pydantic import BaseModel
from typing import Optional, List
from model.usuarios import Usuarios

class UsuariosSchema(BaseModel):
    """ Define como um novo usuário a ser inserida deve ser representado
    """
    cpf: str = "500.725.799-60"
    nome: str = "Lauro Guerra Filho"
    senha: str = "#####"
    email: str = "lauroguerra@uol.com.br"
    telefone: str = "16994566565"
    cep: str = "14.021-650"
    endereco: str = "Avenida Giuseppe Cilento"
    numero: str = "1215"
    bairro: str = "Jardim Botânico"
    cidade: str = "Ribeirão Preto"
    uf: str = "SP"


class ListagemUsuariosSchema(BaseModel):
    """ Define como uma listagem dos usuarios será retornada.
    """
    usuario:List[UsuariosSchema]

def apresenta_usuario(usuario: List[Usuarios]):
    """ Retorna uma representação de um usuario seguindo o schema definido em
        UsuariosViewSchema.
    """
    return {
        "nome": usuario.nome,
        "senha": usuario.senha,
        "cpf": usuario.cpf,
        "email": usuario.email,
        "telefone": usuario.telefone,
        "cep": usuario.cep,
        "endereco": usuario.endereco,
        "numero": usuario.numero,
        "bairro": usuario.bairro,
        "cidade": usuario.cidade,
        "uf": usuario.uf
    }

def apresenta_usuarios(usuarios: List[Usuarios]):
    """ Retorna uma representação do usuario seguindo o schema definido em
        UsuarioViewSchema.
    """
    result = []
    for usuario in usuarios:
        result.append({
            "cpf": usuario.cpf,
            "nome": usuario.nome,
            "senha": usuario.senha,
            "email": usuario.email,
            "telefone": usuario.telefone,
            "cep":  usuario.cep,
            "endereco": usuario.endereco,
            "numero": usuario.numero,
            "bairro": usuario.bairro,
            "cidade": usuario.cidade,
            "uf": usuario.uf
        })

    return {"usuarios": result}


class UsuariosViewSchema(BaseModel):
    """ Define como uma despesa será retornada: despesa.
    """
    id: int = 1
    cpf: str = "500.725.799-60"
    nome: str = "Lauro Guerra Filho"
    senha = "#####"
    email: str = "lauroguerra@uol.com.br"
    telefone: str = "16994566565"
    cep: str = "14.021-650"
    endereco: str = "Avenida Giuseppe Cilento"
    numero: str = "1215"
    bairro: str = "Jardim Botânico"
    cidade: str = "Ribeirão Preto"
    uf: str = "SP"

class UsuariosLoginSchema(BaseModel):
    """ Define como um novo usuário a ser logado deve ser representado
    """
    email: str = "lauroguerra@uol.com.br"
    senha: str = "#####"


def apresenta_login_usuario(usuario: List[Usuarios]):
    """ Retorna uma representação de um usuario seguindo o schema definido em
        UsuariosViewSchema.
    """
    return {
        "email": usuario.email,
        "senha": usuario.senha,


    }

