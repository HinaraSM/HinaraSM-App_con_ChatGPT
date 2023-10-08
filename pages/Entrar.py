import streamlit as st

st.header("Inicio de Sesión")

# Datos del usuario de prueba
usuario_prueba = {
    "usuario": "hinara",
    "contrasena": "hinara12"
}

# Para hacer pruebas, puedes almacenar el usuario de prueba en una lista o un diccionario en memoria
usuarios_registrados = [usuario_prueba]

# Simular la autenticación del usuario
usuario_input = input("Ingrese su nombre de usuario: ")
contrasena_input = input("Ingrese su contraseña: ")

# Verificar las credenciales del usuario
usuario_autenticado = None
for usuario in usuarios_registrados:
    if usuario["usuario"] == usuario_input and usuario["contrasena"] == contrasena_input:
        usuario_autenticado = usuario
        break

if usuario_autenticado:
    print("Inicio de sesión exitoso.")
else:
    print("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

