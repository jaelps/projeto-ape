import pandas
from time import sleep


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
                                                                                                        
                verificadoArquivo = '/projeto-ape/' + log_entrada + '.csv'
                                                                                                
                novoContato = (f'\n{nomeContato},{numeroContato},')

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
                tabela = pandas.read_csv(novaAgenda)
                print(tabela)
                sleep(1)
        #---------    [   Fim - Opção 2    ]     ----------#


        #-----   [   Inicio - Opção 3 - Pesquisa contato   ]      ----#
        elif optionSecundario == 3:# ainda em processo
                
                tabela = pandas.read_csv(novaAgenda)

                pesquisa = str(input('Favor informar nome contato: '))

                tabela2 = pandas.DataFrame(tabela)

                print (tabela2.loc[(tabela2['Nome'] == pesquisa)])
                sleep(1)
                

        #-----  [   Fim - Opção 3    ]      -----#


        #-----  [   Inicio - Opção 4 - excluir contato    ]      -----#
        elif optionSecundario == 4:
                
                data = pandas.read_csv(novaAgenda)
                print(data)
                delete = int(input('Pesquisar contato: '))
                result = data.drop(delete)
                result = result
                print(result)

                #novaAgenda = log_entrada + '.csv'
                with open('text.csv', "w", encoding='utf-8') as dado:
                        dado.write(result)
                sleep(1)

        #-----  [   Fim - Opção 4    ]      -----#

        #-----  [   Inicio - Opção 5 - Alterar contato    ] ------#
        elif optionSecundario == 5:
                data = pandas.read_csv(novaAgenda)
                print(data)
                alterar = int(input('Digite a linha do constato a ser alterado:  '))
                nome = str(input('Nome:  '))
                numero = int(input('Numero:  '))
                data['Nome'][alterar] = nome
                data['Numero'][alterar] = numero
                print(data)
                altrado = dado

                with open('text.csv', "w", encoding='utf-8') as dado:
                        dado.write(altrado)
                sleep(1)
        #-----  [    Fim - Opção 5   ]      -----#

        #-----  [    Inicio - Opção 6  - Excluir Conta ]      -----#
        elif optionSecundario == 6:

                tabela = pandas.read_csv('tabelabd.csv')

                tabela2 = pandas.DataFrame(tabela)

                itemExcluir = tabela2.index[(tabela2['Login'] == log_entrada)].tolist()
                sepandoItens = itemExcluir[0]
                excluindoConta = tabela2.drop(sepandoItens)
                excluindoConta = excluindoConta
                print(excluindoConta)
        #-----  [    Fim - Opção 6   ]      -----#

        #-----  [    Inicio - Opção 7 - Sair   ]      -----#
        elif optionSecundario == 7:
                break
        #-----  [    Fim - Opção 7   ]      -----#
        else:
                print('Opção invalida')
