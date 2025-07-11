import streamlit as st


st.title("Tutoriales Page")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Python", "Javascript", "SQL", "Json", "CSS"])

with tab1:
    st.header("Python tutorial")
    st.write("Python es un lenguaje de alto nivel de programación interpretado")
    st.divider()
    st.write("Aquí tienes cómo consumir una API en Python ")

    st.info("✅ Ejemplo básico utilizando la librería requests")
    st.warning('🔧 Requisitos : Instala requests si no lo tienes')
    st.markdown('>pip install requests')
    st.code(
        """ 
        import requests

        # URL de la API
        url = "https://jsonplaceholder.typicode.com/users"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Lanza un error si el código no es 200-299

            datos = response.json()
            print("Datos recibidos:", datos )

        except requests.exceptions.RequestException as e:
            print("Error al consumir la API:", e)
        """
    )

#####################################################
with tab2:
    st.header("Javascript tutorial")
    st.write(
        "JavaScript (JS) es un lenguaje de programación ligero, interpretado, o compilado justo-a-tiempo (just-in-time) con funciones de primera clase. Si bien es más conocido como un lenguaje de scripting (secuencias de comandos) para páginas web"
    )
    st.divider()
    st.write(
        "Aquí tienes un ejemplo completo de cómo consumir una API usando JavaScript moderno (ES6+), utilizando fetch. Este código se puede ejecutar en el navegador o integrarse en una aplicación web."
    )

    st.info("✅ Ejemplo básico usando fetch ")

    st.code(
        """ 
        // URL de la API (puedes cambiarla por la real que desees usar)
        const apiUrl = "https://jsonplaceholder.typicode.com/users";

        // Función para consumir la API
        async function obtenerDatos() {
        try {
            const respuesta = await fetch(apiUrl);

            if (!respuesta.ok) {
            throw new Error(`Error: ${respuesta.status} ${respuesta.statusText}`);
            }

            const datos = await respuesta.json();
            console.log("Datos recibidos:", datos);
        }catch(error) {
            console.error("Hubo un problema al consumir la API:", error.message);
        }
        }

        // Llamamos a la función
        obtenerDatos();
      """
    )


#####################################################
with tab3:
    st.header("SQL tutorial")

    st.write(
        "SQL (por sus siglas en inglés Structured Query Language; en español lenguaje de consulta estructurada)"
    )

    st.divider()
    st.info("Comandos Basicos SQL")
    st.subheader("Crear base de datos")
    st.code("""CREATE DATABASE my_base;""")
    st.subheader("Eliminar base de datos")
    st.code("""DROP DATABASE my_database;""")
    st.subheader("Crear Tabla users")
    st.code(
        """CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR (255) NOT NULL,
     email VARCHAR (255) NOT NULL UNIQUE,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
     );
     """
    )

    st.subheader("Insertar datos en Tabla users")

    st.code(
        """INSERT INTO db_users (name, email)
                     VALUES ('Juan Lopez', 'juancorreo@gmail.com'),
                            ('Luis Perez ', 'luiscorreo@gmail.com');
     """
    )

    st.subheader("Ver datos de la Tabla users")

    st.code("SELECT * FROM users;")


#####################################################
with tab4:
    st.header("Json tutorial")
    st.divider()

    st.write(
        "JSON (JavaScript Object Notation) es un formato ligero para el intercambio de datos, basado en un subconjunto de la sintaxis de JavaScript para objetos"
    )
    st.divider()
    st.markdown("This is a json :smile:")

    st.json(
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        },
    )
#####################################################

with tab5:
    st.header("CSS tutorial")

    st.write(
        "CSS (Hojas de estilo en cascada) es un lenguaje utilizado para describir la presentación de un documento estructurado con HTML"
    )
    st.write(
        "En otras palabras, CSS se encarga de la apariencia visual de una página web, controlando cosas como el diseño, los colores, las fuentes y la disposición de los elementos"
    )
    st.markdown("### Aqui tienes un ejemplo: ")
    st.code(
        """
    <style>
    .metric-container {
        background-color: red; 
        padding: 15px; 
        border-radius: 10px; 
        display: inline-block; 
        width: 300px;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .metric-value {
        font-size: 36px; 
        font-weight: bold; 
        color: black;
    }

    .btn {
        background-color: blue; 
        padding: 10px;
        border-radius: 10px;  
         border: 5px solid yellow;
    } 

    .btn:hover{
        background-color: darkblue;
    }
    </style>

    <div class="metric-container">
        <div class="metric-value">Valor: 169</div>
       
        <button class="btn">Boton</button>
    </div>
    

    """
    )
    #########################################################
    st.markdown("## Resultado")
    st.html(
        """
    <style>
    .metric-container {
        background-color: red; 
        padding: 15px; 
        border-radius: 10px; 
        display: inline-block; 
        width: 300px;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .metric-value {
        font-size: 36px; 
        font-weight: bold; 
        color: black;
    }
    .btn {
        background-color: blue; 
        padding: 10px;
        border-radius: 10px;
        border: 5px solid yellow;
    } 

    .btn:hover{
        background-color: darkblue;
    }
    </style> 



    <div class="metric-container">
        <div class="metric-value">Valor: 169</div>
       
        <button class="btn">Boton</button>
    </div>
    """
    )

st.divider()
st.markdown("Juamaya 🍺 2025")


st.sidebar.success("Select a page 👆")
