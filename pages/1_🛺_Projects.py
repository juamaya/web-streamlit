import streamlit as st


st.title("Projects Page")


col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("Web repositorios")
    st.image("images/app-repo.png", width=300)
    st.link_button("Visitar  Web", "https://juamaya.github.io/web-repositorios")

with col2:
    st.markdown("Web Documentacion")
    st.image("images/webdocu.png", width=300)
    st.link_button("Visitar Web", "https://juamaya.github.io/webdocu")

with col3:
   st.markdown("Web Rick and Morty")
   st.image("images/morty.png", width=300)
   st.link_button("Visitar Web", "https://juamaya.github.io/morty")

   


st.markdown("Juamaya 🍺 2025")

st.sidebar.success("Select a page 👆")
