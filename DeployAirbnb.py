import pandas as pd
import streamlit as st
import joblib

# Configuração da página (opcional, mas recomendado para portfólio)
st.set_page_config(page_title="Ennio Previsor de Preços", layout="centered")

# Título Principal
st.title("Previsor de Preços Airbnb Rio")

# Subtítulo ou Descrição Curta
st.markdown("""
    ### Estimativa de Preços de Diárias no Rio de Janeiro
    Utilize este modelo de Machine Learning para prever o valor de aluguel baseado em características do imóvel.
""")

st.divider() # Linha visual para separar o cabeçalho dos inputs

numeros = {'host_listings_count':0, 'latitude':0, 'longitude':0 ,'accommodates':0, 'bathrooms':0, 'bedrooms':0, 'beds':0,
           'extra_people':0, 'minimum_nights':0, 'ano':0, 'mes':0, 'n_amenities':0}

boleanas = {'host_is_superhost':0, 'instant_bookable': 0}

categoricas = {
    'property_type' : ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment'],
    'room_type' : ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
    'bed_type' : ['Others', 'Real Bed'],
    'cancellation' : ['policy_Strict','policy_flexible', 'policy_moderate','policy_strict_14_with_grace_period']
}

# 1. Criação dos Inputs
for item in numeros:
    if item in ["latitude", "longitude"]:
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    numeros[item] = valor

for item in boleanas:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    boleanas[item] = 1 if valor == "Sim" else 0

# 2. Tratamento de Categóricas (Onde estava o erro)
dicionario_cat = {}
for item in categoricas:
    selecionado = st.selectbox(f'{item}', categoricas[item])
    for valor in categoricas[item]:
        # Define 1 para a opção escolhida, 0 para as outras (One-Hot Encoding manual)
        dicionario_cat[f'{item}_{valor}'] = 1 if valor == selecionado else 0

botao = st.button('Prever Valor do Imóvel')

if botao:
    # 3. Unificar todos os dados
    dados_input = {}
    dados_input.update(numeros)
    dados_input.update(boleanas)
    dados_input.update(dicionario_cat)

    modelo = joblib.load('modelo_et.pkl')
    # 4. Criar DataFrame e Reordenar
    valores_x = pd.DataFrame(dados_input, index=[0])
    colunas_modelo = modelo.feature_names_in_
    valores_x = valores_x[colunas_modelo]

    # 5. Predição
    preco = modelo.predict(valores_x)
    st.success(f"O valor estimado da diária é: R$ {preco[0]:,.2f}")
