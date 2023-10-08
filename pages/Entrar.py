import streamlit as st

# Datos del usuario de prueba
usuario_prueba = {
    "usuario": "usuario_de_prueba",
    "contrasena": "contrasena_de_prueba"
}

# Título de la aplicación
st.title("Inicia sesión en LitWave")

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
