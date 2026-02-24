# Airbnb Rio: Previsor de Preços com Machine Learning
Este projeto utiliza um modelo de Machine Learning para estimar o valor de diárias de imóveis no Rio de Janeiro. O sistema considera variáveis como localização (latitude/longitude), tipo de propriedade, comodidades e políticas de cancelamento.

## Funcionalidades
Interface Interativa: Desenvolvida com Streamlit para facilitar o uso por usuários não técnicos.

Modelo Otimizado: O modelo original foi reduzido de 5GB para ~81MB (Random Forest/Extra Trees), mantendo uma precisão de 80% (R²), permitindo o deploy direto no GitHub.

Previsão em Tempo Real: Cálculo instantâneo baseado nos inputs do usuário.

## Tecnologias Utilizadas
Linguagem: Python 3.11+

Bibliotecas de ML: Scikit-Learn, Pandas, Joblib.

Interface: Streamlit.

Deploy: Streamlit Community Cloud.

## Campos para Preenchimento (Input)
Para obter a previsão da diária, o usuário deve fornecer as seguintes informações na interface:

### Atributos de Localização e Tempo
Latitude e Longitude: Coordenadas exatas do imóvel (podem ser obtidas via Google Maps).

Ano e Mês: Período pretendido para a reserva (ajuda a capturar sazonalidade).

### Características do Imóvel
Capacidade e Estrutura: Quantidade de hóspedes (accommodates), banheiros (bathrooms), quartos (bedrooms) e camas (beds).

Comodidades: Número total de itens oferecidos (n_amenities) e host_listings_count (total de imóveis do anfitrião).

Regras: Noites mínimas para reserva (minimum_nights) e valor por pessoa extra (extra_people).

### Categorias e Preferências
Tipo de Imóvel: Seleção entre Apartamento, Casa, Loft, etc.

Tipo de Quarto: Imóvel inteiro, quarto privativo ou compartilhado.

Perfil do Anfitrião: Se é um Superhost e se permite Reserva Instantânea.

Política de Cancelamento: Escolha entre políticas flexíveis, moderadas ou estritas.

## Estrutura do Repositório
DeployAirbnb.py: Código principal da aplicação Streamlit.

modelo_et_90.pkl: Modelo de Machine Learning treinado e serializado.

requirements.txt: Lista de dependências para o ambiente de produção.

Treinamento_Modelos_Airbnb.ipynb: Jupyter Notebook com a análise exploratória e treinamento.

## Como rodar localmente
Clone o repositório:

```Bash
git clone https://github.com/EnniodosSantos/Projeto-Previsao-Airbnb.git
Instale as dependências:
```

```Bash
pip install -r requirements.txt
Execute o app:
```

```Bash
streamlit run DeployAirbnb.py
```

## Metodologia
O projeto passou por etapas de limpeza de dados, tratamento de outliers, one-hot encoding para variáveis categóricas e seleção de atributos baseada em correlação. O modelo final foi escolhido pelo equilíbrio entre performance e tamanho de armazenamento.
