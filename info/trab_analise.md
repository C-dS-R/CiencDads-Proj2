# Projeto 2 - Machine Learning


## Introdução
Você deve:
+ Propor 2 problemas de ML:
   + Um de aprendizado **supervisionado**
   + Outro de aprendizado **não supervisionado**.
+ Implementa-los
+ Justifica-los

+ Explorando as variáveis disponíveis
+ Tratando dados de forma adequada
+ Selecionando as features
+ Avaliando os modelos treinados


## Dataset
+ "Brazilian E-Commerce Public Dataset" por Olist
   + Aprox. 100mil pedidos (2016-2018)
+ Informações:
   + Pedidos
   + Pagamentos
   + Entregas
   + Avaliações de clientes
   + Produtos
   + Vendedores
   + Localização
🔗 Link: Brazilian E-Commerce Public Dataset by Olist

### Notebook base
Contem:
+ Download/extração do dataset
+ Leitura dos .csv
+ Análise exploratória básica de todas as tabelas
+ Visualizações com matplotlib e seaborn

Ele serve como ponto de partida para:
   + entender a estrutura dos dados
   + iniciar a construção dos modelos
🔗: Notebook Inicial no Colab


## 3. Estrutura do Projeto

Etapas do projeto:
**1. Exploração Inicial dos Dados**
   + Análise exploratória
      + com visualizações e estatísticas descritivas.
   + Limpeza de dados
      + E tratamento de:
         + Valores ausentes
         + Inconsistências

**2. Problemas de ML**
   + Definição de dois problemas:
      + Um de aprendizado supervisionado
         + classificação ou
         + regressão
      + Um de aprendizado não supervisionado
         + clustering ou
         + detecção de anomalias
   + Definição clara do objetivo de cada modelo.
   + Justificativa pra escolha das features
      + (e, pro supervisionado, do target.)

**3. Modelagem**
   + Min 3 algoritmos pra cada abordagem.
   + Um deles (o baseline) tem que ser:
      + Pra regressão: Regressão Linear
      + Pra classificação: Regressão Logística

   + Usar redução de dimensionalidade em algum prob
      + pode ser para:
         + pré-modelagem
         + ou visualização
      + (ex: PCA, t-SNE, UMAP).

**4. Avaliação dos modelos**
   + Pra regressão: min 3 métricas
      + incluindo R²
   + Pra classificação: use:
      + Acurácia
      + Precisão
      + Recall
      + F1-score
      + Matriz de confusão.
   
   + Apresentar:
      + curva de aprendizado dos modelos
      + análise de desempenho dos modelos
   
   + Explicação sobre overfitting e underfitting (com base nos resultados)


## 4. Entregas

2 entregas (ambas pelo AVA):

### Vídeo Explicativo

+ Max **10 minutos** (com penalização se passar!)
   + Por o link no campo de texto da atividade no AVA.
      + Pode estar no
         + YouTube (não listado)
         + Drive

+ No vídeo, deve apresentar:
   + Os 2 problemas (de classificação/regressão e o de clusterização).
   + A justificativa pra escolha das variáveis (features e target).
   + As decisões de modelagem e interpretação dos resultados.
   + Explicações sobre overfitting/underfitting, avaliação dos modelos e visualizações relevantes.

### Notebook da equipe

+ O arquivo do notebook (.ipynb) deverá ser enviado diretamente na tarefa do AVA (upload do arquivo).
+ O notebook deve conter:
   + Todo o código executado no projeto
   + Comentários explicativos
   + Visualizações e análise exploratória
   + Modelagem supervisionada e não supervisionada
   + Avaliação dos modelos com as métricas obrigatórias
   + Aplicação da técnica de redução de dimensionalidade
```

## 5. Avaliação (0 a 10 pontos)

Critérios:
+ Definição e justificativa dos problemas (supervisionado e não sup.)
+ Escolha e justificativa das features e do target
+ Qualidade do pré-processamento e limpeza dos dados
+ Aplicação de pelo menos 3 algoritmos por abordagem
+ Aplicação de técnica de redução de dimensionalidade
+ Avaliação dos modelos com métricas obrigatórias e curva de aprendizado
+ Análise crítica (overfitting, underfitting, desempenho comparado)
+ Clareza e objetividade na apresentação em vídeo


## 6. Sugestões de Problemas

+ Considerar, preferencialmente, situações:
   + reais
   + úteis para a empresa Olist/seus fornecedores/seus clientes
   + tipo, estrategias para:
      + melhorar o atendimento ao cliente,
      + Otimizar a logística
      + Compreender melhor o comportamento dos consumidores

Formule os problemas de forma justificavel

Sugestões:
+ **Supervisionado:**
   + Prever a nota de avaliação (_review_score_) com base em:
      + dados do pedido
      + produto
      + pagamento
   + Prever se um pedido será entregue no prazo com base em suas características logísticas.
   + Estimar o valor total pago em um pedido.
   + Classificar um pedido como:
      + potencialmente problemático ou não
   + com base nas:
      + características
      + avaliações anteriores.
+ **Não Supervisionado:**
   + Agrupar clientes por comportamento de compra
      + (valores, categorias, frequência).
   + Clusterizar produtos por características como:
      + categoria, preço e dimensões.
   + Identificar regiões com comportamentos de compra semelhantes com base na geolocalização.