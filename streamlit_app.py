import streamlit as st
import gateway

def header():
    st.header('Entrevista con Israel Kirzner')
    st.markdown("##### Pregunte a Israel Kirzner")
    st.text('Version 0 - Last update 08/19/2022')

def instert_text():
    txt = st.text_area("© 2022 por Moris Polanco, para la Universidad de Occidente")
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])

    if colum1.button("Pregunte"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_entrevista_covey(txt)
            status = 200
            
            if status == 200:
                st.text_area(label="Respuesta:", value=new_txt, height=250)
                st.success("Success!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Entrevista con I. Kirzner ❄️")
header()
instert_text()
