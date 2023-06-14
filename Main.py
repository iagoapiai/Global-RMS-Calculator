import csv
import locale
import math

linha = 1

 #Função para ler o arquivo CSV por linha!
# def ler_csv(nome_arquivo):
#    with open(nome_arquivo, 'r') as arquivo:
#        linhas = arquivo.read().splitlines()
#        if len(linhas) > 2:
#            linha_csv = linha - 1
#            valores_linha_1 = linhas[linha_csv].split(';')
#            return valores_linha_1
#        else:
#            print("=== O CÓDIGO VERIFICOU QUE NÃO HÁ ESSE TANTO DE LINHAS NO ARQUIVO ===")

# Função para ler o arquivo CSV por coluna!
def ler_csv(nome_arquivo):
    coluna1 = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        for linha in leitor:
            coluna1.append(linha[0])
    return coluna1[1:]  # exclui o cabeçalho da coluna

# locale.setlocale(locale.LC_ALL, '')

nome_arquivo = '3.csv'
espectro_coluna1 = ler_csv(nome_arquivo)

espectro_coluna1 = [locale.atof(valor.replace(',', '.')) for valor in espectro_coluna1]

amplitudes = espectro_coluna1

# faz todos os valores elevado ao quadrado
soma_quadrados = sum([amp**2 for amp in amplitudes]) 

# depois faz a raiz quadrada da soma de todos os valores
valor_global_rms = math.sqrt(soma_quadrados)

# faz o valor do cálculo - 18,4% (Para bater com a skf)
#valor_global_rms -= valor_global_rms * 0.184

# print do valor formatado com 3 casas decimais
print("============================")
print("== Valor Somado: {:.3f} g ==".format(soma_quadrados))
print("============================")
print("= Valor global RMS: {:.3f}g = ".format(valor_global_rms))
print("============================")
