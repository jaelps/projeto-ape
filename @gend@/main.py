import pandas
import os
#import menu2
#from login import login_agenda
from login_menuP import acessoMenuPrincipal
#------   Guia de alteração de arquivo txt    -----------#

# 'r' leitura
# 'w' escrita ou subistituição de conteúdo do arquivo existente
# 'x' escrita ou retorna um erro caso o arquivo ja exista
# 'a' escrita ou insere os novos dados no final do arquivo
# 'b' modo binario
# 't' modo de texto(padrão)
# '+' atualizar ou tanto leitura quando escrita


optionInicio = ''
while optionInicio != '3' or optionInicio == 'exit':

                #-------------------- Opções do Menu Inicial ---------------------#

                print('''
                ========================== [ @gend@ ] ========================
                ||                                                           ||
                ||                      [ 1 ] Entrar                         ||
                ||                      [ 2 ] Registrar                      ||
                ||                      [ 3 ] Sair                           ||
                ||                                                           ||
                ===============================================================
                ''')
                optionInicio = str(input('Digite a opção desejada: '))

                if optionInicio == '1':
                        acessoMenuPrincipal()

                                
                #----------------------- Inicio =  Opção 2 ---------------------------#       
                elif optionInicio == '2':

                        option_saida = ''
                        while option_saida != 'n':

                                print(5*'==', '[ Novo Perfil ]', 5*'==')

                                client = str(input('\nNome: ')).strip().lower() #entrada de dado

                                if client == 'exit':  #Opção de saida do programa
                                        break

                                log = str(input('Login: ')).strip() #entrada de dado
                                test_log = (log).isnumeric()

                                if log == 'exit':  #Opção de saida do programa
                                        break

                                cont1 = len(log) 
                                
                                if cont1 != 11 or test_log == False:   #Teste para quantidade de caracteres login
                                        print('[ O login deve ter 11 digitos numericos ]\n')
                                        log = (input('Login: ')).strip()
                                        

                                password = str(input('senha: ')).strip().lower()
                                test_password = (password).isalnum()
                                cont2 = len(password)

                                if cont2 != 6 or test_password == False:  #Teste para quantidade de caracteres senha

                                        print('[ Senha deve ter 6 caracteris entre numeros e letras ]\n')
                                        password = input('senha: ').strip().lower()

                                

                                
                                tabela = pandas.read_csv('tabelabd.csv')  # abertura de arquivo para leitura conforme o guia 
                                        

                                verificadorLogin_v =  str(tabela['Login'])
                                verificadorSenha_v = str(tabela['Senha'])
                                verificadorNome_v = str(tabela['Nome'])


                                if log in verificadorLogin_v:  #Teste para existencia de dados do banco de dados
                                        print('[ Este cadastro ja existe ]\n')

                                else:  #caso não esteja cadastrado os dados são inclusos

                                        novo_perfil = (f'\n{client},{log},{password}') # Estrutura de entrada de dados

                                        with open('tabelabd.csv', "a") as dadoEntrada:
                                                dadoEntrada.write(novo_perfil)

                                        
                                        novaAgenda = log + '.csv'

                                        with open(novaAgenda, "w") as dado:
                                                dado.write('Nome,Numero')

                                        
                                        
                                        print('\n\n[ O cadastro foi efetuado com sucesso ]\n')

                                                
                                        print('[  Deseja fazer novo cadastro ?  ]\n Sim ou Não (s/n)') # opção de novo cadastro ou finalização
                                        option_saida = str(input('')).strip().lower()

                                        if option_saida == 'n':
                                                        break

                                        elif option_saida == 's':
                                                pass
                                                
                                        else:
                                                print('Opção invalida')


                #-------------------------  Fim = opção 2  ---------------------------#
                        

                #----------------------- Inicio =  Opção 3 ---------------------------#
                
                elif optionInicio == '3': # saida do programa

                        print('[  Deseja finalizar o  programa  ]\n Sim ou Não (s/n)')
                        option_saida = str(input('')).lower()

                        if option_saida == 's':
                                print('Fim do programa')
                                break

                        elif option_saida == 'n':
                                continue
                        
                        else:
                                print('Opção invalida') 

                #------------------------- Fim = opção 3 ---------------------------#


                #------------------------- Opção invalida ---------------------------#

                else:
                        print('Opção invalida')



        #------------------------- Opção invalida ---------------------------#
