import pandas
import os
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

                        if contadorNsenha != 8 or test_senha == False:
                                print('[ A senha deve ter 8 caracteres entre numeros e letras ]\n')
                                senha_entrada = str(input('Senha: ')).strip().lower()



                        tabela = pandas.read_csv('tabelabd.csv')  # abertura de arquivo para leitura conforme o guia 
                                

                        verificadorLogin_v =  str(tabela['Login'])
                        verificadorSenha_v = str(tabela['Senha'])
                        verificadorNome_v = str(tabela['Nome'])
        


                        if log_entrada not in verificadorLogin_v and password_entrada not in verificadorSenha_v: #teste validade login
                                print('Usuario não identificado')


                        elif log_entrada in verificadorLogin_v and password_entrada in verificadorSenha_v:
                                        continue

                                        # <<<<<<  Incluir Menu 2 >>>>>>>

                               
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

                        if cont2 != 8 or test_password == False:  #Teste para quantidade de caracteres senha

                                print('[ Senha deve ter 8 caracteris entre numeros e letras ]\n')
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
