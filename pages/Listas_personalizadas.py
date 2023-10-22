# mis_libros.py

import streamlit as st

libros_leidos = []
libros_leyendo = []
libros_favoritos = []

# Si el botón "Ver Mis Libros" es seleccionado
# Botón para ver las listas
if st.button("Ver mis libros"):
    # Opción de selección para elegir la lista a mostrar
    categoria_seleccionada = st.selectbox("Selecciona una categoría", ["Leídos", "En Proceso de Lectura", "Favoritos"])

    st.title("Mis Libros")

    # Mostrar la lista seleccionada
    if categoria_seleccionada == "Leídos":
        if libros_leidos:
            st.header("Leídos")
            st.table(libros_leidos)
        else:
            st.info("No hay libros leídos en tu lista.")
    elif categoria_seleccionada == "En Proceso de Lectura":
        if libros_leyendo:
            st.header("En Proceso de Lectura")
            st.table(libros_leyendo)
        else:
            st.info("No hay libros en proceso de lectura en tu lista.")
    elif categoria_seleccionada == "Favoritos":
        if libros_favoritos:
            st.header("Favoritos")
            st.table(libros_favoritos)
        else:
            st.info("No hay libros favoritos en tu lista.")

# Si el botón "Agregar Libros a Mi Lista" es seleccionado


if st.button("Agregar libros a Mi Lista"):
    # ... Código del buscador de libros ...
    # Barra de búsqueda
    busqueda = st.text_input("Buscar libro")
    
    # Filtra los libros según el término de búsqueda
    resultados = []
    for libro in libros:
        if busqueda.lower() in libro["titulo"].lower() or busqueda.lower() in libro["autor"].lower():
            resultados.append(libro)

        # Muestra los resultados en dos columnas
    columnas = st.columns(2)
    for i, resultado in enumerate(resultados):
        with columnas[i % 2]:  # Alternar entre las dos columnas
            st.image(resultado["imagen"], caption=resultado["titulo"], use_column_width=True)
            st.write("**Título:**", resultado["titulo"])
            st.write("**Autor:**", resultado["autor"])
            if st.checkbox("Agregar a la Lista", key=f"checkbox_{i}"):
                selected_books.append(resultado)  # Agregar el libro a la lista cuando se selecciona
    st.markdown("---")
    
    # Mensaje si no hay resultados
    if not resultados:
        st.info("No se encontraron resultados para la búsqueda.")

    
    # Agregar una opción para seleccionar libros
    selected_books = []  # Lista para almacenar los libros seleccionados
    for i, resultado in enumerate(resultados):
        with columnas[i % 2]:

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
