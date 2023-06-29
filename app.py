import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("Ncbi:", st.secrets["NCBI_API_KEY"])
st.write("X_ELS_APIKey:", st.secrets["X_ELS_APIKey"])
st.write("X_ELS_Insttoken:", st.secrets["X_ELS_Insttoken"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])
