import streamlit as st
from pages import login, register


st.title("LitWave")
st.header("Bienvenido a LitWave")
st.write("LitWave es una plataforma para los amantes de la lectura, \
donde puedes descubrir nuevos libros, compartir tus experiencias \
de lectura y conectarte con otros lectores.")
st.markdown("### Características Destacadas:")
st.write("- Descubre nuevos libros recomendados para ti.")
st.write("- Conecta, interactúa y comparte tu pasión por los libros.")
st.write("- Comenta sobre libros, autores y descubre nuevas lecturas.")
st.write("- Ayuda a autores a promocionar sus obras y llegar a nuevos lectores.")
st.write("- Crea tus propias listas de lectura para enriquecer tu experiencia literaria.")
st.write("- Sigue a otros lectores, da me gusta y comenta, !sé parte de una comunidad que gira en torno a la lectura¡.")
# Cargar una imagen
#image = Image.open('libros.png')    

# Mostrar la imagen modificada en Streamlit
#st.image(image, caption='LitWave - Tu plataforma de lectura')
# ... (resto del código de la página de inicio)


# Información de contacto y redes sociales en el pie de página
st.markdown("---")
st.markdown("### Contacto")
st.write("Para consultas y soporte, contáctanos en:")
st.write("Hinara Pastora Sánchez Mata. Correo electrónico: hisanchezm@unal.edu.com")
st.write("Juan Camilo Montoya Mejía. Correo electrónico: jumontoyame@unal.edu.co")

# Pie de página
st.write("© 2023 LitWave. Todos los derechos reservados.")
