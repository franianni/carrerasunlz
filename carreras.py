import streamlit as st

# Datos dummy para ejemplo
facultades = {
    "Derecho": ["Abogacía", "Notariado"],
    "Cs. Sociales": ["Comunicación Social", "Trabajo Social"],
    "Cs. Económicas": ["Contador Público", "Economía"],
    "Cs. Agrarias": ["Agronomía", "Medicina Veterinaria"],
    "Ingeniería": ["Ingeniería Civil", "Ingeniería en Sistemas"]
}

st.title("Buscador de Carreras - UNLZ")

nombre = st.text_input("Por favor, ingresa tu nombre")

if nombre:
    st.write(f"Hola, {nombre}!")

    opcion = st.radio("¿Cómo deseas buscar tu carrera?", (1, 2), format_func=lambda x: "Por Facultad" if x == 1 else "Por nombre o palabra clave")

    if opcion == 1:
        facultad = st.selectbox("Seleccioná la facultad", list(facultades.keys()))
        carreras = facultades[facultad]
        st.write(f"Carreras en {facultad}:")
        for carrera in carreras:
            st.write("- " + carrera)

    else:
        palabra = st.text_input("Colocá el nombre o palabra clave de la carrera")
        if palabra:
            resultados = []
            for facultad, carreras in facultades.items():
                for carrera in carreras:
                    if palabra.lower() in carrera.lower():
                        resultados.append((carrera, facultad))
            if resultados:
                st.write("Resultados encontrados:")
                for carrera, facultad in resultados:
                    st.write(f"- {carrera} (Facultad de {facultad})")
            else:
                st.write("Lo sentimos, esta carrera no se dicta en la UNLZ.")

