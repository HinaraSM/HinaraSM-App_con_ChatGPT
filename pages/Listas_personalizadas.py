# mis_libros.py

import streamlit as st

# Si el botón "Ver Mis Libros" es seleccionado
if st.button("Ver Mis Libros"):
    st.title("Mis Libros")

    st.header("Leídos")
    st.table(libros_leidos)

    st.header("En Proceso de Lectura")
    st.table(libros_leyendo)

    st.header("Favoritos")
    st.table(libros_favoritos)

# Si el botón "Agregar Libros a Mi Lista" es seleccionado
if st.button("Agregar Libros a Mi Lista"):
    # ... Código del buscador de libros ...

    # Agregar una opción para seleccionar libros
    selected_books = []  # Lista para almacenar los libros seleccionados
    for i, resultado in enumerate(resultados):
        with columnas[i % 2]:
            if st.checkbox("Agregar a la Lista", key=f"checkbox_{i}"):
                selected_books.append(resultado)  # Agregar el libro a la lista cuando se selecciona

    # Lógica para agregar libros seleccionados a las listas correspondientes
    for libro in selected_books:
        if libro not in libros_leidos and libro not in libros_leyendo and libro not in libros_favoritos:
            if libro["categoria"] == "leidos":
                libros_leidos.append(libro)
            elif libro["categoria"] == "leyendo":
                libros_leyendo.append(libro)
            elif libro["categoria"] == "favoritos":
                libros_favoritos.append(libro)

    # Guardar las listas en la base de datos o en la memoria
