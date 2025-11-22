# 🌱 Assistente Agrícola Inteligente - FarmTech Solutions

O objetivo é construir um **protótipo de Assistente Agrícola Inteligente** que utiliza **regressão com Scikit-Learn** integrada a um **dashboard interativo em Streamlit** para apoiar decisões de manejo no campo.

---

## 🎥 Vídeo 

👉 https://youtu.be/dh6E4X11Tak
---

## 🎯 Objetivos Atendidos

- Modelar um banco de dados simples com dados agrícolas (umidade, pH, irrigação, fertilizante, produtividade).
- Treinar um modelo de **regressão linear múltipla** com Scikit-Learn.
- Calcular e exibir métricas de desempenho:
  - MAE
  - MSE
  - RMSE
  - R²
- Exibir **gráficos e correlações**, incluindo:
  - Matriz de correlação entre variáveis
  - Gráfico de produtividade real vs prevista
- Implementar um **dashboard em Streamlit** com:
  - Visualização dos dados e estatísticas descritivas
  - Métricas e gráficos do modelo
  - Simulação interativa de cenários
- Sugerir **ações de manejo agrícola**, como:
  - Aumentar ou reduzir irrigação
  - Corrigir pH do solo
  - Ajustar adubação
  - Manter o manejo atual em condições estáveis

---

## 🧠 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib

---

## 📂 Estrutura do Projeto

```text
FarmTech_ML_Streamlit/
├── app.py               # Código principal do dashboard Streamlit
├── gerar_csv.py         # Script para gerar a base de dados simulada
├── dados_agricolas.csv  # Base de dados simulada (umidade, pH, irrigação, etc.)
└── README.md            # Documentação do projeto
