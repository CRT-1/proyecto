import streamlit as st 
import	pandas as pd 
import	lasio 
st.title("Aplicación para registro de pozos ")
st.sidebar.title("Menu")
opciones_inicio = st.sidebar.radio("Selecione una opcion", ["inicio", "datos", "calculos"])
archivo_las = lasio.read("LGAE-040.las")
df = archivo_las.df()

#Crear condicionantes IF
if opciones_inicio == "inicio":
	st.write("Ingreso al inicio")
	st.write(df)

if opciones_inicio == "datos":
	st.write("Ingreso a datos")
	barra_deslizadora = st.slider("Selecione un valor", 1, 100, 30)
	st.write("El valor selecionado es", barra_deslizadora)
	Ingreso_numero = st.number_input("Ingrese un valor", min_value = 1.00, max_value = 1000.00, value = 300.00)
if opciones_inicio == "calculos":
	st.write("Ingreso a calculos")
	seleccion = st.selectbox("Seleccione una opcion", [1,2,3,"A"])
	check1 = st.checkbox("Activar")
	if check1==True:
		st.write("Check activo")
archivo_subido = st.sidebar.file_uploader("Cargar Archivo Excel", type = [".xls", ".xlsx"])
if archivo_subido is not None: 
	df2 = pd.read_excel(archivo_subido)
	st.write(df2)
