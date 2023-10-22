# mis_libros.py
import streamlit as st
from streamlit import session_state

libros_leidos = []
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

# Si el botón "Ver Mis Libros" es seleccionado
# Verifica si el parámetro 'usuario' está presente en la URL
if 'usuario' in st.experimental_get_query_params():
    # Obtiene el nombre de usuario del parámetro de la URL
    usuario = st.experimental_get_query_params()['usuario'][0]
    
    # Verifica si el usuario está autenticado en session_state
    if hasattr(session_state, 'usuario') and session_state.usuario["usuario"] == usuario:
        st.title(f"Bienvenido, {usuario}!")
        # Muestra las opciones específicas para usuarios autenticados
        # ...
    else:
        st.error("Acceso no autorizado.")
else:
        if st.button("Ver mis libros"):
            # Opción de selección para elegir la lista a mostrar
            categoria_seleccionada = st.selectbox("Selecciona una categoría", ["Leídos", "En Proceso de Lectura", "Favoritos"])
        
            st.title("Mis Libros")
        
            # Mostrar la lista seleccionada
            if categoria_seleccionada == "Leídos":
                if libros_leidos:
                    st.header("Leídos")
                    st.table(libros_leidos)
                else:
                    st.info("No hay libros leídos en tu lista.")
            elif categoria_seleccionada == "En Proceso de Lectura":
                if libros_leyendo:
                    st.header("En Proceso de Lectura")
                    st.table(libros_leyendo)
                else:
                    st.info("No hay libros en proceso de lectura en tu lista.")
            elif categoria_seleccionada == "Favoritos":
                if libros_favoritos:
                    st.header("Favoritos")
                    st.table(libros_favoritos)
                else:
                    st.info("No hay libros favoritos en tu lista.")
        
        # Si el botón "Agregar Libros a Mi Lista" es seleccionado
        if st.button("Agregar libros a Mi Lista"):
            # ... Código del buscador de libros ...
            # Barra de búsqueda
            busqueda = st.text_input("Buscar libro")
            
            # Filtra los libros según el término de búsqueda
            resultados = []
            for libro in libros:
                if busqueda.lower() in libro["titulo"].lower() or busqueda.lower() in libro["autor"].lower():
                    resultados.append(libro)
        
            # Muestra los resultados en dos columnas
            columnas = st.columns(2)
            for i, resultado in enumerate(resultados):
                with columnas[i % 2]:  # Alternar entre las dos columnas
                    st.image(resultado["imagen"], caption=resultado["titulo"], use_column_width=True)
                    st.write("**Título:**", resultado["titulo"])
                    st.write("**Autor:**", resultado["autor"])
                    agregar_a_lista = st.button("Agregar a la Lista", key=f"checkbox_{i}")
                    if agregar_a_lista:
                        lista_destino = st.radio("Selecciona una lista:", ["Leídos", "En Proceso de Lectura", "Favoritos"])
                        confirmado = st.checkbox("¿Estás seguro de que quieres agregar este libro?")
                        if confirmado:
                            if lista_destino == "Leídos":
                                libros_leidos.append(resultado)
                            elif lista_destino == "En Proceso de Lectura":
                                libros_leyendo.append(resultado)
                            elif lista_destino == "Favoritos":
                                libros_favoritos.append(resultado)
                            st.success(f"El libro '{resultado['titulo']}' ha sido agregado a {lista_destino}.")
        
            # Mensaje si no hay resultados
            if not resultados:
                st.info("No se encontraron resultados para la búsqueda.")
