import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

umidade = np.random.uniform(20, 80, n)
ph = np.random.uniform(4.5, 7.5, n)
irrigacao = np.random.uniform(0, 30, n)
fertilizante = np.random.uniform(0, 200, n)

produtividade = (
    10 * (umidade / 100) +
    5 * (7 - abs(ph - 6)) +
    0.2 * irrigacao +
    0.05 * fertilizante +
    np.random.normal(0, 2, n)
)

df = pd.DataFrame({
    "umidade": umidade,
    "ph": ph,
    "irrigacao": irrigacao,
    "fertilizante": fertilizante,
    "produtividade": produtividade
})

df.to_csv("dados_agricolas.csv", index=False)

print("CSV criado com sucesso!")
