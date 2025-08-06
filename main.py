import streamlit as st
import pandas as pd
import plotly_express as px

# Título do dashboard
st.title('Meu primeiro Dashboard com Streamlit')

# Carregando os dados (você pode substituir pelo seu próprio arquivo)
# Exemplo: df = pd.read_csv('seu_arquivo.csv')
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

# Exibindo o DataFrame
st.write("Aqui estão os seus dados:")
st.dataframe(df)

# Criando um gráfico de barras interativo com Plotly Express
fig = px.bar(df, x='col1', y='col2', title='Gráfico de Barras')
st.plotly_chart(fig)