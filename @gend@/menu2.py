import pandas
import numpy

print('''
         ========================== [ @gend@ ] ========================
        ||                                                           ||
        ||                  [ 1 ] Adicionar Contato                  ||
        ||                  [ 2 ] Listar Contatos                    ||
        ||                  [ 3 ] Pesquisar Contato                  ||
        ||                  [ 4 ] Remover Contato                    ||
        ||                  [ 5 ] Alterar Contato                    ||
        ||                  [ 6 ] Exluir Contato do Usuário          ||
        ||                  [ 7 ] Sair                               ||
        ||                                                           ||
        ===============================================================
        ''')
optionSecundario = int(input('Digite a opção desejada: '))

while optionSecundario != 7:

        if optionSecundario == 1:
                while noC != 'n':

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
                continue

        elif optionSecundario == 3:
                tabela = pandas.read_csv('text.csv')  # abertura de arquivo para leitura conforme o guia 
                                
                contato =  str(tabela['Nome'])

                pesquisa = str(input('Pesquisar contato: '))
                verifi = contato.count(pesquisa)

                print(contato)
                print(pesquisa)
                print(verifi)
                
        elif optionSecundario == 4:
                #print('[ Informar nome para exclusão ]')

                #contatoExcluir = str(input('Nome do contato: '))
                # Cria um DataFrame a partir de um arquivo csv
                data = pandas.read_csv("text.csv")
                #data = data.drop('maria')
                
                #selecao = str(data['Nome'] == 'maria')
                #position = [selecao]
                itens = data.tz_localize[0,'Nome']
                #resosta = numpy.array_split(position,10)
                print(itens)


                break
                #data.drop(position)
                '''df = pandas.DataFrame(data, columns = ['Nome', 'Numero'])
                indexNames = df[df['Name'] == 'maria'].index
                df.drop(indexNames, inplace=True)'''

                data.drop(0)

                # Descarta os valores passados
                #tips = tips.drop(line=)

                #elif optionSecundario == 5:
                #elif optionSecundario == 6:
        elif optionSecundario == 7:
                break
        else:
                print('Opção invalida')
