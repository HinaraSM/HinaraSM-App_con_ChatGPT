import streamlit as st
from pages import Entrar, Sobre_nosotros, Registrarse

# Lista de libros con datos de prueba (título, autor y URL de la imagen)
libros = [
    {
        "titulo": "El Alquimista",
        "autor": "Paulo Coelho",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/384/original/portada_el-alquimista_paulo-coelho_202306160135.jpg"
    },
    {
        "titulo": "No sé cómo mostrar dónde me duele",
        "autor": "Amalia Andrade",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/386/original/portada_no-se-como-mostrar-donde-me-duele_amalia-andrade_202307311626.png"
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/339/original/338485_portada_1984_george-orwell_202104151338.jpg"
    },
    {
        "titulo": "Don Quijote de la mancha",
        "autor": "Miguel de Cervantes",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/161/original/160444_48282_1_DonQujotedelaMancha.jpg"
    },
    # Agrega más libros según sea necesario
]


st.header("Inicio")

# Barra de búsqueda
busqueda = st.text_input("Buscar libro")

# Filtra los libros según el término de búsqueda
resultados = []
for libro in libros:
    if busqueda.lower() in libro["titulo"].lower() or busqueda.lower() in libro["autor"].lower():
        resultados.append(libro)

# Muestra los resultados en dos columnas
for i in range(0, len(resultados), 2):
    col1, col2 = st.beta_columns(2)
    with col1:
        st.image(resultados[i]["imagen"], caption=resultados[i]["titulo"], use_column_width=True)
        st.write("**Título:**", resultados[i]["titulo"])
        st.write("**Autor:**", resultados[i]["autor"])
    with col2:
        if i + 1 < len(resultados):
            st.image(resultados[i + 1]["imagen"], caption=resultados[i + 1]["titulo"], use_column_width=True)
            st.write("**Título:**", resultados[i + 1]["titulo"])
            st.write("**Autor:**", resultados[i + 1]["autor"])
st.markdown("---")

# Mensaje si no hay resultados
if not resultados:
    st.info("No se encontraron resultados para la búsqueda.")

