import streamlit as st
# Configuración de página
st.set_page_config(page_title="Recetas con harina", page_icon=":cake:", layout="wide")
def bolillo_recipe(harina):
    agua = harina * 0.62
    sal = harina * 0.025
    levadura = harina * 0.022
    manteca = harina * 0.02
    azucar = harina * 0.03
    
    st.write("Debes utilizar los siguientes ingredientes y cantidades:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Agua: {agua} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Levadura: {levadura} gr.")
    st.write(f"Manteca: {manteca} gr.")
    st.write(f"Azúcar: {azucar} gr.")

def conchas_recipe(harina):
    leche = harina * 0.36
    sal = harina * 0.008
    levadura = harina * 0.022
    mantequilla = harina * 0.28
    azucar = harina * 0.3
    huevos = harina * 0.004
    yemas = harina * 0.002
    vainilla = harina * 0.004
    piezas = harina * 0.032
    manteca = harina * 0.3
    azucar_glass = harina * 0.3
    harina_cubierta = harina * 0.3
    vainilla_cubierta = harina * 0.0005
    cocoa_cubierta = harina * 0.003
    porciones = harina * 0.016
    
    st.write("Debes utilizar los siguientes ingredientes y cantidades para el pan:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Leche tibia (36°): {leche} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Levadura: {levadura} gr.")
    st.write(f"Mantequilla: {mantequilla} gr.")
    st.write(f"Azúcar: {azucar} gr.")
    st.write(f"Huevos: {huevos} pz.")
    st.write(f"Yemas: {yemas} pz.")
    st.write(f"Vainilla: {vainilla} pz.")
    st.write(f"Piezas: {piezas} pz.")
    st.write("------------------------------------------------------------------------------------------")
    st.write("Debes utilizar los siguientes ingredientes y cantidades para la cubierta:")
    st.write(f"Manteca vegetal: {manteca} gr.")
    st.write(f"Azúcar Glass: {azucar_glass} gr.")
    st.write(f"Harina: {harina_cubierta} gr.")
    st.write(f"Vainilla: {vainilla_cubierta} cdta.")
    st.write(f"Cocoa: {cocoa_cubierta} gr.")
    st.write(f"Porciones por masa (2 masas, 1 chocolate, 1 vainilla): {porciones} gr.")

def bisquettes_recipe(harina):
    sal = harina * 0.02
    leche = harina * 0.4
    levadura = harina * 0.
def bisquettes_recipe(harina):
    sal = harina * 0.02
    leche = harina * 0.4
    levadura = harina * 0.
    azucar = harina * 0.15
    huevos = harina * 0.004
    mantequilla = harina * 0.35
    huevo_brillo = harina * 0.002
    st.write("Debes utilizar los siguientes ingredientes y cantidades:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Leche tibia (36°): {leche} gr.")
    st.write(f"Levadura: {levadura} gr.")
    st.write(f"Azúcar: {azucar} gr.")
    st.write(f"Huevos: {huevos} pz.")
    st.write(f"Mantequilla: {mantequilla} gr.")
    st.write(f"Huevo (brillo): {huevo_brillo} pz.")
    
def hojaldre_recipe(harina):
    sal = harina * 0.02
    agua = harina * 0.4
    mantequilla_masa = harina * 0.2
    mantequilla_capa = harina * 0.5
    huevos = harina * 0.004
    huevo_brillo = harina * 0.004
    st.write("Debes utilizar los siguientes ingredientes y cantidades:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Agua: {agua} gr.")
    st.write(f"Huevos: {huevos} pz.")
    st.write(f"Mantequilla (masa): {mantequilla_masa} gr.")
    st.write(f"Mantequilla (capa): {mantequilla_capa} gr.")
    st.write(f"Huevo (brillo): {huevo_brillo} pz.")
    
def pizza_recipe(harina):
    agua = harina * 0.6
    sal = harina * 0.025
    levadura = harina * 0.022
    azucar = harina * 0.024
    bicarbonato = harina * 0.001
    jitomates = harina * .0125
    dientes_ajo = harina * 0.003
    aceite_oliva = harina * 0.001
    azucar_salsa = harina * 0.001
    st.write("Debes utilizar los siguientes ingredientes y cantidades para la masa:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Agua: {agua} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Levadura: {levadura} gr.")
    st.write(f"Azúcar: {azucar} gr.")
    st.write("------------------------------------------------------------------------------------------")
    st.write("Debes utilizar los siguientes ingredientes y cantidades para la salsa:")
    st.write(f"Bicarbonato: {bicarbonato} pizca.")
    st.write(f"Jitomates: {jitomates} pz.")
    st.write(f"Dientes de ajo: {dientes_ajo} pz.")
    st.write(f"Aceite de oliva: {aceite_oliva} cda.")
    st.write(f"Azúcar: {azucar_salsa} cda.")
    
def baker_percentage(harina):
    sal = harina * 0.02
    agua = harina * 0.6
    levadura = harina * 0.022
    azucar = harina * 0.03

    st.write("Debes utilizar los siguientes ingredientes y cantidades para la masa:")
    st.write(f"Harina: {harina} gr.")
    st.write(f"Sal: {sal} gr.")
    st.write(f"Agua: {agua} gr.")
    st.write(f"Levadura: {levadura} gr.")
    st.write(f"Azúcar: {azucar} gr.")

# Función principal que muestra el menú

def main():
    # Título
    st.title("Recetas con harina")

    # Creación de columnas
    left_column, right_column = st.columns(2)

    # Input de cantidad de harina
    with left_column:
        harina = st.number_input("Teclea la cantidad de harina a usar:", min_value=1, step=1)

    # Selección de receta
    with right_column:
        recipe_options = ["Bolillo", "Conchas", "Bisquettes", "Hojaldre", "Pizza", "% Panadero"]
        selected_recipe = st.selectbox("Selecciona la receta que deseas consultar:", recipe_options)

    # Cálculo de ingredientes según receta seleccionada
    if selected_recipe == "Bolillo":
        bolillo_recipe(harina)
    elif selected_recipe == "Conchas":
        conchas_recipe(harina)
    elif selected_recipe == "Bisquettes":
        bisquettes_recipe(harina)
    elif selected_recipe == "Hojaldre":
        hojaldre_recipe(harina)
    elif selected_recipe == "Pizza":
        pizza_recipe(harina)
    elif selected_recipe == "% Panadero":
        baker_percentage(harina)

    # Botón para limpiar formulario
    if st.button("Limpiar formulario"):
        st.experimental_rerun()

# Ejecución de la función principal
if __name__ == "__main__":
    main()
