import pandas as pd
import streamlit as st
import joblib

# 1. Carregamento com Cache (Evita lentidão no botão)
@st.cache_resource
def load_model():
    return joblib.load('modelo_et_90.pkl')

st.set_page_config(page_title="Ennio Previsor de Preços", layout="centered")

st.title("Previsor de Preços Airbnb Rio")
st.markdown("""
### Estimativa de Preços de Diárias no Rio de Janeiro
Utilize este modelo de Machine Learning para prever o valor de aluguel baseado em características do imóvel.

#### Projeto de Ennio dos Santos
[Visite meu portfólio aqui](https://enniodossantos.github.io/)
""")
st.divider()

# Dicionários de estrutura
numeros = {'host_listings_count':0, 'latitude':0, 'longitude':0 ,'accommodates':0, 'bathrooms':0, 'bedrooms':0, 'beds':0,'extra_people':0, 'minimum_nights':0, 'ano':0, 'mes':0, 'n_amenities':0}
boleanas = {'host_is_superhost':0, 'instant_bookable': 0}
categoricas = {
    'property_type' : ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment'],
    'room_type' : ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
    'bed_type' : ['Others', 'Real Bed'],
    'cancellation' : ['policy_Strict','policy_flexible', 'policy_moderate','policy_strict_14_with_grace_period']
}

# 2. Criação dos Inputs (Corrigido para salvar todos os valores)
for item in numeros:
    if item in ["latitude", "longitude"]:
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    numeros[item] = valor # Movido para fora para capturar latitude/longitude

for item in boleanas:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    boleanas[item] = 1 if valor == "Sim" else 0

dicionario_cat = {}
for item in categoricas:
    selecionado = st.selectbox(f'{item}', categoricas[item])
    for valor in categoricas[item]:
        dicionario_cat[f'{item}_{valor}'] = 1 if valor == selecionado else 0

# 3. Lógica de Predição
if st.button('Prever Valor do Imóvel'):
    modelo = load_model()

    dados_input = {}
    dados_input.update(numeros)
    dados_input.update(boleanas)
    dados_input.update(dicionario_cat)

    valores_x = pd.DataFrame(dados_input, index=[0])

    # Reordenar colunas conforme treinamento
    colunas_modelo = modelo.feature_names_in_
    valores_x = valores_x[colunas_modelo]

    preco = modelo.predict(valores_x)
    st.success(f"O valor estimado da diária é: R$ {preco[0]:,.2f}")
