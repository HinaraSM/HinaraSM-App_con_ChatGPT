import streamlit as st
from pages import home, login, register


st.title("LitWave")
# Información de contacto y redes sociales en el pie de página
st.markdown("---")
st.markdown("### Contacto")
st.write("Para consultas y soporte, contáctanos en:")
st.write("Hinara Pastora Sánchez Mata. Correo electrónico: hisanchezm@unal.edu.com")
st.write("Juan Camilo Montoya Mejía. Correo electrónico: jumontoyame@unal.edu.co")

# Pie de página
st.write("© 2023 LitWave. Todos los derechos reservados.")
