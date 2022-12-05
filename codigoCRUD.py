#python

from PyQt5 import uic, QtWidgets
import sys
import os 
import mysql.connector 



os.system('pip install mysql-connector-python')

def conectarBD(host,usuario,senha,DB):
    connection = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = DB,
    )

    return connection


#Insert


def insert_BD():
    connection = conectarBD("localhost","root","02122","Cliente") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    Cpf = TelinhaCadastrar.TxtCpf.text()
    Nome = TelinhaCadastrar.TxtNome.text()
    Idade = TelinhaCadastrar.TxtIdade.text()
    Logradouro = TelinhaCadastrar.TxtLogradouro.text()
    Numero = TelinhaCadastrar.TxtNumero.text()
    Bairro = TelinhaCadastrar.TxtBairro.text()
    Estado = TelinhaCadastrar.TxtEstado.text()
    ddd = TelinhaCadastrar.Txtddd.text()
    Telefone = TelinhaCadastrar.TxtTelefone.text()
    Email = TelinhaCadastrar.TxtEmail.text()

    
    sql = "INSERT INTO Clientes (Cpf, Nome, Idade, Logradouro, Numero, Bairro, Estado, ddd, Telefone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (
    Cpf,
    Nome,
    Idade,
    Logradouro,
    Numero,
    Bairro,
    Estado,
    ddd,
    Telefone,
    Email
    )
    
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    userid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD


    QtWidgets.QMessageBox.about(TelinhaCadastrar, 'SUCESSO!', "Foi cadastrado o novo cliente de CPF: " + str(Cpf))


def read_BD():
    connection = conectarBD("localhost","root","02122","Cliente") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    
    sql = "SELECT * FROM Clientes WHERE cpf = '" + TelinhaConsultar.TxtCpf.text() +"';" #Realizando um select para mostrar todas as linhas e colunas da tabela    
    

    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtém todas as linhas no conjunto de resultados da consulta
    
    
    cursor.close() #
    connection.close() #Fecha a conexão com o banco

    for result in results: #Ler os registros existentes com o select
        
        TelinhaConsultar.TxtNome.setText(str(result[2]))
        TelinhaConsultar.TxtIdade.setText(str(result[3]))   #Formando o valor que vai aparecer na caixa de texto
        TelinhaConsultar.TxtLogradouro.setText(str(result[4]))
        TelinhaConsultar.TxtNumero.setText(str(result[5]))
        TelinhaConsultar.TxtBairro.setText(str(result[6]))
        TelinhaConsultar.TxtEstado.setText(str(result[7]))
        TelinhaConsultar.Txtddd.setText(str(result[8]))
        TelinhaConsultar.TxtTelefone.setText(str(result[9]))
        TelinhaConsultar.TxtEmail.setText(str(result[10]))

def update_Cliente_BD():
    connection = conectarBD("localhost", "root", "02122", "Cliente") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    Nome = TelinhaConsultar.TxtNome.text()
    Idade = TelinhaConsultar.TxtIdade.text()
    Logradouro = TelinhaConsultar.TxtLogradouro.text()
    Numero = TelinhaConsultar.TxtNumero.text()
    Bairro = TelinhaConsultar.TxtBairro.text()
    Estado = TelinhaConsultar.TxtEstado.text()
    ddd = TelinhaConsultar.Txtddd.text()
    Telefone = TelinhaConsultar.TxtTelefone.text()
    Email = TelinhaConsultar.TxtEmail.text()

    sql = "UPDATE Clientes SET Nome=%s, Idade=%s, Logradouro=%s, Numero=%s, Bairro=%s, Estado=%s, ddd=%s, Telefone=%s, Email=%s"
    data = (
    Nome,
    Idade,
    Logradouro,
    Numero,
    Bairro,
    Estado,
    ddd,
    Telefone,
    Email
    )

    cursor.execute(sql,data) #Executa o comando SQL
    connection.commit()

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close()
    connection.close() #Fecha a conexão com o banco

    QtWidgets.QMessageBox.about(TelinhaConsultar,'SUCESSO', "registros alterados!")

def delete_BD(cpf):
    connection = conectarBD("localhost", "root", "02122", "Cliente") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "DELETE FROM Clientes WHERE cpf = '" + TelinhaConsultar.TxtCpf.text() +"';"
   
    
    cursor.execute(sql) #Executa o comando SQL
    connection.commit()

    cursor.close()
    connection.close()
    
    QtWidgets.QMessageBox.about(TelinhaConsultar, 'SUCESSO', "CPF apagado")
    

def VoltarTelaMenu():
    TelinhaMenu.show()
    TelinhaConsultar.close()
    TelinhaCadastrar.close()




def Limpar(): #Função usada para limpar o texto das caixas de texto
    TelinhaCadastrar.TxtNome.setText("")
    TelinhaCadastrar.TxtCpf.setText("")
    TelinhaCadastrar.TxtLogradouro.setText("")
    TelinhaCadastrar.TxtBairro.setText("")
    TelinhaCadastrar.TxtNumero.setText("")
    TelinhaCadastrar.TxtTelefone.setText("")
    TelinhaCadastrar.Txtddd.setText("")
    TelinhaCadastrar.TxtEmail.setText("")
    TelinhaCadastrar.TxtIdade.setText("")
    TelinhaCadastrar.TxtEstado.setText("")



def AbrirTelinhaCadastro(): #Abre a tela de cadastro do projeto
    TelinhaCadastrar.show()
    TelinhaMenu.close()



def AbrirTelinhaConsulta():  #Abre a tela de consulta/deletar/atualizar
    TelinhaConsultar.show()
    TelinhaMenu.close()

app = QtWidgets.QApplication(sys.argv)

TelinhaMenu = uic.loadUi('TelinhaMenu.ui')
TelinhaConsultar = uic.loadUi('TelinhaConsultar.ui')
TelinhaCadastrar = uic.loadUi('TelinhaCadastrar.ui')

TelinhaMenu.show()



TelinhaMenu.btnTelaCadastro.clicked.connect(AbrirTelinhaCadastro) 
TelinhaMenu.btnTelaConsulta.clicked.connect(AbrirTelinhaConsulta)


#Cadastrar(CREATE)

TelinhaCadastrar.BtnCadastrar.clicked.connect(insert_BD)


#Consultar (READ)

TelinhaConsultar.BtnConsultar.clicked.connect(read_BD)


#Atualizar (UPDATE)

TelinhaConsultar.BtnAtualizar.clicked.connect(update_Cliente_BD)


#Deletar   (DELETE)

TelinhaConsultar.BtnDeletar.clicked.connect(delete_BD)



#Voltar

TelinhaCadastrar.BtnVoltar.clicked.connect(VoltarTelaMenu)

TelinhaConsultar.BtnVoltar1.clicked.connect(VoltarTelaMenu)


#Limpar

TelinhaCadastrar.BtnLimpar.clicked.connect(Limpar) #Vinculando a função Limpar ao botão btnLimpar




app.exec()
