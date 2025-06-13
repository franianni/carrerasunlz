import streamlit as st

facultades = {
    "Facultad de Derecho": ["Abogacía", "Ciclos de Complementación Curricular:", "*Licenciatura en Seguridad", "*Licenciatura en Comercio Internacional y Aduanas"],
    "Facultad de Cs. Sociales": ["Ciencias de la Educación (Licenciatura y Profesorado)", "Comunicación Social (Licenciatura y Profesorado)", "Letras (Licenciatura y Profesorado)", "Minoridad y Familia (Tecnicatura)", "Periodismo (Tecnicatura y Licenciatura)", "Psicopedagogía (Licenciatura y Profesorado)", "Publicidad (Tecnicatura y Licenciatura)", "Relaciones Laborales (Tecnicatura y Licenciatura)", "Relaciones Públicas (Tecnicatura y Licenciatura)", "Trabajo Social (Licenciatura)"],
    "Facultad de Cs. Económicas": ["Contador Público", "Licenciado en Administración"],
    "Facultad de Cs. Agrarias": ["Ingeniería Agronómica", "Ingeniería Zootecnista", "Técnico Universitario en Procesamiento Agroalimentario", "Técnico Universitario en Producción Vegetal", "Técnico Universitario en Producción Animal", "Técnico Universitario en Diseño y Mantenimiento de Espacios Verdes", "Técnico Universitario en Arboricultura y Vivericultura
"Tecnicatura Universitaria en Agroecología"],
    "Facultad de Ingeniería": ["Ingeniería Industrial", "Ingeniería Industrial", "Ingeniería Mecátrónica", "Ingeniería Ferroviaria", "Ingeniería Mecánica", "Licenciatura en Higiene y Seguridad en el Trabajo*", "Licenciatura en Gestión de Sistemas de Automatización y Robótica*", "Licenciatura en Gestión de la Información*", "Licenciatura en Enseñanza de la Matemática*"
, "*Se cursan en sedes"]
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

