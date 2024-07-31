import streamlit as st

st.title("Meu primeiro Deploy")

slider = st.slider("Selecione o ano: ", min_value=1995, max_value=2014)
st.write(f'O ano selecionado foi: {slider}')

st.select_slider("Selecione um ano: ", options=[1995, 1996, 1997,1998,1999,2000])