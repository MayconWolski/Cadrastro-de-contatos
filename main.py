
from pickle import TRUE
from connect_DB import atualizar_contato, buscarCPF, exibir_dados, exibir_tabelas, inserir, remove_contato
from modelo import Pessoa
from flask import Flask, render_template, redirect
from flask.globals import request
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    result = exibir_dados()
    return render_template('index.html', result=result)

@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    pessoa = Pessoa(nome, sobrenome, cpf, email, telefone)
    inserir(pessoa)
    return redirect("/")

@app.route("/deletar/<int:cpf>")
def deletar(cpf):
    try:
        remove_contato(cpf)
        return redirect("/")
    except:
        return "Algo deu errado"

@app.route('/atualizar/<int:cpf>',methods=["POST","GET"])
def atualizar(cpf):   
    if request.method == 'POST':
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        cpf = request.form["cpf"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        pessoa = Pessoa(nome, sobrenome, cpf, email, telefone)
        try:
            atualizar_contato(cpf,pessoa)
            return redirect('/')
        except:
            return 'algo deu errado'
    else:
        pessoa = buscarCPF(cpf)
        return render_template('update.html',pessoa = pessoa)
        


if __name__ == "__main__":
    app.run(port=3000, debug=TRUE)    
