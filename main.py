import streamlit as st
from pages import home, login, register

def main():
    st.title("LitWave")
    menu = st.sidebar.selectbox("Menú", ["Inicio", "Entrar", "Registrarse"])

    if menu == "Inicio":
        home.show()

    elif menu == "Entrar":
        login.show()

    elif menu == "Registrarse":
        register.show()

if __name__ == "__main__":
    main()
