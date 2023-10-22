# mis_libros.py
import streamlit as st
from streamlit import session_state

libros_leidos = [    {
        "titulo": "No sé cómo mostrar dónde me duele",
        "autor": "Amalia Andrade",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/386/original/portada_no-se-como-mostrar-donde-me-duele_amalia-andrade_202307311626.png"
    }]
libros_leyendo = [    {
        "titulo": "El Alquimista",
        "autor": "Paulo Coelho",
        "imagen": "https://planetadelibrosco2.cdnstatics.com/usuaris/libros/fotos/384/original/portada_el-alquimista_paulo-coelho_202306160135.jpg"
    }]
libros_favoritos = []

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
]

# Estado de la aplicación usando session_state
if "libros_leidos" not in st.session_state:
    st.session_state.libros_leidos = []
if "libros_leyendo" not in st.session_state:
    st.session_state.libros_leyendo = []
if "libros_favoritos" not in st.session_state:
    st.session_state.libros_favoritos = []

# Verifica si el parámetro 'usuario' está presente en la URL
if 'usuario' in st.experimental_get_query_params():
    # ... código para verificar el usuario (omitiendo para la explicación) ...
    
    # Formulario para agregar libros a la lista
    st.subheader("Agregar libros a la lista")
    busqueda = st.text_input("Buscar libro")
    resultado_seleccionado = st.selectbox("Selecciona un libro", [libro["titulo"] for libro in libros])
    lista_destino = st.radio("Selecciona una lista:", ["Leídos", "En Proceso de Lectura", "Favoritos"])
    confirmado = st.checkbox("¿Estás seguro de que quieres agregar este libro?")
    agregar_libro = st.form_submit_button("Agregar a la Lista")

    if agregar_libro:
        # Lógica para agregar el libro seleccionado a la lista correspondiente
        libro_seleccionado = next((libro for libro in libros if libro["titulo"] == resultado_seleccionado), None)
        if libro_seleccionado and confirmado:
            if lista_destino == "Leídos":
                st.session_state.libros_leidos.append(libro_seleccionado)
            elif lista_destino == "En Proceso de Lectura":
                st.session_state.libros_leyendo.append(libro_seleccionado)
            elif lista_destino == "Favoritos":
                st.session_state.libros_favoritos.append(libro_seleccionado)
            st.success(f"El libro '{libro_seleccionado['titulo']}' ha sido agregado a {lista_destino}.")

# Mostrar la lista seleccionada
if categoria_seleccionada == "Leídos":
    if st.session_state.libros_leidos:
        st.header("Leídos")
        for libro in st.session_state.libros_leidos:
            st.image(libro["imagen"], caption=libro["titulo"], use_column_width=True)
            st.write("**Título:**", libro["titulo"])
            st.write("**Autor:**", libro["autor"])
    else:
        st.info("No hay libros leídos en tu lista.")
elif categoria_seleccionada == "En Proceso de Lectura":
    if st.session_state.libros_leyendo:
        st.header("En Proceso de Lectura")
        for libro in st.session_state.libros_leyendo:
            st.image(libro["imagen"], caption=libro["titulo"], use_column_width=True)
            st.write("**Título:**", libro["titulo"])
            st.write("**Autor:**", libro["autor"])
    else:
        st.info("No hay libros en proceso de lectura en tu lista.")
elif categoria_seleccionada == "Favoritos":
    if st.session_state.libros_favoritos:
        st.header("Favoritos")
        for libro in st.session_state.libros_favoritos:
            st.image(libro["imagen"], caption=libro["titulo"], use_column_width=True)
            st.write("**Título:**", libro["titulo"])
            st.write("**Autor:**", libro["autor"])
    else:
        st.info("No hay libros favoritos en tu lista.")
        
            # Mensaje si no hay resultados
            if not resultados:
                st.info("No se encontraron resultados para la búsqueda.")
    else:
        st.error("Acceso no autorizado.")
