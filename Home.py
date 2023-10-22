import streamlit as st
from pages import Entrar, Sobre_nosotros, Registrarse

# Logo en la esquina superior derecha
st.markdown(
    """
    <style>
    .logo-container {
        position: fixed;
        top: 50px;
        right: 10px;
    }
    </style>
    <div class="logo-container">
        <img src="https://i.ibb.co/CWhPGm1/logo.png" alt="logo"style="max-width: 150px; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

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

from streamlit import session_state

# Verifica si hay parámetros en la URL
params = st.experimental_get_query_params()

if not params:
    # Muestra las opciones predeterminadas del menú
    st.sidebar.title("Menú")
    selected_page = st.sidebar.radio("Selecciona una opción", ["Inicio", "Entrar", "Registrarse"])
else:
    # Oculta las opciones de "Entrar" y "Registrarse" en el menú
    st.sidebar.title("Menú")
    selected_page = st.sidebar.radio("Selecciona una opción", ["Inicio"])

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
    st.header("Explora y descubre nuevos autores y libros")
    
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
    st.markdown("---")
    
    # Mensaje si no hay resultados
    if not resultados:
        st.info("No se encontraron resultados para la búsqueda.")
