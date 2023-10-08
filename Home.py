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
st.write("- **Fomentar la comunidad de lectores:** Proporcionamos un espacio donde los amantes de la lectura pueden conectarse, interactuar y compartir sus pasiones por los libros.")
st.write("- **Facilitar la discusión:** Permite a los usuarios discutir sus libros favoritos, autores, géneros y temas literarios, incluyendo reseñas, comentarios y recomendaciones.")
st.write("- **Descubrimiento de nuevos libros:** Ayudamos a los usuarios a descubrir nuevas lecturas a través de recomendaciones personalizadas, basadas en los intereses y hábitos de lectura de cada persona.")
st.write("- **Participación en clubes de lectura:** Facilitamos la creación y participación en clubes de lectura en línea, donde los miembros pueden elegir y discutir libros juntos.")
st.write("- **Promoción de autores y libros independientes:** Ofrecemos una plataforma para que autores noveles o menos conocidos puedan promocionar sus obras y llegar a nuevos lectores.")
st.write("- **Eventos y desafíos literarios:** Organizamos eventos, concursos y desafíos relacionados con la lectura para mantener a los usuarios comprometidos y motivados.")
st.write("- **Recursos de lectura:** Proporcionamos recursos útiles, como listas de libros recomendados, guías de lectura y artículos relacionados con la literatura.")
st.write("- **Interacción social:** Permite a los usuarios seguir a otros lectores, dar me gusta y comentar en sus actividades, y construir una comunidad en línea en torno a la lectura.")

# Cargar una imagen
image = Image.open('libros.png')    

# Mostrar la imagen modificada en Streamlit
st.image(image, caption='LitWave - Tu plataforma de lectura')
# ... (resto del código de la página de inicio)


# Información de contacto y redes sociales en el pie de página
st.markdown("---")
st.markdown("### Contacto")
st.write("Para consultas y soporte, contáctanos en:")
st.write("Hinara Pastora Sánchez Mata. Correo electrónico: hisanchezm@unal.edu.com")
st.write("Juan Camilo Montoya Mejía. Correo electrónico: jumontoyame@unal.edu.co")

# Pie de página
st.write("© 2023 LitWave. Todos los derechos reservados.")
