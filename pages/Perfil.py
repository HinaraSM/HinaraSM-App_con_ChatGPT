import streamlit as st
from streamlit import session_state

# Obtener el nombre de usuario de la URL
if 'usuario' in st.experimental_get_query_params():
    usuario = st.experimental_get_query_params()['usuario'][0]

    # Verificar si el usuario está autenticado y autorizado
    if hasattr(session_state, 'usuario') and session_state.usuario["usuario"] == usuario:
        st.title(f"Bienvenido, {usuario}!")

        # Obtener y mostrar los datos actuales del usuario
        nombre_actual = session_state.usuario.get("nombre", "")
        email_actual = session_state.usuario.get("email", "")

        # Campo de entrada para el nuevo nombre
        nuevo_nombre = st.text_input("Nuevo Nombre", nombre_actual)

        # Campo de entrada para el nuevo correo electrónico
        nuevo_email = st.text_input("Nuevo Correo Electrónico", email_actual)

        # Botón para guardar los cambios
        if st.button("Guardar Cambios"):
            # Guardar los nuevos datos del usuario (reemplaza esto con tu propia lógica)
            session_state.usuario["nombre"] = nuevo_nombre
            session_state.usuario["email"] = nuevo_email
            st.success("Cambios guardados exitosamente.")

        # Campo de entrada para cambiar la contraseña
        nueva_contrasena = st.text_input("Nueva Contraseña", type="password")
        confirmar_contrasena = st.text_input("Confirmar Contraseña", type="password")

        # Botón para cambiar la contraseña
        if st.button("Cambiar Contraseña"):
            if nueva_contrasena == confirmar_contrasena:
                # Lógica para cambiar la contraseña (reemplaza esto con tu propia lógica)
                st.success("Contraseña cambiada exitosamente.")
            else:
                st.error("Las contraseñas no coinciden. Inténtalo de nuevo.")

        # Botón para cerrar sesión
        if st.button("Cerrar Sesión"):
            del session_state.usuario
            st.success("Sesión cerrada exitosamente. ¡Hasta luego!")
    else:
        st.error("Acceso no autorizado, inicie sesión para poder acceder.")
