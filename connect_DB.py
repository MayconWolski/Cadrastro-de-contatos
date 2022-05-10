from statistics import mode
from modelo import Pessoa
from tinydb import TinyDB, Query
import pandas as pd

#FAZ A CRIAÇÃO DO BANCO DE DADOS .JSON

bd = TinyDB('Pessoas.json')
usuario = Query()

# CREATE\ CRIAR

def inserir(model: Pessoa):
    bd.insert({"nome": model.nome, 
    "sobrenome": model.sobrenome, 
    "CPF":model.CPF,
    "email":model.email,
    "telefone":model.telefone})

#READ\ EXIBIR DADOS 

def exibir_dados():
    todos = bd.all()
    return todos

#DELETE\ REMOVE     

def remove_contato(cpf: int):
    if bd.search (usuario.CPF ==str(cpf)):
        bd.remove(usuario.CPF==str(cpf))
        print("Usuário apagado com sucesso")
    else:
        print("Usuario não encontrado")

#UPDATE \ ATUALIZAR DADOS
def atualizar_contato(cpf: int, model:Pessoa):
    if bd.search(usuario.CPF==cpf):
        bd.remove(usuario.CPF==cpf)
        inserir(model)
    else:
        print("Esse usuário não existie")

#READ\ TODAS AS TABELAS \ COM PANDAS

def exibir_tabelas():
    todos = pd.DataFrame(bd)
    return todos

#BUSCAR CPF
def buscarCPF(cpf):
    return bd.search(usuario.CPF==str(cpf))