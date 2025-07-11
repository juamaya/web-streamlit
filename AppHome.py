import streamlit as st

st.set_page_config(page_title="App Multipage | Juamaya", page_icon="🔥",  layout="centered")


st.header("Main Page")
st.markdown("That is so funny! :joy:")
st.image("images/streamlit.jpg", width=300)
st.link_button("Go to Streamlit", "https://streamlit.io/")


st.subheader("Build powerful apps only with Python")

st.image("images/python.png", width=50)


if st.button("Send balloons!"):
    st.balloons()






st.markdown("Juamaya 🍺 2025")
st.sidebar.success("Select a page 👆")
