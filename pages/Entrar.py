import streamlit as st
# from pymongo import MongoClient
from datetime import datetime

# Conexión a la base de datos MongoDB
#client = MongoClient("mongodb://tu_usuario:tu_contraseña@tu_host:tu_puerto/tu_base_de_datos")
#db = client.tu_base_de_datos
#usuarios_collection = db.usuarios

# Datos del usuario de prueba
usuario_prueba = {
    "usuario": "hinara",
    "contrasena": "hinara12",
    "nombres_apellidos": "Hinara Pastora Sánchez Mata"
}

# Función para verificar las credenciales del usuario en la base de datos
def verificar_credenciales(usuario_input, contrasena_input):
    if usuario_prueba["usuario"]== usuario_input and usuario_prueba["contrasena"]== contrasena_input:
        usuario_encontrado= usuario_prueba
    return usuario_encontrado

# Estado de la aplicación
is_authenticated = False

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
        <img src="https://i.ibb.co/CWhPGm1/logo.png" alt="logo" style="max-width: 150px; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

if not is_authenticated:
    st.title("Inicia sesión en LitWave")

    usuario_input = st.text_input("Ingrese su nombre de usuario")
    contrasena_input = st.text_input("Ingrese su contraseña", type="password")

    if st.button("Iniciar Sesión"):
        usuario = verificar_credenciales(usuario_input, contrasena_input)
        if usuario:
            is_authenticated = True
            st.success("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario["nombres_apellidos"]))
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
else:
    st.title("¡Bienvenido a LitWave!")

    # Opciones para usuarios autenticados
    # Puedes agregar aquí las secciones específicas para los usuarios logueados.
    # Por ejemplo:
    # st.write("¡Hola, usuario! Aquí están las opciones disponibles para ti:")

    # Sección 1
    st.header("Mis Tareas")
    # ... Aquí puedes agregar el contenido de la sección de tareas ...

    # Sección 2
    st.header("Perfil")
    # ... Aquí puedes agregar el contenido de la sección de perfil ...

    # Sección 3
    st.header("Configuración")
    # ... Aquí puedes agregar el contenido de la sección de configuración ...

