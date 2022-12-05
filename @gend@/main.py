import pickle
login = ''
senha = ''
#ecolhendo uma opção para iniciar
print('''
============ [ @gend@ ] ===========
||                                ||
||         [ 1 ] Entrar           ||
||         [ 2 ] Registrar        ||
||         [ 3 ] Sair             ||
||                                ||
====================================
''')
optionInicio = int(input('Digite a opção desejada: '))
while optionInicio != 3:
    if optionInicio == 1:
        for i in range(1,2):
                #print('[ Favor informar login e senha ]')
                #login = str(input('Login: ')).strip
                
                dado = open('83988888449.txt', 'r')
            
                #convert1 = str(verificador_login)
                #convert1= verificador_login
                verificador = dado.readlines()
                print(verificador)

                #if login != verificador_login:
                    #print('Usuario não identificado')

                #senha = str(input('Senha: ')).strip

                #arquivo = open('jaelson pereira.txt', 'r')
                #verificador_senha = arquivo.readline()[58:66]
                #convert2 = str(verificador_senha)
                #convert2 = verificador_senha
                #arquivo.close()

                #if senha != verificador_senha:
                    #print('Senha invalida')

# 'r' leitura
# 'w' escrita ou subistituição de conteúdo do arquivo existente
# 'x' escrita ou retorna um erro caso o arquivo ja exista
# 'a' escrita ou insere os novos dados no final do arquivo
# 'b' modo binario
# 't' modo de texto(padrão)
# '+' atualizar ou tanto leitura quando escrita
        
                
        
    elif optionInicio == 2:
        print(5*'==', '[ Novo Perfil ]', 5*'==')

        nome = str(input('Nome: ')).strip().lower()
        login = str(input('Login: ')).strip()
        adm = login
        cont1 = len(login)
        

        if cont1 != 11:
                print('[ O login deve ter 11 digitos ]')
                login = (input('Login: ')).strip().split()

        senha = str(input('senha: ')).strip()
        passord = senha
        cont2 = len(senha)

        if cont2 != 8:
            print('Senha deve ter 8 caracteris entre numeros e letras')
            senha = input('senha: ').strip()

        nome_arquivo = adm + '.txt'

        novo_perfil = {} 
        novo_perfil = {'nome':nome,'login':adm,'senha':passord}

        with open(nome_arquivo, "w") as dado:
                dado.write(str(novo_perfil))
        dado.close()
        
            
        

        # 'r' leitura
        # 'w' escrita ou subistituição de conteúdo do arquivo existente
        # 'x' escrita ou retorna um erro caso o arquivo ja exista
        # 'a' escrita ou insere os novos dados no final do arquivo
        # 'b' modo binario
        # 't' modo de texto(padrão)
        # '+' atualizar ou tanto leitura quando escrita

    else:
        print('Opção invalida')
