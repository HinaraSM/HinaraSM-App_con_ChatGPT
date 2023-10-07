import streamlit as st
from pages import home, login, register

def main():
    st.title("LitWave")
    home.show()
    login.show()
    register.show()

if __name__ == "__main__":
    main()
