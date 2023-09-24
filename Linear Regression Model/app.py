import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('homeprices_2.csv')
x = df[['area', 'age', 'bedrooms']]
y = df['price']
model = linear_model.LinearRegression()
model.fit(x, y)

st.set_page_config(
    page_title='Home Price Prediction',
    page_icon='🏠',
    layout='wide'
)

# Change the sidebar background color to #4D2DB7
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #4D2DB7 !important;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Home Price Prediction App')

st.sidebar.header('User Input')
area = st.sidebar.number_input('Area (in sq. ft.)', value=1000, step=100)
age = st.sidebar.number_input('Age (in years)', value=10, step=1)
bedrooms = st.sidebar.number_input('Bedrooms', value=2, step=1)

if st.sidebar.button('Predict'):
    result = model.predict([[area, age, bedrooms]])
    st.success(f'The predicted price is: ${result[0]:,.2f}')

fig, axs = plt.subplots(1, 3, figsize=(16, 5))

axs[0].plot(df['area'], df['price'], marker='o', color='red')
axs[0].set_title('Area Vs Price')
axs[0].set_xlabel('Area (sq. ft.)')
axs[0].set_ylabel('Price ($)')
axs[0].grid(True)

axs[1].plot(df['age'], df['price'], marker='o', color='blue')
axs[1].set_title('Age Vs Price')
axs[1].set_xlabel('Age (years)')
axs[1].set_ylabel('Price ($)')
axs[1].grid(True)

axs[2].plot(df['bedrooms'], df['price'], marker='o', color='green')
axs[2].set_title('Bedrooms Vs Price')
axs[2].set_xlabel('Bedrooms')
axs[2].set_ylabel('Price ($)')
axs[2].grid(True)

st.header('Visualizations')
st.pyplot(fig)
