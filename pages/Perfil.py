import streamlit as st
from streamlit import session_state

# Datos del usuario (simulados)
usuario_prueba = {
    "usuario": "hinara",
    "nombres_apellidos": "Hinara Pastora Sánchez Mata"
}

# Estado de la aplicación
if not hasattr(session_state, "is_authenticated"):
    session_state.is_authenticated = False

# Verificar si el usuario está autenticado (puedes implementar tu propia lógica de autenticación aquí)
if not session_state.is_authenticated:
    st.warning("Por favor, inicia sesión para acceder al perfil del usuario.")
    usuario_input = st.text_input("Usuario")
    contrasena_input = st.text_input("Contraseña", type="password")
    if st.button("Iniciar Sesión"):
        # Lógica de autenticación (reemplaza esto con tu propia lógica)
        if usuario_input == usuario_prueba["usuario"]:
            session_state.is_authenticated = True

if session_state.is_authenticated:
    st.title(f"Bienvenido, {usuario_prueba['nombres_apellidos']}!")

    # Opción para cambiar la contraseña
    nueva_contrasena = st.text_input("Nueva Contraseña", type="password")
    confirmar_contrasena = st.text_input("Confirmar Contraseña", type="password")
    if st.button("Cambiar Contraseña"):
        if nueva_contrasena == confirmar_contrasena:
            # Lógica para cambiar la contraseña (reemplaza esto con tu propia lógica)
            st.success("Contraseña cambiada exitosamente.")
        else:
            st.error("Las contraseñas no coinciden. Inténtalo de nuevo.")

    # Botón para cerrar sesión
    if st.button("Cerrar Sesión"):
        session_state.is_authenticated = False
        st.success("Sesión cerrada exitosamente. ¡Hasta luego!")

# Resto de tu aplicación aquí...
