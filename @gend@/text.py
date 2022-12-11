import pandas
import os

'''client = str(input('\nNome: ')).strip().lower() #entrada de dado


log = str(input('Login: ')).strip() #entrada de dado
test_log = (log).isnumeric()
cont1 = len(log) 
                        
if cont1 != 11 or test_log == False:   #Teste para quantidade de caracteres login
                print('[ O login deve ter 11 digitos numericos ]\n')
                log = (input('Login: ')).strip()
                                

password = str(input('senha: ')).strip().lower()
test_password = (password).isalnum()
cont2 = len(password)

if cont2 != 8 or test_password == False:  #Teste para quantidade de caracteres senha

                print('[ Senha deve ter 8 caracteris entre numeros e letras ]\n')
                password = input('senha: ').strip().lower()

dado = (f'\n{client},{log},{password}')
with open('tabelabd.csv', "x") as dadoEntrada:
    dadoEntrada.write('x')
    if dadoEntrada == 'FileExistsError: [Errno 17] File exists: "tabelabd.csv"':
        print('já existe')

tabela = pandas.read_csv('tabelabd.csv')
print(tabela['Nome'])
print(tabela['Senha'])'''

# urilizar esta formatação {'Nome': 'jaelson pereira', 'Login': 83988888449, 'Senha':'caju1234'}


'''novoPerfil = (f'{"Nome":"{client}", "Login": "{log}", "Senha":"{password}"}')
#troca = novoPerfil[]
#novoP2 = '"' + novoPerfil + '"'
Nome,Login,Senha
#novo_perfil = client,log,password

# Estrutura de entrada de dados

with open('arquivo_cadastro.txt', "a") as dadoEntrada:
    dadoEntrada.write(str({novoPerfil}))

with open('arquivo_cadastro.txt', 'r') as bDados:
    consulta = bDados.read()

d2 = 'Nome,Login,Senha'   # Extrutura para formatação de dados para class dict( dicionario )
edit = '""'

for i in range(0,len(edit)):
        d1 = d1.replace(edit[i],'')

keys = d2.split(',')
values = d1.split(',')
dadosClient = {}
dadosClient = ast.literal_eval(dadosClient)
verificador = str(dadosClient)


valor = ast.literal_eval(consulta)
print(type(valor))'''

verificadoArquivo = '83988888449.csv'

if os.path.isfile(verificadoArquivo):
         respost = True

         print(respost)
