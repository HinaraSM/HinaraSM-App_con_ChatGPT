import streamlit as st
from PIL import Image

# Logo en la esquina superior derecha
st.markdown(
    """
    <style>
    .logo-container {
        position: fixed;
        top: 40px;
        right: 10px;
    }
    </style>
    <div class="logo-container">
        <img src="https://images.vexels.com/media/users/3/229082/isolated/preview/6fabc24c3830d75486725cc6d786dfbb-logotipo-de-circulos-de-libro.png" alt="Logo" style="width:100px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("LitWave")
st.markdown("## Bienvenido a la red social de los lectores")
st.markdown("### LitWave es una plataforma para los amantes de la lectura, donde podrás:")
st.write("- Descubrir nuevos libros recomendados especialmente para ti.")
st.write("- Conectar, interactuar y compartir tu pasión por los libros.")
st.write("- Comentar tus opiniones sobre libros y autores.")
st.write("- Crear tus propias listas de lectura para enriquecer tu experiencia literaria.")
st.write("- Seguir a otros lectores, dar me gusta y comentarles")

# Cargar una imagen
#image = Image.open('libros.png')    

# Mostrar la imagen modificada en Streamlit
#st.image(image, caption='LitWave - Tu plataforma de lectura')
# ... (resto del código de la página de inicio)


# Información de contacto y redes sociales en el pie de página
st.markdown("---")
st.markdown("### Contactos")
st.write("Para consultas y soporte, contáctanos en:")
st.write("Hinara Pastora Sánchez Mata. Correo electrónico: hisanchezm@unal.edu.com")
st.write("Juan Camilo Montoya Mejía. Correo electrónico: jumontoyame@unal.edu.co")

# Pie de página
st.write("© 2023 LitWave. Todos los derechos reservados.")
