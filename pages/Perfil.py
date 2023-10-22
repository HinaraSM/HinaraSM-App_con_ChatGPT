import streamlit as st
from streamlit import session_state

# Verifica si el parámetro 'usuario' está presente en la URL
if 'usuario' in st.experimental_get_query_params():
    # Obtiene el nombre de usuario del parámetro de la URL
    usuario = st.experimental_get_query_params()['usuario'][0]

    # Verifica si el usuario está autenticado en session_state
    if hasattr(session_state, 'usuario') and session_state.usuario["usuario"] == usuario:
    # Verificar si el usuario está autenticado (puedes implementar tu propia lógica de autenticación aquí)        
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

    else:
        st.error("Acceso no autorizado.")
        
            # Botón para cerrar sesión
            if st.button("Cerrar Sesión"):
                session_state.is_authenticated = False
                st.success("Sesión cerrada exitosamente. ¡Hasta luego!")

# Resto de tu aplicación aquí...
