import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ==============================
# 1. Carregar dados
# ==============================
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados_agricolas.csv")

# ==============================
# 2. Treinar modelo
# ==============================
@st.cache_resource
def treinar_modelo(df):
    X = df[["umidade", "ph", "irrigacao", "fertilizante"]]
    y = df["produtividade"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    metricas = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R²": r2_score(y_test, y_pred)
    }

    return modelo, metricas, X_test, y_test, y_pred

# ==============================
# 3. Regras simples
# ==============================
def sugerir_acoes(umidade, ph, irrigacao, fertilizante, prod_prev):
    rec = []

    if umidade < 40:
        rec.append("- Umidade baixa: aumentar irrigação em 20–30%.")
    elif umidade > 70:
        rec.append("- Umidade alta: reduzir irrigação.")

    if ph < 5.5:
        rec.append("- pH baixo: aplicar calcário.")
    elif ph > 7.0:
        rec.append("- pH alto: usar gesso agrícola.")

    if prod_prev < 50:
        rec.append("- Produtividade baixa: reforçar adubação.")
    elif prod_prev > 80:
        rec.append("- Produtividade alta: manter manejo atual.")

    if not rec:
        rec.append("- Condições estáveis: manter plano atual.")

    return rec

# ==============================
# 4. Dashboard
# ==============================
st.title("🌱 Assistente Agrícola Inteligente")

df = carregar_dados()
modelo, metricas, X_test, y_test, y_pred = treinar_modelo(df)

tab1, tab2, tab3 = st.tabs(["📊 Dados", "📈 Métricas", "🤖 Previsão"])

with tab1:
    st.subheader("Visualização dos Dados")
    st.dataframe(df.head())
    st.write(df.describe())

with tab2:
    st.subheader("Métricas do Modelo")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MAE", f"{metricas['MAE']:.2f}")
    col2.metric("MSE", f"{metricas['MSE']:.2f}")
    col3.metric("RMSE", f"{metricas['RMSE']:.2f}")
    col4.metric("R²", f"{metricas['R²']:.2f}")

    st.subheader("Matriz de Correlação")
    corr = df.corr(numeric_only=True)
    fig_corr, ax_corr = plt.subplots()
    cax = ax_corr.matshow(corr)
    fig_corr.colorbar(cax)
    ax_corr.set_xticks(range(len(corr.columns)))
    ax_corr.set_yticks(range(len(corr.columns)))
    ax_corr.set_xticklabels(corr.columns, rotation=90)
    ax_corr.set_yticklabels(corr.columns)
    st.pyplot(fig_corr)

    st.subheader("Real vs Previsto")
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    st.pyplot(fig)


with tab3:
    st.subheader("Simulação de Cenário")

    u = st.slider("Umidade (%)", 10, 90, 50)
    ph = st.slider("pH", 4.0, 8.0, 6.0)
    irr = st.slider("Irrigação (mm)", 0, 50, 10)
    fert = st.slider("Fertilizante (kg/ha)", 0, 300, 100)

    if st.button("Calcular Produtividade"):
        novo = pd.DataFrame([{
            "umidade": u,
            "ph": ph,
            "irrigacao": irr,
            "fertilizante": fert
        }])

        prod_prev = modelo.predict(novo)[0]
        st.success(f"Produtividade prevista: {prod_prev:.2f}")

        st.subheader("Recomendações:")
        for r in sugerir_acoes(u, ph, irr, fert, prod_prev):
            st.write(r)
