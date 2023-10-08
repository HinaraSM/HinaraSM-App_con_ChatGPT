import streamlit as st
from pymongo import MongoClient
import hashlib

# Conexión a la base de datos MongoDB
#client = MongoClient("mongodb://tu_usuario:tu_contraseña@tu_host/tu_base_de_datos")
#db = client.tu_base_de_datos
#usuarios_collection = db.usuarios

usuarios_collection = {
    "usuario": hinara,
    "contrasena": hi121212
}

st.header("Inicio de Sesión")

# Casilla de entrada para el nombre de usuario
usuario = st.text_input("Usuario")

# Casilla de entrada para la contraseña
contrasena = st.text_input("Contraseña", type="password")

# Botón para iniciar sesión
if st.button("Iniciar Sesión"):
    # Hash de la contraseña para compararla con la base de datos
    hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
    
    # Verificar si el usuario y la contraseña coinciden en la base de datos
    usuario_encontrado = usuarios_collection.find_one({"usuario": usuario, "contrasena": hashed_password})
    
    if usuario_encontrado:
        st.success("Inicio de sesión exitoso.")
        # Puedes redirigir al usuario a otra página o realizar acciones adicionales después del inicio de sesión.
    else:
        st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

