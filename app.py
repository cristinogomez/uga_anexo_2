import streamlit as st
import pandas as pd
from acv import acv
from cot import cot
from CRUD_Bloqueos import crud_bloqueo

st.set_page_config(page_title='UGA-Anexo',page_icon='logo.jpeg',layout='wide')

def main():
    st.title('Gestión de Agendas')

    st.sidebar.write('UGA-Anexo')
    menu = ['Inicio','COT','ACV']
    menu2 = ['CRUD-Bloqueos','Busqueda de bloqueos']
   
    choice=st.sidebar.selectbox('Servicio',menu)

    if choice =='Inicio':
        st.subheader("Software de gestión de agendas")
    elif choice =='COT':
        choice2=st.sidebar.selectbox('COT',menu2)
        if choice2=='CRUD-Bloqueos':
                crud_bloqueo()
        elif choice2=='Busqueda de bloqueos':
                cot()
    else:
                acv()   


if __name__=='__main__':
    main()