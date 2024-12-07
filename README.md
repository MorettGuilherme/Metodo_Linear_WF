O método do Filtro de Wiener (Wiener Filtering - WF) estima os parâmetros da amplitude, fase ou pedestal, por meio da estatística do conjunto de dados de pulsos de sinais e também dos dados simulados para o parâmetro de referência, por meio do cálculo da matriz de autocorrelação e do vetor de correção cruzada dos pulsos de sinais. Ele não emprega em sua composição a função pulso de referência nem os dados de ruídos. Os resultados foram bem satisfatórios, principalmente para a fase.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_WF_amplitude_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da amplitude.

2. Dados_Estatisticos_WF_fase_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase.
  
3. Dados_Estatisticos_WF_pedestal_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação do pedestal.

4. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído eletrônico computados a cada 25 ns.
  
5. K_Fold_amplitude_DP_Dados_Estatisticos_WF_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

6. K_Fold_amplitude_DP_Desempenho_WF_OC
  * Essa pasta contém um arquivo com os dados da análise estatística do desvio padrão do erro de estimação da amplitude para o janelamento ideal 13 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

7. K_Fold_amplitude_EME_Desempenho_WF_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da amplitude para o janelamento ideal 13 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

8. K_Fold_amplitude_MAE_Desempenho_WF_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da amplitude para o janelamento ideal 13 calculados pela técnica de validação cruzada K-Fold.

9. K_Fold_amplitude_media_Dados_Estatisticos_WF_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

10. K_Fold_amplitude_MSE_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da amplitude para o janelamento ideal 13 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

11. K_Fold_amplitude_SNR_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da amplitude para o janelamento ideal 13 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

12. K_Fold_amplitude_var_Dados_Estatisticos_WF_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

13. K_Fold_fase_DP_Dados_Estatisticos_WF_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

14. K_Fold_fase_DP_Desempenho_WF_OC
  * Essa pasta contém um arquivo dos dados estatísticos para cada ocupação do desvio padrão para o erro de estimação da fase para o janelamento ideal 7.

15. K_Fold_fase_EME_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

16. K_Fold_fase_MAE_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

17. K_Fold_fase_media_Dados_Estatisticos_WF_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase pela amplitude estimada calculados pela técnica de validação cruzada K-Fold.

18. K_Fold_fase_MSE_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

19. K_Fold_fase_SNR_Desempenho_WF_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da fase pela amplitude estimada para o janelamento ideal 7 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

20. K_Fold_fase_var_Dados_Estatisticos_WF_OC
   * Essa pasta contém arquivos para cada uma das ocupações dos dados estatísticos da variância do erro de estimação da fase.

21. K_Fold_pedestal_DP_Dados_Estatisticos_WF_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

22. K_Fold_pedestal_DP_Desempenho_WF_OC
   * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

23. K_Fold_pedestal_EME_Desempenho_WF_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

24. K_Fold_pedestal_MAE_Desempenho_WF_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

25.  K_Fold_pedestal_media_Dados_Estatisticos_WF_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

26. K_Fold_pedestal_MSE_Desempenho_WF_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

27. K_Fold_pedestal_SNR_Desempenho_WF_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

28. K_Fold_pedestal_var_Dados_Estatisticos_WF_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

29. Resultados_WF_Amplitude
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

30. Resultados_WF_Fase
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela amplitude estimada pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.
   
31. Resultados_WF_Pedestal
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação do pedestal pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

32. arquivo_saida_dados_estatisticos_WF.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método Wiener Filtering (WF).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.

33. arquivo_saida_desempenho_WF.py
   * Instrução para salvar em arquivos os dados estatísticos do desempenho do método WF.
   * Função para o cálculo do desempenho do método WF pelo Erro Médio de Estimação (EME).
   * Função para o cálculo do desempenho do método WF pelo Erro Médio Quadrático (Mean Squared Error - MSE).
   * Função para o cálculo do desempenho do método WF pelo Erro Médio Absoluto (Mean Absolute Error - MAE).
   * Função para o cálculo do desempenho do método WF pela Relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
   * Função para o cálculo do desempenho do método WF pelo desvio padrão (DP).
   * Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método WF.
   * Instrução principal do código.

34. arquivo_saida_k_fold_WF.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.
   
35. grafico_dado_estatistico_janelamento_WF.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

36. grafico_desempenho_WF.py
   * Função para a leitura dos dados do desempenho do método BLUE 1 de todas as ocupações para o janelamento ideal.
   * Instrução para o plote do gráfico do desempenho do método BLUE 1 ao longo das ocupações para o janelamento ideal.
   * Instrução principal do código.

37. grafico_k_fold_WF.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal do código.
   
38. histograma_erro_parametro_WF.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo A do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo B do erro de estimação da amplitude, fase ou pedestal.
   * Instrução principal do código.
   
39. leitura_dados_ocupacao_WF.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

40. metodo_WF.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para o método WF.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a matriz de covariância foram os mesmos que para os pulsos de sinais.

Obs.: antes da aplicação do método, o valor constante do pedestal foi retirado dos dados referentes aos pulsos de sinais.
O vetor da fase de referência foi multiplicado por 0,5; pois esse valor representa a resolução da fase.
