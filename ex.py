import pandas

Nome = []
Login = []
Senha = []

dados = {
'Nome':Nome,
'Login':Login,
'Senha':Senha
}

cadastro = pandas.DataFrame(dados)
cadastro.to_csv('cadastroraiz.csv')