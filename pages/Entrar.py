import streamlit as st
# from pymongo import MongoClient
from datetime import datetime

# Conexión a la base de datos MongoDB
#client = MongoClient("mongodb://tu_usuario:tu_contraseña@tu_host:tu_puerto/tu_base_de_datos")
#db = client.tu_base_de_datos
#usuarios_collection = db.usuarios
from streamlit import session_state


def redirigir_a_pagina_privada():
    # Establece los parámetros de la URL para redirigir a la página privada
    st.experimental_set_query_params(usuario=session_state.usuario["usuario"])
    # Redirige a la nueva URL
    st.experimental_rerun()
    # Limpia los parámetros de la URL después de redirigir
    st.experimental_set_query_params()


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
            st.success("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario["nombres_apellidos"]))
            session_state.usuario = usuario
            is_authenticated=True
            redirigir_a_pagina_privada()  # Llama a la función de redirección
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")


