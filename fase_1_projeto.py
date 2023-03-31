# a) Leitura do arquivo: os dados do arquivo devem ser carregados para memória e disponibilizados em uma lista de listas/tuplas.
# O programa deve exibir a lista com todos os dados

if 1 == 1:
    print()
listaTuplaComDados = []
# Abertura do arquivo com proposito "read"
print('- Critério 1 ')
arquivo = open('ArquivoDadosProjeto.csv', 'r')
# For responsável por percorrer as linhas do arquivo
for linha in arquivo:
    saida = linha[:-1].split(';')
    data = saida[0]
    precipitacao = saida[1]
    maxima = saida[2]
    minima = saida[3]
    horas_insolarada = saida[4]
    temperatura_media = saida[5]
    umidade_relativa = saida[6]
    velocidade_vento = saida[7]
    # Variável responsável por receber os dados do arquivo
    dadosEmTupla = (data,  precipitacao, maxima, minima, horas_insolarada,
                    temperatura_media, umidade_relativa, velocidade_vento)
    # Adicionando os dados do arquivo em forma de lista de tupla
    listaTuplaComDados.append((dadosEmTupla))
# Exibindo a lista de tupla com todos os dados do arquivo
print(listaTuplaComDados)

###################################################################################################################################################################################

# b) Visualização de dados de precipitação: a partir de entradas do usuário, a implementação deve permitir a visualização da precipitação que ocorreu em determinado período.
# O usuário informa o mês e ano e o programa exibe a precipitação que ocorreu em cada dia do período informado.

# # Criada uma nova lista na qual serão exibidas as data e as precipitações informadas pelo usuário
visualizacaoDeDadosDePrecipitacao = []
controleDeOpcaoMes = True
controleDeOpcaoAno = True

# Enquanto o usuário não digitar um mês válido, o programa continuará rodando
print('- Critério 2')
while controleDeOpcaoMes:
    mes = int(input('Digite um mês: '))
    # Valida o mês
    if mes >= 1 and mes <= 12:
        controleDeOpcaoMes = False
        # Adicionado outro while para controle de ano, pois sem esse while o usuário teria de digitar o mês novamente. Dessa forma, o mês já fica armazenado e o usuário dará seguimento após
        # digitar um ano válido
        while controleDeOpcaoAno:
            ano = int(input('Digite um ano: '))
            # Valida o ano
            if ano >= 1961 and ano <= 2016:
                controleDeOpcaoAno = False
                # Valida se o mês é entre 1 e 9: adicionada essa validação pois o mês estava chegando sem o zero na esquerda nesta etapa. Se o usuário digitasse "01/2000", retornaria os dados de novembro
                # também, pois 1/XXXX contêm em novembro (1(1)/2000)
                if mes >= 1 and mes <= 9:
                    mesEAno = f'0{mes}/{ano}'
                else:
                    mesEAno = f'{mes}/{ano}'
                # Percorre a lista de tuplas com os dados do arquivo
                for dados in listaTuplaComDados:
                    # Se a posição zero (data) contêm o mês e o ano concatenado
                    if dados[0].__contains__(mesEAno):
                        # Adiciona a data e a precipitação na lista
                        visualizacaoDeDadosDePrecipitacao.append(
                            (dados[0], dados[1]))
                print(visualizacaoDeDadosDePrecipitacao)
            else:
                print('Ano inválido!')
    else:
        print('Mês inválido!')

###################################################################################################################################################################################

# c) Visualização de dados de temperatura: a implementação deve calcular e exibir a visualização da temperatura máxima que ocorreu nos primeiros 7 dias de
# cada mês de um ano informado pelo usuário.

print('- Critério 3')
listaVisualizaTemperatura = []
anoInformadoUsuario = input('Digite um ano: ')
mes = 1
dia = 8
for itens in listaTuplaComDados:
    if itens[0].__contains__(f'0{dia}/{mes}/{anoInformadoUsuario}') or itens[0].__contains__(f'{dia}/{mes}/{anoInformadoUsuario}'):
        dia = dia + 1
        continue
    elif itens[0].__contains__(anoInformadoUsuario):
        dia = 8
        mes = f'{itens[0][-7]}{itens[0][-6]}'
        listaVisualizaTemperatura.append((itens[0], itens[2]))
        continue
print(listaVisualizaTemperatura)
arquivo.close
