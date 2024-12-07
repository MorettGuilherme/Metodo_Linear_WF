# EXPERIMENTO ATLAS - Reconstrução de sinal - Filtro de Wiener (Wiener Filtering - WF) - Estimação da amplitude, fase ou pedestal.
# Autor: Guilherme Barroso Morett.
# Data: 05 de dezembro de 2024.

# Objetivo do código: aplicação do método Filtro de Wiener (Wiener Filtering - WF) para a estimação da amplitude, fase ou pedestal.

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count), a fase de referência (ns) e o ruído eletrônico (ADC Count).
O valor de referência considerado para o pedestal foi de 30 ADC Count.

Funções presentes:

1) Função para a matriz de autocorrelação RS.
Entrada: matriz de pulsos de sinais da etapa de treino janelados.
Saída: matriz RS.

2) Função para o vetor de correlação cruzada p.
Entrada: matriz de pulsos de sinais da etapa de treino janelados e vetor do parâmetro de referência da etapa de treino janelado.
Saída: vetor p.

3) Função do método de Filtro de Wiener.
Entrada: matriz de pulsos de sinais da etapa de treino janelados, matriz de pulsos de sinais da etapa de teste janelados, vetor de parâmetro de referência janelado e vetor de parâmetro de referência da etapa de teste janelado.
Saída: lista do erro de estimação do parâmetro.
"""


import numpy as np
# Importação dos arquivos.
from leitura_dados_ocupacao_WF import *

### ---------------------------------------- 1) FUNÇÃO PARA A MATRIZ DE AUTOCORRELAÇÃO RS ---------------------------------------------------- ###

# Definição da função para o cálculo da matriz de autocorrelação RS.
def matriz_autocorrelacao_RS(Matriz_Pulsos_Sinais_Treino_Janelado):
    
    # A variável n_amostras recebe a quantidade de linhas da matriz Matriz_Pulsos_Sinais_Treino_Janelado.
    n_amostras = Matriz_Pulsos_Sinais_Treino_Janelado.shape[0]
    
    # Cálculo da Matriz_RS.
    Matriz_RS = np.dot(Matriz_Pulsos_Sinais_Treino_Janelado.T, Matriz_Pulsos_Sinais_Treino_Janelado) / n_amostras
    
    # A função retorna Matriz_RS.
    return Matriz_RS

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ----------------------------------------- 2) FUNÇÃO PARA O VETOR DE CORRELAÇÃO CRUZADA p ------------------------------------------------- ###

# Definição da função para o cálculo do vetor de correlação cruzada p.
def vetor_correlacao_cruzada_p(Matriz_Pulsos_Sinais_Treino_Janelado, vetor_parametro_referencia_treino_janelado):
    
    # A variável n_amostras recebe a quantidade de linhas da matriz Matriz_Pulsos_Sinais_Treino_Janelado.
    n_amostras = Matriz_Pulsos_Sinais_Treino_Janelado.shape[0]
    
    # Cálculo do vetor_p.
    vetor_p = np.dot(Matriz_Pulsos_Sinais_Treino_Janelado.T, vetor_parametro_referencia_treino_janelado) / n_amostras
    
    # A função retorna vetor vetor_p.
    return vetor_p

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ---------------------------------------------- 3) FUNÇÃO PARA O MÉTODO WF ---------------------------------------------------------------- ###

# Definição da função do método de Filtro de Wiener.
def metodo_WF(Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_treino_janelado, vetor_parametro_referencia_teste_janelado):
    
    # Garantir que as variáveis sejam do tipo numpy arrays
    Matriz_Pulsos_Sinais_Treino_Janelado = np.asarray(Matriz_Pulsos_Sinais_Treino_Janelado)
    Matriz_Pulsos_Sinais_Teste_Janelado = np.asarray(Matriz_Pulsos_Sinais_Teste_Janelado)
    vetor_parametro_referencia_treino_janelado = np.asarray(vetor_parametro_referencia_treino_janelado)
    vetor_parametro_referencia_teste_janelado = np.asarray(vetor_parametro_referencia_teste_janelado)

    # Adição da coluna unitária na matriz de pulsos de sinais da etapa de treino janelados para funcionar como viés.
    n_linhas_matriz_pulsos_treino_janelado = Matriz_Pulsos_Sinais_Treino_Janelado.shape[0]
    coluna_unitaria = np.ones((n_linhas_matriz_pulsos_treino_janelado, 1))
    Matriz_Pulsos_Sinais_Treino_Janelado_Coluna_Unitaria = np.hstack((Matriz_Pulsos_Sinais_Treino_Janelado, coluna_unitaria))

    # A variável Matriz_Rs recebe o valor de retorno da função matriz_autocorrelacao_Rs.
    Matriz_RS = matriz_autocorrelacao_RS(Matriz_Pulsos_Sinais_Treino_Janelado_Coluna_Unitaria)
    
    # A variável vetor_p recebe o valor de retorno da função vetor_correlacao_cruzada_p.
    vetor_p = vetor_correlacao_cruzada_p(Matriz_Pulsos_Sinais_Treino_Janelado_Coluna_Unitaria, vetor_parametro_referencia_treino_janelado)

    # A variável vetor_pesos_WF recebe a solução do sistema linear que envolve a matriz RS e o vetor p.
    vetor_pesos_WF = np.linalg.solve(Matriz_RS, vetor_p)

    # Separar o viés dos pesos
    vetor_pesos_WF_sem_vies = vetor_pesos_WF[:-1]
    valor_vies_WF = vetor_pesos_WF[-1]

    # Cálculo do parâmetro estimado e do erro de estimação
    estimativas = np.dot(Matriz_Pulsos_Sinais_Teste_Janelado, vetor_pesos_WF_sem_vies) + valor_vies_WF
    lista_erro_estimacao_parametro = vetor_parametro_referencia_teste_janelado - estimativas

    # A varíavel lista_erro_estimacao_parametro é convertida para o tipo lista.
    lista_erro_estimacao_parametro = lista_erro_estimacao_parametro.tolist()

    # A função retorna a variável lista_erro_estimacao_parametro.
    return lista_erro_estimacao_parametro

### ------------------------------------------------------------------------------------------------------------------------------------------ ###