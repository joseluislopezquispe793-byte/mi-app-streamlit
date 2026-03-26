import streamlit as st

st.title("App de Despachos 🚚")

placa = st.text_input("Placa del vehículo")
empresa = st.text_input("Empresa de transporte")
operador = st.text_input("Operador de montacarga")

peso_neto = st.number_input("Peso neto (kg)")
peso_esperado = st.number_input("Peso esperado (kg)")

diferencia = peso_neto - peso_esperado

st.write(f"Diferencia: {round(diferencia)} kg")

if st.button("Validar despacho"):
    if abs(diferencia) <= 5:
        st.success("Despacho conforme")
    else:
        st.error("Despacho con diferencia")
