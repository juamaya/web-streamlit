import streamlit as st
import random
import requests

# Funcion para obtener datos de un pokemon
def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code==200:
            return response.json()
        else:
            return None
    except:
        return None
    
# Funcion para obtener datos de un pokemon aleatorio

def get_random_pokemon():
    random_id= random.randint(1, 1010)
    return get_pokemon_data(str(random_id))


# data = get_pokemon_data("pikachu")
# print(data)

# Titulo y descripcion

st.title(" 🔥 Explorador de Pokemon")
st.divider()
 
# Crear dos columnas para la busqueda y boton aleatorio

col1, col2 = st.columns([1,1])

with col1:
    pokemon_name = st.text_input("ingresa el nombre de un pokemon:","")

with col2:
    random_button = st.button("Pokemon Aleatorio! 🎲")

pokemon_data = None


# Manejar la busqueda y boton aleatorio

if pokemon_name:
    pokemon_data = get_pokemon_data(pokemon_name)
elif random_button:
    pokemon_data = get_random_pokemon()

 
# Mostrar informacion del pokemon  
if pokemon_data:
   # Crear dos columnas para la imagen y la informacion
    img_col, info_col = st.columns([2,1])

    with img_col:
        # Mostrar imagen  del pokemon  
        st.image(
            pokemon_data["sprites"]["other"]["official-artwork"]["front_default"],
            caption=f" ID: {pokemon_data["id"]} ",
            width=200
        )

    with info_col:
       # Informacion Basica
       st.subheader ("Informacion Basica")
       st.write(f"**Nombre:** {pokemon_data["name"].title()}")
       st.write(f"**Altura:** {pokemon_data["height"]/10 } m")
       st.write(f"**Peso:** {pokemon_data["weight"]/10 } kg")
       # Tipos
       st.subheader("Tipos")
       tipos = [tipo["type"]["name"] for tipo in pokemon_data["types"]]
       for tipo in tipos:
           st.write(f" 🔸 {tipo.title()}")

    st.divider()
    # Estadisticas
    st.info(" ### Estadisticas")
    stats_cols = st.columns(3)
    stats = pokemon_data["stats"]

    for idx, stat in enumerate (stats):
        col_idx = idx % 3
        with stats_cols [col_idx]:
            st.metric(
                label=stat["stat"]["name"].replace("-", " ").title(),
                value=stat["base_stat"]
            )

    st.divider() 
    # Habilidades
    st.info(" ### Habilidades")
    abilities= [ability["ability"]["name"].replace("-", " ").title()
                for ability in pokemon_data["abilities"]]

    for ability in abilities:
        st.write (f" ⭐ {ability}")

elif pokemon_name:
    st.error("Pokemon no encontrado! Verifica el nombre e intenta nuevamente")
else:
    st.info(" 👆 Ingresa el nombre de un pokemon o prueba con uno aleatorio  👆")




st.divider()
st.warning("###### Juamaya 🍺 2025")
############################################################################
############################################################################


st.divider()

st.success('##### Aqui tienes el codigo completo de la App:  Explorador de Pokemon')

st.markdown('>App.py')
st.code(
        """
import streamlit as st
import random
import requests

# Funcion para obtener datos de un pokemon
def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code==200:
            return response.json()
        else:
            return None
    except:
        return None
    
# Funcion para obtener datos de un pokemon aleatorio

def get_random_pokemon():
    random_id= random.randint(1, 1010)
    return get_pokemon_data(str(random_id))


# data = get_pokemon_data("pikachu")
# print(data)

# Titulo y descripcion

st.title(" 🔥 Explorador de Pokemon")
st.divider()
 
# Crear dos columnas para la busqueda y boton aleatorio

col1, col2 = st.columns([1,1])

with col1:
    pokemon_name = st.text_input("ingresa el nombre de un pokemon:","")

with col2:
    random_button = st.button("Pokemon Aleatorio! 🎲")

pokemon_data = None


# Manejar la busqueda y boton aleatorio

if pokemon_name:
    pokemon_data = get_pokemon_data(pokemon_name)
elif random_button:
    pokemon_data = get_random_pokemon()

 
# Mostrar informacion del pokemon  
if pokemon_data:
   # Crear dos columnas para la imagen y la informacion
    img_col, info_col = st.columns([2,1])

    with img_col:
        # Mostrar imagen  del pokemon  
        st.image(
            pokemon_data["sprites"]["other"]["official-artwork"]["front_default"],
            caption=f" ID: {pokemon_data["id"]} ",
            width=200
        )

    with info_col:
       # Informacion Basica
       st.subheader ("Informacion Basica")
       st.write(f"**Nombre:** {pokemon_data["name"].title()}")
       st.write(f"**Altura:** {pokemon_data["height"]/10 } m")
       st.write(f"**Peso:** {pokemon_data["weight"]/10 } kg")
       # Tipos
       st.subheader("Tipos")
       tipos = [tipo["type"]["name"] for tipo in pokemon_data["types"]]
       for tipo in tipos:
           st.write(f" 🔸 {tipo.title()}")

    st.divider()
    # Estadisticas
    st.info(" ### Estadisticas")
    stats_cols = st.columns(3)
    stats = pokemon_data["stats"]

    for idx, stat in enumerate (stats):
        col_idx = idx % 3
        with stats_cols [col_idx]:
            st.metric(
                label=stat["stat"]["name"].replace("-", " ").title(),
                value=stat["base_stat"]
            )

    st.divider() 
    # Habilidades
    st.info(" ### Habilidades")
    abilities= [ability["ability"]["name"].replace("-", " ").title()
                for ability in pokemon_data["abilities"]]

    for ability in abilities:
        st.write (f" ⭐ {ability}")

elif pokemon_name:
    st.error("Pokemon no encontrado! Verifica el nombre e intenta nuevamente")
else:
    st.info(" 👆 Ingresa el nombre de un pokemon o prueba con uno aleatorio  👆")

st.divider()
   """)
 

st.markdown("Juamaya 🍺 2025")
st.sidebar.success("Select a page 👆")
