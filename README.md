# Projeto: Análise de Séries Temporais, Mineração de Texto e Web Scraping

Repositório contendo três atividades desenvolvidas para a disciplina de Análise de Séries Temporais, Mineração de Texto e Web Scraping.

## Estrutura do Repositório

```text
analise-series-mineracao-webscraping/
├── exercicio1-arima-sarima/     # Código e notebooks ARIMA/SARIMA
│   ├── data/                    # Datasets de séries temporais
│   ├── notebooks/               # Jupyter Notebooks da análise
│   └── scripts/                 # Scripts Python de modelagem
├── exercicio2-text-mining/      # Mineração de Texto
│   ├── data/                    # comments_dataset_pt_improved.csv
│   ├── notebooks/               # Notebooks com as 8 técnicas
│   │   └── second_exercicio_final_v3.ipynb
│   ├── scripts/                 # second_exercicio_improved.py
│   └── second_exercicio_improved.zip
└── exercicio3-webscraping/      # Web Scraping
    ├── scripts/                 # tabuaMare.py, teste2.py
    ├── notebooks/               # questao3_webscraping.ipynb
    └── questao3_package.zip
```

## Exercício 1 – ARIMA e SARIMA

**Local:** `exercicio1-arima-sarima/`

1. **Dataset**: coleções de séries do Banco Central em `data/`.
2. **Análise**: notebooks em `notebooks/`, com:
   - Teste de estacionaridade (ADF)
   - Identificação de parâmetros via ACF/PACF
   - Ajuste de modelos ARIMA e SARIMA
   - Comparação de métricas (AIC, BIC, RMSE)
   - Previsões com intervalos de confiança
3. **Scripts**: exemplos de uso em `scripts/`.

## Exercício 2 – Mineração de Texto

**Local:** `exercicio2-text-mining/`

1. **Dataset**: `data/comments_dataset_pt_improved.csv` (500 comentários em português de Instagram, Facebook e X).
2. **Notebook**: `notebooks/second_exercicio_final_v3.ipynb` com as 8 técnicas:
   - Keyword Analysis
   - TF-IDF
   - Sentiment Analysis
   - Topic Modeling (LDA)
   - Named Entity Recognition (RegEx)
   - Qualitative Coding
   - Text Similarity (cosine)
   - Visualizations (bar chart e wordcloud)
3. **Scripts**: `scripts/second_exercicio_improved.py` executável via terminal.
4. **Pacote**: `second_exercicio_improved.zip` pronto para entrega.

## Exercício 3 – Web Scraping

**Local:** `exercicio3-webscraping/`

1. **Scripts**: `scripts/tabuaMare.py` (tábua de marés) e `scripts/teste2.py` (sol e lua) usando Selenium.
2. **Notebook**: `notebooks/questao3_webscraping.ipynb` que integra scraping e conversão para CSV:
   - `tabua_mare_25.csv`
   - `resultado_teste2.csv`
3. **Pacote**: `questao3_package.zip` com scripts, notebook e `requirements.txt`.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/gustavojose136/analise-series-mineracao-webscraping.git
   cd analise-series-mineracao-webscraping
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Para cada exercício, instale dependências e execute:
   - **Exercício 1**:
     ```bash
     cd exercicio1-arima-sarima
     pip install -r scripts/requirements.txt
     jupyter notebook notebooks
     ```
   - **Exercício 2**:
     ```bash
     cd ../exercicio2-text-mining
     pip install -r requirements.txt
     jupyter notebook notebooks/second_exercicio_final_v3.ipynb
     ```
   - **Exercício 3**:
     ```bash
     cd ../exercicio3-webscraping
     pip install -r requirements.txt
     jupyter notebook notebooks/questao3_webscraping.ipynb
     ```

## Contribuições

1. Faça um fork do repositório.
2. Crie uma branch (`git checkout -b feature/nome-da-feature`).
3. Faça suas alterações e commits.
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Consulte `LICENSE` para detalhes.

---

**Autor**: Gustavo José Rosa\
**Data**: 2025-07-02

