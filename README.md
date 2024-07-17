A primeira versão do método Melhor Estimador Linear Não Enviesado (BEst Linear Blue Estimador - BLUE 1) tem o objetivo de encontrar um vetor de parâmetros estimados, cujos componentes são respectivamente: amplitude, amplitude vezes a fase e pedestal.
Nesse repositório, o algoritmo foi desenvolvido para o cálculo individual do erro de estimação desses parâmetros pela técnica de validação cruzada K-Fold.
Comentários sobre os resultados: de acordo com a análise estatística notou-se que não há um janelamento ideal para amplitude visto que o desvio padrão não se estabiliza para um certo valor de janelamento adotado. 
Ademais para a fase, os resultados não foram satisfatórios, devido ao fato da dispersão dos dados em relação a média serem elevados. Portanto, novas estrátegias para o cálculo da fase devem ser avaliadas.
Obs.: nesse algoritmo, a fase estimada é calculada pela divisão entre o termo da amplitude versus a fase dividida pela amplitude estimada.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_BLUE1_amplitude_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da amplitude.

2. Dados_Estatisticos_BLUE1_fase_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase.
  
3. Dados_Estatisticos_BLUE1_pedestal_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação do pedestal.
  
4. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído computados a cada 25 ns (período de colisões das partículas atômicas no LHC).
  
5. K_Fold_amplitude_DP_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

6. K_Fold_amplitude_DP_Desempenho_BLUE1_OC
  * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

7. K_Fold_amplitude_EME_Desempenho_BLUE1_OC
  * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

8. K_Fold_amplitude_MAE_Desempenho_BLUE1_OC
  * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

9. K_Fold_amplitude_media_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

10. K_Fold_amplitude_MSE_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

11. K_Fold_amplitude_SNR_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

12. K_Fold_amplitude_var_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

13. K_Fold_fase_DP_Dados_Estatisticos_BLUE1_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

14. K_Fold_fase_DP_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

15. K_Fold_fase_EME_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

16. K_Fold_fase_MAE_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

17. K_Fold_fase_media_Dados_Estatisticos_BLUE1_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

18. K_Fold_fase_MSE_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

19. K_Fold_fase_SNR_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

20. K_Fold_fase_var_Dados_Estatisticos_BLUE1_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase calculados pela técnica de validação cruzada K-Fold.

21. K_Fold_pedestal_DP_Dados_Estatisticos_BLUE1_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

22. K_Fold_pedestal_DP_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

23. K_Fold_pedestal_EME_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

24. K_Fold_pedestal_MAE_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

25.  K_Fold_pedestal_media_Dados_Estatisticos_BLUE1_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

26. K_Fold_pedestal_MSE_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

27. K_Fold_pedestal_SNR_Desempenho_BLUE1_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

28. K_Fold_pedestal_var_Dados_Estatisticos_BLUE1_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

29. Resultados_BLUE1_Amplitude
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

30. Resultados_BLUE1_Fase
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.
   
31. Resultados_BLUE1_Pedestal
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação do pedestal pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.
   
32. arquivo_saida_dados_estatisticos_BLUE1.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método Best Linear Unbiased Estimator (BLUE 1).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.

33. arquivo_saida_desempenho_BLUE1.py
   * Instrução para salvar em arquivos os dados estatísticos do desempenho do método BLUE 1.
   * Função para o cálculo do desempenho do método BLUE 1 pelo Erro Médio de Estimação (EME).
   * Função para o cálculo do desempenho do método BLUE 1 pelo Erro Médio Quadrático (Mean Squared Error - MSE).
   * Função para o cálculo do desempenho do método BLUE 1 pelo Erro Médio Absoluto (Mean Absolute Error - MAE).
   * Função para o cálculo do desempenho do método BLUE 1 pela Relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
   * Função para o cálculo do desempenho do método BLUE 1 pelo desvio padrão (DP).
   * Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método BLUE 1.
   * Instrução principal do código.

34. arquivo_saida_k_fold_BLUE1.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.
   
35. grafico_dado_estatistico_janelamento_BLUE1.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

36. grafico_desempenho_BLUE1.py
   * Função para a leitura dos dados do desempenho do método BLUE 1 de todas as ocupações para o janelamento ideal.
   * Instrução para o plote do gráfico do desempenho do método BLUE 1 ao longo das ocupações para o janelamento ideal.
   * Instrução principal do código.

37. grafico_k_fold_BLUE1.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
   
38. histograma_erro_parametro_BLUE1.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Função para o plote do histograma do erro de estimação da amplitude, fase ou pedestal.
   * Função principal.
   
39. leitura_dados_ocupacao_BLUE1.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

40. leitura_dados_ruidos_BLUE1.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância.
   * Função para a construção da matriz de covariância como identidade.

41. metodo_BLUE1.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para o método BLUE 1.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a matriz de covariância foram os mesmos que para os pulsos de sinais.

Obs.: antes da aplicação do método, o valor constante do pedestal foi retirado dos dados referentes aos pulsos de sinais.
