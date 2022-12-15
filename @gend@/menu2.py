import pandas
import numpy


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
                                                                
        elif optionSecundario == 2:
                tabela = pandas.read_csv('text.csv')
                print(tabela)
        

        elif optionSecundario == 3:# ainda em processo
                
                tabela = pandas.read_csv('text.csv')  # abertura de arquivo para leitura conforme o guia 
                
                                
                #contato =  str(tabela['Nome'])
                

                pesquisa = str(input('Pesquisar contato: '))
                #verifi = contato.count(pesquisa)
                

                #print(contato)
                #print(pesquisa)
                #print(verifi)
                
        elif optionSecundario == 4:
                
                data = pandas.read_csv("text.csv")
                print(data)
                delete = int(input('Pesquisar contato: '))
                result = data.drop(delete)
                result = result
                print(result)

                #novaAgenda = log_entrada + '.csv'
                with open('text.csv', "w", encoding='utf-8') as dado:
                        dado.write(result)

        elif optionSecundario == 5:
                data = pandas.read_csv("text.csv")
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

        #elif optionSecundario == 6:
        elif optionSecundario == 7:
                break
        else:
                print('Opção invalida')
