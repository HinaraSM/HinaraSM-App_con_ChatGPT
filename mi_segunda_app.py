import streamlit as st

# Título y autor de la app
st.title("Conversor universal")
st.write("Esta app fue elaborada por 'Hinara Pastora Sánchez Mata'.")

# Lista de categorías y conversiones
categorias = {
    "Conversiones de temperatura": [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ],
    "Conversiones de longitud": [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ],
    "Conversiones de peso/masa": [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ],
    "Conversiones de volumen": [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ],
    "Conversiones de tiempo": [
        "Horas a Minutos",
        "Minutos a Segundos",
        "Días a Horas",
        "Semanas a Días"
    ],
    "Conversiones de velocidad": [
        "Millas por hora a Kilómetros por hora",
        "Kilómetros por hora a Metros por segundo",
        "Nudos a Millas por hora",
        "Metros por segundo a Pies por segundo"
    ],
    "Conversiones de área": [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ],
    "Conversiones de energía": [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ],
    "Conversiones de presión": [
        "Pascales a Atmósferas",
        "Atmósferas a Pascales",
        "Barras a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Bares"
    ],
    "Conversiones de tamaño de datos": [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ]
}

# Seleccionar la categoría
categoria_seleccionada = st.selectbox("Selecciona una categoría", list(categorias.keys()))

# Seleccionar la conversión dentro de la categoría
conversion_seleccionada = st.selectbox("Selecciona una conversión", categorias[categoria_seleccionada])

# Solicitar el valor a convertir
valor_a_convertir = st.number_input("Ingresa el valor a convertir")

# Realizar las conversiones según la selección
# Conversiones de temperatura
elif conversion_seleccionada == "Celsius a Fahrenheit":
    resultado = (valor_a_convertir * 9/5) + 32
    st.write(f"{valor_a_convertir} grados Celsius equivale a {resultado} grados Fahrenheit")
elif conversion_seleccionada == "Fahrenheit a Celsius":
    resultado = (valor_a_convertir - 32) * 5/9
    st.write(f"{valor_a_convertir} grados Fahrenheit equivale a {resultado} grados Celsius")
elif conversion_seleccionada == "Celsius a Kelvin":
    resultado = valor_a_convertir + 273.15
    st.write(f"{valor_a_convertir} grados Celsius equivale a {resultado} Kelvin")
elif conversion_seleccionada == "Kelvin a Celsius":
    resultado = valor_a_convertir - 273.15
    st.write(f"{valor_a_convertir} Kelvin equivale a {resultado} grados Celsius")

# Conversiones de longitud
elif conversion_seleccionada == "Pies a Metros":
    resultado = valor_a_convertir * 0.3048
    st.write(f"{valor_a_convertir} pies equivale a {resultado} metros")
elif conversion_seleccionada == "Metros a Pies":
    resultado = valor_a_convertir / 0.3048
    st.write(f"{valor_a_convertir} metros equivale a {resultado} pies")
elif conversion_seleccionada == "Pulgadas a Centímetros":
    resultado = valor_a_convertir * 2.54
    st.write(f"{valor_a_convertir} pulgadas equivale a {resultado} centímetros")
elif conversion_seleccionada == "Centímetros a Pulgadas":
    resultado = valor_a_convertir / 2.54
    st.write(f"{valor_a_convertir} centímetros equivale a {resultado} pulgadas")

# Conversiones de peso/masa
elif conversion_seleccionada == "Libras a Kilogramos":
    resultado = valor_a_convertir * 0.453592
    st.write(f"{valor_a_convertir} libras equivale a {resultado} kilogramos")
elif conversion_seleccionada == "Kilogramos a Libras":
    resultado = valor_a_convertir / 0.453592
    st.write(f"{valor_a_convertir} kilogramos equivale a {resultado} libras")
elif conversion_seleccionada == "Onzas a Gramos":
    resultado = valor_a_convertir * 28.3495
    st.write(f"{valor_a_convertir} onzas equivale a {resultado} gramos")
elif conversion_seleccionada == "Gramos a Onzas":
    resultado = valor_a_convertir / 28.3495
    st.write(f"{valor_a_convertir} gramos equivale a {resultado} onzas")

# Conversiones de volumen
elif conversion_seleccionada == "Galones a Litros":
    resultado = valor_a_convertir * 3.78541
    st.write(f"{valor_a_convertir} galones equivale a {resultado} litros")
elif conversion_seleccionada == "Litros a Galones":
    resultado = valor_a_convertir / 3.78541
    st.write(f"{valor_a_convertir} litros equivale a {resultado} galones")
elif conversion_seleccionada == "Pulgadas Cúbicas a Centímetros Cúbicos":
    resultado = valor_a_convertir * 16.387
    st.write(f"{valor_a_convertir} pulgadas cúbicas equivale a {resultado} centímetros cúbicos")
elif conversion_seleccionada == "Centímetros Cúbicos a Pulgadas Cúbicas":
    resultado = valor_a_convertir / 16.387
    st.write(f"{valor_a_convertir} centímetros cúbicos equivale a {resultado} pulgadas cúbicas")

# Conversiones de tiempo
elif conversion_seleccionada == "Horas a Minutos":
    resultado = valor_a_convertir * 60
    st.write(f"{valor_a_convertir} horas equivale a {resultado} minutos")
elif conversion_seleccionada == "Minutos a Segundos":
    resultado = valor_a_convertir * 60
    st.write(f"{valor_a_convertir} minutos equivale a {resultado} segundos")
elif conversion_seleccionada == "Días a Horas":
    resultado = valor_a_convertir * 24
    st.write(f"{valor_a_convertir} días equivale a {resultado} horas")
elif conversion_seleccionada == "Semanas a Días":
    resultado = valor_a_convertir * 7
    st.write(f"{valor_a_convertir} semanas equivale a {resultado} días")

# Conversiones de velocidad
elif conversion_seleccionada == "Millas por hora a Kilómetros por hora":
    resultado = valor_a_convertir * 1.60934
    st.write(f"{valor_a_convertir} millas por hora equivale a {resultado} kilómetros por hora")
elif conversion_seleccionada == "Kilómetros por hora a Metros por segundo":
    resultado = valor_a_convertir * 0.277778
    st.write(f"{valor_a_convertir} kilómetros por hora equivale a {resultado} metros por segundo")
elif conversion_seleccionada == "Nudos a Millas por hora":
    resultado = valor_a_convertir * 1.15078
    st.write(f"{valor_a_convertir} nudos equivale a {resultado} millas por hora")
elif conversion_seleccionada == "Metros por segundo a Pies por segundo":
    resultado = valor_a_convertir * 3.28084
    st.write(f"{valor_a_convertir} metros por segundo equivale a {resultado} pies por segundo")

# Conversiones de área
elif conversion_seleccionada == "Metros cuadrados a Pies cuadrados":
    resultado = valor_a_convertir * 10.7639
    st.write(f"{valor_a_convertir} metros cuadrados equivale a {resultado} pies cuadrados")
elif conversion_seleccionada == "Pies cuadrados a Metros cuadrados":
    resultado = valor_a_convertir * 0.092903
    st.write(f"{valor_a_convertir} pies cuadrados equivale a {resultado} metros cuadrados")
elif conversion_seleccionada == "Kilómetros cuadrados a Millas cuadradas":
    resultado = valor_a_convertir * 0.386102
    st.write(f"{valor_a_convertir} kilómetros cuadrados equivale a {resultado} millas cuadradas")
elif conversion_seleccionada == "Millas cuadradas a Kilómetros cuadrados":
    resultado = valor_a_convertir * 2.58999
    st.write(f"{valor_a_convertir} millas cuadradas equivale a {resultado} kilómetros cuadrados")

# Conversiones de energía
elif conversion_seleccionada == "Julios a Calorías":
    resultado = valor_a_convertir * 0.239006
    st.write(f"{valor_a_convertir} julios equivale a {resultado} calorías")
elif conversion_seleccionada == "Calorías a Kilojulios":
    resultado = valor_a_convertir * 0.004184
    st.write(f"{valor_a_convertir} calorías equivale a {resultado} kilojulios")
elif conversion_seleccionada == "Kilovatios-hora a Megajulios":
    resultado = valor_a_convertir * 1000
    st.write(f"{valor_a_convertir} kilovatios-hora equivale a {resultado} megajulios")
elif conversion_seleccionada == "Megajulios a Kilovatios-hora":
    resultado = valor_a_convertir * 0.001
    st.write(f"{valor_a_convertir} megajulios equivale a {resultado} kilovatios-hora")

# Conversiones de presión
elif conversion_seleccionada == "Pascales a Atmósferas":
    resultado = valor_a_convertir * 9.8692e-6
    st.write(f"{valor_a_convertir} pascales equivale a {resultado} atmósferas")
elif conversion_seleccionada == "Atmósferas a Pascales":
    resultado = valor_a_convertir * 101325
    st.write(f"{valor_a_convertir} atmósferas equivale a {resultado} pascales")
elif conversion_seleccionada == "Barras a Libras por Pulgada Cuadrada":
    resultado = valor_a_convertir * 14.5038
    st.write(f"{valor_a_convertir} barras equivale a {resultado} libras por pulgada cuadrada")
elif conversion_seleccionada == "Libras por Pulgada Cuadrada a Bares":
    resultado = valor_a_convertir * 0.0689476
    st.write(f"{valor_a_convertir} libras por pulgada cuadrada equivale a {resultado} bares")

# Conversiones de tamaño de datos
elif conversion_seleccionada == "Megabytes a Gigabytes":
    resultado = valor_a_convertir * 0.001
    st.write(f"{valor_a_convertir} megabytes equivale a {resultado} gigabytes")
elif conversion_seleccionada == "Gigabytes a Terabytes":
    resultado = valor_a_convertir * 0.001
    st.write(f"{valor_a_convertir} gigabytes equivale a {resultado} terabytes")
elif conversion_seleccionada == "Kilobytes a Megabytes":
    resultado = valor_a_convertir * 0.001
    st.write(f"{valor_a_convertir} kilobytes equivale a {resultado} megabytes")
elif conversion_seleccionada == "Terabytes a Petabytes":
    resultado = valor_a_convertir * 0.001
    st.write(f"{valor_a_convertir} terabytes equivale a {resultado} petabytes")






