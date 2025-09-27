# Projeto de Classificação de Avaliações do E-Commerce - Desafio Bravium

Este repositório contém a resolução do desafio técnico para o processo seletivo de estágio, focado em desenvolver um modelo de Machine Learning para classificar reviews de produtos como "Positivas" ou "Negativas".

## Sobre o Projeto

O objetivo principal foi construir um classificador de texto utilizando um dataset público de reviews de um e-commerce brasileiro. O projeto abrange desde a análise exploratória e pré-processamento dos dados até o treinamento, avaliação e interpretação de um modelo de Regressão Logística.

## Tecnologias Utilizadas

- Python 3
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Como Executar

Siga os passos abaixo para configurar o ambiente e reproduzir os resultados.

1.  **Clone o Repositório**
    ```
    git clone https://github.com/HigorMauricio/DesafioBravium-ML-Classificacao.git
    cd DesafioBravium-ML-Classificacao
    ```

2.  **Instale as Dependências**
    É recomendado criar um ambiente virtual. As bibliotecas necessárias podem ser instaladas via `pip`:
    ```
    pip install pandas scikit-learn matplotlib seaborn jupyter
    ```

3.  **Obtenha os Dados**
    O dataset utilizado é público e pode ser baixado do Kaggle.
    - **Link para Download:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
    - Após o download, crie a estrutura de pastas `data/raw/` e coloque o arquivo `olist_order_reviews_dataset.csv` dentro dela.

4.  **Execute os Notebooks**
    Os notebooks devem ser executados na seguinte ordem:
    1.  `notebooks/preProcessamento.ipynb`: Para limpeza dos dados e criação das features.
    2.  `notebooks/modelo.ipynb`: Para treinamento, avaliação e interpretação do modelo.

## Resultados

O modelo de Regressão Logística treinado alcançou uma **acurácia geral de 92%** no conjunto de teste. Uma análise mais detalhada da performance é apresentada no notebook modelo.ipynb.

A análise do relatório mostra que o modelo é extremamente eficaz em identificar reviews positivas (Recall de 99%). Para as reviews negativas, o modelo é bastante preciso quando faz uma classificação (Precisão de 90%), mas ainda deixa de identificar 38% das críticas reais (Recall de 62%), um comportamento comum em datasets desbalanceados.

## Fatores de Decisão do Modelo

Para atender ao requisito bônus, os coeficientes do modelo foram extraídos para identificar as palavras com maior influência nas previsões. Abaixo estão as 10 palavras mais associadas a cada sentimento:

**(Aqui você pode colocar uma imagem com a sua tabela de palavras ou colá-la como texto)**

**Top 5 Palavras Positivas:**
1. ótimo
2. excelente
3. lindo
4. rápida
5. testei

**Top 5 Palavras Negativas:**
1. insatisfeita
2. inferior
3. má
4. passou
5. pessimo

## Conclusão

O projeto resultou em um modelo robusto e com alta acurácia. A análise aprofundada revelou um bom desempenho geral, com uma clara oportunidade de melhoria no reconhecimento de reviews negativas, com o desbalanceamento dos dados.