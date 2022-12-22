import pandas
from time import sleep
import sys



def acessoMenuPrincipal():
        log_entrada = ''
        password_entrada = ''
        while log_entrada != 'exit' or password_entrada != 'exit':
                    print('[ Favor informar login e senha ]')

                    log_entrada = str(input('Login: ')).strip()#entrada de dados login
                    test_log = (log_entrada).isnumeric()
                    contadorNlog = len(log_entrada)

                    if log_entrada == 'exit':
                            break

                    if contadorNlog != 11 or test_log == False:
                            print('[ o login deve ter 11 digitos numericos ]\n')
                            log_entrada = str(input('Login: ')).strip()
                                        

                    password_entrada = str(input('Senha: ')).strip().lower()   #entrada de dados senha
                    test_senha = (password_entrada).isalnum()
                    contadorNsenha = len(password_entrada)

                    if password_entrada == 'exit':
                            break

                    if contadorNsenha != 6 or test_senha == False:
                            print('[ A senha deve ter 6 caracteres entre numeros e letras ]\n')
                            password_entrada = str(input('Senha: ')).strip().lower()



                    tabela = pandas.read_csv('cadastroraiz.csv')  # abertura de arquivo para leitura conforme o guia 

                    
                    verificadorLogin_v =  str(tabela['Login'])
                    verificadorSenha_v = str(tabela['Senha'])

 


                    if log_entrada not in verificadorLogin_v and password_entrada not in verificadorSenha_v: #teste validade login
                                print('Usuario não identificado')


                    elif log_entrada in verificadorLogin_v and password_entrada in verificadorSenha_v:
                        optionSecundario = ''
                        while optionSecundario != 7:
                                print('''
                                ========================== [ @gend@ ] ========================
                                ||                                                           ||
                                ||                  [ 1 ] Adicionar Contato                  ||
                                ||                  [ 2 ] Listar Contatos                    ||
                                ||                  [ 3 ] Pesquisar Contato                  ||
                                ||                  [ 4 ] Remover Contato                    ||
                                ||                  [ 5 ] Alterar Contato                    ||
                                ||                  [ 6 ] Exluir Conta do Usuário            ||
                                ||                  [ 7 ] Sair                               ||
                                ||                                                           ||
                                ===============================================================
                                ''')
                                optionSecundario = int(input('Digite a opção desejada: '))

                                #-------------- [ Inicio - Opção 1 - adicinar contato ] ----------------#
                                if optionSecundario == 1:
                                        print('\n--------[ Novo contato ]-----------')
                                        nomeContato = str(input('Nome Contato: ')).strip().lower()

                                        numeroContato = str(input('Numero Telefone: ')).strip().lower()
                                        digitosN = len(numeroContato)

                                        if numeroContato not in '1234567890' and digitosN != 11:
                                                print('\n[ Erro é necessario 11 digitos numericos ]\n')
                                                                                                                        
                                                                                                                        
                                        novoContato = (f'\n{nomeContato},{numeroContato}')

                                        #lg = log_entrada

                                        novaAgenda = log_entrada + '.csv'

                                        with open(novaAgenda, "a", encoding='utf-8') as dado:
                                                dado.write(novoContato)



                                        print('[ Novo contato foi adicionado ]')
                                        print('[ Deseja adnicionar novo contato ]')
                                        print('Sim s/n Não')

                                        noC = str(input('Opção: '))
                                #----------------- [ Fim - Opção 1 ] ---------------#

                                #----------- [ Inicio - Opção 2 - Mostrar contato ] ----#                                            
                                elif optionSecundario == 2:
                                        
                                        novaAgenda = log_entrada + '.csv'
                                        tabela = pandas.read_csv(novaAgenda)
                                        print(tabela)
                                        sleep(1)
                                #---------    [   Fim - Opção 2    ]     ----------#


                                #-----   [   Inicio - Opção 3 - Pesquisa contato   ]      ----#
                                elif optionSecundario == 3:# ainda em processo
                                        novaAgenda = log_entrada + '.csv'
                                        tabela = pandas.read_csv(novaAgenda)

                                        pesquisa = str(input('Favor informar nome contato: '))

                                        tabela2 = pandas.DataFrame(tabela)

                                        print (tabela2.loc[(tabela2['Nome'] == pesquisa)])
                                        sleep(1)
                                        

                                #-----  [   Fim - Opção 3    ]      -----#


                                #-----  [   Inicio - Opção 4 - excluir contato    ]      -----#
                                elif optionSecundario == 4:
                                        novaAgenda = log_entrada + '.csv'
                                        arquivo_contatos = pandas.read_csv(novaAgenda)
                                        print(arquivo_contatos)
                                        delete = int(input('Informe a linha do contato: '))
                                        result = arquivo_contatos.drop(delete)
                                        result = str(result)
                                        print(result)


                                        with open(novaAgenda, "w+", encoding='utf-8') as dado:
                                                dado.write(str(result))
                                        sleep(1)

                                #-----  [   Fim - Opção 4    ]      -----#

                                #-----  [   Inicio - Opção 5 - Alterar contato    ] ------#
                                elif optionSecundario == 5:
                                        novaAgenda = log_entrada + '.csv'
                                        data = pandas.read_csv(novaAgenda)
                                        print(data)
                                        alterar = int(input('Digite a linha do constato a ser alterado:  '))
                                        nome = str(input('Nome:  '))
                                        numero = int(input('Numero:  '))
                                        data['Nome'][alterar] = nome
                                        data['Numero'][alterar] = numero
                                        print(data)
                                        alterado = data

                                        with open(novaAgenda, "w", encoding='utf-8') as dado:
                                                dado.write(str(alterado))
                                        sleep(1)
                                #-----  [    Fim - Opção 5   ]      -----#

                                #-----  [    Inicio - Opção 6  - Excluir Conta ] ok     -----#
                                elif optionSecundario == 6:

                                        print('Deseja excluir sua conta?')
                                        print('Sim s/n Não')
                                        pergunta = str(input('Opção: ')).lower()

                                        if pergunta == 'n':
                                                break
                                        elif pergunta == 's':
                                                novoL = int(log_entrada)
                                                tabela = pandas.read_csv('cadastroraiz.csv')
                                                tabela2 = pandas.DataFrame(tabela)

                                                itemExcluir = tabela2.index[(tabela2['Login'] == novoL)].tolist()

                                                excluindoConta = tabela2.drop(itemExcluir)
                                                excluindoConta = excluindoConta
                                                print(excluindoConta)

                                                with open('cadastroraiz.csv', "w", encoding='utf-8') as dado:
                                                        dado.write(str(excluindoConta))
                                #-----  [    Fim - Opção 6   ]      -----#

                                #-----  [    Inicio - Opção 7 - Sair   ]ok      -----#
                                elif optionSecundario == 7:
                                        break
                                #-----  [    Fim - Opção 7   ]      -----#
                                else:
                                        print('Opção invalida')
