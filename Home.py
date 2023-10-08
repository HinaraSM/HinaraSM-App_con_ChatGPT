import streamlit as st
from pages import login, register


st.title("LitWave")
st.header("Bienvenido a LitWave")
st.write("LitWave es una plataforma para los amantes de la lectura, \
donde puedes descubrir nuevos libros, compartir tus experiencias \
de lectura y conectarte con otros lectores.")
st.markdown("### Características Destacadas:")
st.write("- Descubre nuevos libros recomendados para ti.")
st.write("- Conecta con otros lectores y comparte tus recomendaciones.")
# ... (resto del código de la página de inicio)


# Información de contacto y redes sociales en el pie de página
st.markdown("---")
st.markdown("### Contacto")
st.write("Para consultas y soporte, contáctanos en:")
st.write("Hinara Pastora Sánchez Mata. Correo electrónico: hisanchezm@unal.edu.com")
st.write("Juan Camilo Montoya Mejía. Correo electrónico: jumontoyame@unal.edu.co")

# Pie de página
st.write("© 2023 LitWave. Todos los derechos reservados.")
