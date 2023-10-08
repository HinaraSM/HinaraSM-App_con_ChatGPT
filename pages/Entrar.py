import streamlit as st

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

# Título de la aplicación
st.title("Inicia sesión en LitWave")

# Datos del usuario de prueba
usuario_prueba = {
    "usuario": "hinara",
    "contrasena": "hinara12"
}

# Casilla de entrada para el nombre de usuario
usuario_input = st.text_input("Ingrese su nombre de usuario")

# Casilla de entrada para la contraseña
contrasena_input = st.text_input("Ingrese su contraseña", type="password")

# Botón para iniciar sesión
if st.button("Iniciar Sesión"):
    # Verificar las credenciales del usuario
    if usuario_input == usuario_prueba["usuario"] and contrasena_input == usuario_prueba["contrasena"]:
        st.success("Inicio de sesión exitoso.")
    else:
        st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
