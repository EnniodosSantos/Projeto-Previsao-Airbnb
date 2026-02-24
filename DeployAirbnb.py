import pandas as pd
import streamlit as st
import joblib

numeros = {'host_listings_count':0, 'latitude':0, 'longitude':0 ,'accommodates':0, 'bathrooms':0, 'bedrooms':0, 'beds':0,
           'extra_people':0, 'minimum_nights':0, 'ano':0, 'mes':0, 'n_amenities':0}

boleanas = {'host_is_superhost':0, 'instant_bookable': 0}

categoricas = {'property_type' : ['Apartment', 'Bed and breakfast',
       'Condominium', 'Guest suite',
       'Guesthouse', 'Hostel',
       'House', 'Loft', 'Others',
       'Serviced apartment'], 'room_type' : ['Entire home/apt',
       'Hotel room', 'Private room',
       'Shared room'], 'bed_type' : ['Others', 'Real Bed'], 'cancellation' : ['policy_Strict','policy_flexible',
       'policy_moderate','policy_strict_14_with_grace_period']}

for item in numeros:
    if item == "latitude" or item == "longitude":
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format ="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}',step=1, value=0)
    numeros[item] = valor

for item in boleanas:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == "Sim":
        boleanas[item] = 1
    else:
        boleanas[item] = 0

for item in categoricas:
    valor = st.selectbox(f'{item}', categoricas[item])

botao = st.button('Prever Valor do Imóvel')
