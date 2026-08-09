import streamlit as st
import pandas as pd
import plotly.express as px

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv') 

# Criar o cabeçalho
st.header('Análise de Vendas de Veículos')

# Criar o botão do histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)



    exit()