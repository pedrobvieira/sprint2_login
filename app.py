from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template, request, abort, flash, session
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Usuarios
from logger import logger
from schemas import *
from flask_cors import CORS


import hashlib


info = Info(title="Login API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Cadastro dos usuarios à base e autentica para uso")


@app.route('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get ('/login', tags=[usuario_tag],
         responses={"200": ListagemUsuariosSchema, "404": ErrorSchema})

def do_login(query: UsuariosLoginSchema):
    """Faz o Login no sistema

    retorna o usuário autenticado
    """

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    usuario_email = request.args.get('email')
    usuario_senha = request.args.get('senha')
    usuario_query = session.query(Usuarios).filter(Usuarios.email == usuario_email).first()

    if not usuario_query:
        # se o produto não foi encontrado
        error_msg = "Usuario não encontrado na base :/"
        logger.warning(f"Erro ao buscar usuario '{usuario_email}', {error_msg}")
        return {"mesage": "Usuário não encontrado"}, 404
    else:
        # criptografando a senha digitada
        senha_enc = usuario_senha.encode()
        md5_senha = hashlib.md5(senha_enc)
        usuario_senha = md5_senha.hexdigest()
        logger.debug(f"Usuário econtrado: '{usuario_query.nome}'")
        # retorna a representação de usuario
        return {"mesage": "Usuário encontrado", "nome": usuario_query.nome, "senha": usuario_query.senha, "senha_dig": usuario_senha}



@app.post('/cadastrar_usuario', tags=[usuario_tag],
          responses={"200": UsuariosViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_usuario(form: UsuariosSchema):
    """Adiciona um novo usuario à base de dados

    Retorna o usuário adicionado
    """
    usuario = Usuarios(
        cpf=form.cpf,
        nome=form.nome,
        senha=form.senha,
        email=form.email,
        telefone=form.telefone,
        cep=form.cep,
        endereco=form.endereco,
        numero=form.numero,
        bairro=form.bairro,
        cidade=form.cidade,
        uf=form.uf)
    try:
        #criptografando a senha
        senha_enc = usuario.senha.encode()
        md5_senha = hashlib.md5(senha_enc)
        usuario.senha = md5_senha.hexdigest()
        # criando conexão com a base
        session = Session()
        # adicionando usuário
        session.add(usuario)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return {"mesage": "Usuario CADASTRADO", "nome": usuario.nome, "senha": usuario.senha}

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Usuário já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


